# Item Models

- [Item Models Schema](item_model.schema.json)

## Root

- **compound**: The root tag of an item model.

### `parent` (string)

Loads a different model from a resource location.
If both `"parent"` and `"elements"` are set, the `"elements"` tag overrides the parent’s elements.

- `"item/generated"` — uses a 2D icon‑based model.
- `"builtin/entity"` — loads a model from an entity file. Only works for:
  - chests
  - ender chests
  - mob heads
  - shields
  - banners
  - tridents

---

## `display` (compound)

Defines how the item is displayed in various contexts.

### Display Positions (compound)

Valid keys:

- `thirdperson_righthand`
- `thirdperson_lefthand`
- `firstperson_righthand`
- `firstperson_lefthand`
- `gui`
- `head`
- `ground`
- `fixed` (item frames)
- `on_shelf`

Each position may contain:

#### `rotation` (list)

`[x, y, z]` — rotation angles.

#### `translation` (list)

`[x, y, z]` — position offset.
Values are clamped to the range `[-80, 80]`.

#### `scale` (list)

`[x, y, z]` — scale factors.
Values are clamped to a maximum of `4`.

---

## `textures` (compound)

Defines texture variables using resource locations.

### Texture Fields

- `layerN` (string)
  Used for item icons. Supports multiple layers (e.g., leather armor, trimmed armor).
  Works only with `"item/generated"`.

- `particle` (string)
  Texture used for particle effects (food crumbs, barrier particles).

- _Texture variable_ (string)
  Any custom variable name mapping to a texture.

---

## `gui_light` (string)

Controls shading in GUI:

- `"front"` — flat item shading.
- `"side"` — block‑like shading (default).

---

## `elements` (list)

Defines cuboid elements of the model.
If `"parent"` and `"elements"` are both present, this list overrides the parent.

### Element (compound)

#### `from` (list)

Start point `[x, y, z]` — must be between `-16` and `32`.

#### `to` (list)

End point `[x, y, z]` — must be between `-16` and `32`.

#### `rotation` (compound)

- `origin` (list) — rotation center `[x, y, z]`
- `axis` (string) — `"x"`, `"y"`, or `"z"`
- `angle` (float) — between `-45` and `45`
- `rescale` (bool) — default `false`

#### `shade` (bool)

Whether faces are shaded (`true` by default).

#### `light_emission` (int)

Minimum light level (0–15). Default: `0`.

#### `faces` (compound)

Each face is optional. Valid face keys:

- `down`
- `up`
- `north`
- `south`
- `west`
- `east`

##### Face Properties

- `uv` (list) — `[x1, y1, x2, y2]`
  Optional; auto‑generated if omitted.

- `texture` (string) — texture variable reference, e.g. `"#layer0"`

- `cullface` (string) — face direction for culling and lighting

- `rotation` (int) — `0`, `90`, `180`, or `270`

- `tintindex` (int) — applies tint from item model definition

---

## `overrides` (list)

**Removed as of 24w45a / 1.21.4+.**
Replaced by a new system documented under _Items model definition_.

---

## Item Models - JSON Schema‑Style Representation

This is not a literal JSON model, but a structural template describing valid fields and types.

```json
{
  "parent": "string (resource location)",

  "display": {
    "position": {
      "rotation": ["x", "y", "z"],
      "translation": ["x", "y", "z (clamped -80..80)"],
      "scale": ["x", "y", "z (clamped ≤ 4)"]
    }
  },

  "textures": {
    "layerN": "string (resource location)",
    "particle": "string (resource location)",
    "texture_variable": "string (resource location)"
  },

  "gui_light": "front | side",

  "elements": [
    {
      "from": ["x (-16..32)", "y", "z"],
      "to": ["x (-16..32)", "y", "z"],

      "rotation": {
        "origin": ["x", "y", "z"],
        "axis": "x | y | z",
        "angle": "float (-45..45)",
        "rescale": "boolean"
      },

      "shade": "boolean",
      "light_emission": "int (0..15)",

      "faces": {
        "face": {
          "uv": ["x1", "y1", "x2", "y2"],
          "texture": "string (#texture_variable)",
          "cullface": "down | up | north | south | west | east",
          "rotation": "0 | 90 | 180 | 270",
          "tintindex": "int"
        }
      }
    }
  ],

  "overrides": "REMOVED in 24w45a / 1.21.4+"
}
```
