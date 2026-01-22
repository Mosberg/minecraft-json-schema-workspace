# Copilot Instructions for Minecraft JSON Schema Workspace

## Project Overview

- This workspace is for authoring and generating JSON Schema files (`*.schema.json`) for Minecraft Java Edition 1.21.11.
- The structure mirrors vanilla Minecraft's `assets/` and `data/` layouts for strict validation and editor autocomplete.
- Schemas are mapped to real vanilla files in `resources/` and to downstream pack/mod files in `src/main/resources/`.

## Key Directories & Files

- **resources/assets/minecraft/**: Reference vanilla asset files.
- **resources/data/minecraft/**: Reference vanilla data files.
- **schemas/**: All schema definitions, organized to match vanilla folder structure.
- **.vscode/settings.json**: Maps file globs to schemas for automatic validation in VS Code.
- **tools/schema_tool.py**: Python utility for generating/checking schema files based on VS Code settings.

## Developer Workflows

- **Schema Generation:**
  - Run `./gradlew generateSchemas` to create missing schemas (uses `tools/schema_tool.py`).
  - Run `./gradlew check` to validate all referenced schemas for existence and JSON correctness.
- **VS Code Integration:**
  - Schema validation is automatic via `.vscode/settings.json` mappings; no need to add `$schema` manually.
  - Update `.vscode/settings.json` when adding/renaming schemas or changing file globs.
- **Updating for New Minecraft Versions:**
  1. Update vanilla files in `resources/`.
  2. Regenerate schemas and adjust for format changes.
  3. Keep schema paths/folders in sync with vanilla file structure.

## Project-Specific Patterns & Conventions

- Schemas use `$defs` for shared structures; avoid duplication.
- Each schema covers a single format family (e.g., one per folder/type).
- Use `oneOf`/`anyOf` only for true format divergence; avoid permissive schemas.
- Fallback schemas (`any_asset_json.schema.json`, `any_data_json.schema.json`) catch files not covered by specific schemas.
- Exclusion patterns in `.vscode/settings.json` prevent fallback schemas from overriding specific ones.

## Integration Points & Dependencies

- **Python**: Required for running schema generation/check scripts.
- **Gradle**: Orchestrates schema generation and validation tasks.
- **VS Code**: Recommended editor for schema mapping and validation.

## Examples

- To generate schemas: `./gradlew generateSchemas`
- To check schemas: `./gradlew check`
- To add a new schema: Place in `schemas/` matching the vanilla folder, update `.vscode/settings.json` with a new mapping.

## References

- [README.md](../README.md): High-level overview and quick start.
- [tools/schema_tool.py](../tools/schema_tool.py): Schema generation/check logic.
- [.vscode/settings.json](../.vscode/settings.json): Schema mapping for validation.

---

**Feedback:** If any section is unclear or missing, please specify which workflows, conventions, or integration details need more coverage.
