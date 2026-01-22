# Minecraft Java Edition 1.21.11 — JSON Schema Workspace

A schema-driven workspace for authoring and generating `*.schema.json` files for vanilla Minecraft Java Edition **1.21.11**, structured to mirror Minecraft’s own `assets/` and `data/` layouts.

## Table of contents

- [Minecraft Java Edition 1.21.11 — JSON Schema Workspace](#minecraft-java-edition-12111--json-schema-workspace)
  - [Table of contents](#table-of-contents)
  - [What this repository is](#what-this-repository-is)
    - [Goals](#goals)
  - [Repository layout](#repository-layout)
    - [Where to look](#where-to-look)
  - [Quick start](#quick-start)
    - [Prerequisites](#prerequisites)
    - [Clone](#clone)
  - [Generate schemas](#generate-schemas)
  - [VS Code integration](#vs-code-integration)
    - [What gets validated](#what-gets-validated)
    - [Editing the mapping](#editing-the-mapping)
  - [Schema workflow](#schema-workflow)
    - [Updating to a new Minecraft version](#updating-to-a-new-minecraft-version)
    - [Authoring guidelines](#authoring-guidelines)
  - [Contributing](#contributing)
  - [License](#license)

## What this repository is

This repository exists to make Minecraft JSON formats easier to work with by providing schemas that drive validation and autocomplete in editors.
It includes a local reference corpus of vanilla Minecraft files (assets + data) so schemas stay grounded in real examples.

### Goals

- Provide schemas strict enough to catch mistakes while matching vanilla reality.
- Keep schema paths aligned with the vanilla folder structure they describe.
- Validate both the bundled vanilla corpus (`resources/**`) and downstream pack/mod JSON (`src/main/resources/**`).

## Repository layout

High-level layout (trimmed); for the complete listing see the docs.

```text
minecraft-json-schema-workspace
├─ .vscode/
│  └─ settings.json
├─ docs
│  └─ project-structure.md
├─ gradle
│  └─ wrapper
│     └─ gradle-wrapper.properties
├─ gradle.properties
├─ guild.gradle
├─ LICENSE
├─ README.md
├─ schemas
│  ├─ assets
│  └─ data
├─ settings.gradle
└─ tools
   └─ schema_tool.py
```

Full structure: [docs/project-structure.md](docs/project-structure.md).

### Where to look

- Vanilla assets: `resources/assets/minecraft/`
- Vanilla data: `resources/data/minecraft/`
- Schemas: `schemas/`
- VS Code schema mapping: `.vscode/settings.json`

## Quick start

### Prerequisites

- Git
- A JSON Schema-capable editor (VS Code recommended)
- Python (for schema generation)
- Gradle (or the Gradle wrapper)

### Clone

```bash
git clone <repo-url>
cd <repo-folder>
```

## Generate schemas

Schemas are generated from code (recommended: Python generator orchestrated by Gradle), so contributors can run a single command and get reproducible output.

Recommended tasks (adjust to your actual task names/paths):

```bash
./gradlew generateSchemas
./gradlew check
```

> If you rename tasks, keep this section updated—this README is meant to be the “single source of truth” for schema generation.

## VS Code integration

VS Code supports mapping file globs to schema files using `json.schemas` in workspace settings, and it supports relative schema paths when configured in `.vscode/settings.json`.
This repository ships a workspace mapping in `.vscode/settings.json` so JSON files validate automatically without adding `$schema` to each file.

### What gets validated

The schema mappings target both:

- The vanilla corpus bundled in this repo: `resources/**`
- Downstream packs/mods in a typical project layout: `src/main/resources/**`

### Editing the mapping

Update `.vscode/settings.json` when you add/rename schema outputs or want new globs covered.
VS Code `fileMatch` supports wildcards and exclusion patterns starting with `!` (useful for avoiding fallback rules overriding specific ones).

## Schema workflow

### Updating to a new Minecraft version

1. Update the vanilla reference files under `resources/` (both `assets/` and `data/`).
2. Regenerate schemas and adjust for format changes.
3. Keep folder parity: schema paths should mirror the vanilla file paths they describe.

### Authoring guidelines

- Prefer reusable `$defs` for shared shapes instead of copy/pasting structures.
- Keep schemas focused per format family (e.g., one schema per JSON “type” or folder convention).
- Use `oneOf`/`anyOf` only when formats truly diverge; avoid over-permissive schemas.

## Contributing

Contributions are welcome, especially:

- Tightening correctness (types/enums, required fields) while staying compatible with vanilla examples.
- Adding missing coverage for formats that appear in `resources/`.
- Refactoring schemas for maintainability (shared `$defs`, reduced duplication).

When opening a PR, include:

- A short rationale (which vanilla files motivated the change).
- A minimal example that should pass and one that should fail.
- Notes on any intentional looseness (where vanilla is inconsistent).

## License

This project is licensed under the MIT License.
See: [LICENSE](LICENSE).
