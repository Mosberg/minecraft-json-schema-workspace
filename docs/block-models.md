# Block Models

- [Block Models Schema](block_model.schema.json)

## Root

- **compound** — The root tag of a block model.

### `parent` (string)

Loads another model from a resource location.
If both `"parent"` and `"elements"` are present, the child `"elements"` override the parent’s.

- `"builtin/generated"` — uses an icon‑based model.
  Only the first layer is supported; rotation must be done via blockstate files.

---

## `ambientocclusion` (boolean)

Controls ambient occlusion shading.

- `true` — enabled (default)
- `false` — disabled

---

## `display` (compound)

Defines how the block is displayed in various item contexts.

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

Each position may contain:

#### `rotation` (list)

`[x, y, z]` — rotation angles.

#### `translation` (list)

`[x, y, z]` — translation values, clamped to `[-80, 80]`.

#### `scale` (list)

`[x, y, z]` — scale factors, clamped to a maximum of `4`.

---

## `textures` (compound)

Defines texture variables using resource locations.

### Texture Fields

- `particle` (string)
  Texture used for:
  - block breaking particles (for model‑based blocks)
  - nether portal overlay
  - water and lava still textures
    Also available as a texture variable: `"#particle"`.

- _Texture variable_ (string)
  Any custom variable name mapping to a texture.

---

## `elements` (list)

Defines cuboid elements of the model.
If `"parent"` and `"elements"` are both present, this list overrides the parent.

### Element (compound)

#### `from` (list)

Start point `[x, y, z]` — values must be between `-16` and `32`.

#### `to` (list)

End point `[x, y, z]` — values must be between `-16` and `32`.

#### `rotation` (compound)

Defines rotation of the element.

- `origin` (list) — rotation center `[x, y, z]`
- `x` (float) — rotation around X axis
- `y` (float) — rotation around Y axis
- `z` (float) — rotation around Z axis
  _(ignored if `axis` and `angle` are specified)_

- `axis` (string) — `"x"`, `"y"`, or `"z"`
- `angle` (float) — rotation angle
- `rescale` (bool) — scales faces by `1 / cos(angle)` when true (default: false)

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
  UV outside `[0, 16]` behaves inconsistently.
  Swapping `x1` and `x2` flips the texture.

- `texture` (string) — texture variable reference, e.g. `"#side"`

- `cullface` (string) — face direction for culling and lighting

- `rotation` (int) — `0`, `90`, `180`, or `270`
  Clockwise rotation (counterclockwise for `down`).

- `tintindex` (int)
  - `-1` — no tint
  - any other value — passed to BlockColors
    Vanilla blocks rarely use multiple tint indices, but modded blocks may.

---

## Block Models — JSON Schema‑Style Structure

This is not a literal JSON model, but a structural template describing valid fields and types.

```json
{
  "parent": "string (resource location)",

  "ambientocclusion": "boolean",

  "display": {
    "position": {
      "rotation": ["x", "y", "z"],
      "translation": ["x (-80..80)", "y", "z"],
      "scale": ["x (≤4)", "y", "z"]
    }
  },

  "textures": {
    "particle": "string (resource location)",
    "texture_variable": "string (resource location)"
  },

  "elements": [
    {
      "from": ["x (-16..32)", "y", "z"],
      "to": ["x (-16..32)", "y", "z"],

      "rotation": {
        "origin": ["x", "y", "z"],
        "x": "float",
        "y": "float",
        "z": "float",
        "axis": "x | y | z",
        "angle": "float",
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
  ]
}
```
