# Minecraft JSON Schemas — Workspace & Reference

A schema-driven workspace for authoring and maintaining `*.schema.json` files that validate Minecraft resource-pack and data-pack JSON formats (validation + autocomplete in editors such as VS Code).

- Schemas live in: [`/schemas`](schemas)
- Asset-focused schemas: [`/schemas/assets`](schemas/assets)
- Data-focused schemas: [`/schemas/data`](schemas/data)

---

## What this repo provides

- **JSON Schema files** (`*.schema.json`) that model vanilla Minecraft JSON formats closely, while still allowing practical extension points where vanilla is inconsistent.
- A workspace-friendly structure that mirrors Minecraft’s own folder layout (`assets/**` and `data/**`), so it’s easy to find “the schema that matches the file you’re editing”.

---

## Repository layout (high level)

```text
.vscode/
  settings.json          # VS Code json.schemas mapping (globs -> schemas)
schemas/
  assets/
    minecraft/
      ...                # Schemas that target assets/minecraft/** JSON
  data/
    minecraft/
      ...                # Schemas that target data/minecraft/** JSON
```

---

## VS Code integration

This repository is intended to “just work” in VS Code via workspace settings.

### Use it in this workspace

1. Open the repository folder in VS Code.
2. Ensure VS Code uses the workspace mapping in [`.vscode/settings.json`](.vscode/settings.json).
3. Edit JSON anywhere under:
   - `resources/**` (if you keep a vanilla reference corpus here)
   - `src/main/resources/**` (typical mod/project resources layout)

### Use schemas in another project

Options (pick one):

- **Workspace mapping**: copy/adapt the `json.schemas` mappings from [`.vscode/settings.json`](.vscode/settings.json).
- **Per-file `$schema`**: add a `$schema` property at the top of a JSON file and point it to a schema URL/path.
  - Tip: prefer stable, raw links (or vendoring schemas into your project) so teammates get the same results.

---

## Schema catalog

The schemas are grouped by the Minecraft path they model. Each entry below describes what the schema validates and what it helps with (validation + autocomplete).

### assets/minecraft/\*\*

<details>
<summary><strong>General asset JSON formats</strong></summary>

- `atlases.schema.json` — Texture atlas definitions (`assets/minecraft/atlases/*.json`).
- `blockstates.schema.json` — Blockstate definitions (`assets/minecraft/blockstates/*.json`), including `variants` and `multipart`.
- `equipment.schema.json` — Equipment mappings (`assets/minecraft/equipment/*.json`).
- `font.schema.json` — Font providers and glyph mapping (`assets/minecraft/font/*.json`).
- `gpu_warnlist.schema.json` — GPU warnlist file (typically `gpu_warnlist.json`).
- `items.schema.json` — Item definitions / model override-style structures (`assets/minecraft/items/*.json`).
- `lang.schema.json` — Language files (`assets/minecraft/lang/*.json`), mapping keys to strings.
- `particles.schema.json` — Particle definitions (`assets/minecraft/particles/*.json`).
- `post_effect.schema.json` — Post-processing effects (`assets/minecraft/post_effect/*.json`).
- `regional_compliancies.schema.json` — Region compliance data (typically `regional_compliancies.json`).
- `texts.schema.json` — Text resource lists (`assets/minecraft/texts/*.json`) such as credits/splashes.
- `waypoint_style.schema.json` — Waypoint style definitions (`assets/minecraft/waypoint_style/*.json`).

</details>

### assets/minecraft/models/block/\*\*

<details>
<summary><strong>Block model schemas</strong></summary>

- `any_model.schema.json` — Generic fallback: validates “common block-model shape” without enforcing a specific vanilla template.
- Template schemas (stricter, vanilla-shaped):
  `button.schema.json`, `cross.schema.json`, `cube.schema.json`, `cube_all.schema.json`, `cube_bottom_top.schema.json`, `cube_column.schema.json`,
  `door.schema.json`, `fence.schema.json`, `fence_gate.schema.json`, `pressure_plate.schema.json`, `slab.schema.json`, `stairs.schema.json`,
  `trapdoor.schema.json`

</details>

### assets/minecraft/models/item/\*\*

<details>
<summary><strong>Item model schemas</strong></summary>

- `any_item_model.schema.json` — Generic fallback: validates “common item-model shape” without enforcing a specific vanilla template.
- Template schemas (stricter, vanilla-shaped):
  `block_item.schema.json`, `generated.schema.json`, `handheld.schema.json`, `trident_in_hand.schema.json`

</details>

### data/minecraft/\*\*

<details>
<summary><strong>Data pack / registry-driven formats</strong></summary>

- `advancements.schema.json` — Advancement JSON (`data/minecraft/advancement/*.json`) including `criteria`, `rewards`, and `display`.
- Registry-style entry schemas (structure + required fields per type):
  `banner_pattern.schema.json`, `cat_variant.schema.json`, `chat_type.schema.json`, `chicken_variant.schema.json`, `cow_variant.schema.json`,
  `damage_type.schema.json`, `dialog.schema.json`, `dimension_type.schema.json`, `enchantment.schema.json`, `enchantment_provider.schema.json`,
  `frog_variant.schema.json`, `instrument.schema.json`, `jukebox_song.schema.json`, `painting_variant.schema.json`, `pig_variant.schema.json`,
  `test_environment.schema.json`, `test_instance.schema.json`, `timeline.schema.json`, `trial_spawner.schema.json`,
  `trim_material.schema.json`, `trim_pattern.schema.json`, `wolf_sound_variant.schema.json`, `wolf_variant.schema.json`,
  `zombie_nautilus_variant.schema.json`

</details>

---

## Contributing & workflow

- Keep schemas close to vanilla reality, but prefer reusable `$defs` to avoid duplication.
- When adding or tightening a schema:
  - Provide one example that should pass and one that should fail.
  - Mention which vanilla files motivated the change.
- If this repo includes a schema generator, keep its output reproducible and document the command(s) here (for example via Gradle tasks or a Python tool).

License: MIT (see [`LICENSE`](LICENSE)).
