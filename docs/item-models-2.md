# Item Models

- [Item Models Schema](item_model_2.schema.json)

Item models define how items are rendered in inventories, hands, GUIs, and other contexts.
They are stored in:

```
assets/<namespace>/models/item/
```

Item model filenames are **hardcoded** and must not be changed.

---

## Root Structure

### `parent` (string)

Loads another model using a resource location.
If both `parent` and `elements` are present, the child `elements` override the parent’s.

Special values:

- `"item/generated"` — creates a 2D icon‑based model
- `"builtin/entity"` — loads a model from an entity file
  - Only works for: chests, ender chests, mob heads, shields, banners, tridents

---

## `display` (compound)

Defines how the item is displayed in different contexts.

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

`[x, y, z]` — clamped to `[-80, 80]`.

#### `scale` (list)

`[x, y, z]` — clamped to a maximum of `4`.

If a display position is defined but missing one of these fields, the missing fields are **not inherited** from the parent.

---

## `textures` (compound)

Defines texture variables using resource locations.

### Texture Fields

- `layerN` — icon layers (only works with `"item/generated"`)
- `particle` — texture used for:
  - food crumb particles
  - barrier particles
  - fallback blockbreaking particles
- _Texture variable_ — any custom variable name mapping to a texture

---

## `gui_light` (string)

Controls shading in GUI:

- `"front"` — flat shading
- `"side"` — block‑like shading (default)

---

## `elements` (list)

Defines cuboid elements of the model.
If `parent` and `elements` are both present, this list overrides the parent.

### Element (compound)

#### `from` (list)

Start point `[x, y, z]` — must be between `-16` and `32`.

#### `to` (list)

End point `[x, y, z]` — must be between `-16` and `32`.

---

### `rotation` (compound)

- `origin` — rotation center `[x, y, z]`
- `axis` — `"x"`, `"y"`, or `"z"`
- `angle` — rotation angle (−45 to 45, in 22.5° increments)
- `rescale` — whether to scale faces to preserve size

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

- `texture` — texture variable reference, e.g. `"#layer0"`

- `cullface` — face direction for culling and lighting

- `rotation` — `0`, `90`, `180`, `270`

- `tintindex` — tint index used by item tinting logic

---

## `overrides` (list)

Defines conditional model overrides based on item predicates.

Each override entry contains:

### `predicate` (compound)

A set of conditions.
If all conditions match, the override applies.

### `model` (string)

Resource location of the model to use.

Overrides are evaluated **top to bottom**, and the **last matching override wins**.
Overrides do not recurse.

---

# Item Predicates

These values are used inside `predicate` objects:

- `"angle"` — compass angle (0–1)
- `"blocking"` — shield blocking state (0 or 1)
- `"broken"` — durability is 1 (0 or 1)
- `"cast"` — fishing rod cast (0 or 1)
- `"cooldown"` — cooldown progress (0–1)
- `"damage"` — durability fraction (0–1)
- `"damaged"` — whether item is damaged (0 or 1)
- `"lefthanded"` — left‑handed player (0 or 1)
- `"pull"` — bow/crossbow pull amount (0–1)
- `"pulling"` — bow/crossbow pulling (0 or 1)
- `"charged"` — crossbow charged (0 or 1)
- `"firework"` — crossbow loaded with firework (0 or 1)
- `"throwing"` — trident throwing (0 or 1)
- `"time"` — clock time (0–1)
- `"custom_model_data"` — integer, compared to item’s custom model data
- `"level"` — light block level (0–1)
- `"filled"` — bundle fill ratio (0–1)
- `"tooting"` — goat horn tooting (0 or 1)
- `"trim_type"` — armor trim material (0–1)
- `"brushing"` — brush animation progress (0–1)
- `"honey_level"` — honey level (0–1)

---

# Examples

## Simple 2D Bed

```json
{
  "parent": "item/generated",
  "textures": {
    "layer0": "item/red_bed"
  }
}
```

---

## Torch Item

```json
{
  "parent": "item/generated",
  "textures": {
    "layer0": "block/torch"
  },
  "display": {
    "thirdperson_righthand": {
      "rotation": [-90, 0, 0],
      "translation": [0, 1, -3],
      "scale": [0.55, 0.55, 0.55]
    },
    "firstperson_lefthand": {
      "rotation": [0, -135, 25],
      "translation": [0, 4, 2],
      "scale": [0.9, 0.9, 0.9]
    }
  }
}
```

---

## Fishing Rod (with override)

```json
{
  "parent": "item/handheld_rod",
  "textures": {
    "layer0": "item/fishing_rod_uncast"
  },
  "overrides": [
    {
      "predicate": { "cast": 1 },
      "model": "item/fishing_rod_cast"
    }
  ]
}
```

---

# 📦 Item Model JSON Schema (`item_model.schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Minecraft Item Model",
  "type": "object",

  "properties": {
    "parent": { "type": "string" },

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

    "gui_light": {
      "type": "string",
      "enum": ["front", "side"]
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
    },

    "overrides": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "predicate": {
            "type": "object",
            "additionalProperties": { "type": "number" }
          },
          "model": { "type": "string" }
        }
      }
    }
  }
}
```

---
