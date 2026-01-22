#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


JSON_LIKE_SUFFIXES = {".json", ".mcmeta"}  # include pack.mcmeta and *.png.mcmeta


def _strip_jsonc(text: str) -> str:
    # Remove // and /* */ comments (VS Code settings.json is JSONC).
    text = re.sub(r"//.*?$", "", text, flags=re.MULTILINE)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return text


def _load_jsonc(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    return json.loads(_strip_jsonc(raw))


def _normalize_schema_url(url: str) -> Path:
    # VS Code settings typically use "./schemas/..."
    if url.startswith("./"):
        url = url[2:]
    return Path(url)


def _schema_title_from_path(schema_rel_path: Path) -> str:
    return schema_rel_path.as_posix()


def _json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    # Fallback (shouldn't happen for json.loads)
    return "object"


def _schema_from_example(example: Any, schema_rel_path: Path, source_rel_path: Path) -> dict:
    t = _json_type(example)

    base: dict = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": _schema_title_from_path(schema_rel_path),
        "description": "Generated schema from resources corpus; refine for stricter validation over time.",
        # Helpful non-standard metadata:
        "x-generated-from": source_rel_path.as_posix(),
        "type": t,
    }

    if t == "object":
        base["additionalProperties"] = True
    elif t == "array":
        base["items"] = {}
    return base


def _is_json_like(path: Path) -> bool:
    name = path.name
    if name.endswith(".schema.json"):
        return False
    if path.suffix in JSON_LIKE_SUFFIXES:
        return True
    # handle pack.mcmeta specifically (suffix is ".mcmeta" already covered, but keep explicit)
    if name == "pack.mcmeta":
        return True
    return False


def _iter_resource_json_files(resources_dir: Path) -> list[Path]:
    if not resources_dir.exists():
        raise FileNotFoundError(f"resources dir not found: {resources_dir}")

    files: list[Path] = []
    for p in resources_dir.rglob("*"):
        if p.is_file() and _is_json_like(p):
            files.append(p)
    return sorted(files)


def _schema_path_for_resource(resources_dir: Path, schemas_dir: Path, resource_file: Path) -> tuple[Path, Path]:
    """
    Returns (schema_abs_path, schema_rel_path_from_repo_root)
    """
    rel = resource_file.relative_to(resources_dir)

    # Convert filename to *.schema.json:
    # - foo.json -> foo.schema.json
    # - pack.mcmeta -> pack.mcmeta.schema.json
    # - foo.png.mcmeta -> foo.png.mcmeta.schema.json
    schema_name = rel.name + ".schema.json"
    if rel.name.endswith(".json"):
        schema_name = rel.name[:-len(".json")] + ".schema.json"

    schema_rel = rel.with_name(schema_name)
    schema_abs = schemas_dir / schema_rel
    return schema_abs, schema_rel


def _ensure_unique_outputs(pairs: list[tuple[Path, Path, Path]]) -> None:
    """
    pairs items: (resource_file, schema_abs, schema_rel)
    """
    seen: dict[Path, Path] = {}
    collisions: list[str] = []

    for resource_file, schema_abs, _schema_rel in pairs:
        if schema_abs in seen and seen[schema_abs] != resource_file:
            collisions.append(
                f"Schema output collision: {schema_abs.as_posix()} "
                f"from {seen[schema_abs].as_posix()} and {resource_file.as_posix()}"
            )
        else:
            seen[schema_abs] = resource_file

    if collisions:
        for c in collisions:
            print(c, file=sys.stderr)
        raise SystemExit(f"Aborting due to {len(collisions)} duplicate schema output path(s).")


def cmd_generate(
    resources_dir: Path,
    schemas_dir: Path,
    settings_path: Path | None,
    overwrite: bool,
) -> int:
    resources_dir = resources_dir.resolve()
    schemas_dir = schemas_dir.resolve()

    resource_files = _iter_resource_json_files(resources_dir)

    # Build mapping resource -> schema path
    pairs: list[tuple[Path, Path, Path]] = []
    for rf in resource_files:
        schema_abs, schema_rel = _schema_path_for_resource(resources_dir, schemas_dir, rf)
        pairs.append((rf, schema_abs, schema_rel))

    _ensure_unique_outputs(pairs)

    created = 0
    updated = 0
    skipped = 0
    failed = 0

    for rf, schema_abs, schema_rel in pairs:
        schema_abs.parent.mkdir(parents=True, exist_ok=True)

        try:
            example = json.loads(rf.read_text(encoding="utf-8"))
        except Exception as e:
            failed += 1
            print(f"Skipping non-parseable JSON file: {rf} ({e})", file=sys.stderr)
            continue

        schema = _schema_from_example(example, schema_rel, rf.relative_to(resources_dir))

        if schema_abs.exists() and not overwrite:
            skipped += 1
            continue

        schema_abs.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if schema_abs.exists() and overwrite:
            updated += 1
        else:
            created += 1

    # Optional: also ensure VS Code referenced schema URLs exist (so editor config is consistent)
    if settings_path is not None and settings_path.exists():
        settings = _load_jsonc(settings_path)
        for entry in settings.get("json.schemas", []):
            url = entry.get("url")
            if not url:
                continue
            rel = _normalize_schema_url(url)
            abs_path = Path.cwd() / rel
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            if not abs_path.exists():
                # Create a minimal placeholder so VS Code mapping never points at missing files.
                abs_path.write_text(
                    json.dumps(
                        {
                            "$schema": "https://json-schema.org/draft/2020-12/schema",
                            "title": rel.as_posix(),
                            "description": "Generated placeholder to satisfy VS Code schema mapping.",
                            "type": ["object", "array"],
                            "additionalProperties": True,
                        },
                        indent=2,
                        ensure_ascii=False,
                    )
                    + "\n",
                    encoding="utf-8",
                )

    print(
        f"generate: scanned={len(resource_files)} created={created} updated={updated} "
        f"skipped={skipped} failed={failed}"
    )
    return 0 if failed == 0 else 1


def cmd_check(resources_dir: Path, schemas_dir: Path, settings_path: Path | None) -> int:
    resources_dir = resources_dir.resolve()
    schemas_dir = schemas_dir.resolve()

    resource_files = _iter_resource_json_files(resources_dir)

    pairs: list[tuple[Path, Path, Path]] = []
    for rf in resource_files:
        schema_abs, schema_rel = _schema_path_for_resource(resources_dir, schemas_dir, rf)
        pairs.append((rf, schema_abs, schema_rel))

    # Check for output collisions deterministically.
    try:
        _ensure_unique_outputs(pairs)
    except SystemExit:
        return 1

    errors: list[str] = []

    # Ensure every resource JSON has a schema file.
    for rf, schema_abs, _schema_rel in pairs:
        if not schema_abs.exists():
            errors.append(f"Missing schema for resource: {rf.as_posix()} -> {schema_abs.as_posix()}")
            continue
        try:
            json.loads(schema_abs.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"Invalid JSON schema file: {schema_abs.as_posix()} ({e})")

    # Also validate VS Code mapping URLs if provided.
    if settings_path is not None and settings_path.exists():
        settings = _load_jsonc(settings_path)
        for entry in settings.get("json.schemas", []):
            url = entry.get("url")
            if not url:
                continue
            rel = _normalize_schema_url(url)
            abs_path = Path.cwd() / rel
            if not abs_path.exists():
                errors.append(f"Missing schema file referenced by settings: {rel.as_posix()}")

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"check failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"check OK (resources json files: {len(resource_files)})")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="schema_tool")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="Scrape resources/** and generate schemas/**.")
    g.add_argument("--resources", type=Path, default=Path("resources"))
    g.add_argument("--out", type=Path, default=Path("schemas"))
    g.add_argument("--settings", type=Path, default=Path(".vscode/settings.json"))
    g.add_argument("--no-settings", action="store_true", help="Do not read/write VS Code settings mappings.")
    g.add_argument("--overwrite", action="store_true", help="Overwrite existing schema files.")

    c = sub.add_parser("check", help="Verify schemas exist for resources/** (and optionally VS Code mapping).")
    c.add_argument("--resources", type=Path, default=Path("resources"))
    c.add_argument("--out", type=Path, default=Path("schemas"))
    c.add_argument("--settings", type=Path, default=Path(".vscode/settings.json"))
    c.add_argument("--no-settings", action="store_true", help="Do not validate VS Code settings mappings.")

    args = p.parse_args(argv)

    if args.cmd == "generate":
        settings_path = None if args.no_settings else args.settings
        return cmd_generate(args.resources, args.out, settings_path, args.overwrite)

    if args.cmd == "check":
        settings_path = None if args.no_settings else args.settings
        return cmd_check(args.resources, args.out, settings_path)

    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
