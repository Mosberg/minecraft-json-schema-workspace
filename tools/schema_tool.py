#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def _strip_jsonc(text: str) -> str:
    text = re.sub(r"//.*?$", "", text, flags=re.MULTILINE)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return text


def _load_vscode_settings_jsonc(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    return json.loads(_strip_jsonc(raw))


def _normalize_schema_url(url: str) -> Path:
    if url.startswith("./"):
        url = url[2:]
    return Path(url)


def _schema_title_from_path(schema_path: Path) -> str:
    p = schema_path.as_posix()
    if p.endswith(".schema.json"):
        return p[:-len(".schema.json")]
    if p.endswith(".json"):
        return p[:-len(".json")]
    return p


def _placeholder_schema(schema_path: Path) -> dict:
    title = _schema_title_from_path(schema_path)
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": title,
        "description": "Generated placeholder schema. Replace with a strict schema as coverage improves.",
        "type": ["object", "array"],
        "additionalProperties": True,
    }


def _iter_schema_urls(settings: dict) -> list[Path]:
    entries = settings.get("json.schemas", [])
    out: list[Path] = []
    seen: set[Path] = set()
    for e in entries:
        url = e.get("url")
        if not url:
            continue
        p = _normalize_schema_url(url)
        if p not in seen:
            out.append(p)
            seen.add(p)
    return out


def cmd_generate(settings_path: Path) -> int:
    settings = _load_vscode_settings_jsonc(settings_path)
    urls = _iter_schema_urls(settings)

    created = 0
    for rel in urls:
        out_path = Path.cwd() / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)

        if out_path.exists():
            continue

        schema = _placeholder_schema(rel)
        out_path.write_text(
            json.dumps(schema, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        created += 1

    print(f"Generated {created} schema file(s).")
    return 0


def cmd_check(settings_path: Path) -> int:
    settings = _load_vscode_settings_jsonc(settings_path)
    urls = _iter_schema_urls(settings)

    errors: list[str] = []
    for rel in urls:
        path = Path.cwd() / rel
        if not path.exists():
            errors.append(f"Missing schema file referenced by settings: {rel.as_posix()}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"Invalid JSON schema file: {rel.as_posix()} ({e})")

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"checkSchemas failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"checkSchemas OK ({len(urls)} referenced schema file(s)).")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="schema_tool")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate")
    g.add_argument("--settings", type=Path, default=Path(".vscode/settings.json"))

    c = sub.add_parser("check")
    c.add_argument("--settings", type=Path, default=Path(".vscode/settings.json"))

    args = p.parse_args(argv)

    if args.cmd == "generate":
        return cmd_generate(args.settings)
    if args.cmd == "check":
        return cmd_check(args.settings)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
