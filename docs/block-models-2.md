# Block Models

- [Block Models Schema](block_model_2.schema.json)

Block model files are stored in:

```
assets/<namespace>/models/block/
```

The filenames must match the names referenced in blockstate files.

---

## Root Structure

### `parent` (string)

Loads another model using a resource location.
If both `parent` and `elements` are present, the child `elements` override the parent’s.

- `"builtin/generated"` — creates a model from an icon
  - Only the first texture layer is supported
  - Rotation must be done via blockstate files

---

### `ambientocclusion` (boolean)

Controls ambient occlusion shading.

- `true` — enabled (default)
- `false` — disabled
  _(Only works when defined in the parent model.)_

---

## `display` (compound)

Defines how the block is displayed when held or viewed as an item.

### Display Positions

Valid keys:

- `thirdperson_righthand`
- `thirdperson_lefthand`
- `firstperson_righthand`
- `firstperson_lefthand`
- `gui`
- `head`
- `ground`
- `fixed`

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
  Used for:
  - block breaking particles (for model‑based blocks)
  - nether portal overlay
  - water/lava still textures
    Also available as a texture variable: `"#particle"`.

- _Texture variable_ (string)
  Any custom variable name mapping to a texture.

---

## `elements` (list)

Defines cuboid elements of the model.
If `parent` and `elements` are both present, this list overrides the parent.

### Element (compound)

#### `from` (list)

Start point `[x, y, z]` — values must be between `-16` and `32`.

#### `to` (list)

End point `[x, y, z]` — values must be between `-16` and `32`.

---

### `rotation` (compound)

Defines rotation of the element.

- `origin` — rotation center `[x, y, z]`
- `axis` — `"x"`, `"y"`, or `"z"`
- `angle` — rotation angle (−45 to 45, in 22.5° increments)
- `rescale` — whether to scale faces to preserve size (`true`/`false`)

---

### `shade` (boolean)

Whether shadows are rendered (`true` by default).

---

### `faces` (compound)

Each face is optional. Valid keys:

- `down`
- `up`
- `north`
- `south`
- `west`
- `east`

#### Face Properties

- `uv` — `[x1, y1, x2, y2]`
  Optional; auto‑generated if omitted.
  UV outside `[0, 16]` behaves inconsistently.
  Swapping `x1` and `x2` flips the texture.

- `texture` — texture variable reference, e.g. `"#side"`

- `cullface` — face direction for culling and lighting

- `rotation` — `0`, `90`, `180`, `270`
  Clockwise rotation (counterclockwise for `down`).

- `tintindex` —
  - `-1` → no tint
  - any other value → passed to BlockColors
    Vanilla rarely uses multiple tint indices; modded blocks may.

---

# Examples

## Standing Torch

### `template_torch.json`

```json
{
  "ambientocclusion": false,
  "textures": {
    "particle": "#torch"
  },
  "elements": [
    {
      "from": [7, 0, 7],
      "to": [9, 10, 9],
      "shade": false,
      "faces": {
        "down": { "uv": [7, 13, 9, 15], "texture": "#torch" },
        "up": { "uv": [7, 6, 9, 8], "texture": "#torch" }
      }
    },
    {
      "from": [7, 0, 0],
      "to": [9, 16, 16],
      "shade": false,
      "faces": {
        "west": { "uv": [0, 0, 16, 16], "texture": "#torch" },
        "east": { "uv": [0, 0, 16, 16], "texture": "#torch" }
      }
    },
    {
      "from": [0, 0, 7],
      "to": [16, 16, 9],
      "shade": false,
      "faces": {
        "north": { "uv": [0, 0, 16, 16], "texture": "#torch" },
        "south": { "uv": [0, 0, 16, 16], "texture": "#torch" }
      }
    }
  ]
}
```

### `torch.json`

```json
{
  "parent": "block/template_torch",
  "textures": {
    "torch": "block/torch"
  }
}
```

---

## Cube Model (Used by Most Blocks)

```json
{
  "elements": [
    {
      "from": [0, 0, 0],
      "to": [16, 16, 16],
      "faces": {
        "down": { "texture": "#down", "cullface": "down" },
        "up": { "texture": "#up", "cullface": "up" },
        "north": { "texture": "#north", "cullface": "north" },
        "south": { "texture": "#south", "cullface": "south" },
        "west": { "texture": "#west", "cullface": "west" },
        "east": { "texture": "#east", "cullface": "east" }
      }
    }
  ]
}
```

---

## Sapling (Cross Model)

```json
{
  "ambientocclusion": false,
  "textures": {
    "particle": "#cross"
  },
  "elements": [
    {
      "from": [0.8, 0, 8],
      "to": [15.2, 16, 8],
      "rotation": { "origin": [8, 8, 8], "axis": "y", "angle": 45, "rescale": true },
      "shade": false,
      "faces": {
        "north": { "uv": [0, 0, 16, 16], "texture": "#cross" },
        "south": { "uv": [0, 0, 16, 16], "texture": "#cross" }
      }
    },
    {
      "from": [8, 0, 0.8],
      "to": [8, 16, 15.2],
      "rotation": { "origin": [8, 8, 8], "axis": "y", "angle": 45, "rescale": true },
      "shade": false,
      "faces": {
        "west": { "uv": [0, 0, 16, 16], "texture": "#cross" },
        "east": { "uv": [0, 0, 16, 16], "texture": "#cross" }
      }
    }
  ]
}
```

---

# 📦 Block Model JSON Schema (`block_model.schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Minecraft Block Model",
  "type": "object",

  "properties": {
    "parent": { "type": "string" },

    "ambientocclusion": { "type": "boolean" },

    "display": {
      "type": "object",
      "patternProperties": {
        "^(thirdperson_righthand|thirdperson_lefthand|firstperson_righthand|firstperson_lefthand|gui|head|ground|fixed)$": {
          "type": "object",
          "properties": {
            "rotation": {
              "type": "array",
              "items": { "type": "number" },
              "minItems": 3,
              "maxItems": 3
            },
            "translation": {
              "type": "array",
              "items": { "type": "number" },
              "minItems": 3,
              "maxItems": 3
            },
            "scale": {
              "type": "array",
              "items": { "type": "number" },
              "minItems": 3,
              "maxItems": 3
            }
          }
        }
      }
    },

    "textures": {
      "type": "object",
      "additionalProperties": { "type": "string" }
    },

    "elements": {
      "type": "array",
      "items": {
        "type": "object",

        "properties": {
          "from": {
            "type": "array",
            "items": { "type": "number" },
            "minItems": 3,
            "maxItems": 3
          },
          "to": {
            "type": "array",
            "items": { "type": "number" },
            "minItems": 3,
            "maxItems": 3
          },

          "rotation": {
            "type": "object",
            "properties": {
              "origin": {
                "type": "array",
                "items": { "type": "number" },
                "minItems": 3,
                "maxItems": 3
              },
              "axis": {
                "type": "string",
                "enum": ["x", "y", "z"]
              },
              "angle": { "type": "number" },
              "rescale": { "type": "boolean" }
            }
          },

          "shade": { "type": "boolean" },

          "faces": {
            "type": "object",
            "patternProperties": {
              "^(down|up|north|south|west|east)$": {
                "type": "object",
                "properties": {
                  "uv": {
                    "type": "array",
                    "items": { "type": "number" },
                    "minItems": 4,
                    "maxItems": 4
                  },
                  "texture": { "type": "string" },
                  "cullface": {
                    "type": "string",
                    "enum": ["down", "up", "north", "south", "west", "east"]
                  },
                  "rotation": {
                    "type": "integer",
                    "enum": [0, 90, 180, 270]
                  },
                  "tintindex": { "type": "integer" }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

---
