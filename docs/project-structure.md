# Project Structure

The project is organized into several directories and files, each serving a specific purpose. Below is an overview of the main components of the project structure:

```
minecraft-json-schema-workspace
├─ build
│  ├─ libs
│  │  └─ minecraft-json-schema-workspace.jar
│  └─ tmp
│     └─ jar
│        └─ MANIFEST.MF
├─ build.gradle
├─ docs
│  └─ project-structure.md
├─ gradle
│  └─ wrapper
│     ├─ gradle-wrapper.jar
│     └─ gradle-wrapper.properties
├─ gradle.properties
├─ gradlew
├─ gradlew.bat
├─ LICENSE
├─ README.md
├─ resources
│  ├─ assets
│  │  └─ minecraft
│  │     ├─ atlases
│  │     │  ├─ armor_trims.json
│  │     │  ├─ banner_patterns.json
│  │     │  ├─ beds.json
│  │     │  ├─ blocks.json
│  │     │  ├─ celestials.json
│  │     │  ├─ chests.json
│  │     │  ├─ decorated_pot.json
│  │     │  ├─ gui.json
│  │     │  ├─ items.json
│  │     │  ├─ map_decorations.json
│  │     │  ├─ paintings.json
│  │     │  ├─ particles.json
│  │     │  ├─ shield_patterns.json
│  │     │  ├─ shulker_boxes.json
│  │     │  └─ signs.json
│  │     ├─ blockstates
│  │     │  ├─ acacia_button.json
│  │     │  ├─ acacia_door.json
│  │     │  ├─ acacia_fence.json
│  │     │  ├─ acacia_fence_gate.json
│  │     │  ├─ acacia_hanging_sign.json
│  │     │  ├─ acacia_leaves.json
│  │     │  ├─ acacia_log.json
│  │     │  ├─ acacia_planks.json
│  │     │  ├─ acacia_pressure_plate.json
│  │     │  ├─ acacia_sapling.json
│  │     │  ├─ acacia_shelf.json
│  │     │  ├─ acacia_sign.json
│  │     │  ├─ acacia_slab.json
│  │     │  ├─ acacia_stairs.json
│  │     │  ├─ acacia_trapdoor.json
│  │     │  ├─ acacia_wall_hanging_sign.json
│  │     │  ├─ acacia_wall_sign.json
│  │     │  ├─ acacia_wood.json
│  │     │  ├─ activator_rail.json
│  │     │  ├─ air.json
│  │     │  ├─ allium.json
│  │     │  ├─ amethyst_block.json
│  │     │  ├─ amethyst_cluster.json
│  │     │  ├─ ancient_debris.json
│  │     │  ├─ andesite.json
│  │     │  ├─ andesite_slab.json
│  │     │  ├─ andesite_stairs.json
│  │     │  ├─ andesite_wall.json
│  │     │  ├─ anvil.json
│  │     │  ├─ attached_melon_stem.json
│  │     │  ├─ attached_pumpkin_stem.json
│  │     │  ├─ azalea.json
│  │     │  ├─ azalea_leaves.json
│  │     │  ├─ azure_bluet.json
│  │     │  ├─ bamboo.json
│  │     │  ├─ bamboo_block.json
│  │     │  ├─ bamboo_button.json
│  │     │  ├─ bamboo_door.json
│  │     │  ├─ bamboo_fence.json
│  │     │  ├─ bamboo_fence_gate.json
│  │     │  ├─ bamboo_hanging_sign.json
│  │     │  ├─ bamboo_mosaic.json
│  │     │  ├─ bamboo_mosaic_slab.json
│  │     │  ├─ bamboo_mosaic_stairs.json
│  │     │  ├─ bamboo_planks.json
│  │     │  ├─ bamboo_pressure_plate.json
│  │     │  ├─ bamboo_sapling.json
│  │     │  ├─ bamboo_shelf.json
│  │     │  ├─ bamboo_sign.json
│  │     │  ├─ bamboo_slab.json
│  │     │  ├─ bamboo_stairs.json
│  │     │  ├─ bamboo_trapdoor.json
│  │     │  ├─ bamboo_wall_hanging_sign.json
│  │     │  ├─ bamboo_wall_sign.json
│  │     │  ├─ barrel.json
│  │     │  ├─ barrier.json
│  │     │  ├─ basalt.json
│  │     │  ├─ beacon.json
│  │     │  ├─ bedrock.json
│  │     │  ├─ beehive.json
│  │     │  ├─ beetroots.json
│  │     │  ├─ bee_nest.json
│  │     │  ├─ bell.json
│  │     │  ├─ big_dripleaf.json
│  │     │  ├─ big_dripleaf_stem.json
│  │     │  ├─ birch_button.json
│  │     │  ├─ birch_door.json
│  │     │  ├─ birch_fence.json
│  │     │  ├─ birch_fence_gate.json
│  │     │  ├─ birch_hanging_sign.json
│  │     │  ├─ birch_leaves.json
│  │     │  ├─ birch_log.json
│  │     │  ├─ birch_planks.json
│  │     │  ├─ birch_pressure_plate.json
│  │     │  ├─ birch_sapling.json
│  │     │  ├─ birch_shelf.json
│  │     │  ├─ birch_sign.json
│  │     │  ├─ birch_slab.json
│  │     │  ├─ birch_stairs.json
│  │     │  ├─ birch_trapdoor.json
│  │     │  ├─ birch_wall_hanging_sign.json
│  │     │  ├─ birch_wall_sign.json
│  │     │  ├─ birch_wood.json
│  │     │  ├─ blackstone.json
│  │     │  ├─ blackstone_slab.json
│  │     │  ├─ blackstone_stairs.json
│  │     │  ├─ blackstone_wall.json
│  │     │  ├─ black_banner.json
│  │     │  ├─ black_bed.json
│  │     │  ├─ black_candle.json
│  │     │  ├─ black_candle_cake.json
│  │     │  ├─ black_carpet.json
│  │     │  ├─ black_concrete.json
│  │     │  ├─ black_concrete_powder.json
│  │     │  ├─ black_glazed_terracotta.json
│  │     │  ├─ black_shulker_box.json
│  │     │  ├─ black_stained_glass.json
│  │     │  ├─ black_stained_glass_pane.json
│  │     │  ├─ black_terracotta.json
│  │     │  ├─ black_wall_banner.json
│  │     │  ├─ black_wool.json
│  │     │  ├─ blast_furnace.json
│  │     │  ├─ blue_banner.json
│  │     │  ├─ blue_bed.json
│  │     │  ├─ blue_candle.json
│  │     │  ├─ blue_candle_cake.json
│  │     │  ├─ blue_carpet.json
│  │     │  ├─ blue_concrete.json
│  │     │  ├─ blue_concrete_powder.json
│  │     │  ├─ blue_glazed_terracotta.json
│  │     │  ├─ blue_ice.json
│  │     │  ├─ blue_orchid.json
│  │     │  ├─ blue_shulker_box.json
│  │     │  ├─ blue_stained_glass.json
│  │     │  ├─ blue_stained_glass_pane.json
│  │     │  ├─ blue_terracotta.json
│  │     │  ├─ blue_wall_banner.json
│  │     │  ├─ blue_wool.json
│  │     │  ├─ bone_block.json
│  │     │  ├─ bookshelf.json
│  │     │  ├─ brain_coral.json
│  │     │  ├─ brain_coral_block.json
│  │     │  ├─ brain_coral_fan.json
│  │     │  ├─ brain_coral_wall_fan.json
│  │     │  ├─ brewing_stand.json
│  │     │  ├─ bricks.json
│  │     │  ├─ brick_slab.json
│  │     │  ├─ brick_stairs.json
│  │     │  ├─ brick_wall.json
│  │     │  ├─ brown_banner.json
│  │     │  ├─ brown_bed.json
│  │     │  ├─ brown_candle.json
│  │     │  ├─ brown_candle_cake.json
│  │     │  ├─ brown_carpet.json
│  │     │  ├─ brown_concrete.json
│  │     │  ├─ brown_concrete_powder.json
│  │     │  ├─ brown_glazed_terracotta.json
│  │     │  ├─ brown_mushroom.json
│  │     │  ├─ brown_mushroom_block.json
│  │     │  ├─ brown_shulker_box.json
│  │     │  ├─ brown_stained_glass.json
│  │     │  ├─ brown_stained_glass_pane.json
│  │     │  ├─ brown_terracotta.json
│  │     │  ├─ brown_wall_banner.json
│  │     │  ├─ brown_wool.json
│  │     │  ├─ bubble_column.json
│  │     │  ├─ bubble_coral.json
│  │     │  ├─ bubble_coral_block.json
│  │     │  ├─ bubble_coral_fan.json
│  │     │  ├─ bubble_coral_wall_fan.json
│  │     │  ├─ budding_amethyst.json
│  │     │  ├─ bush.json
│  │     │  ├─ cactus.json
│  │     │  ├─ cactus_flower.json
│  │     │  ├─ cake.json
│  │     │  ├─ calcite.json
│  │     │  ├─ calibrated_sculk_sensor.json
│  │     │  ├─ campfire.json
│  │     │  ├─ candle.json
│  │     │  ├─ candle_cake.json
│  │     │  ├─ carrots.json
│  │     │  ├─ cartography_table.json
│  │     │  ├─ carved_pumpkin.json
│  │     │  ├─ cauldron.json
│  │     │  ├─ cave_air.json
│  │     │  ├─ cave_vines.json
│  │     │  ├─ cave_vines_plant.json
│  │     │  ├─ chain_command_block.json
│  │     │  ├─ cherry_button.json
│  │     │  ├─ cherry_door.json
│  │     │  ├─ cherry_fence.json
│  │     │  ├─ cherry_fence_gate.json
│  │     │  ├─ cherry_hanging_sign.json
│  │     │  ├─ cherry_leaves.json
│  │     │  ├─ cherry_log.json
│  │     │  ├─ cherry_planks.json
│  │     │  ├─ cherry_pressure_plate.json
│  │     │  ├─ cherry_sapling.json
│  │     │  ├─ cherry_shelf.json
│  │     │  ├─ cherry_sign.json
│  │     │  ├─ cherry_slab.json
│  │     │  ├─ cherry_stairs.json
│  │     │  ├─ cherry_trapdoor.json
│  │     │  ├─ cherry_wall_hanging_sign.json
│  │     │  ├─ cherry_wall_sign.json
│  │     │  ├─ cherry_wood.json
│  │     │  ├─ chest.json
│  │     │  ├─ chipped_anvil.json
│  │     │  ├─ chiseled_bookshelf.json
│  │     │  ├─ chiseled_copper.json
│  │     │  ├─ chiseled_deepslate.json
│  │     │  ├─ chiseled_nether_bricks.json
│  │     │  ├─ chiseled_polished_blackstone.json
│  │     │  ├─ chiseled_quartz_block.json
│  │     │  ├─ chiseled_red_sandstone.json
│  │     │  ├─ chiseled_resin_bricks.json
│  │     │  ├─ chiseled_sandstone.json
│  │     │  ├─ chiseled_stone_bricks.json
│  │     │  ├─ chiseled_tuff.json
│  │     │  ├─ chiseled_tuff_bricks.json
│  │     │  ├─ chorus_flower.json
│  │     │  ├─ chorus_plant.json
│  │     │  ├─ clay.json
│  │     │  ├─ closed_eyeblossom.json
│  │     │  ├─ coal_block.json
│  │     │  ├─ coal_ore.json
│  │     │  ├─ coarse_dirt.json
│  │     │  ├─ cobbled_deepslate.json
│  │     │  ├─ cobbled_deepslate_slab.json
│  │     │  ├─ cobbled_deepslate_stairs.json
│  │     │  ├─ cobbled_deepslate_wall.json
│  │     │  ├─ cobblestone.json
│  │     │  ├─ cobblestone_slab.json
│  │     │  ├─ cobblestone_stairs.json
│  │     │  ├─ cobblestone_wall.json
│  │     │  ├─ cobweb.json
│  │     │  ├─ cocoa.json
│  │     │  ├─ command_block.json
│  │     │  ├─ comparator.json
│  │     │  ├─ composter.json
│  │     │  ├─ conduit.json
│  │     │  ├─ copper_bars.json
│  │     │  ├─ copper_block.json
│  │     │  ├─ copper_bulb.json
│  │     │  ├─ copper_chain.json
│  │     │  ├─ copper_chest.json
│  │     │  ├─ copper_door.json
│  │     │  ├─ copper_golem_statue.json
│  │     │  ├─ copper_grate.json
│  │     │  ├─ copper_lantern.json
│  │     │  ├─ copper_ore.json
│  │     │  ├─ copper_torch.json
│  │     │  ├─ copper_trapdoor.json
│  │     │  ├─ copper_wall_torch.json
│  │     │  ├─ cornflower.json
│  │     │  ├─ cracked_deepslate_bricks.json
│  │     │  ├─ cracked_deepslate_tiles.json
│  │     │  ├─ cracked_nether_bricks.json
│  │     │  ├─ cracked_polished_blackstone_bricks.json
│  │     │  ├─ cracked_stone_bricks.json
│  │     │  ├─ crafter.json
│  │     │  ├─ crafting_table.json
│  │     │  ├─ creaking_heart.json
│  │     │  ├─ creeper_head.json
│  │     │  ├─ creeper_wall_head.json
│  │     │  ├─ crimson_button.json
│  │     │  ├─ crimson_door.json
│  │     │  ├─ crimson_fence.json
│  │     │  ├─ crimson_fence_gate.json
│  │     │  ├─ crimson_fungus.json
│  │     │  ├─ crimson_hanging_sign.json
│  │     │  ├─ crimson_hyphae.json
│  │     │  ├─ crimson_nylium.json
│  │     │  ├─ crimson_planks.json
│  │     │  ├─ crimson_pressure_plate.json
│  │     │  ├─ crimson_roots.json
│  │     │  ├─ crimson_shelf.json
│  │     │  ├─ crimson_sign.json
│  │     │  ├─ crimson_slab.json
│  │     │  ├─ crimson_stairs.json
│  │     │  ├─ crimson_stem.json
│  │     │  ├─ crimson_trapdoor.json
│  │     │  ├─ crimson_wall_hanging_sign.json
│  │     │  ├─ crimson_wall_sign.json
│  │     │  ├─ crying_obsidian.json
│  │     │  ├─ cut_copper.json
│  │     │  ├─ cut_copper_slab.json
│  │     │  ├─ cut_copper_stairs.json
│  │     │  ├─ cut_red_sandstone.json
│  │     │  ├─ cut_red_sandstone_slab.json
│  │     │  ├─ cut_sandstone.json
│  │     │  ├─ cut_sandstone_slab.json
│  │     │  ├─ cyan_banner.json
│  │     │  ├─ cyan_bed.json
│  │     │  ├─ cyan_candle.json
│  │     │  ├─ cyan_candle_cake.json
│  │     │  ├─ cyan_carpet.json
│  │     │  ├─ cyan_concrete.json
│  │     │  ├─ cyan_concrete_powder.json
│  │     │  ├─ cyan_glazed_terracotta.json
│  │     │  ├─ cyan_shulker_box.json
│  │     │  ├─ cyan_stained_glass.json
│  │     │  ├─ cyan_stained_glass_pane.json
│  │     │  ├─ cyan_terracotta.json
│  │     │  ├─ cyan_wall_banner.json
│  │     │  ├─ cyan_wool.json
│  │     │  ├─ damaged_anvil.json
│  │     │  ├─ dandelion.json
│  │     │  ├─ dark_oak_button.json
│  │     │  ├─ dark_oak_door.json
│  │     │  ├─ dark_oak_fence.json
│  │     │  ├─ dark_oak_fence_gate.json
│  │     │  ├─ dark_oak_hanging_sign.json
│  │     │  ├─ dark_oak_leaves.json
│  │     │  ├─ dark_oak_log.json
│  │     │  ├─ dark_oak_planks.json
│  │     │  ├─ dark_oak_pressure_plate.json
│  │     │  ├─ dark_oak_sapling.json
│  │     │  ├─ dark_oak_shelf.json
│  │     │  ├─ dark_oak_sign.json
│  │     │  ├─ dark_oak_slab.json
│  │     │  ├─ dark_oak_stairs.json
│  │     │  ├─ dark_oak_trapdoor.json
│  │     │  ├─ dark_oak_wall_hanging_sign.json
│  │     │  ├─ dark_oak_wall_sign.json
│  │     │  ├─ dark_oak_wood.json
│  │     │  ├─ dark_prismarine.json
│  │     │  ├─ dark_prismarine_slab.json
│  │     │  ├─ dark_prismarine_stairs.json
│  │     │  ├─ daylight_detector.json
│  │     │  ├─ dead_brain_coral.json
│  │     │  ├─ dead_brain_coral_block.json
│  │     │  ├─ dead_brain_coral_fan.json
│  │     │  ├─ dead_brain_coral_wall_fan.json
│  │     │  ├─ dead_bubble_coral.json
│  │     │  ├─ dead_bubble_coral_block.json
│  │     │  ├─ dead_bubble_coral_fan.json
│  │     │  ├─ dead_bubble_coral_wall_fan.json
│  │     │  ├─ dead_bush.json
│  │     │  ├─ dead_fire_coral.json
│  │     │  ├─ dead_fire_coral_block.json
│  │     │  ├─ dead_fire_coral_fan.json
│  │     │  ├─ dead_fire_coral_wall_fan.json
│  │     │  ├─ dead_horn_coral.json
│  │     │  ├─ dead_horn_coral_block.json
│  │     │  ├─ dead_horn_coral_fan.json
│  │     │  ├─ dead_horn_coral_wall_fan.json
│  │     │  ├─ dead_tube_coral.json
│  │     │  ├─ dead_tube_coral_block.json
│  │     │  ├─ dead_tube_coral_fan.json
│  │     │  ├─ dead_tube_coral_wall_fan.json
│  │     │  ├─ decorated_pot.json
│  │     │  ├─ deepslate.json
│  │     │  ├─ deepslate_bricks.json
│  │     │  ├─ deepslate_brick_slab.json
│  │     │  ├─ deepslate_brick_stairs.json
│  │     │  ├─ deepslate_brick_wall.json
│  │     │  ├─ deepslate_coal_ore.json
│  │     │  ├─ deepslate_copper_ore.json
│  │     │  ├─ deepslate_diamond_ore.json
│  │     │  ├─ deepslate_emerald_ore.json
│  │     │  ├─ deepslate_gold_ore.json
│  │     │  ├─ deepslate_iron_ore.json
│  │     │  ├─ deepslate_lapis_ore.json
│  │     │  ├─ deepslate_redstone_ore.json
│  │     │  ├─ deepslate_tiles.json
│  │     │  ├─ deepslate_tile_slab.json
│  │     │  ├─ deepslate_tile_stairs.json
│  │     │  ├─ deepslate_tile_wall.json
│  │     │  ├─ detector_rail.json
│  │     │  ├─ diamond_block.json
│  │     │  ├─ diamond_ore.json
│  │     │  ├─ diorite.json
│  │     │  ├─ diorite_slab.json
│  │     │  ├─ diorite_stairs.json
│  │     │  ├─ diorite_wall.json
│  │     │  ├─ dirt.json
│  │     │  ├─ dirt_path.json
│  │     │  ├─ dispenser.json
│  │     │  ├─ dragon_egg.json
│  │     │  ├─ dragon_head.json
│  │     │  ├─ dragon_wall_head.json
│  │     │  ├─ dried_ghast.json
│  │     │  ├─ dried_kelp_block.json
│  │     │  ├─ dripstone_block.json
│  │     │  ├─ dropper.json
│  │     │  ├─ emerald_block.json
│  │     │  ├─ emerald_ore.json
│  │     │  ├─ enchanting_table.json
│  │     │  ├─ ender_chest.json
│  │     │  ├─ end_gateway.json
│  │     │  ├─ end_portal.json
│  │     │  ├─ end_portal_frame.json
│  │     │  ├─ end_rod.json
│  │     │  ├─ end_stone.json
│  │     │  ├─ end_stone_bricks.json
│  │     │  ├─ end_stone_brick_slab.json
│  │     │  ├─ end_stone_brick_stairs.json
│  │     │  ├─ end_stone_brick_wall.json
│  │     │  ├─ exposed_chiseled_copper.json
│  │     │  ├─ exposed_copper.json
│  │     │  ├─ exposed_copper_bars.json
│  │     │  ├─ exposed_copper_bulb.json
│  │     │  ├─ exposed_copper_chain.json
│  │     │  ├─ exposed_copper_chest.json
│  │     │  ├─ exposed_copper_door.json
│  │     │  ├─ exposed_copper_golem_statue.json
│  │     │  ├─ exposed_copper_grate.json
│  │     │  ├─ exposed_copper_lantern.json
│  │     │  ├─ exposed_copper_trapdoor.json
│  │     │  ├─ exposed_cut_copper.json
│  │     │  ├─ exposed_cut_copper_slab.json
│  │     │  ├─ exposed_cut_copper_stairs.json
│  │     │  ├─ exposed_lightning_rod.json
│  │     │  ├─ farmland.json
│  │     │  ├─ fern.json
│  │     │  ├─ fire.json
│  │     │  ├─ firefly_bush.json
│  │     │  ├─ fire_coral.json
│  │     │  ├─ fire_coral_block.json
│  │     │  ├─ fire_coral_fan.json
│  │     │  ├─ fire_coral_wall_fan.json
│  │     │  ├─ fletching_table.json
│  │     │  ├─ flowering_azalea.json
│  │     │  ├─ flowering_azalea_leaves.json
│  │     │  ├─ flower_pot.json
│  │     │  ├─ frogspawn.json
│  │     │  ├─ frosted_ice.json
│  │     │  ├─ furnace.json
│  │     │  ├─ gilded_blackstone.json
│  │     │  ├─ glass.json
│  │     │  ├─ glass_pane.json
│  │     │  ├─ glowstone.json
│  │     │  ├─ glow_item_frame.json
│  │     │  ├─ glow_lichen.json
│  │     │  ├─ gold_block.json
│  │     │  ├─ gold_ore.json
│  │     │  ├─ granite.json
│  │     │  ├─ granite_slab.json
│  │     │  ├─ granite_stairs.json
│  │     │  ├─ granite_wall.json
│  │     │  ├─ grass_block.json
│  │     │  ├─ gravel.json
│  │     │  ├─ gray_banner.json
│  │     │  ├─ gray_bed.json
│  │     │  ├─ gray_candle.json
│  │     │  ├─ gray_candle_cake.json
│  │     │  ├─ gray_carpet.json
│  │     │  ├─ gray_concrete.json
│  │     │  ├─ gray_concrete_powder.json
│  │     │  ├─ gray_glazed_terracotta.json
│  │     │  ├─ gray_shulker_box.json
│  │     │  ├─ gray_stained_glass.json
│  │     │  ├─ gray_stained_glass_pane.json
│  │     │  ├─ gray_terracotta.json
│  │     │  ├─ gray_wall_banner.json
│  │     │  ├─ gray_wool.json
│  │     │  ├─ green_banner.json
│  │     │  ├─ green_bed.json
│  │     │  ├─ green_candle.json
│  │     │  ├─ green_candle_cake.json
│  │     │  ├─ green_carpet.json
│  │     │  ├─ green_concrete.json
│  │     │  ├─ green_concrete_powder.json
│  │     │  ├─ green_glazed_terracotta.json
│  │     │  ├─ green_shulker_box.json
│  │     │  ├─ green_stained_glass.json
│  │     │  ├─ green_stained_glass_pane.json
│  │     │  ├─ green_terracotta.json
│  │     │  ├─ green_wall_banner.json
│  │     │  ├─ green_wool.json
│  │     │  ├─ grindstone.json
│  │     │  ├─ hanging_roots.json
│  │     │  ├─ hay_block.json
│  │     │  ├─ heavy_core.json
│  │     │  ├─ heavy_weighted_pressure_plate.json
│  │     │  ├─ honeycomb_block.json
│  │     │  ├─ honey_block.json
│  │     │  ├─ hopper.json
│  │     │  ├─ horn_coral.json
│  │     │  ├─ horn_coral_block.json
│  │     │  ├─ horn_coral_fan.json
│  │     │  ├─ horn_coral_wall_fan.json
│  │     │  ├─ ice.json
│  │     │  ├─ infested_chiseled_stone_bricks.json
│  │     │  ├─ infested_cobblestone.json
│  │     │  ├─ infested_cracked_stone_bricks.json
│  │     │  ├─ infested_deepslate.json
│  │     │  ├─ infested_mossy_stone_bricks.json
│  │     │  ├─ infested_stone.json
│  │     │  ├─ infested_stone_bricks.json
│  │     │  ├─ iron_bars.json
│  │     │  ├─ iron_block.json
│  │     │  ├─ iron_chain.json
│  │     │  ├─ iron_door.json
│  │     │  ├─ iron_ore.json
│  │     │  ├─ iron_trapdoor.json
│  │     │  ├─ item_frame.json
│  │     │  ├─ jack_o_lantern.json
│  │     │  ├─ jigsaw.json
│  │     │  ├─ jukebox.json
│  │     │  ├─ jungle_button.json
│  │     │  ├─ jungle_door.json
│  │     │  ├─ jungle_fence.json
│  │     │  ├─ jungle_fence_gate.json
│  │     │  ├─ jungle_hanging_sign.json
│  │     │  ├─ jungle_leaves.json
│  │     │  ├─ jungle_log.json
│  │     │  ├─ jungle_planks.json
│  │     │  ├─ jungle_pressure_plate.json
│  │     │  ├─ jungle_sapling.json
│  │     │  ├─ jungle_shelf.json
│  │     │  ├─ jungle_sign.json
│  │     │  ├─ jungle_slab.json
│  │     │  ├─ jungle_stairs.json
│  │     │  ├─ jungle_trapdoor.json
│  │     │  ├─ jungle_wall_hanging_sign.json
│  │     │  ├─ jungle_wall_sign.json
│  │     │  ├─ jungle_wood.json
│  │     │  ├─ kelp.json
│  │     │  ├─ kelp_plant.json
│  │     │  ├─ ladder.json
│  │     │  ├─ lantern.json
│  │     │  ├─ lapis_block.json
│  │     │  ├─ lapis_ore.json
│  │     │  ├─ large_amethyst_bud.json
│  │     │  ├─ large_fern.json
│  │     │  ├─ lava.json
│  │     │  ├─ lava_cauldron.json
│  │     │  ├─ leaf_litter.json
│  │     │  ├─ lectern.json
│  │     │  ├─ lever.json
│  │     │  ├─ light.json
│  │     │  ├─ lightning_rod.json
│  │     │  ├─ light_blue_banner.json
│  │     │  ├─ light_blue_bed.json
│  │     │  ├─ light_blue_candle.json
│  │     │  ├─ light_blue_candle_cake.json
│  │     │  ├─ light_blue_carpet.json
│  │     │  ├─ light_blue_concrete.json
│  │     │  ├─ light_blue_concrete_powder.json
│  │     │  ├─ light_blue_glazed_terracotta.json
│  │     │  ├─ light_blue_shulker_box.json
│  │     │  ├─ light_blue_stained_glass.json
│  │     │  ├─ light_blue_stained_glass_pane.json
│  │     │  ├─ light_blue_terracotta.json
│  │     │  ├─ light_blue_wall_banner.json
│  │     │  ├─ light_blue_wool.json
│  │     │  ├─ light_gray_banner.json
│  │     │  ├─ light_gray_bed.json
│  │     │  ├─ light_gray_candle.json
│  │     │  ├─ light_gray_candle_cake.json
│  │     │  ├─ light_gray_carpet.json
│  │     │  ├─ light_gray_concrete.json
│  │     │  ├─ light_gray_concrete_powder.json
│  │     │  ├─ light_gray_glazed_terracotta.json
│  │     │  ├─ light_gray_shulker_box.json
│  │     │  ├─ light_gray_stained_glass.json
│  │     │  ├─ light_gray_stained_glass_pane.json
│  │     │  ├─ light_gray_terracotta.json
│  │     │  ├─ light_gray_wall_banner.json
│  │     │  ├─ light_gray_wool.json
│  │     │  ├─ light_weighted_pressure_plate.json
│  │     │  ├─ lilac.json
│  │     │  ├─ lily_of_the_valley.json
│  │     │  ├─ lily_pad.json
│  │     │  ├─ lime_banner.json
│  │     │  ├─ lime_bed.json
│  │     │  ├─ lime_candle.json
│  │     │  ├─ lime_candle_cake.json
│  │     │  ├─ lime_carpet.json
│  │     │  ├─ lime_concrete.json
│  │     │  ├─ lime_concrete_powder.json
│  │     │  ├─ lime_glazed_terracotta.json
│  │     │  ├─ lime_shulker_box.json
│  │     │  ├─ lime_stained_glass.json
│  │     │  ├─ lime_stained_glass_pane.json
│  │     │  ├─ lime_terracotta.json
│  │     │  ├─ lime_wall_banner.json
│  │     │  ├─ lime_wool.json
│  │     │  ├─ lodestone.json
│  │     │  ├─ loom.json
│  │     │  ├─ magenta_banner.json
│  │     │  ├─ magenta_bed.json
│  │     │  ├─ magenta_candle.json
│  │     │  ├─ magenta_candle_cake.json
│  │     │  ├─ magenta_carpet.json
│  │     │  ├─ magenta_concrete.json
│  │     │  ├─ magenta_concrete_powder.json
│  │     │  ├─ magenta_glazed_terracotta.json
│  │     │  ├─ magenta_shulker_box.json
│  │     │  ├─ magenta_stained_glass.json
│  │     │  ├─ magenta_stained_glass_pane.json
│  │     │  ├─ magenta_terracotta.json
│  │     │  ├─ magenta_wall_banner.json
│  │     │  ├─ magenta_wool.json
│  │     │  ├─ magma_block.json
│  │     │  ├─ mangrove_button.json
│  │     │  ├─ mangrove_door.json
│  │     │  ├─ mangrove_fence.json
│  │     │  ├─ mangrove_fence_gate.json
│  │     │  ├─ mangrove_hanging_sign.json
│  │     │  ├─ mangrove_leaves.json
│  │     │  ├─ mangrove_log.json
│  │     │  ├─ mangrove_planks.json
│  │     │  ├─ mangrove_pressure_plate.json
│  │     │  ├─ mangrove_propagule.json
│  │     │  ├─ mangrove_roots.json
│  │     │  ├─ mangrove_shelf.json
│  │     │  ├─ mangrove_sign.json
│  │     │  ├─ mangrove_slab.json
│  │     │  ├─ mangrove_stairs.json
│  │     │  ├─ mangrove_trapdoor.json
│  │     │  ├─ mangrove_wall_hanging_sign.json
│  │     │  ├─ mangrove_wall_sign.json
│  │     │  ├─ mangrove_wood.json
│  │     │  ├─ medium_amethyst_bud.json
│  │     │  ├─ melon.json
│  │     │  ├─ melon_stem.json
│  │     │  ├─ mossy_cobblestone.json
│  │     │  ├─ mossy_cobblestone_slab.json
│  │     │  ├─ mossy_cobblestone_stairs.json
│  │     │  ├─ mossy_cobblestone_wall.json
│  │     │  ├─ mossy_stone_bricks.json
│  │     │  ├─ mossy_stone_brick_slab.json
│  │     │  ├─ mossy_stone_brick_stairs.json
│  │     │  ├─ mossy_stone_brick_wall.json
│  │     │  ├─ moss_block.json
│  │     │  ├─ moss_carpet.json
│  │     │  ├─ moving_piston.json
│  │     │  ├─ mud.json
│  │     │  ├─ muddy_mangrove_roots.json
│  │     │  ├─ mud_bricks.json
│  │     │  ├─ mud_brick_slab.json
│  │     │  ├─ mud_brick_stairs.json
│  │     │  ├─ mud_brick_wall.json
│  │     │  ├─ mushroom_stem.json
│  │     │  ├─ mycelium.json
│  │     │  ├─ netherite_block.json
│  │     │  ├─ netherrack.json
│  │     │  ├─ nether_bricks.json
│  │     │  ├─ nether_brick_fence.json
│  │     │  ├─ nether_brick_slab.json
│  │     │  ├─ nether_brick_stairs.json
│  │     │  ├─ nether_brick_wall.json
│  │     │  ├─ nether_gold_ore.json
│  │     │  ├─ nether_portal.json
│  │     │  ├─ nether_quartz_ore.json
│  │     │  ├─ nether_sprouts.json
│  │     │  ├─ nether_wart.json
│  │     │  ├─ nether_wart_block.json
│  │     │  ├─ note_block.json
│  │     │  ├─ oak_button.json
│  │     │  ├─ oak_door.json
│  │     │  ├─ oak_fence.json
│  │     │  ├─ oak_fence_gate.json
│  │     │  ├─ oak_hanging_sign.json
│  │     │  ├─ oak_leaves.json
│  │     │  ├─ oak_log.json
│  │     │  ├─ oak_planks.json
│  │     │  ├─ oak_pressure_plate.json
│  │     │  ├─ oak_sapling.json
│  │     │  ├─ oak_shelf.json
│  │     │  ├─ oak_sign.json
│  │     │  ├─ oak_slab.json
│  │     │  ├─ oak_stairs.json
│  │     │  ├─ oak_trapdoor.json
│  │     │  ├─ oak_wall_hanging_sign.json
│  │     │  ├─ oak_wall_sign.json
│  │     │  ├─ oak_wood.json
│  │     │  ├─ observer.json
│  │     │  ├─ obsidian.json
│  │     │  ├─ ochre_froglight.json
│  │     │  ├─ open_eyeblossom.json
│  │     │  ├─ orange_banner.json
│  │     │  ├─ orange_bed.json
│  │     │  ├─ orange_candle.json
│  │     │  ├─ orange_candle_cake.json
│  │     │  ├─ orange_carpet.json
│  │     │  ├─ orange_concrete.json
│  │     │  ├─ orange_concrete_powder.json
│  │     │  ├─ orange_glazed_terracotta.json
│  │     │  ├─ orange_shulker_box.json
│  │     │  ├─ orange_stained_glass.json
│  │     │  ├─ orange_stained_glass_pane.json
│  │     │  ├─ orange_terracotta.json
│  │     │  ├─ orange_tulip.json
│  │     │  ├─ orange_wall_banner.json
│  │     │  ├─ orange_wool.json
│  │     │  ├─ oxeye_daisy.json
│  │     │  ├─ oxidized_chiseled_copper.json
│  │     │  ├─ oxidized_copper.json
│  │     │  ├─ oxidized_copper_bars.json
│  │     │  ├─ oxidized_copper_bulb.json
│  │     │  ├─ oxidized_copper_chain.json
│  │     │  ├─ oxidized_copper_chest.json
│  │     │  ├─ oxidized_copper_door.json
│  │     │  ├─ oxidized_copper_golem_statue.json
│  │     │  ├─ oxidized_copper_grate.json
│  │     │  ├─ oxidized_copper_lantern.json
│  │     │  ├─ oxidized_copper_trapdoor.json
│  │     │  ├─ oxidized_cut_copper.json
│  │     │  ├─ oxidized_cut_copper_slab.json
│  │     │  ├─ oxidized_cut_copper_stairs.json
│  │     │  ├─ oxidized_lightning_rod.json
│  │     │  ├─ packed_ice.json
│  │     │  ├─ packed_mud.json
│  │     │  ├─ pale_hanging_moss.json
│  │     │  ├─ pale_moss_block.json
│  │     │  ├─ pale_moss_carpet.json
│  │     │  ├─ pale_oak_button.json
│  │     │  ├─ pale_oak_door.json
│  │     │  ├─ pale_oak_fence.json
│  │     │  ├─ pale_oak_fence_gate.json
│  │     │  ├─ pale_oak_hanging_sign.json
│  │     │  ├─ pale_oak_leaves.json
│  │     │  ├─ pale_oak_log.json
│  │     │  ├─ pale_oak_planks.json
│  │     │  ├─ pale_oak_pressure_plate.json
│  │     │  ├─ pale_oak_sapling.json
│  │     │  ├─ pale_oak_shelf.json
│  │     │  ├─ pale_oak_sign.json
│  │     │  ├─ pale_oak_slab.json
│  │     │  ├─ pale_oak_stairs.json
│  │     │  ├─ pale_oak_trapdoor.json
│  │     │  ├─ pale_oak_wall_hanging_sign.json
│  │     │  ├─ pale_oak_wall_sign.json
│  │     │  ├─ pale_oak_wood.json
│  │     │  ├─ pearlescent_froglight.json
│  │     │  ├─ peony.json
│  │     │  ├─ petrified_oak_slab.json
│  │     │  ├─ piglin_head.json
│  │     │  ├─ piglin_wall_head.json
│  │     │  ├─ pink_banner.json
│  │     │  ├─ pink_bed.json
│  │     │  ├─ pink_candle.json
│  │     │  ├─ pink_candle_cake.json
│  │     │  ├─ pink_carpet.json
│  │     │  ├─ pink_concrete.json
│  │     │  ├─ pink_concrete_powder.json
│  │     │  ├─ pink_glazed_terracotta.json
│  │     │  ├─ pink_petals.json
│  │     │  ├─ pink_shulker_box.json
│  │     │  ├─ pink_stained_glass.json
│  │     │  ├─ pink_stained_glass_pane.json
│  │     │  ├─ pink_terracotta.json
│  │     │  ├─ pink_tulip.json
│  │     │  ├─ pink_wall_banner.json
│  │     │  ├─ pink_wool.json
│  │     │  ├─ piston.json
│  │     │  ├─ piston_head.json
│  │     │  ├─ pitcher_crop.json
│  │     │  ├─ pitcher_plant.json
│  │     │  ├─ player_head.json
│  │     │  ├─ player_wall_head.json
│  │     │  ├─ podzol.json
│  │     │  ├─ pointed_dripstone.json
│  │     │  ├─ polished_andesite.json
│  │     │  ├─ polished_andesite_slab.json
│  │     │  ├─ polished_andesite_stairs.json
│  │     │  ├─ polished_basalt.json
│  │     │  ├─ polished_blackstone.json
│  │     │  ├─ polished_blackstone_bricks.json
│  │     │  ├─ polished_blackstone_brick_slab.json
│  │     │  ├─ polished_blackstone_brick_stairs.json
│  │     │  ├─ polished_blackstone_brick_wall.json
│  │     │  ├─ polished_blackstone_button.json
│  │     │  ├─ polished_blackstone_pressure_plate.json
│  │     │  ├─ polished_blackstone_slab.json
│  │     │  ├─ polished_blackstone_stairs.json
│  │     │  ├─ polished_blackstone_wall.json
│  │     │  ├─ polished_deepslate.json
│  │     │  ├─ polished_deepslate_slab.json
│  │     │  ├─ polished_deepslate_stairs.json
│  │     │  ├─ polished_deepslate_wall.json
│  │     │  ├─ polished_diorite.json
│  │     │  ├─ polished_diorite_slab.json
│  │     │  ├─ polished_diorite_stairs.json
│  │     │  ├─ polished_granite.json
│  │     │  ├─ polished_granite_slab.json
│  │     │  ├─ polished_granite_stairs.json
│  │     │  ├─ polished_tuff.json
│  │     │  ├─ polished_tuff_slab.json
│  │     │  ├─ polished_tuff_stairs.json
│  │     │  ├─ polished_tuff_wall.json
│  │     │  ├─ poppy.json
│  │     │  ├─ potatoes.json
│  │     │  ├─ potted_acacia_sapling.json
│  │     │  ├─ potted_allium.json
│  │     │  ├─ potted_azalea_bush.json
│  │     │  ├─ potted_azure_bluet.json
│  │     │  ├─ potted_bamboo.json
│  │     │  ├─ potted_birch_sapling.json
│  │     │  ├─ potted_blue_orchid.json
│  │     │  ├─ potted_brown_mushroom.json
│  │     │  ├─ potted_cactus.json
│  │     │  ├─ potted_cherry_sapling.json
│  │     │  ├─ potted_closed_eyeblossom.json
│  │     │  ├─ potted_cornflower.json
│  │     │  ├─ potted_crimson_fungus.json
│  │     │  ├─ potted_crimson_roots.json
│  │     │  ├─ potted_dandelion.json
│  │     │  ├─ potted_dark_oak_sapling.json
│  │     │  ├─ potted_dead_bush.json
│  │     │  ├─ potted_fern.json
│  │     │  ├─ potted_flowering_azalea_bush.json
│  │     │  ├─ potted_jungle_sapling.json
│  │     │  ├─ potted_lily_of_the_valley.json
│  │     │  ├─ potted_mangrove_propagule.json
│  │     │  ├─ potted_oak_sapling.json
│  │     │  ├─ potted_open_eyeblossom.json
│  │     │  ├─ potted_orange_tulip.json
│  │     │  ├─ potted_oxeye_daisy.json
│  │     │  ├─ potted_pale_oak_sapling.json
│  │     │  ├─ potted_pink_tulip.json
│  │     │  ├─ potted_poppy.json
│  │     │  ├─ potted_red_mushroom.json
│  │     │  ├─ potted_red_tulip.json
│  │     │  ├─ potted_spruce_sapling.json
│  │     │  ├─ potted_torchflower.json
│  │     │  ├─ potted_warped_fungus.json
│  │     │  ├─ potted_warped_roots.json
│  │     │  ├─ potted_white_tulip.json
│  │     │  ├─ potted_wither_rose.json
│  │     │  ├─ powder_snow.json
│  │     │  ├─ powder_snow_cauldron.json
│  │     │  ├─ powered_rail.json
│  │     │  ├─ prismarine.json
│  │     │  ├─ prismarine_bricks.json
│  │     │  ├─ prismarine_brick_slab.json
│  │     │  ├─ prismarine_brick_stairs.json
│  │     │  ├─ prismarine_slab.json
│  │     │  ├─ prismarine_stairs.json
│  │     │  ├─ prismarine_wall.json
│  │     │  ├─ pumpkin.json
│  │     │  ├─ pumpkin_stem.json
│  │     │  ├─ purple_banner.json
│  │     │  ├─ purple_bed.json
│  │     │  ├─ purple_candle.json
│  │     │  ├─ purple_candle_cake.json
│  │     │  ├─ purple_carpet.json
│  │     │  ├─ purple_concrete.json
│  │     │  ├─ purple_concrete_powder.json
│  │     │  ├─ purple_glazed_terracotta.json
│  │     │  ├─ purple_shulker_box.json
│  │     │  ├─ purple_stained_glass.json
│  │     │  ├─ purple_stained_glass_pane.json
│  │     │  ├─ purple_terracotta.json
│  │     │  ├─ purple_wall_banner.json
│  │     │  ├─ purple_wool.json
│  │     │  ├─ purpur_block.json
│  │     │  ├─ purpur_pillar.json
│  │     │  ├─ purpur_slab.json
│  │     │  ├─ purpur_stairs.json
│  │     │  ├─ quartz_block.json
│  │     │  ├─ quartz_bricks.json
│  │     │  ├─ quartz_pillar.json
│  │     │  ├─ quartz_slab.json
│  │     │  ├─ quartz_stairs.json
│  │     │  ├─ rail.json
│  │     │  ├─ raw_copper_block.json
│  │     │  ├─ raw_gold_block.json
│  │     │  ├─ raw_iron_block.json
│  │     │  ├─ redstone_block.json
│  │     │  ├─ redstone_lamp.json
│  │     │  ├─ redstone_ore.json
│  │     │  ├─ redstone_torch.json
│  │     │  ├─ redstone_wall_torch.json
│  │     │  ├─ redstone_wire.json
│  │     │  ├─ red_banner.json
│  │     │  ├─ red_bed.json
│  │     │  ├─ red_candle.json
│  │     │  ├─ red_candle_cake.json
│  │     │  ├─ red_carpet.json
│  │     │  ├─ red_concrete.json
│  │     │  ├─ red_concrete_powder.json
│  │     │  ├─ red_glazed_terracotta.json
│  │     │  ├─ red_mushroom.json
│  │     │  ├─ red_mushroom_block.json
│  │     │  ├─ red_nether_bricks.json
│  │     │  ├─ red_nether_brick_slab.json
│  │     │  ├─ red_nether_brick_stairs.json
│  │     │  ├─ red_nether_brick_wall.json
│  │     │  ├─ red_sand.json
│  │     │  ├─ red_sandstone.json
│  │     │  ├─ red_sandstone_slab.json
│  │     │  ├─ red_sandstone_stairs.json
│  │     │  ├─ red_sandstone_wall.json
│  │     │  ├─ red_shulker_box.json
│  │     │  ├─ red_stained_glass.json
│  │     │  ├─ red_stained_glass_pane.json
│  │     │  ├─ red_terracotta.json
│  │     │  ├─ red_tulip.json
│  │     │  ├─ red_wall_banner.json
│  │     │  ├─ red_wool.json
│  │     │  ├─ reinforced_deepslate.json
│  │     │  ├─ repeater.json
│  │     │  ├─ repeating_command_block.json
│  │     │  ├─ resin_block.json
│  │     │  ├─ resin_bricks.json
│  │     │  ├─ resin_brick_slab.json
│  │     │  ├─ resin_brick_stairs.json
│  │     │  ├─ resin_brick_wall.json
│  │     │  ├─ resin_clump.json
│  │     │  ├─ respawn_anchor.json
│  │     │  ├─ rooted_dirt.json
│  │     │  ├─ rose_bush.json
│  │     │  ├─ sand.json
│  │     │  ├─ sandstone.json
│  │     │  ├─ sandstone_slab.json
│  │     │  ├─ sandstone_stairs.json
│  │     │  ├─ sandstone_wall.json
│  │     │  ├─ scaffolding.json
│  │     │  ├─ sculk.json
│  │     │  ├─ sculk_catalyst.json
│  │     │  ├─ sculk_sensor.json
│  │     │  ├─ sculk_shrieker.json
│  │     │  ├─ sculk_vein.json
│  │     │  ├─ seagrass.json
│  │     │  ├─ sea_lantern.json
│  │     │  ├─ sea_pickle.json
│  │     │  ├─ short_dry_grass.json
│  │     │  ├─ short_grass.json
│  │     │  ├─ shroomlight.json
│  │     │  ├─ shulker_box.json
│  │     │  ├─ skeleton_skull.json
│  │     │  ├─ skeleton_wall_skull.json
│  │     │  ├─ slime_block.json
│  │     │  ├─ small_amethyst_bud.json
│  │     │  ├─ small_dripleaf.json
│  │     │  ├─ smithing_table.json
│  │     │  ├─ smoker.json
│  │     │  ├─ smooth_basalt.json
│  │     │  ├─ smooth_quartz.json
│  │     │  ├─ smooth_quartz_slab.json
│  │     │  ├─ smooth_quartz_stairs.json
│  │     │  ├─ smooth_red_sandstone.json
│  │     │  ├─ smooth_red_sandstone_slab.json
│  │     │  ├─ smooth_red_sandstone_stairs.json
│  │     │  ├─ smooth_sandstone.json
│  │     │  ├─ smooth_sandstone_slab.json
│  │     │  ├─ smooth_sandstone_stairs.json
│  │     │  ├─ smooth_stone.json
│  │     │  ├─ smooth_stone_slab.json
│  │     │  ├─ sniffer_egg.json
│  │     │  ├─ snow.json
│  │     │  ├─ snow_block.json
│  │     │  ├─ soul_campfire.json
│  │     │  ├─ soul_fire.json
│  │     │  ├─ soul_lantern.json
│  │     │  ├─ soul_sand.json
│  │     │  ├─ soul_soil.json
│  │     │  ├─ soul_torch.json
│  │     │  ├─ soul_wall_torch.json
│  │     │  ├─ spawner.json
│  │     │  ├─ sponge.json
│  │     │  ├─ spore_blossom.json
│  │     │  ├─ spruce_button.json
│  │     │  ├─ spruce_door.json
│  │     │  ├─ spruce_fence.json
│  │     │  ├─ spruce_fence_gate.json
│  │     │  ├─ spruce_hanging_sign.json
│  │     │  ├─ spruce_leaves.json
│  │     │  ├─ spruce_log.json
│  │     │  ├─ spruce_planks.json
│  │     │  ├─ spruce_pressure_plate.json
│  │     │  ├─ spruce_sapling.json
│  │     │  ├─ spruce_shelf.json
│  │     │  ├─ spruce_sign.json
│  │     │  ├─ spruce_slab.json
│  │     │  ├─ spruce_stairs.json
│  │     │  ├─ spruce_trapdoor.json
│  │     │  ├─ spruce_wall_hanging_sign.json
│  │     │  ├─ spruce_wall_sign.json
│  │     │  ├─ spruce_wood.json
│  │     │  ├─ sticky_piston.json
│  │     │  ├─ stone.json
│  │     │  ├─ stonecutter.json
│  │     │  ├─ stone_bricks.json
│  │     │  ├─ stone_brick_slab.json
│  │     │  ├─ stone_brick_stairs.json
│  │     │  ├─ stone_brick_wall.json
│  │     │  ├─ stone_button.json
│  │     │  ├─ stone_pressure_plate.json
│  │     │  ├─ stone_slab.json
│  │     │  ├─ stone_stairs.json
│  │     │  ├─ stripped_acacia_log.json
│  │     │  ├─ stripped_acacia_wood.json
│  │     │  ├─ stripped_bamboo_block.json
│  │     │  ├─ stripped_birch_log.json
│  │     │  ├─ stripped_birch_wood.json
│  │     │  ├─ stripped_cherry_log.json
│  │     │  ├─ stripped_cherry_wood.json
│  │     │  ├─ stripped_crimson_hyphae.json
│  │     │  ├─ stripped_crimson_stem.json
│  │     │  ├─ stripped_dark_oak_log.json
│  │     │  ├─ stripped_dark_oak_wood.json
│  │     │  ├─ stripped_jungle_log.json
│  │     │  ├─ stripped_jungle_wood.json
│  │     │  ├─ stripped_mangrove_log.json
│  │     │  ├─ stripped_mangrove_wood.json
│  │     │  ├─ stripped_oak_log.json
│  │     │  ├─ stripped_oak_wood.json
│  │     │  ├─ stripped_pale_oak_log.json
│  │     │  ├─ stripped_pale_oak_wood.json
│  │     │  ├─ stripped_spruce_log.json
│  │     │  ├─ stripped_spruce_wood.json
│  │     │  ├─ stripped_warped_hyphae.json
│  │     │  ├─ stripped_warped_stem.json
│  │     │  ├─ structure_block.json
│  │     │  ├─ structure_void.json
│  │     │  ├─ sugar_cane.json
│  │     │  ├─ sunflower.json
│  │     │  ├─ suspicious_gravel.json
│  │     │  ├─ suspicious_sand.json
│  │     │  ├─ sweet_berry_bush.json
│  │     │  ├─ tall_dry_grass.json
│  │     │  ├─ tall_grass.json
│  │     │  ├─ tall_seagrass.json
│  │     │  ├─ target.json
│  │     │  ├─ terracotta.json
│  │     │  ├─ test_block.json
│  │     │  ├─ test_instance_block.json
│  │     │  ├─ tinted_glass.json
│  │     │  ├─ tnt.json
│  │     │  ├─ torch.json
│  │     │  ├─ torchflower.json
│  │     │  ├─ torchflower_crop.json
│  │     │  ├─ trapped_chest.json
│  │     │  ├─ trial_spawner.json
│  │     │  ├─ tripwire.json
│  │     │  ├─ tripwire_hook.json
│  │     │  ├─ tube_coral.json
│  │     │  ├─ tube_coral_block.json
│  │     │  ├─ tube_coral_fan.json
│  │     │  ├─ tube_coral_wall_fan.json
│  │     │  ├─ tuff.json
│  │     │  ├─ tuff_bricks.json
│  │     │  ├─ tuff_brick_slab.json
│  │     │  ├─ tuff_brick_stairs.json
│  │     │  ├─ tuff_brick_wall.json
│  │     │  ├─ tuff_slab.json
│  │     │  ├─ tuff_stairs.json
│  │     │  ├─ tuff_wall.json
│  │     │  ├─ turtle_egg.json
│  │     │  ├─ twisting_vines.json
│  │     │  ├─ twisting_vines_plant.json
│  │     │  ├─ vault.json
│  │     │  ├─ verdant_froglight.json
│  │     │  ├─ vine.json
│  │     │  ├─ void_air.json
│  │     │  ├─ wall_torch.json
│  │     │  ├─ warped_button.json
│  │     │  ├─ warped_door.json
│  │     │  ├─ warped_fence.json
│  │     │  ├─ warped_fence_gate.json
│  │     │  ├─ warped_fungus.json
│  │     │  ├─ warped_hanging_sign.json
│  │     │  ├─ warped_hyphae.json
│  │     │  ├─ warped_nylium.json
│  │     │  ├─ warped_planks.json
│  │     │  ├─ warped_pressure_plate.json
│  │     │  ├─ warped_roots.json
│  │     │  ├─ warped_shelf.json
│  │     │  ├─ warped_sign.json
│  │     │  ├─ warped_slab.json
│  │     │  ├─ warped_stairs.json
│  │     │  ├─ warped_stem.json
│  │     │  ├─ warped_trapdoor.json
│  │     │  ├─ warped_wall_hanging_sign.json
│  │     │  ├─ warped_wall_sign.json
│  │     │  ├─ warped_wart_block.json
│  │     │  ├─ water.json
│  │     │  ├─ water_cauldron.json
│  │     │  ├─ waxed_chiseled_copper.json
│  │     │  ├─ waxed_copper_bars.json
│  │     │  ├─ waxed_copper_block.json
│  │     │  ├─ waxed_copper_bulb.json
│  │     │  ├─ waxed_copper_chain.json
│  │     │  ├─ waxed_copper_chest.json
│  │     │  ├─ waxed_copper_door.json
│  │     │  ├─ waxed_copper_golem_statue.json
│  │     │  ├─ waxed_copper_grate.json
│  │     │  ├─ waxed_copper_lantern.json
│  │     │  ├─ waxed_copper_trapdoor.json
│  │     │  ├─ waxed_cut_copper.json
│  │     │  ├─ waxed_cut_copper_slab.json
│  │     │  ├─ waxed_cut_copper_stairs.json
│  │     │  ├─ waxed_exposed_chiseled_copper.json
│  │     │  ├─ waxed_exposed_copper.json
│  │     │  ├─ waxed_exposed_copper_bars.json
│  │     │  ├─ waxed_exposed_copper_bulb.json
│  │     │  ├─ waxed_exposed_copper_chain.json
│  │     │  ├─ waxed_exposed_copper_chest.json
│  │     │  ├─ waxed_exposed_copper_door.json
│  │     │  ├─ waxed_exposed_copper_golem_statue.json
│  │     │  ├─ waxed_exposed_copper_grate.json
│  │     │  ├─ waxed_exposed_copper_lantern.json
│  │     │  ├─ waxed_exposed_copper_trapdoor.json
│  │     │  ├─ waxed_exposed_cut_copper.json
│  │     │  ├─ waxed_exposed_cut_copper_slab.json
│  │     │  ├─ waxed_exposed_cut_copper_stairs.json
│  │     │  ├─ waxed_exposed_lightning_rod.json
│  │     │  ├─ waxed_lightning_rod.json
│  │     │  ├─ waxed_oxidized_chiseled_copper.json
│  │     │  ├─ waxed_oxidized_copper.json
│  │     │  ├─ waxed_oxidized_copper_bars.json
│  │     │  ├─ waxed_oxidized_copper_bulb.json
│  │     │  ├─ waxed_oxidized_copper_chain.json
│  │     │  ├─ waxed_oxidized_copper_chest.json
│  │     │  ├─ waxed_oxidized_copper_door.json
│  │     │  ├─ waxed_oxidized_copper_golem_statue.json
│  │     │  ├─ waxed_oxidized_copper_grate.json
│  │     │  ├─ waxed_oxidized_copper_lantern.json
│  │     │  ├─ waxed_oxidized_copper_trapdoor.json
│  │     │  ├─ waxed_oxidized_cut_copper.json
│  │     │  ├─ waxed_oxidized_cut_copper_slab.json
│  │     │  ├─ waxed_oxidized_cut_copper_stairs.json
│  │     │  ├─ waxed_oxidized_lightning_rod.json
│  │     │  ├─ waxed_weathered_chiseled_copper.json
│  │     │  ├─ waxed_weathered_copper.json
│  │     │  ├─ waxed_weathered_copper_bars.json
│  │     │  ├─ waxed_weathered_copper_bulb.json
│  │     │  ├─ waxed_weathered_copper_chain.json
│  │     │  ├─ waxed_weathered_copper_chest.json
│  │     │  ├─ waxed_weathered_copper_door.json
│  │     │  ├─ waxed_weathered_copper_golem_statue.json
│  │     │  ├─ waxed_weathered_copper_grate.json
│  │     │  ├─ waxed_weathered_copper_lantern.json
│  │     │  ├─ waxed_weathered_copper_trapdoor.json
│  │     │  ├─ waxed_weathered_cut_copper.json
│  │     │  ├─ waxed_weathered_cut_copper_slab.json
│  │     │  ├─ waxed_weathered_cut_copper_stairs.json
│  │     │  ├─ waxed_weathered_lightning_rod.json
│  │     │  ├─ weathered_chiseled_copper.json
│  │     │  ├─ weathered_copper.json
│  │     │  ├─ weathered_copper_bars.json
│  │     │  ├─ weathered_copper_bulb.json
│  │     │  ├─ weathered_copper_chain.json
│  │     │  ├─ weathered_copper_chest.json
│  │     │  ├─ weathered_copper_door.json
│  │     │  ├─ weathered_copper_golem_statue.json
│  │     │  ├─ weathered_copper_grate.json
│  │     │  ├─ weathered_copper_lantern.json
│  │     │  ├─ weathered_copper_trapdoor.json
│  │     │  ├─ weathered_cut_copper.json
│  │     │  ├─ weathered_cut_copper_slab.json
│  │     │  ├─ weathered_cut_copper_stairs.json
│  │     │  ├─ weathered_lightning_rod.json
│  │     │  ├─ weeping_vines.json
│  │     │  ├─ weeping_vines_plant.json
│  │     │  ├─ wet_sponge.json
│  │     │  ├─ wheat.json
│  │     │  ├─ white_banner.json
│  │     │  ├─ white_bed.json
│  │     │  ├─ white_candle.json
│  │     │  ├─ white_candle_cake.json
│  │     │  ├─ white_carpet.json
│  │     │  ├─ white_concrete.json
│  │     │  ├─ white_concrete_powder.json
│  │     │  ├─ white_glazed_terracotta.json
│  │     │  ├─ white_shulker_box.json
│  │     │  ├─ white_stained_glass.json
│  │     │  ├─ white_stained_glass_pane.json
│  │     │  ├─ white_terracotta.json
│  │     │  ├─ white_tulip.json
│  │     │  ├─ white_wall_banner.json
│  │     │  ├─ white_wool.json
│  │     │  ├─ wildflowers.json
│  │     │  ├─ wither_rose.json
│  │     │  ├─ wither_skeleton_skull.json
│  │     │  ├─ wither_skeleton_wall_skull.json
│  │     │  ├─ yellow_banner.json
│  │     │  ├─ yellow_bed.json
│  │     │  ├─ yellow_candle.json
│  │     │  ├─ yellow_candle_cake.json
│  │     │  ├─ yellow_carpet.json
│  │     │  ├─ yellow_concrete.json
│  │     │  ├─ yellow_concrete_powder.json
│  │     │  ├─ yellow_glazed_terracotta.json
│  │     │  ├─ yellow_shulker_box.json
│  │     │  ├─ yellow_stained_glass.json
│  │     │  ├─ yellow_stained_glass_pane.json
│  │     │  ├─ yellow_terracotta.json
│  │     │  ├─ yellow_wall_banner.json
│  │     │  ├─ yellow_wool.json
│  │     │  ├─ zombie_head.json
│  │     │  └─ zombie_wall_head.json
│  │     ├─ equipment
│  │     │  ├─ armadillo_scute.json
│  │     │  ├─ black_carpet.json
│  │     │  ├─ black_harness.json
│  │     │  ├─ blue_carpet.json
│  │     │  ├─ blue_harness.json
│  │     │  ├─ brown_carpet.json
│  │     │  ├─ brown_harness.json
│  │     │  ├─ chainmail.json
│  │     │  ├─ copper.json
│  │     │  ├─ cyan_carpet.json
│  │     │  ├─ cyan_harness.json
│  │     │  ├─ diamond.json
│  │     │  ├─ elytra.json
│  │     │  ├─ gold.json
│  │     │  ├─ gray_carpet.json
│  │     │  ├─ gray_harness.json
│  │     │  ├─ green_carpet.json
│  │     │  ├─ green_harness.json
│  │     │  ├─ iron.json
│  │     │  ├─ leather.json
│  │     │  ├─ light_blue_carpet.json
│  │     │  ├─ light_blue_harness.json
│  │     │  ├─ light_gray_carpet.json
│  │     │  ├─ light_gray_harness.json
│  │     │  ├─ lime_carpet.json
│  │     │  ├─ lime_harness.json
│  │     │  ├─ magenta_carpet.json
│  │     │  ├─ magenta_harness.json
│  │     │  ├─ netherite.json
│  │     │  ├─ orange_carpet.json
│  │     │  ├─ orange_harness.json
│  │     │  ├─ pink_carpet.json
│  │     │  ├─ pink_harness.json
│  │     │  ├─ purple_carpet.json
│  │     │  ├─ purple_harness.json
│  │     │  ├─ red_carpet.json
│  │     │  ├─ red_harness.json
│  │     │  ├─ saddle.json
│  │     │  ├─ trader_llama.json
│  │     │  ├─ turtle_scute.json
│  │     │  ├─ white_carpet.json
│  │     │  ├─ white_harness.json
│  │     │  ├─ yellow_carpet.json
│  │     │  └─ yellow_harness.json
│  │     ├─ font
│  │     │  ├─ alt.json
│  │     │  ├─ default.json
│  │     │  ├─ illageralt.json
│  │     │  ├─ include
│  │     │  │  ├─ default.json
│  │     │  │  ├─ space.json
│  │     │  │  └─ unifont.json
│  │     │  └─ uniform.json
│  │     ├─ gpu_warnlist.json
│  │     ├─ items
│  │     │  ├─ acacia_boat.json
│  │     │  ├─ acacia_button.json
│  │     │  ├─ acacia_chest_boat.json
│  │     │  ├─ acacia_door.json
│  │     │  ├─ acacia_fence.json
│  │     │  ├─ acacia_fence_gate.json
│  │     │  ├─ acacia_hanging_sign.json
│  │     │  ├─ acacia_leaves.json
│  │     │  ├─ acacia_log.json
│  │     │  ├─ acacia_planks.json
│  │     │  ├─ acacia_pressure_plate.json
│  │     │  ├─ acacia_sapling.json
│  │     │  ├─ acacia_shelf.json
│  │     │  ├─ acacia_sign.json
│  │     │  ├─ acacia_slab.json
│  │     │  ├─ acacia_stairs.json
│  │     │  ├─ acacia_trapdoor.json
│  │     │  ├─ acacia_wood.json
│  │     │  ├─ activator_rail.json
│  │     │  ├─ air.json
│  │     │  ├─ allay_spawn_egg.json
│  │     │  ├─ allium.json
│  │     │  ├─ amethyst_block.json
│  │     │  ├─ amethyst_cluster.json
│  │     │  ├─ amethyst_shard.json
│  │     │  ├─ ancient_debris.json
│  │     │  ├─ andesite.json
│  │     │  ├─ andesite_slab.json
│  │     │  ├─ andesite_stairs.json
│  │     │  ├─ andesite_wall.json
│  │     │  ├─ angler_pottery_sherd.json
│  │     │  ├─ anvil.json
│  │     │  ├─ apple.json
│  │     │  ├─ archer_pottery_sherd.json
│  │     │  ├─ armadillo_scute.json
│  │     │  ├─ armadillo_spawn_egg.json
│  │     │  ├─ armor_stand.json
│  │     │  ├─ arms_up_pottery_sherd.json
│  │     │  ├─ arrow.json
│  │     │  ├─ axolotl_bucket.json
│  │     │  ├─ axolotl_spawn_egg.json
│  │     │  ├─ azalea.json
│  │     │  ├─ azalea_leaves.json
│  │     │  ├─ azure_bluet.json
│  │     │  ├─ baked_potato.json
│  │     │  ├─ bamboo.json
│  │     │  ├─ bamboo_block.json
│  │     │  ├─ bamboo_button.json
│  │     │  ├─ bamboo_chest_raft.json
│  │     │  ├─ bamboo_door.json
│  │     │  ├─ bamboo_fence.json
│  │     │  ├─ bamboo_fence_gate.json
│  │     │  ├─ bamboo_hanging_sign.json
│  │     │  ├─ bamboo_mosaic.json
│  │     │  ├─ bamboo_mosaic_slab.json
│  │     │  ├─ bamboo_mosaic_stairs.json
│  │     │  ├─ bamboo_planks.json
│  │     │  ├─ bamboo_pressure_plate.json
│  │     │  ├─ bamboo_raft.json
│  │     │  ├─ bamboo_shelf.json
│  │     │  ├─ bamboo_sign.json
│  │     │  ├─ bamboo_slab.json
│  │     │  ├─ bamboo_stairs.json
│  │     │  ├─ bamboo_trapdoor.json
│  │     │  ├─ barrel.json
│  │     │  ├─ barrier.json
│  │     │  ├─ basalt.json
│  │     │  ├─ bat_spawn_egg.json
│  │     │  ├─ beacon.json
│  │     │  ├─ bedrock.json
│  │     │  ├─ beef.json
│  │     │  ├─ beehive.json
│  │     │  ├─ beetroot.json
│  │     │  ├─ beetroot_seeds.json
│  │     │  ├─ beetroot_soup.json
│  │     │  ├─ bee_nest.json
│  │     │  ├─ bee_spawn_egg.json
│  │     │  ├─ bell.json
│  │     │  ├─ big_dripleaf.json
│  │     │  ├─ birch_boat.json
│  │     │  ├─ birch_button.json
│  │     │  ├─ birch_chest_boat.json
│  │     │  ├─ birch_door.json
│  │     │  ├─ birch_fence.json
│  │     │  ├─ birch_fence_gate.json
│  │     │  ├─ birch_hanging_sign.json
│  │     │  ├─ birch_leaves.json
│  │     │  ├─ birch_log.json
│  │     │  ├─ birch_planks.json
│  │     │  ├─ birch_pressure_plate.json
│  │     │  ├─ birch_sapling.json
│  │     │  ├─ birch_shelf.json
│  │     │  ├─ birch_sign.json
│  │     │  ├─ birch_slab.json
│  │     │  ├─ birch_stairs.json
│  │     │  ├─ birch_trapdoor.json
│  │     │  ├─ birch_wood.json
│  │     │  ├─ blackstone.json
│  │     │  ├─ blackstone_slab.json
│  │     │  ├─ blackstone_stairs.json
│  │     │  ├─ blackstone_wall.json
│  │     │  ├─ black_banner.json
│  │     │  ├─ black_bed.json
│  │     │  ├─ black_bundle.json
│  │     │  ├─ black_candle.json
│  │     │  ├─ black_carpet.json
│  │     │  ├─ black_concrete.json
│  │     │  ├─ black_concrete_powder.json
│  │     │  ├─ black_dye.json
│  │     │  ├─ black_glazed_terracotta.json
│  │     │  ├─ black_harness.json
│  │     │  ├─ black_shulker_box.json
│  │     │  ├─ black_stained_glass.json
│  │     │  ├─ black_stained_glass_pane.json
│  │     │  ├─ black_terracotta.json
│  │     │  ├─ black_wool.json
│  │     │  ├─ blade_pottery_sherd.json
│  │     │  ├─ blast_furnace.json
│  │     │  ├─ blaze_powder.json
│  │     │  ├─ blaze_rod.json
│  │     │  ├─ blaze_spawn_egg.json
│  │     │  ├─ blue_banner.json
│  │     │  ├─ blue_bed.json
│  │     │  ├─ blue_bundle.json
│  │     │  ├─ blue_candle.json
│  │     │  ├─ blue_carpet.json
│  │     │  ├─ blue_concrete.json
│  │     │  ├─ blue_concrete_powder.json
│  │     │  ├─ blue_dye.json
│  │     │  ├─ blue_egg.json
│  │     │  ├─ blue_glazed_terracotta.json
│  │     │  ├─ blue_harness.json
│  │     │  ├─ blue_ice.json
│  │     │  ├─ blue_orchid.json
│  │     │  ├─ blue_shulker_box.json
│  │     │  ├─ blue_stained_glass.json
│  │     │  ├─ blue_stained_glass_pane.json
│  │     │  ├─ blue_terracotta.json
│  │     │  ├─ blue_wool.json
│  │     │  ├─ bogged_spawn_egg.json
│  │     │  ├─ bolt_armor_trim_smithing_template.json
│  │     │  ├─ bone.json
│  │     │  ├─ bone_block.json
│  │     │  ├─ bone_meal.json
│  │     │  ├─ book.json
│  │     │  ├─ bookshelf.json
│  │     │  ├─ bordure_indented_banner_pattern.json
│  │     │  ├─ bow.json
│  │     │  ├─ bowl.json
│  │     │  ├─ brain_coral.json
│  │     │  ├─ brain_coral_block.json
│  │     │  ├─ brain_coral_fan.json
│  │     │  ├─ bread.json
│  │     │  ├─ breeze_rod.json
│  │     │  ├─ breeze_spawn_egg.json
│  │     │  ├─ brewer_pottery_sherd.json
│  │     │  ├─ brewing_stand.json
│  │     │  ├─ brick.json
│  │     │  ├─ bricks.json
│  │     │  ├─ brick_slab.json
│  │     │  ├─ brick_stairs.json
│  │     │  ├─ brick_wall.json
│  │     │  ├─ brown_banner.json
│  │     │  ├─ brown_bed.json
│  │     │  ├─ brown_bundle.json
│  │     │  ├─ brown_candle.json
│  │     │  ├─ brown_carpet.json
│  │     │  ├─ brown_concrete.json
│  │     │  ├─ brown_concrete_powder.json
│  │     │  ├─ brown_dye.json
│  │     │  ├─ brown_egg.json
│  │     │  ├─ brown_glazed_terracotta.json
│  │     │  ├─ brown_harness.json
│  │     │  ├─ brown_mushroom.json
│  │     │  ├─ brown_mushroom_block.json
│  │     │  ├─ brown_shulker_box.json
│  │     │  ├─ brown_stained_glass.json
│  │     │  ├─ brown_stained_glass_pane.json
│  │     │  ├─ brown_terracotta.json
│  │     │  ├─ brown_wool.json
│  │     │  ├─ brush.json
│  │     │  ├─ bubble_coral.json
│  │     │  ├─ bubble_coral_block.json
│  │     │  ├─ bubble_coral_fan.json
│  │     │  ├─ bucket.json
│  │     │  ├─ budding_amethyst.json
│  │     │  ├─ bundle.json
│  │     │  ├─ burn_pottery_sherd.json
│  │     │  ├─ bush.json
│  │     │  ├─ cactus.json
│  │     │  ├─ cactus_flower.json
│  │     │  ├─ cake.json
│  │     │  ├─ calcite.json
│  │     │  ├─ calibrated_sculk_sensor.json
│  │     │  ├─ camel_husk_spawn_egg.json
│  │     │  ├─ camel_spawn_egg.json
│  │     │  ├─ campfire.json
│  │     │  ├─ candle.json
│  │     │  ├─ carrot.json
│  │     │  ├─ carrot_on_a_stick.json
│  │     │  ├─ cartography_table.json
│  │     │  ├─ carved_pumpkin.json
│  │     │  ├─ cat_spawn_egg.json
│  │     │  ├─ cauldron.json
│  │     │  ├─ cave_spider_spawn_egg.json
│  │     │  ├─ chainmail_boots.json
│  │     │  ├─ chainmail_chestplate.json
│  │     │  ├─ chainmail_helmet.json
│  │     │  ├─ chainmail_leggings.json
│  │     │  ├─ chain_command_block.json
│  │     │  ├─ charcoal.json
│  │     │  ├─ cherry_boat.json
│  │     │  ├─ cherry_button.json
│  │     │  ├─ cherry_chest_boat.json
│  │     │  ├─ cherry_door.json
│  │     │  ├─ cherry_fence.json
│  │     │  ├─ cherry_fence_gate.json
│  │     │  ├─ cherry_hanging_sign.json
│  │     │  ├─ cherry_leaves.json
│  │     │  ├─ cherry_log.json
│  │     │  ├─ cherry_planks.json
│  │     │  ├─ cherry_pressure_plate.json
│  │     │  ├─ cherry_sapling.json
│  │     │  ├─ cherry_shelf.json
│  │     │  ├─ cherry_sign.json
│  │     │  ├─ cherry_slab.json
│  │     │  ├─ cherry_stairs.json
│  │     │  ├─ cherry_trapdoor.json
│  │     │  ├─ cherry_wood.json
│  │     │  ├─ chest.json
│  │     │  ├─ chest_minecart.json
│  │     │  ├─ chicken.json
│  │     │  ├─ chicken_spawn_egg.json
│  │     │  ├─ chipped_anvil.json
│  │     │  ├─ chiseled_bookshelf.json
│  │     │  ├─ chiseled_copper.json
│  │     │  ├─ chiseled_deepslate.json
│  │     │  ├─ chiseled_nether_bricks.json
│  │     │  ├─ chiseled_polished_blackstone.json
│  │     │  ├─ chiseled_quartz_block.json
│  │     │  ├─ chiseled_red_sandstone.json
│  │     │  ├─ chiseled_resin_bricks.json
│  │     │  ├─ chiseled_sandstone.json
│  │     │  ├─ chiseled_stone_bricks.json
│  │     │  ├─ chiseled_tuff.json
│  │     │  ├─ chiseled_tuff_bricks.json
│  │     │  ├─ chorus_flower.json
│  │     │  ├─ chorus_fruit.json
│  │     │  ├─ chorus_plant.json
│  │     │  ├─ clay.json
│  │     │  ├─ clay_ball.json
│  │     │  ├─ clock.json
│  │     │  ├─ closed_eyeblossom.json
│  │     │  ├─ coal.json
│  │     │  ├─ coal_block.json
│  │     │  ├─ coal_ore.json
│  │     │  ├─ coarse_dirt.json
│  │     │  ├─ coast_armor_trim_smithing_template.json
│  │     │  ├─ cobbled_deepslate.json
│  │     │  ├─ cobbled_deepslate_slab.json
│  │     │  ├─ cobbled_deepslate_stairs.json
│  │     │  ├─ cobbled_deepslate_wall.json
│  │     │  ├─ cobblestone.json
│  │     │  ├─ cobblestone_slab.json
│  │     │  ├─ cobblestone_stairs.json
│  │     │  ├─ cobblestone_wall.json
│  │     │  ├─ cobweb.json
│  │     │  ├─ cocoa_beans.json
│  │     │  ├─ cod.json
│  │     │  ├─ cod_bucket.json
│  │     │  ├─ cod_spawn_egg.json
│  │     │  ├─ command_block.json
│  │     │  ├─ command_block_minecart.json
│  │     │  ├─ comparator.json
│  │     │  ├─ compass.json
│  │     │  ├─ composter.json
│  │     │  ├─ conduit.json
│  │     │  ├─ cooked_beef.json
│  │     │  ├─ cooked_chicken.json
│  │     │  ├─ cooked_cod.json
│  │     │  ├─ cooked_mutton.json
│  │     │  ├─ cooked_porkchop.json
│  │     │  ├─ cooked_rabbit.json
│  │     │  ├─ cooked_salmon.json
│  │     │  ├─ cookie.json
│  │     │  ├─ copper_axe.json
│  │     │  ├─ copper_bars.json
│  │     │  ├─ copper_block.json
│  │     │  ├─ copper_boots.json
│  │     │  ├─ copper_bulb.json
│  │     │  ├─ copper_chain.json
│  │     │  ├─ copper_chest.json
│  │     │  ├─ copper_chestplate.json
│  │     │  ├─ copper_door.json
│  │     │  ├─ copper_golem_spawn_egg.json
│  │     │  ├─ copper_golem_statue.json
│  │     │  ├─ copper_grate.json
│  │     │  ├─ copper_helmet.json
│  │     │  ├─ copper_hoe.json
│  │     │  ├─ copper_horse_armor.json
│  │     │  ├─ copper_ingot.json
│  │     │  ├─ copper_lantern.json
│  │     │  ├─ copper_leggings.json
│  │     │  ├─ copper_nautilus_armor.json
│  │     │  ├─ copper_nugget.json
│  │     │  ├─ copper_ore.json
│  │     │  ├─ copper_pickaxe.json
│  │     │  ├─ copper_shovel.json
│  │     │  ├─ copper_spear.json
│  │     │  ├─ copper_sword.json
│  │     │  ├─ copper_torch.json
│  │     │  ├─ copper_trapdoor.json
│  │     │  ├─ cornflower.json
│  │     │  ├─ cow_spawn_egg.json
│  │     │  ├─ cracked_deepslate_bricks.json
│  │     │  ├─ cracked_deepslate_tiles.json
│  │     │  ├─ cracked_nether_bricks.json
│  │     │  ├─ cracked_polished_blackstone_bricks.json
│  │     │  ├─ cracked_stone_bricks.json
│  │     │  ├─ crafter.json
│  │     │  ├─ crafting_table.json
│  │     │  ├─ creaking_heart.json
│  │     │  ├─ creaking_spawn_egg.json
│  │     │  ├─ creeper_banner_pattern.json
│  │     │  ├─ creeper_head.json
│  │     │  ├─ creeper_spawn_egg.json
│  │     │  ├─ crimson_button.json
│  │     │  ├─ crimson_door.json
│  │     │  ├─ crimson_fence.json
│  │     │  ├─ crimson_fence_gate.json
│  │     │  ├─ crimson_fungus.json
│  │     │  ├─ crimson_hanging_sign.json
│  │     │  ├─ crimson_hyphae.json
│  │     │  ├─ crimson_nylium.json
│  │     │  ├─ crimson_planks.json
│  │     │  ├─ crimson_pressure_plate.json
│  │     │  ├─ crimson_roots.json
│  │     │  ├─ crimson_shelf.json
│  │     │  ├─ crimson_sign.json
│  │     │  ├─ crimson_slab.json
│  │     │  ├─ crimson_stairs.json
│  │     │  ├─ crimson_stem.json
│  │     │  ├─ crimson_trapdoor.json
│  │     │  ├─ crossbow.json
│  │     │  ├─ crying_obsidian.json
│  │     │  ├─ cut_copper.json
│  │     │  ├─ cut_copper_slab.json
│  │     │  ├─ cut_copper_stairs.json
│  │     │  ├─ cut_red_sandstone.json
│  │     │  ├─ cut_red_sandstone_slab.json
│  │     │  ├─ cut_sandstone.json
│  │     │  ├─ cut_sandstone_slab.json
│  │     │  ├─ cyan_banner.json
│  │     │  ├─ cyan_bed.json
│  │     │  ├─ cyan_bundle.json
│  │     │  ├─ cyan_candle.json
│  │     │  ├─ cyan_carpet.json
│  │     │  ├─ cyan_concrete.json
│  │     │  ├─ cyan_concrete_powder.json
│  │     │  ├─ cyan_dye.json
│  │     │  ├─ cyan_glazed_terracotta.json
│  │     │  ├─ cyan_harness.json
│  │     │  ├─ cyan_shulker_box.json
│  │     │  ├─ cyan_stained_glass.json
│  │     │  ├─ cyan_stained_glass_pane.json
│  │     │  ├─ cyan_terracotta.json
│  │     │  ├─ cyan_wool.json
│  │     │  ├─ damaged_anvil.json
│  │     │  ├─ dandelion.json
│  │     │  ├─ danger_pottery_sherd.json
│  │     │  ├─ dark_oak_boat.json
│  │     │  ├─ dark_oak_button.json
│  │     │  ├─ dark_oak_chest_boat.json
│  │     │  ├─ dark_oak_door.json
│  │     │  ├─ dark_oak_fence.json
│  │     │  ├─ dark_oak_fence_gate.json
│  │     │  ├─ dark_oak_hanging_sign.json
│  │     │  ├─ dark_oak_leaves.json
│  │     │  ├─ dark_oak_log.json
│  │     │  ├─ dark_oak_planks.json
│  │     │  ├─ dark_oak_pressure_plate.json
│  │     │  ├─ dark_oak_sapling.json
│  │     │  ├─ dark_oak_shelf.json
│  │     │  ├─ dark_oak_sign.json
│  │     │  ├─ dark_oak_slab.json
│  │     │  ├─ dark_oak_stairs.json
│  │     │  ├─ dark_oak_trapdoor.json
│  │     │  ├─ dark_oak_wood.json
│  │     │  ├─ dark_prismarine.json
│  │     │  ├─ dark_prismarine_slab.json
│  │     │  ├─ dark_prismarine_stairs.json
│  │     │  ├─ daylight_detector.json
│  │     │  ├─ dead_brain_coral.json
│  │     │  ├─ dead_brain_coral_block.json
│  │     │  ├─ dead_brain_coral_fan.json
│  │     │  ├─ dead_bubble_coral.json
│  │     │  ├─ dead_bubble_coral_block.json
│  │     │  ├─ dead_bubble_coral_fan.json
│  │     │  ├─ dead_bush.json
│  │     │  ├─ dead_fire_coral.json
│  │     │  ├─ dead_fire_coral_block.json
│  │     │  ├─ dead_fire_coral_fan.json
│  │     │  ├─ dead_horn_coral.json
│  │     │  ├─ dead_horn_coral_block.json
│  │     │  ├─ dead_horn_coral_fan.json
│  │     │  ├─ dead_tube_coral.json
│  │     │  ├─ dead_tube_coral_block.json
│  │     │  ├─ dead_tube_coral_fan.json
│  │     │  ├─ debug_stick.json
│  │     │  ├─ decorated_pot.json
│  │     │  ├─ deepslate.json
│  │     │  ├─ deepslate_bricks.json
│  │     │  ├─ deepslate_brick_slab.json
│  │     │  ├─ deepslate_brick_stairs.json
│  │     │  ├─ deepslate_brick_wall.json
│  │     │  ├─ deepslate_coal_ore.json
│  │     │  ├─ deepslate_copper_ore.json
│  │     │  ├─ deepslate_diamond_ore.json
│  │     │  ├─ deepslate_emerald_ore.json
│  │     │  ├─ deepslate_gold_ore.json
│  │     │  ├─ deepslate_iron_ore.json
│  │     │  ├─ deepslate_lapis_ore.json
│  │     │  ├─ deepslate_redstone_ore.json
│  │     │  ├─ deepslate_tiles.json
│  │     │  ├─ deepslate_tile_slab.json
│  │     │  ├─ deepslate_tile_stairs.json
│  │     │  ├─ deepslate_tile_wall.json
│  │     │  ├─ detector_rail.json
│  │     │  ├─ diamond.json
│  │     │  ├─ diamond_axe.json
│  │     │  ├─ diamond_block.json
│  │     │  ├─ diamond_boots.json
│  │     │  ├─ diamond_chestplate.json
│  │     │  ├─ diamond_helmet.json
│  │     │  ├─ diamond_hoe.json
│  │     │  ├─ diamond_horse_armor.json
│  │     │  ├─ diamond_leggings.json
│  │     │  ├─ diamond_nautilus_armor.json
│  │     │  ├─ diamond_ore.json
│  │     │  ├─ diamond_pickaxe.json
│  │     │  ├─ diamond_shovel.json
│  │     │  ├─ diamond_spear.json
│  │     │  ├─ diamond_sword.json
│  │     │  ├─ diorite.json
│  │     │  ├─ diorite_slab.json
│  │     │  ├─ diorite_stairs.json
│  │     │  ├─ diorite_wall.json
│  │     │  ├─ dirt.json
│  │     │  ├─ dirt_path.json
│  │     │  ├─ disc_fragment_5.json
│  │     │  ├─ dispenser.json
│  │     │  ├─ dolphin_spawn_egg.json
│  │     │  ├─ donkey_spawn_egg.json
│  │     │  ├─ dragon_breath.json
│  │     │  ├─ dragon_egg.json
│  │     │  ├─ dragon_head.json
│  │     │  ├─ dried_ghast.json
│  │     │  ├─ dried_kelp.json
│  │     │  ├─ dried_kelp_block.json
│  │     │  ├─ dripstone_block.json
│  │     │  ├─ dropper.json
│  │     │  ├─ drowned_spawn_egg.json
│  │     │  ├─ dune_armor_trim_smithing_template.json
│  │     │  ├─ echo_shard.json
│  │     │  ├─ egg.json
│  │     │  ├─ elder_guardian_spawn_egg.json
│  │     │  ├─ elytra.json
│  │     │  ├─ emerald.json
│  │     │  ├─ emerald_block.json
│  │     │  ├─ emerald_ore.json
│  │     │  ├─ enchanted_book.json
│  │     │  ├─ enchanted_golden_apple.json
│  │     │  ├─ enchanting_table.json
│  │     │  ├─ enderman_spawn_egg.json
│  │     │  ├─ endermite_spawn_egg.json
│  │     │  ├─ ender_chest.json
│  │     │  ├─ ender_dragon_spawn_egg.json
│  │     │  ├─ ender_eye.json
│  │     │  ├─ ender_pearl.json
│  │     │  ├─ end_crystal.json
│  │     │  ├─ end_portal_frame.json
│  │     │  ├─ end_rod.json
│  │     │  ├─ end_stone.json
│  │     │  ├─ end_stone_bricks.json
│  │     │  ├─ end_stone_brick_slab.json
│  │     │  ├─ end_stone_brick_stairs.json
│  │     │  ├─ end_stone_brick_wall.json
│  │     │  ├─ evoker_spawn_egg.json
│  │     │  ├─ experience_bottle.json
│  │     │  ├─ explorer_pottery_sherd.json
│  │     │  ├─ exposed_chiseled_copper.json
│  │     │  ├─ exposed_copper.json
│  │     │  ├─ exposed_copper_bars.json
│  │     │  ├─ exposed_copper_bulb.json
│  │     │  ├─ exposed_copper_chain.json
│  │     │  ├─ exposed_copper_chest.json
│  │     │  ├─ exposed_copper_door.json
│  │     │  ├─ exposed_copper_golem_statue.json
│  │     │  ├─ exposed_copper_grate.json
│  │     │  ├─ exposed_copper_lantern.json
│  │     │  ├─ exposed_copper_trapdoor.json
│  │     │  ├─ exposed_cut_copper.json
│  │     │  ├─ exposed_cut_copper_slab.json
│  │     │  ├─ exposed_cut_copper_stairs.json
│  │     │  ├─ exposed_lightning_rod.json
│  │     │  ├─ eye_armor_trim_smithing_template.json
│  │     │  ├─ farmland.json
│  │     │  ├─ feather.json
│  │     │  ├─ fermented_spider_eye.json
│  │     │  ├─ fern.json
│  │     │  ├─ field_masoned_banner_pattern.json
│  │     │  ├─ filled_map.json
│  │     │  ├─ firefly_bush.json
│  │     │  ├─ firework_rocket.json
│  │     │  ├─ firework_star.json
│  │     │  ├─ fire_charge.json
│  │     │  ├─ fire_coral.json
│  │     │  ├─ fire_coral_block.json
│  │     │  ├─ fire_coral_fan.json
│  │     │  ├─ fishing_rod.json
│  │     │  ├─ fletching_table.json
│  │     │  ├─ flint.json
│  │     │  ├─ flint_and_steel.json
│  │     │  ├─ flowering_azalea.json
│  │     │  ├─ flowering_azalea_leaves.json
│  │     │  ├─ flower_banner_pattern.json
│  │     │  ├─ flower_pot.json
│  │     │  ├─ flow_armor_trim_smithing_template.json
│  │     │  ├─ flow_banner_pattern.json
│  │     │  ├─ flow_pottery_sherd.json
│  │     │  ├─ fox_spawn_egg.json
│  │     │  ├─ friend_pottery_sherd.json
│  │     │  ├─ frogspawn.json
│  │     │  ├─ frog_spawn_egg.json
│  │     │  ├─ furnace.json
│  │     │  ├─ furnace_minecart.json
│  │     │  ├─ ghast_spawn_egg.json
│  │     │  ├─ ghast_tear.json
│  │     │  ├─ gilded_blackstone.json
│  │     │  ├─ glass.json
│  │     │  ├─ glass_bottle.json
│  │     │  ├─ glass_pane.json
│  │     │  ├─ glistering_melon_slice.json
│  │     │  ├─ globe_banner_pattern.json
│  │     │  ├─ glowstone.json
│  │     │  ├─ glowstone_dust.json
│  │     │  ├─ glow_berries.json
│  │     │  ├─ glow_ink_sac.json
│  │     │  ├─ glow_item_frame.json
│  │     │  ├─ glow_lichen.json
│  │     │  ├─ glow_squid_spawn_egg.json
│  │     │  ├─ goat_horn.json
│  │     │  ├─ goat_spawn_egg.json
│  │     │  ├─ golden_apple.json
│  │     │  ├─ golden_axe.json
│  │     │  ├─ golden_boots.json
│  │     │  ├─ golden_carrot.json
│  │     │  ├─ golden_chestplate.json
│  │     │  ├─ golden_helmet.json
│  │     │  ├─ golden_hoe.json
│  │     │  ├─ golden_horse_armor.json
│  │     │  ├─ golden_leggings.json
│  │     │  ├─ golden_nautilus_armor.json
│  │     │  ├─ golden_pickaxe.json
│  │     │  ├─ golden_shovel.json
│  │     │  ├─ golden_spear.json
│  │     │  ├─ golden_sword.json
│  │     │  ├─ gold_block.json
│  │     │  ├─ gold_ingot.json
│  │     │  ├─ gold_nugget.json
│  │     │  ├─ gold_ore.json
│  │     │  ├─ granite.json
│  │     │  ├─ granite_slab.json
│  │     │  ├─ granite_stairs.json
│  │     │  ├─ granite_wall.json
│  │     │  ├─ grass_block.json
│  │     │  ├─ gravel.json
│  │     │  ├─ gray_banner.json
│  │     │  ├─ gray_bed.json
│  │     │  ├─ gray_bundle.json
│  │     │  ├─ gray_candle.json
│  │     │  ├─ gray_carpet.json
│  │     │  ├─ gray_concrete.json
│  │     │  ├─ gray_concrete_powder.json
│  │     │  ├─ gray_dye.json
│  │     │  ├─ gray_glazed_terracotta.json
│  │     │  ├─ gray_harness.json
│  │     │  ├─ gray_shulker_box.json
│  │     │  ├─ gray_stained_glass.json
│  │     │  ├─ gray_stained_glass_pane.json
│  │     │  ├─ gray_terracotta.json
│  │     │  ├─ gray_wool.json
│  │     │  ├─ green_banner.json
│  │     │  ├─ green_bed.json
│  │     │  ├─ green_bundle.json
│  │     │  ├─ green_candle.json
│  │     │  ├─ green_carpet.json
│  │     │  ├─ green_concrete.json
│  │     │  ├─ green_concrete_powder.json
│  │     │  ├─ green_dye.json
│  │     │  ├─ green_glazed_terracotta.json
│  │     │  ├─ green_harness.json
│  │     │  ├─ green_shulker_box.json
│  │     │  ├─ green_stained_glass.json
│  │     │  ├─ green_stained_glass_pane.json
│  │     │  ├─ green_terracotta.json
│  │     │  ├─ green_wool.json
│  │     │  ├─ grindstone.json
│  │     │  ├─ guardian_spawn_egg.json
│  │     │  ├─ gunpowder.json
│  │     │  ├─ guster_banner_pattern.json
│  │     │  ├─ guster_pottery_sherd.json
│  │     │  ├─ hanging_roots.json
│  │     │  ├─ happy_ghast_spawn_egg.json
│  │     │  ├─ hay_block.json
│  │     │  ├─ heartbreak_pottery_sherd.json
│  │     │  ├─ heart_of_the_sea.json
│  │     │  ├─ heart_pottery_sherd.json
│  │     │  ├─ heavy_core.json
│  │     │  ├─ heavy_weighted_pressure_plate.json
│  │     │  ├─ hoglin_spawn_egg.json
│  │     │  ├─ honeycomb.json
│  │     │  ├─ honeycomb_block.json
│  │     │  ├─ honey_block.json
│  │     │  ├─ honey_bottle.json
│  │     │  ├─ hopper.json
│  │     │  ├─ hopper_minecart.json
│  │     │  ├─ horn_coral.json
│  │     │  ├─ horn_coral_block.json
│  │     │  ├─ horn_coral_fan.json
│  │     │  ├─ horse_spawn_egg.json
│  │     │  ├─ host_armor_trim_smithing_template.json
│  │     │  ├─ howl_pottery_sherd.json
│  │     │  ├─ husk_spawn_egg.json
│  │     │  ├─ ice.json
│  │     │  ├─ infested_chiseled_stone_bricks.json
│  │     │  ├─ infested_cobblestone.json
│  │     │  ├─ infested_cracked_stone_bricks.json
│  │     │  ├─ infested_deepslate.json
│  │     │  ├─ infested_mossy_stone_bricks.json
│  │     │  ├─ infested_stone.json
│  │     │  ├─ infested_stone_bricks.json
│  │     │  ├─ ink_sac.json
│  │     │  ├─ iron_axe.json
│  │     │  ├─ iron_bars.json
│  │     │  ├─ iron_block.json
│  │     │  ├─ iron_boots.json
│  │     │  ├─ iron_chain.json
│  │     │  ├─ iron_chestplate.json
│  │     │  ├─ iron_door.json
│  │     │  ├─ iron_golem_spawn_egg.json
│  │     │  ├─ iron_helmet.json
│  │     │  ├─ iron_hoe.json
│  │     │  ├─ iron_horse_armor.json
│  │     │  ├─ iron_ingot.json
│  │     │  ├─ iron_leggings.json
│  │     │  ├─ iron_nautilus_armor.json
│  │     │  ├─ iron_nugget.json
│  │     │  ├─ iron_ore.json
│  │     │  ├─ iron_pickaxe.json
│  │     │  ├─ iron_shovel.json
│  │     │  ├─ iron_spear.json
│  │     │  ├─ iron_sword.json
│  │     │  ├─ iron_trapdoor.json
│  │     │  ├─ item_frame.json
│  │     │  ├─ jack_o_lantern.json
│  │     │  ├─ jigsaw.json
│  │     │  ├─ jukebox.json
│  │     │  ├─ jungle_boat.json
│  │     │  ├─ jungle_button.json
│  │     │  ├─ jungle_chest_boat.json
│  │     │  ├─ jungle_door.json
│  │     │  ├─ jungle_fence.json
│  │     │  ├─ jungle_fence_gate.json
│  │     │  ├─ jungle_hanging_sign.json
│  │     │  ├─ jungle_leaves.json
│  │     │  ├─ jungle_log.json
│  │     │  ├─ jungle_planks.json
│  │     │  ├─ jungle_pressure_plate.json
│  │     │  ├─ jungle_sapling.json
│  │     │  ├─ jungle_shelf.json
│  │     │  ├─ jungle_sign.json
│  │     │  ├─ jungle_slab.json
│  │     │  ├─ jungle_stairs.json
│  │     │  ├─ jungle_trapdoor.json
│  │     │  ├─ jungle_wood.json
│  │     │  ├─ kelp.json
│  │     │  ├─ knowledge_book.json
│  │     │  ├─ ladder.json
│  │     │  ├─ lantern.json
│  │     │  ├─ lapis_block.json
│  │     │  ├─ lapis_lazuli.json
│  │     │  ├─ lapis_ore.json
│  │     │  ├─ large_amethyst_bud.json
│  │     │  ├─ large_fern.json
│  │     │  ├─ lava_bucket.json
│  │     │  ├─ lead.json
│  │     │  ├─ leaf_litter.json
│  │     │  ├─ leather.json
│  │     │  ├─ leather_boots.json
│  │     │  ├─ leather_chestplate.json
│  │     │  ├─ leather_helmet.json
│  │     │  ├─ leather_horse_armor.json
│  │     │  ├─ leather_leggings.json
│  │     │  ├─ lectern.json
│  │     │  ├─ lever.json
│  │     │  ├─ light.json
│  │     │  ├─ lightning_rod.json
│  │     │  ├─ light_blue_banner.json
│  │     │  ├─ light_blue_bed.json
│  │     │  ├─ light_blue_bundle.json
│  │     │  ├─ light_blue_candle.json
│  │     │  ├─ light_blue_carpet.json
│  │     │  ├─ light_blue_concrete.json
│  │     │  ├─ light_blue_concrete_powder.json
│  │     │  ├─ light_blue_dye.json
│  │     │  ├─ light_blue_glazed_terracotta.json
│  │     │  ├─ light_blue_harness.json
│  │     │  ├─ light_blue_shulker_box.json
│  │     │  ├─ light_blue_stained_glass.json
│  │     │  ├─ light_blue_stained_glass_pane.json
│  │     │  ├─ light_blue_terracotta.json
│  │     │  ├─ light_blue_wool.json
│  │     │  ├─ light_gray_banner.json
│  │     │  ├─ light_gray_bed.json
│  │     │  ├─ light_gray_bundle.json
│  │     │  ├─ light_gray_candle.json
│  │     │  ├─ light_gray_carpet.json
│  │     │  ├─ light_gray_concrete.json
│  │     │  ├─ light_gray_concrete_powder.json
│  │     │  ├─ light_gray_dye.json
│  │     │  ├─ light_gray_glazed_terracotta.json
│  │     │  ├─ light_gray_harness.json
│  │     │  ├─ light_gray_shulker_box.json
│  │     │  ├─ light_gray_stained_glass.json
│  │     │  ├─ light_gray_stained_glass_pane.json
│  │     │  ├─ light_gray_terracotta.json
│  │     │  ├─ light_gray_wool.json
│  │     │  ├─ light_weighted_pressure_plate.json
│  │     │  ├─ lilac.json
│  │     │  ├─ lily_of_the_valley.json
│  │     │  ├─ lily_pad.json
│  │     │  ├─ lime_banner.json
│  │     │  ├─ lime_bed.json
│  │     │  ├─ lime_bundle.json
│  │     │  ├─ lime_candle.json
│  │     │  ├─ lime_carpet.json
│  │     │  ├─ lime_concrete.json
│  │     │  ├─ lime_concrete_powder.json
│  │     │  ├─ lime_dye.json
│  │     │  ├─ lime_glazed_terracotta.json
│  │     │  ├─ lime_harness.json
│  │     │  ├─ lime_shulker_box.json
│  │     │  ├─ lime_stained_glass.json
│  │     │  ├─ lime_stained_glass_pane.json
│  │     │  ├─ lime_terracotta.json
│  │     │  ├─ lime_wool.json
│  │     │  ├─ lingering_potion.json
│  │     │  ├─ llama_spawn_egg.json
│  │     │  ├─ lodestone.json
│  │     │  ├─ loom.json
│  │     │  ├─ mace.json
│  │     │  ├─ magenta_banner.json
│  │     │  ├─ magenta_bed.json
│  │     │  ├─ magenta_bundle.json
│  │     │  ├─ magenta_candle.json
│  │     │  ├─ magenta_carpet.json
│  │     │  ├─ magenta_concrete.json
│  │     │  ├─ magenta_concrete_powder.json
│  │     │  ├─ magenta_dye.json
│  │     │  ├─ magenta_glazed_terracotta.json
│  │     │  ├─ magenta_harness.json
│  │     │  ├─ magenta_shulker_box.json
│  │     │  ├─ magenta_stained_glass.json
│  │     │  ├─ magenta_stained_glass_pane.json
│  │     │  ├─ magenta_terracotta.json
│  │     │  ├─ magenta_wool.json
│  │     │  ├─ magma_block.json
│  │     │  ├─ magma_cream.json
│  │     │  ├─ magma_cube_spawn_egg.json
│  │     │  ├─ mangrove_boat.json
│  │     │  ├─ mangrove_button.json
│  │     │  ├─ mangrove_chest_boat.json
│  │     │  ├─ mangrove_door.json
│  │     │  ├─ mangrove_fence.json
│  │     │  ├─ mangrove_fence_gate.json
│  │     │  ├─ mangrove_hanging_sign.json
│  │     │  ├─ mangrove_leaves.json
│  │     │  ├─ mangrove_log.json
│  │     │  ├─ mangrove_planks.json
│  │     │  ├─ mangrove_pressure_plate.json
│  │     │  ├─ mangrove_propagule.json
│  │     │  ├─ mangrove_roots.json
│  │     │  ├─ mangrove_shelf.json
│  │     │  ├─ mangrove_sign.json
│  │     │  ├─ mangrove_slab.json
│  │     │  ├─ mangrove_stairs.json
│  │     │  ├─ mangrove_trapdoor.json
│  │     │  ├─ mangrove_wood.json
│  │     │  ├─ map.json
│  │     │  ├─ medium_amethyst_bud.json
│  │     │  ├─ melon.json
│  │     │  ├─ melon_seeds.json
│  │     │  ├─ melon_slice.json
│  │     │  ├─ milk_bucket.json
│  │     │  ├─ minecart.json
│  │     │  ├─ miner_pottery_sherd.json
│  │     │  ├─ mojang_banner_pattern.json
│  │     │  ├─ mooshroom_spawn_egg.json
│  │     │  ├─ mossy_cobblestone.json
│  │     │  ├─ mossy_cobblestone_slab.json
│  │     │  ├─ mossy_cobblestone_stairs.json
│  │     │  ├─ mossy_cobblestone_wall.json
│  │     │  ├─ mossy_stone_bricks.json
│  │     │  ├─ mossy_stone_brick_slab.json
│  │     │  ├─ mossy_stone_brick_stairs.json
│  │     │  ├─ mossy_stone_brick_wall.json
│  │     │  ├─ moss_block.json
│  │     │  ├─ moss_carpet.json
│  │     │  ├─ mourner_pottery_sherd.json
│  │     │  ├─ mud.json
│  │     │  ├─ muddy_mangrove_roots.json
│  │     │  ├─ mud_bricks.json
│  │     │  ├─ mud_brick_slab.json
│  │     │  ├─ mud_brick_stairs.json
│  │     │  ├─ mud_brick_wall.json
│  │     │  ├─ mule_spawn_egg.json
│  │     │  ├─ mushroom_stem.json
│  │     │  ├─ mushroom_stew.json
│  │     │  ├─ music_disc_11.json
│  │     │  ├─ music_disc_13.json
│  │     │  ├─ music_disc_5.json
│  │     │  ├─ music_disc_blocks.json
│  │     │  ├─ music_disc_cat.json
│  │     │  ├─ music_disc_chirp.json
│  │     │  ├─ music_disc_creator.json
│  │     │  ├─ music_disc_creator_music_box.json
│  │     │  ├─ music_disc_far.json
│  │     │  ├─ music_disc_lava_chicken.json
│  │     │  ├─ music_disc_mall.json
│  │     │  ├─ music_disc_mellohi.json
│  │     │  ├─ music_disc_otherside.json
│  │     │  ├─ music_disc_pigstep.json
│  │     │  ├─ music_disc_precipice.json
│  │     │  ├─ music_disc_relic.json
│  │     │  ├─ music_disc_stal.json
│  │     │  ├─ music_disc_strad.json
│  │     │  ├─ music_disc_tears.json
│  │     │  ├─ music_disc_wait.json
│  │     │  ├─ music_disc_ward.json
│  │     │  ├─ mutton.json
│  │     │  ├─ mycelium.json
│  │     │  ├─ name_tag.json
│  │     │  ├─ nautilus_shell.json
│  │     │  ├─ nautilus_spawn_egg.json
│  │     │  ├─ netherite_axe.json
│  │     │  ├─ netherite_block.json
│  │     │  ├─ netherite_boots.json
│  │     │  ├─ netherite_chestplate.json
│  │     │  ├─ netherite_helmet.json
│  │     │  ├─ netherite_hoe.json
│  │     │  ├─ netherite_horse_armor.json
│  │     │  ├─ netherite_ingot.json
│  │     │  ├─ netherite_leggings.json
│  │     │  ├─ netherite_nautilus_armor.json
│  │     │  ├─ netherite_pickaxe.json
│  │     │  ├─ netherite_scrap.json
│  │     │  ├─ netherite_shovel.json
│  │     │  ├─ netherite_spear.json
│  │     │  ├─ netherite_sword.json
│  │     │  ├─ netherite_upgrade_smithing_template.json
│  │     │  ├─ netherrack.json
│  │     │  ├─ nether_brick.json
│  │     │  ├─ nether_bricks.json
│  │     │  ├─ nether_brick_fence.json
│  │     │  ├─ nether_brick_slab.json
│  │     │  ├─ nether_brick_stairs.json
│  │     │  ├─ nether_brick_wall.json
│  │     │  ├─ nether_gold_ore.json
│  │     │  ├─ nether_quartz_ore.json
│  │     │  ├─ nether_sprouts.json
│  │     │  ├─ nether_star.json
│  │     │  ├─ nether_wart.json
│  │     │  ├─ nether_wart_block.json
│  │     │  ├─ note_block.json
│  │     │  ├─ oak_boat.json
│  │     │  ├─ oak_button.json
│  │     │  ├─ oak_chest_boat.json
│  │     │  ├─ oak_door.json
│  │     │  ├─ oak_fence.json
│  │     │  ├─ oak_fence_gate.json
│  │     │  ├─ oak_hanging_sign.json
│  │     │  ├─ oak_leaves.json
│  │     │  ├─ oak_log.json
│  │     │  ├─ oak_planks.json
│  │     │  ├─ oak_pressure_plate.json
│  │     │  ├─ oak_sapling.json
│  │     │  ├─ oak_shelf.json
│  │     │  ├─ oak_sign.json
│  │     │  ├─ oak_slab.json
│  │     │  ├─ oak_stairs.json
│  │     │  ├─ oak_trapdoor.json
│  │     │  ├─ oak_wood.json
│  │     │  ├─ observer.json
│  │     │  ├─ obsidian.json
│  │     │  ├─ ocelot_spawn_egg.json
│  │     │  ├─ ochre_froglight.json
│  │     │  ├─ ominous_bottle.json
│  │     │  ├─ ominous_trial_key.json
│  │     │  ├─ open_eyeblossom.json
│  │     │  ├─ orange_banner.json
│  │     │  ├─ orange_bed.json
│  │     │  ├─ orange_bundle.json
│  │     │  ├─ orange_candle.json
│  │     │  ├─ orange_carpet.json
│  │     │  ├─ orange_concrete.json
│  │     │  ├─ orange_concrete_powder.json
│  │     │  ├─ orange_dye.json
│  │     │  ├─ orange_glazed_terracotta.json
│  │     │  ├─ orange_harness.json
│  │     │  ├─ orange_shulker_box.json
│  │     │  ├─ orange_stained_glass.json
│  │     │  ├─ orange_stained_glass_pane.json
│  │     │  ├─ orange_terracotta.json
│  │     │  ├─ orange_tulip.json
│  │     │  ├─ orange_wool.json
│  │     │  ├─ oxeye_daisy.json
│  │     │  ├─ oxidized_chiseled_copper.json
│  │     │  ├─ oxidized_copper.json
│  │     │  ├─ oxidized_copper_bars.json
│  │     │  ├─ oxidized_copper_bulb.json
│  │     │  ├─ oxidized_copper_chain.json
│  │     │  ├─ oxidized_copper_chest.json
│  │     │  ├─ oxidized_copper_door.json
│  │     │  ├─ oxidized_copper_golem_statue.json
│  │     │  ├─ oxidized_copper_grate.json
│  │     │  ├─ oxidized_copper_lantern.json
│  │     │  ├─ oxidized_copper_trapdoor.json
│  │     │  ├─ oxidized_cut_copper.json
│  │     │  ├─ oxidized_cut_copper_slab.json
│  │     │  ├─ oxidized_cut_copper_stairs.json
│  │     │  ├─ oxidized_lightning_rod.json
│  │     │  ├─ packed_ice.json
│  │     │  ├─ packed_mud.json
│  │     │  ├─ painting.json
│  │     │  ├─ pale_hanging_moss.json
│  │     │  ├─ pale_moss_block.json
│  │     │  ├─ pale_moss_carpet.json
│  │     │  ├─ pale_oak_boat.json
│  │     │  ├─ pale_oak_button.json
│  │     │  ├─ pale_oak_chest_boat.json
│  │     │  ├─ pale_oak_door.json
│  │     │  ├─ pale_oak_fence.json
│  │     │  ├─ pale_oak_fence_gate.json
│  │     │  ├─ pale_oak_hanging_sign.json
│  │     │  ├─ pale_oak_leaves.json
│  │     │  ├─ pale_oak_log.json
│  │     │  ├─ pale_oak_planks.json
│  │     │  ├─ pale_oak_pressure_plate.json
│  │     │  ├─ pale_oak_sapling.json
│  │     │  ├─ pale_oak_shelf.json
│  │     │  ├─ pale_oak_sign.json
│  │     │  ├─ pale_oak_slab.json
│  │     │  ├─ pale_oak_stairs.json
│  │     │  ├─ pale_oak_trapdoor.json
│  │     │  ├─ pale_oak_wood.json
│  │     │  ├─ panda_spawn_egg.json
│  │     │  ├─ paper.json
│  │     │  ├─ parched_spawn_egg.json
│  │     │  ├─ parrot_spawn_egg.json
│  │     │  ├─ pearlescent_froglight.json
│  │     │  ├─ peony.json
│  │     │  ├─ petrified_oak_slab.json
│  │     │  ├─ phantom_membrane.json
│  │     │  ├─ phantom_spawn_egg.json
│  │     │  ├─ piglin_banner_pattern.json
│  │     │  ├─ piglin_brute_spawn_egg.json
│  │     │  ├─ piglin_head.json
│  │     │  ├─ piglin_spawn_egg.json
│  │     │  ├─ pig_spawn_egg.json
│  │     │  ├─ pillager_spawn_egg.json
│  │     │  ├─ pink_banner.json
│  │     │  ├─ pink_bed.json
│  │     │  ├─ pink_bundle.json
│  │     │  ├─ pink_candle.json
│  │     │  ├─ pink_carpet.json
│  │     │  ├─ pink_concrete.json
│  │     │  ├─ pink_concrete_powder.json
│  │     │  ├─ pink_dye.json
│  │     │  ├─ pink_glazed_terracotta.json
│  │     │  ├─ pink_harness.json
│  │     │  ├─ pink_petals.json
│  │     │  ├─ pink_shulker_box.json
│  │     │  ├─ pink_stained_glass.json
│  │     │  ├─ pink_stained_glass_pane.json
│  │     │  ├─ pink_terracotta.json
│  │     │  ├─ pink_tulip.json
│  │     │  ├─ pink_wool.json
│  │     │  ├─ piston.json
│  │     │  ├─ pitcher_plant.json
│  │     │  ├─ pitcher_pod.json
│  │     │  ├─ player_head.json
│  │     │  ├─ plenty_pottery_sherd.json
│  │     │  ├─ podzol.json
│  │     │  ├─ pointed_dripstone.json
│  │     │  ├─ poisonous_potato.json
│  │     │  ├─ polar_bear_spawn_egg.json
│  │     │  ├─ polished_andesite.json
│  │     │  ├─ polished_andesite_slab.json
│  │     │  ├─ polished_andesite_stairs.json
│  │     │  ├─ polished_basalt.json
│  │     │  ├─ polished_blackstone.json
│  │     │  ├─ polished_blackstone_bricks.json
│  │     │  ├─ polished_blackstone_brick_slab.json
│  │     │  ├─ polished_blackstone_brick_stairs.json
│  │     │  ├─ polished_blackstone_brick_wall.json
│  │     │  ├─ polished_blackstone_button.json
│  │     │  ├─ polished_blackstone_pressure_plate.json
│  │     │  ├─ polished_blackstone_slab.json
│  │     │  ├─ polished_blackstone_stairs.json
│  │     │  ├─ polished_blackstone_wall.json
│  │     │  ├─ polished_deepslate.json
│  │     │  ├─ polished_deepslate_slab.json
│  │     │  ├─ polished_deepslate_stairs.json
│  │     │  ├─ polished_deepslate_wall.json
│  │     │  ├─ polished_diorite.json
│  │     │  ├─ polished_diorite_slab.json
│  │     │  ├─ polished_diorite_stairs.json
│  │     │  ├─ polished_granite.json
│  │     │  ├─ polished_granite_slab.json
│  │     │  ├─ polished_granite_stairs.json
│  │     │  ├─ polished_tuff.json
│  │     │  ├─ polished_tuff_slab.json
│  │     │  ├─ polished_tuff_stairs.json
│  │     │  ├─ polished_tuff_wall.json
│  │     │  ├─ popped_chorus_fruit.json
│  │     │  ├─ poppy.json
│  │     │  ├─ porkchop.json
│  │     │  ├─ potato.json
│  │     │  ├─ potion.json
│  │     │  ├─ powder_snow_bucket.json
│  │     │  ├─ powered_rail.json
│  │     │  ├─ prismarine.json
│  │     │  ├─ prismarine_bricks.json
│  │     │  ├─ prismarine_brick_slab.json
│  │     │  ├─ prismarine_brick_stairs.json
│  │     │  ├─ prismarine_crystals.json
│  │     │  ├─ prismarine_shard.json
│  │     │  ├─ prismarine_slab.json
│  │     │  ├─ prismarine_stairs.json
│  │     │  ├─ prismarine_wall.json
│  │     │  ├─ prize_pottery_sherd.json
│  │     │  ├─ pufferfish.json
│  │     │  ├─ pufferfish_bucket.json
│  │     │  ├─ pufferfish_spawn_egg.json
│  │     │  ├─ pumpkin.json
│  │     │  ├─ pumpkin_pie.json
│  │     │  ├─ pumpkin_seeds.json
│  │     │  ├─ purple_banner.json
│  │     │  ├─ purple_bed.json
│  │     │  ├─ purple_bundle.json
│  │     │  ├─ purple_candle.json
│  │     │  ├─ purple_carpet.json
│  │     │  ├─ purple_concrete.json
│  │     │  ├─ purple_concrete_powder.json
│  │     │  ├─ purple_dye.json
│  │     │  ├─ purple_glazed_terracotta.json
│  │     │  ├─ purple_harness.json
│  │     │  ├─ purple_shulker_box.json
│  │     │  ├─ purple_stained_glass.json
│  │     │  ├─ purple_stained_glass_pane.json
│  │     │  ├─ purple_terracotta.json
│  │     │  ├─ purple_wool.json
│  │     │  ├─ purpur_block.json
│  │     │  ├─ purpur_pillar.json
│  │     │  ├─ purpur_slab.json
│  │     │  ├─ purpur_stairs.json
│  │     │  ├─ quartz.json
│  │     │  ├─ quartz_block.json
│  │     │  ├─ quartz_bricks.json
│  │     │  ├─ quartz_pillar.json
│  │     │  ├─ quartz_slab.json
│  │     │  ├─ quartz_stairs.json
│  │     │  ├─ rabbit.json
│  │     │  ├─ rabbit_foot.json
│  │     │  ├─ rabbit_hide.json
│  │     │  ├─ rabbit_spawn_egg.json
│  │     │  ├─ rabbit_stew.json
│  │     │  ├─ rail.json
│  │     │  ├─ raiser_armor_trim_smithing_template.json
│  │     │  ├─ ravager_spawn_egg.json
│  │     │  ├─ raw_copper.json
│  │     │  ├─ raw_copper_block.json
│  │     │  ├─ raw_gold.json
│  │     │  ├─ raw_gold_block.json
│  │     │  ├─ raw_iron.json
│  │     │  ├─ raw_iron_block.json
│  │     │  ├─ recovery_compass.json
│  │     │  ├─ redstone.json
│  │     │  ├─ redstone_block.json
│  │     │  ├─ redstone_lamp.json
│  │     │  ├─ redstone_ore.json
│  │     │  ├─ redstone_torch.json
│  │     │  ├─ red_banner.json
│  │     │  ├─ red_bed.json
│  │     │  ├─ red_bundle.json
│  │     │  ├─ red_candle.json
│  │     │  ├─ red_carpet.json
│  │     │  ├─ red_concrete.json
│  │     │  ├─ red_concrete_powder.json
│  │     │  ├─ red_dye.json
│  │     │  ├─ red_glazed_terracotta.json
│  │     │  ├─ red_harness.json
│  │     │  ├─ red_mushroom.json
│  │     │  ├─ red_mushroom_block.json
│  │     │  ├─ red_nether_bricks.json
│  │     │  ├─ red_nether_brick_slab.json
│  │     │  ├─ red_nether_brick_stairs.json
│  │     │  ├─ red_nether_brick_wall.json
│  │     │  ├─ red_sand.json
│  │     │  ├─ red_sandstone.json
│  │     │  ├─ red_sandstone_slab.json
│  │     │  ├─ red_sandstone_stairs.json
│  │     │  ├─ red_sandstone_wall.json
│  │     │  ├─ red_shulker_box.json
│  │     │  ├─ red_stained_glass.json
│  │     │  ├─ red_stained_glass_pane.json
│  │     │  ├─ red_terracotta.json
│  │     │  ├─ red_tulip.json
│  │     │  ├─ red_wool.json
│  │     │  ├─ reinforced_deepslate.json
│  │     │  ├─ repeater.json
│  │     │  ├─ repeating_command_block.json
│  │     │  ├─ resin_block.json
│  │     │  ├─ resin_brick.json
│  │     │  ├─ resin_bricks.json
│  │     │  ├─ resin_brick_slab.json
│  │     │  ├─ resin_brick_stairs.json
│  │     │  ├─ resin_brick_wall.json
│  │     │  ├─ resin_clump.json
│  │     │  ├─ respawn_anchor.json
│  │     │  ├─ rib_armor_trim_smithing_template.json
│  │     │  ├─ rooted_dirt.json
│  │     │  ├─ rose_bush.json
│  │     │  ├─ rotten_flesh.json
│  │     │  ├─ saddle.json
│  │     │  ├─ salmon.json
│  │     │  ├─ salmon_bucket.json
│  │     │  ├─ salmon_spawn_egg.json
│  │     │  ├─ sand.json
│  │     │  ├─ sandstone.json
│  │     │  ├─ sandstone_slab.json
│  │     │  ├─ sandstone_stairs.json
│  │     │  ├─ sandstone_wall.json
│  │     │  ├─ scaffolding.json
│  │     │  ├─ scrape_pottery_sherd.json
│  │     │  ├─ sculk.json
│  │     │  ├─ sculk_catalyst.json
│  │     │  ├─ sculk_sensor.json
│  │     │  ├─ sculk_shrieker.json
│  │     │  ├─ sculk_vein.json
│  │     │  ├─ seagrass.json
│  │     │  ├─ sea_lantern.json
│  │     │  ├─ sea_pickle.json
│  │     │  ├─ sentry_armor_trim_smithing_template.json
│  │     │  ├─ shaper_armor_trim_smithing_template.json
│  │     │  ├─ sheaf_pottery_sherd.json
│  │     │  ├─ shears.json
│  │     │  ├─ sheep_spawn_egg.json
│  │     │  ├─ shelter_pottery_sherd.json
│  │     │  ├─ shield.json
│  │     │  ├─ short_dry_grass.json
│  │     │  ├─ short_grass.json
│  │     │  ├─ shroomlight.json
│  │     │  ├─ shulker_box.json
│  │     │  ├─ shulker_shell.json
│  │     │  ├─ shulker_spawn_egg.json
│  │     │  ├─ silence_armor_trim_smithing_template.json
│  │     │  ├─ silverfish_spawn_egg.json
│  │     │  ├─ skeleton_horse_spawn_egg.json
│  │     │  ├─ skeleton_skull.json
│  │     │  ├─ skeleton_spawn_egg.json
│  │     │  ├─ skull_banner_pattern.json
│  │     │  ├─ skull_pottery_sherd.json
│  │     │  ├─ slime_ball.json
│  │     │  ├─ slime_block.json
│  │     │  ├─ slime_spawn_egg.json
│  │     │  ├─ small_amethyst_bud.json
│  │     │  ├─ small_dripleaf.json
│  │     │  ├─ smithing_table.json
│  │     │  ├─ smoker.json
│  │     │  ├─ smooth_basalt.json
│  │     │  ├─ smooth_quartz.json
│  │     │  ├─ smooth_quartz_slab.json
│  │     │  ├─ smooth_quartz_stairs.json
│  │     │  ├─ smooth_red_sandstone.json
│  │     │  ├─ smooth_red_sandstone_slab.json
│  │     │  ├─ smooth_red_sandstone_stairs.json
│  │     │  ├─ smooth_sandstone.json
│  │     │  ├─ smooth_sandstone_slab.json
│  │     │  ├─ smooth_sandstone_stairs.json
│  │     │  ├─ smooth_stone.json
│  │     │  ├─ smooth_stone_slab.json
│  │     │  ├─ sniffer_egg.json
│  │     │  ├─ sniffer_spawn_egg.json
│  │     │  ├─ snort_pottery_sherd.json
│  │     │  ├─ snout_armor_trim_smithing_template.json
│  │     │  ├─ snow.json
│  │     │  ├─ snowball.json
│  │     │  ├─ snow_block.json
│  │     │  ├─ snow_golem_spawn_egg.json
│  │     │  ├─ soul_campfire.json
│  │     │  ├─ soul_lantern.json
│  │     │  ├─ soul_sand.json
│  │     │  ├─ soul_soil.json
│  │     │  ├─ soul_torch.json
│  │     │  ├─ spawner.json
│  │     │  ├─ spectral_arrow.json
│  │     │  ├─ spider_eye.json
│  │     │  ├─ spider_spawn_egg.json
│  │     │  ├─ spire_armor_trim_smithing_template.json
│  │     │  ├─ splash_potion.json
│  │     │  ├─ sponge.json
│  │     │  ├─ spore_blossom.json
│  │     │  ├─ spruce_boat.json
│  │     │  ├─ spruce_button.json
│  │     │  ├─ spruce_chest_boat.json
│  │     │  ├─ spruce_door.json
│  │     │  ├─ spruce_fence.json
│  │     │  ├─ spruce_fence_gate.json
│  │     │  ├─ spruce_hanging_sign.json
│  │     │  ├─ spruce_leaves.json
│  │     │  ├─ spruce_log.json
│  │     │  ├─ spruce_planks.json
│  │     │  ├─ spruce_pressure_plate.json
│  │     │  ├─ spruce_sapling.json
│  │     │  ├─ spruce_shelf.json
│  │     │  ├─ spruce_sign.json
│  │     │  ├─ spruce_slab.json
│  │     │  ├─ spruce_stairs.json
│  │     │  ├─ spruce_trapdoor.json
│  │     │  ├─ spruce_wood.json
│  │     │  ├─ spyglass.json
│  │     │  ├─ squid_spawn_egg.json
│  │     │  ├─ stick.json
│  │     │  ├─ sticky_piston.json
│  │     │  ├─ stone.json
│  │     │  ├─ stonecutter.json
│  │     │  ├─ stone_axe.json
│  │     │  ├─ stone_bricks.json
│  │     │  ├─ stone_brick_slab.json
│  │     │  ├─ stone_brick_stairs.json
│  │     │  ├─ stone_brick_wall.json
│  │     │  ├─ stone_button.json
│  │     │  ├─ stone_hoe.json
│  │     │  ├─ stone_pickaxe.json
│  │     │  ├─ stone_pressure_plate.json
│  │     │  ├─ stone_shovel.json
│  │     │  ├─ stone_slab.json
│  │     │  ├─ stone_spear.json
│  │     │  ├─ stone_stairs.json
│  │     │  ├─ stone_sword.json
│  │     │  ├─ stray_spawn_egg.json
│  │     │  ├─ strider_spawn_egg.json
│  │     │  ├─ string.json
│  │     │  ├─ stripped_acacia_log.json
│  │     │  ├─ stripped_acacia_wood.json
│  │     │  ├─ stripped_bamboo_block.json
│  │     │  ├─ stripped_birch_log.json
│  │     │  ├─ stripped_birch_wood.json
│  │     │  ├─ stripped_cherry_log.json
│  │     │  ├─ stripped_cherry_wood.json
│  │     │  ├─ stripped_crimson_hyphae.json
│  │     │  ├─ stripped_crimson_stem.json
│  │     │  ├─ stripped_dark_oak_log.json
│  │     │  ├─ stripped_dark_oak_wood.json
│  │     │  ├─ stripped_jungle_log.json
│  │     │  ├─ stripped_jungle_wood.json
│  │     │  ├─ stripped_mangrove_log.json
│  │     │  ├─ stripped_mangrove_wood.json
│  │     │  ├─ stripped_oak_log.json
│  │     │  ├─ stripped_oak_wood.json
│  │     │  ├─ stripped_pale_oak_log.json
│  │     │  ├─ stripped_pale_oak_wood.json
│  │     │  ├─ stripped_spruce_log.json
│  │     │  ├─ stripped_spruce_wood.json
│  │     │  ├─ stripped_warped_hyphae.json
│  │     │  ├─ stripped_warped_stem.json
│  │     │  ├─ structure_block.json
│  │     │  ├─ structure_void.json
│  │     │  ├─ sugar.json
│  │     │  ├─ sugar_cane.json
│  │     │  ├─ sunflower.json
│  │     │  ├─ suspicious_gravel.json
│  │     │  ├─ suspicious_sand.json
│  │     │  ├─ suspicious_stew.json
│  │     │  ├─ sweet_berries.json
│  │     │  ├─ tadpole_bucket.json
│  │     │  ├─ tadpole_spawn_egg.json
│  │     │  ├─ tall_dry_grass.json
│  │     │  ├─ tall_grass.json
│  │     │  ├─ target.json
│  │     │  ├─ terracotta.json
│  │     │  ├─ test_block.json
│  │     │  ├─ test_instance_block.json
│  │     │  ├─ tide_armor_trim_smithing_template.json
│  │     │  ├─ tinted_glass.json
│  │     │  ├─ tipped_arrow.json
│  │     │  ├─ tnt.json
│  │     │  ├─ tnt_minecart.json
│  │     │  ├─ torch.json
│  │     │  ├─ torchflower.json
│  │     │  ├─ torchflower_seeds.json
│  │     │  ├─ totem_of_undying.json
│  │     │  ├─ trader_llama_spawn_egg.json
│  │     │  ├─ trapped_chest.json
│  │     │  ├─ trial_key.json
│  │     │  ├─ trial_spawner.json
│  │     │  ├─ trident.json
│  │     │  ├─ tripwire_hook.json
│  │     │  ├─ tropical_fish.json
│  │     │  ├─ tropical_fish_bucket.json
│  │     │  ├─ tropical_fish_spawn_egg.json
│  │     │  ├─ tube_coral.json
│  │     │  ├─ tube_coral_block.json
│  │     │  ├─ tube_coral_fan.json
│  │     │  ├─ tuff.json
│  │     │  ├─ tuff_bricks.json
│  │     │  ├─ tuff_brick_slab.json
│  │     │  ├─ tuff_brick_stairs.json
│  │     │  ├─ tuff_brick_wall.json
│  │     │  ├─ tuff_slab.json
│  │     │  ├─ tuff_stairs.json
│  │     │  ├─ tuff_wall.json
│  │     │  ├─ turtle_egg.json
│  │     │  ├─ turtle_helmet.json
│  │     │  ├─ turtle_scute.json
│  │     │  ├─ turtle_spawn_egg.json
│  │     │  ├─ twisting_vines.json
│  │     │  ├─ vault.json
│  │     │  ├─ verdant_froglight.json
│  │     │  ├─ vex_armor_trim_smithing_template.json
│  │     │  ├─ vex_spawn_egg.json
│  │     │  ├─ villager_spawn_egg.json
│  │     │  ├─ vindicator_spawn_egg.json
│  │     │  ├─ vine.json
│  │     │  ├─ wandering_trader_spawn_egg.json
│  │     │  ├─ warden_spawn_egg.json
│  │     │  ├─ ward_armor_trim_smithing_template.json
│  │     │  ├─ warped_button.json
│  │     │  ├─ warped_door.json
│  │     │  ├─ warped_fence.json
│  │     │  ├─ warped_fence_gate.json
│  │     │  ├─ warped_fungus.json
│  │     │  ├─ warped_fungus_on_a_stick.json
│  │     │  ├─ warped_hanging_sign.json
│  │     │  ├─ warped_hyphae.json
│  │     │  ├─ warped_nylium.json
│  │     │  ├─ warped_planks.json
│  │     │  ├─ warped_pressure_plate.json
│  │     │  ├─ warped_roots.json
│  │     │  ├─ warped_shelf.json
│  │     │  ├─ warped_sign.json
│  │     │  ├─ warped_slab.json
│  │     │  ├─ warped_stairs.json
│  │     │  ├─ warped_stem.json
│  │     │  ├─ warped_trapdoor.json
│  │     │  ├─ warped_wart_block.json
│  │     │  ├─ water_bucket.json
│  │     │  ├─ waxed_chiseled_copper.json
│  │     │  ├─ waxed_copper_bars.json
│  │     │  ├─ waxed_copper_block.json
│  │     │  ├─ waxed_copper_bulb.json
│  │     │  ├─ waxed_copper_chain.json
│  │     │  ├─ waxed_copper_chest.json
│  │     │  ├─ waxed_copper_door.json
│  │     │  ├─ waxed_copper_golem_statue.json
│  │     │  ├─ waxed_copper_grate.json
│  │     │  ├─ waxed_copper_lantern.json
│  │     │  ├─ waxed_copper_trapdoor.json
│  │     │  ├─ waxed_cut_copper.json
│  │     │  ├─ waxed_cut_copper_slab.json
│  │     │  ├─ waxed_cut_copper_stairs.json
│  │     │  ├─ waxed_exposed_chiseled_copper.json
│  │     │  ├─ waxed_exposed_copper.json
│  │     │  ├─ waxed_exposed_copper_bars.json
│  │     │  ├─ waxed_exposed_copper_bulb.json
│  │     │  ├─ waxed_exposed_copper_chain.json
│  │     │  ├─ waxed_exposed_copper_chest.json
│  │     │  ├─ waxed_exposed_copper_door.json
│  │     │  ├─ waxed_exposed_copper_golem_statue.json
│  │     │  ├─ waxed_exposed_copper_grate.json
│  │     │  ├─ waxed_exposed_copper_lantern.json
│  │     │  ├─ waxed_exposed_copper_trapdoor.json
│  │     │  ├─ waxed_exposed_cut_copper.json
│  │     │  ├─ waxed_exposed_cut_copper_slab.json
│  │     │  ├─ waxed_exposed_cut_copper_stairs.json
│  │     │  ├─ waxed_exposed_lightning_rod.json
│  │     │  ├─ waxed_lightning_rod.json
│  │     │  ├─ waxed_oxidized_chiseled_copper.json
│  │     │  ├─ waxed_oxidized_copper.json
│  │     │  ├─ waxed_oxidized_copper_bars.json
│  │     │  ├─ waxed_oxidized_copper_bulb.json
│  │     │  ├─ waxed_oxidized_copper_chain.json
│  │     │  ├─ waxed_oxidized_copper_chest.json
│  │     │  ├─ waxed_oxidized_copper_door.json
│  │     │  ├─ waxed_oxidized_copper_golem_statue.json
│  │     │  ├─ waxed_oxidized_copper_grate.json
│  │     │  ├─ waxed_oxidized_copper_lantern.json
│  │     │  ├─ waxed_oxidized_copper_trapdoor.json
│  │     │  ├─ waxed_oxidized_cut_copper.json
│  │     │  ├─ waxed_oxidized_cut_copper_slab.json
│  │     │  ├─ waxed_oxidized_cut_copper_stairs.json
│  │     │  ├─ waxed_oxidized_lightning_rod.json
│  │     │  ├─ waxed_weathered_chiseled_copper.json
│  │     │  ├─ waxed_weathered_copper.json
│  │     │  ├─ waxed_weathered_copper_bars.json
│  │     │  ├─ waxed_weathered_copper_bulb.json
│  │     │  ├─ waxed_weathered_copper_chain.json
│  │     │  ├─ waxed_weathered_copper_chest.json
│  │     │  ├─ waxed_weathered_copper_door.json
│  │     │  ├─ waxed_weathered_copper_golem_statue.json
│  │     │  ├─ waxed_weathered_copper_grate.json
│  │     │  ├─ waxed_weathered_copper_lantern.json
│  │     │  ├─ waxed_weathered_copper_trapdoor.json
│  │     │  ├─ waxed_weathered_cut_copper.json
│  │     │  ├─ waxed_weathered_cut_copper_slab.json
│  │     │  ├─ waxed_weathered_cut_copper_stairs.json
│  │     │  ├─ waxed_weathered_lightning_rod.json
│  │     │  ├─ wayfinder_armor_trim_smithing_template.json
│  │     │  ├─ weathered_chiseled_copper.json
│  │     │  ├─ weathered_copper.json
│  │     │  ├─ weathered_copper_bars.json
│  │     │  ├─ weathered_copper_bulb.json
│  │     │  ├─ weathered_copper_chain.json
│  │     │  ├─ weathered_copper_chest.json
│  │     │  ├─ weathered_copper_door.json
│  │     │  ├─ weathered_copper_golem_statue.json
│  │     │  ├─ weathered_copper_grate.json
│  │     │  ├─ weathered_copper_lantern.json
│  │     │  ├─ weathered_copper_trapdoor.json
│  │     │  ├─ weathered_cut_copper.json
│  │     │  ├─ weathered_cut_copper_slab.json
│  │     │  ├─ weathered_cut_copper_stairs.json
│  │     │  ├─ weathered_lightning_rod.json
│  │     │  ├─ weeping_vines.json
│  │     │  ├─ wet_sponge.json
│  │     │  ├─ wheat.json
│  │     │  ├─ wheat_seeds.json
│  │     │  ├─ white_banner.json
│  │     │  ├─ white_bed.json
│  │     │  ├─ white_bundle.json
│  │     │  ├─ white_candle.json
│  │     │  ├─ white_carpet.json
│  │     │  ├─ white_concrete.json
│  │     │  ├─ white_concrete_powder.json
│  │     │  ├─ white_dye.json
│  │     │  ├─ white_glazed_terracotta.json
│  │     │  ├─ white_harness.json
│  │     │  ├─ white_shulker_box.json
│  │     │  ├─ white_stained_glass.json
│  │     │  ├─ white_stained_glass_pane.json
│  │     │  ├─ white_terracotta.json
│  │     │  ├─ white_tulip.json
│  │     │  ├─ white_wool.json
│  │     │  ├─ wildflowers.json
│  │     │  ├─ wild_armor_trim_smithing_template.json
│  │     │  ├─ wind_charge.json
│  │     │  ├─ witch_spawn_egg.json
│  │     │  ├─ wither_rose.json
│  │     │  ├─ wither_skeleton_skull.json
│  │     │  ├─ wither_skeleton_spawn_egg.json
│  │     │  ├─ wither_spawn_egg.json
│  │     │  ├─ wolf_armor.json
│  │     │  ├─ wolf_spawn_egg.json
│  │     │  ├─ wooden_axe.json
│  │     │  ├─ wooden_hoe.json
│  │     │  ├─ wooden_pickaxe.json
│  │     │  ├─ wooden_shovel.json
│  │     │  ├─ wooden_spear.json
│  │     │  ├─ wooden_sword.json
│  │     │  ├─ writable_book.json
│  │     │  ├─ written_book.json
│  │     │  ├─ yellow_banner.json
│  │     │  ├─ yellow_bed.json
│  │     │  ├─ yellow_bundle.json
│  │     │  ├─ yellow_candle.json
│  │     │  ├─ yellow_carpet.json
│  │     │  ├─ yellow_concrete.json
│  │     │  ├─ yellow_concrete_powder.json
│  │     │  ├─ yellow_dye.json
│  │     │  ├─ yellow_glazed_terracotta.json
│  │     │  ├─ yellow_harness.json
│  │     │  ├─ yellow_shulker_box.json
│  │     │  ├─ yellow_stained_glass.json
│  │     │  ├─ yellow_stained_glass_pane.json
│  │     │  ├─ yellow_terracotta.json
│  │     │  ├─ yellow_wool.json
│  │     │  ├─ zoglin_spawn_egg.json
│  │     │  ├─ zombie_head.json
│  │     │  ├─ zombie_horse_spawn_egg.json
│  │     │  ├─ zombie_nautilus_spawn_egg.json
│  │     │  ├─ zombie_spawn_egg.json
│  │     │  ├─ zombie_villager_spawn_egg.json
│  │     │  └─ zombified_piglin_spawn_egg.json
│  │     ├─ lang
│  │     │  ├─ deprecated.json
│  │     │  └─ en_us.json
│  │     ├─ models
│  │     │  ├─ block
│  │     │  │  ├─ acacia_button.json
│  │     │  │  ├─ acacia_button_inventory.json
│  │     │  │  ├─ acacia_button_pressed.json
│  │     │  │  ├─ acacia_door_bottom_left.json
│  │     │  │  ├─ acacia_door_bottom_left_open.json
│  │     │  │  ├─ acacia_door_bottom_right.json
│  │     │  │  ├─ acacia_door_bottom_right_open.json
│  │     │  │  ├─ acacia_door_top_left.json
│  │     │  │  ├─ acacia_door_top_left_open.json
│  │     │  │  ├─ acacia_door_top_right.json
│  │     │  │  ├─ acacia_door_top_right_open.json
│  │     │  │  ├─ acacia_fence_gate.json
│  │     │  │  ├─ acacia_fence_gate_open.json
│  │     │  │  ├─ acacia_fence_gate_wall.json
│  │     │  │  ├─ acacia_fence_gate_wall_open.json
│  │     │  │  ├─ acacia_fence_inventory.json
│  │     │  │  ├─ acacia_fence_post.json
│  │     │  │  ├─ acacia_fence_side.json
│  │     │  │  ├─ acacia_hanging_sign.json
│  │     │  │  ├─ acacia_leaves.json
│  │     │  │  ├─ acacia_log.json
│  │     │  │  ├─ acacia_log_horizontal.json
│  │     │  │  ├─ acacia_planks.json
│  │     │  │  ├─ acacia_pressure_plate.json
│  │     │  │  ├─ acacia_pressure_plate_down.json
│  │     │  │  ├─ acacia_sapling.json
│  │     │  │  ├─ acacia_shelf.json
│  │     │  │  ├─ acacia_shelf_center.json
│  │     │  │  ├─ acacia_shelf_inventory.json
│  │     │  │  ├─ acacia_shelf_left.json
│  │     │  │  ├─ acacia_shelf_right.json
│  │     │  │  ├─ acacia_shelf_unconnected.json
│  │     │  │  ├─ acacia_shelf_unpowered.json
│  │     │  │  ├─ acacia_sign.json
│  │     │  │  ├─ acacia_slab.json
│  │     │  │  ├─ acacia_slab_top.json
│  │     │  │  ├─ acacia_stairs.json
│  │     │  │  ├─ acacia_stairs_inner.json
│  │     │  │  ├─ acacia_stairs_outer.json
│  │     │  │  ├─ acacia_trapdoor_bottom.json
│  │     │  │  ├─ acacia_trapdoor_open.json
│  │     │  │  ├─ acacia_trapdoor_top.json
│  │     │  │  ├─ acacia_wood.json
│  │     │  │  ├─ activator_rail.json
│  │     │  │  ├─ activator_rail_on.json
│  │     │  │  ├─ activator_rail_on_raised_ne.json
│  │     │  │  ├─ activator_rail_on_raised_sw.json
│  │     │  │  ├─ activator_rail_raised_ne.json
│  │     │  │  ├─ activator_rail_raised_sw.json
│  │     │  │  ├─ air.json
│  │     │  │  ├─ allium.json
│  │     │  │  ├─ amethyst_block.json
│  │     │  │  ├─ amethyst_cluster.json
│  │     │  │  ├─ ancient_debris.json
│  │     │  │  ├─ andesite.json
│  │     │  │  ├─ andesite_slab.json
│  │     │  │  ├─ andesite_slab_top.json
│  │     │  │  ├─ andesite_stairs.json
│  │     │  │  ├─ andesite_stairs_inner.json
│  │     │  │  ├─ andesite_stairs_outer.json
│  │     │  │  ├─ andesite_wall_inventory.json
│  │     │  │  ├─ andesite_wall_post.json
│  │     │  │  ├─ andesite_wall_side.json
│  │     │  │  ├─ andesite_wall_side_tall.json
│  │     │  │  ├─ anvil.json
│  │     │  │  ├─ attached_melon_stem.json
│  │     │  │  ├─ attached_pumpkin_stem.json
│  │     │  │  ├─ azalea.json
│  │     │  │  ├─ azalea_leaves.json
│  │     │  │  ├─ azure_bluet.json
│  │     │  │  ├─ bamboo1_age0.json
│  │     │  │  ├─ bamboo1_age1.json
│  │     │  │  ├─ bamboo2_age0.json
│  │     │  │  ├─ bamboo2_age1.json
│  │     │  │  ├─ bamboo3_age0.json
│  │     │  │  ├─ bamboo3_age1.json
│  │     │  │  ├─ bamboo4_age0.json
│  │     │  │  ├─ bamboo4_age1.json
│  │     │  │  ├─ bamboo_block.json
│  │     │  │  ├─ bamboo_block_x.json
│  │     │  │  ├─ bamboo_block_y.json
│  │     │  │  ├─ bamboo_block_z.json
│  │     │  │  ├─ bamboo_button.json
│  │     │  │  ├─ bamboo_button_inventory.json
│  │     │  │  ├─ bamboo_button_pressed.json
│  │     │  │  ├─ bamboo_door_bottom_left.json
│  │     │  │  ├─ bamboo_door_bottom_left_open.json
│  │     │  │  ├─ bamboo_door_bottom_right.json
│  │     │  │  ├─ bamboo_door_bottom_right_open.json
│  │     │  │  ├─ bamboo_door_top_left.json
│  │     │  │  ├─ bamboo_door_top_left_open.json
│  │     │  │  ├─ bamboo_door_top_right.json
│  │     │  │  ├─ bamboo_door_top_right_open.json
│  │     │  │  ├─ bamboo_fence_gate.json
│  │     │  │  ├─ bamboo_fence_gate_open.json
│  │     │  │  ├─ bamboo_fence_gate_wall.json
│  │     │  │  ├─ bamboo_fence_gate_wall_open.json
│  │     │  │  ├─ bamboo_fence_inventory.json
│  │     │  │  ├─ bamboo_fence_post.json
│  │     │  │  ├─ bamboo_fence_side_east.json
│  │     │  │  ├─ bamboo_fence_side_north.json
│  │     │  │  ├─ bamboo_fence_side_south.json
│  │     │  │  ├─ bamboo_fence_side_west.json
│  │     │  │  ├─ bamboo_hanging_sign.json
│  │     │  │  ├─ bamboo_large_leaves.json
│  │     │  │  ├─ bamboo_mosaic.json
│  │     │  │  ├─ bamboo_mosaic_slab.json
│  │     │  │  ├─ bamboo_mosaic_slab_top.json
│  │     │  │  ├─ bamboo_mosaic_stairs.json
│  │     │  │  ├─ bamboo_mosaic_stairs_inner.json
│  │     │  │  ├─ bamboo_mosaic_stairs_outer.json
│  │     │  │  ├─ bamboo_planks.json
│  │     │  │  ├─ bamboo_pressure_plate.json
│  │     │  │  ├─ bamboo_pressure_plate_down.json
│  │     │  │  ├─ bamboo_sapling.json
│  │     │  │  ├─ bamboo_shelf.json
│  │     │  │  ├─ bamboo_shelf_center.json
│  │     │  │  ├─ bamboo_shelf_inventory.json
│  │     │  │  ├─ bamboo_shelf_left.json
│  │     │  │  ├─ bamboo_shelf_right.json
│  │     │  │  ├─ bamboo_shelf_unconnected.json
│  │     │  │  ├─ bamboo_shelf_unpowered.json
│  │     │  │  ├─ bamboo_sign.json
│  │     │  │  ├─ bamboo_slab.json
│  │     │  │  ├─ bamboo_slab_top.json
│  │     │  │  ├─ bamboo_small_leaves.json
│  │     │  │  ├─ bamboo_stairs.json
│  │     │  │  ├─ bamboo_stairs_inner.json
│  │     │  │  ├─ bamboo_stairs_outer.json
│  │     │  │  ├─ bamboo_trapdoor_bottom.json
│  │     │  │  ├─ bamboo_trapdoor_open.json
│  │     │  │  ├─ bamboo_trapdoor_top.json
│  │     │  │  ├─ banner.json
│  │     │  │  ├─ barrel.json
│  │     │  │  ├─ barrel_open.json
│  │     │  │  ├─ barrier.json
│  │     │  │  ├─ basalt.json
│  │     │  │  ├─ beacon.json
│  │     │  │  ├─ bed.json
│  │     │  │  ├─ bedrock.json
│  │     │  │  ├─ bedrock_mirrored.json
│  │     │  │  ├─ beehive_empty.json
│  │     │  │  ├─ beehive_honey.json
│  │     │  │  ├─ beetroots_stage0.json
│  │     │  │  ├─ beetroots_stage1.json
│  │     │  │  ├─ beetroots_stage2.json
│  │     │  │  ├─ beetroots_stage3.json
│  │     │  │  ├─ bee_nest_empty.json
│  │     │  │  ├─ bee_nest_honey.json
│  │     │  │  ├─ bell_between_walls.json
│  │     │  │  ├─ bell_ceiling.json
│  │     │  │  ├─ bell_floor.json
│  │     │  │  ├─ bell_wall.json
│  │     │  │  ├─ big_dripleaf.json
│  │     │  │  ├─ big_dripleaf_full_tilt.json
│  │     │  │  ├─ big_dripleaf_partial_tilt.json
│  │     │  │  ├─ big_dripleaf_stem.json
│  │     │  │  ├─ birch_button.json
│  │     │  │  ├─ birch_button_inventory.json
│  │     │  │  ├─ birch_button_pressed.json
│  │     │  │  ├─ birch_door_bottom_left.json
│  │     │  │  ├─ birch_door_bottom_left_open.json
│  │     │  │  ├─ birch_door_bottom_right.json
│  │     │  │  ├─ birch_door_bottom_right_open.json
│  │     │  │  ├─ birch_door_top_left.json
│  │     │  │  ├─ birch_door_top_left_open.json
│  │     │  │  ├─ birch_door_top_right.json
│  │     │  │  ├─ birch_door_top_right_open.json
│  │     │  │  ├─ birch_fence_gate.json
│  │     │  │  ├─ birch_fence_gate_open.json
│  │     │  │  ├─ birch_fence_gate_wall.json
│  │     │  │  ├─ birch_fence_gate_wall_open.json
│  │     │  │  ├─ birch_fence_inventory.json
│  │     │  │  ├─ birch_fence_post.json
│  │     │  │  ├─ birch_fence_side.json
│  │     │  │  ├─ birch_hanging_sign.json
│  │     │  │  ├─ birch_leaves.json
│  │     │  │  ├─ birch_log.json
│  │     │  │  ├─ birch_log_horizontal.json
│  │     │  │  ├─ birch_planks.json
│  │     │  │  ├─ birch_pressure_plate.json
│  │     │  │  ├─ birch_pressure_plate_down.json
│  │     │  │  ├─ birch_sapling.json
│  │     │  │  ├─ birch_shelf.json
│  │     │  │  ├─ birch_shelf_center.json
│  │     │  │  ├─ birch_shelf_inventory.json
│  │     │  │  ├─ birch_shelf_left.json
│  │     │  │  ├─ birch_shelf_right.json
│  │     │  │  ├─ birch_shelf_unconnected.json
│  │     │  │  ├─ birch_shelf_unpowered.json
│  │     │  │  ├─ birch_sign.json
│  │     │  │  ├─ birch_slab.json
│  │     │  │  ├─ birch_slab_top.json
│  │     │  │  ├─ birch_stairs.json
│  │     │  │  ├─ birch_stairs_inner.json
│  │     │  │  ├─ birch_stairs_outer.json
│  │     │  │  ├─ birch_trapdoor_bottom.json
│  │     │  │  ├─ birch_trapdoor_open.json
│  │     │  │  ├─ birch_trapdoor_top.json
│  │     │  │  ├─ birch_wood.json
│  │     │  │  ├─ blackstone.json
│  │     │  │  ├─ blackstone_slab.json
│  │     │  │  ├─ blackstone_slab_top.json
│  │     │  │  ├─ blackstone_stairs.json
│  │     │  │  ├─ blackstone_stairs_inner.json
│  │     │  │  ├─ blackstone_stairs_outer.json
│  │     │  │  ├─ blackstone_wall_inventory.json
│  │     │  │  ├─ blackstone_wall_post.json
│  │     │  │  ├─ blackstone_wall_side.json
│  │     │  │  ├─ blackstone_wall_side_tall.json
│  │     │  │  ├─ black_candle_cake.json
│  │     │  │  ├─ black_candle_cake_lit.json
│  │     │  │  ├─ black_candle_four_candles.json
│  │     │  │  ├─ black_candle_four_candles_lit.json
│  │     │  │  ├─ black_candle_one_candle.json
│  │     │  │  ├─ black_candle_one_candle_lit.json
│  │     │  │  ├─ black_candle_three_candles.json
│  │     │  │  ├─ black_candle_three_candles_lit.json
│  │     │  │  ├─ black_candle_two_candles.json
│  │     │  │  ├─ black_candle_two_candles_lit.json
│  │     │  │  ├─ black_carpet.json
│  │     │  │  ├─ black_concrete.json
│  │     │  │  ├─ black_concrete_powder.json
│  │     │  │  ├─ black_glazed_terracotta.json
│  │     │  │  ├─ black_shulker_box.json
│  │     │  │  ├─ black_stained_glass.json
│  │     │  │  ├─ black_stained_glass_pane_noside.json
│  │     │  │  ├─ black_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ black_stained_glass_pane_post.json
│  │     │  │  ├─ black_stained_glass_pane_side.json
│  │     │  │  ├─ black_stained_glass_pane_side_alt.json
│  │     │  │  ├─ black_terracotta.json
│  │     │  │  ├─ black_wool.json
│  │     │  │  ├─ blast_furnace.json
│  │     │  │  ├─ blast_furnace_on.json
│  │     │  │  ├─ block.json
│  │     │  │  ├─ blue_candle_cake.json
│  │     │  │  ├─ blue_candle_cake_lit.json
│  │     │  │  ├─ blue_candle_four_candles.json
│  │     │  │  ├─ blue_candle_four_candles_lit.json
│  │     │  │  ├─ blue_candle_one_candle.json
│  │     │  │  ├─ blue_candle_one_candle_lit.json
│  │     │  │  ├─ blue_candle_three_candles.json
│  │     │  │  ├─ blue_candle_three_candles_lit.json
│  │     │  │  ├─ blue_candle_two_candles.json
│  │     │  │  ├─ blue_candle_two_candles_lit.json
│  │     │  │  ├─ blue_carpet.json
│  │     │  │  ├─ blue_concrete.json
│  │     │  │  ├─ blue_concrete_powder.json
│  │     │  │  ├─ blue_glazed_terracotta.json
│  │     │  │  ├─ blue_ice.json
│  │     │  │  ├─ blue_orchid.json
│  │     │  │  ├─ blue_shulker_box.json
│  │     │  │  ├─ blue_stained_glass.json
│  │     │  │  ├─ blue_stained_glass_pane_noside.json
│  │     │  │  ├─ blue_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ blue_stained_glass_pane_post.json
│  │     │  │  ├─ blue_stained_glass_pane_side.json
│  │     │  │  ├─ blue_stained_glass_pane_side_alt.json
│  │     │  │  ├─ blue_terracotta.json
│  │     │  │  ├─ blue_wool.json
│  │     │  │  ├─ bone_block.json
│  │     │  │  ├─ bookshelf.json
│  │     │  │  ├─ brain_coral.json
│  │     │  │  ├─ brain_coral_block.json
│  │     │  │  ├─ brain_coral_fan.json
│  │     │  │  ├─ brain_coral_wall_fan.json
│  │     │  │  ├─ brewing_stand.json
│  │     │  │  ├─ brewing_stand_bottle0.json
│  │     │  │  ├─ brewing_stand_bottle1.json
│  │     │  │  ├─ brewing_stand_bottle2.json
│  │     │  │  ├─ brewing_stand_empty0.json
│  │     │  │  ├─ brewing_stand_empty1.json
│  │     │  │  ├─ brewing_stand_empty2.json
│  │     │  │  ├─ bricks.json
│  │     │  │  ├─ brick_slab.json
│  │     │  │  ├─ brick_slab_top.json
│  │     │  │  ├─ brick_stairs.json
│  │     │  │  ├─ brick_stairs_inner.json
│  │     │  │  ├─ brick_stairs_outer.json
│  │     │  │  ├─ brick_wall_inventory.json
│  │     │  │  ├─ brick_wall_post.json
│  │     │  │  ├─ brick_wall_side.json
│  │     │  │  ├─ brick_wall_side_tall.json
│  │     │  │  ├─ brown_candle_cake.json
│  │     │  │  ├─ brown_candle_cake_lit.json
│  │     │  │  ├─ brown_candle_four_candles.json
│  │     │  │  ├─ brown_candle_four_candles_lit.json
│  │     │  │  ├─ brown_candle_one_candle.json
│  │     │  │  ├─ brown_candle_one_candle_lit.json
│  │     │  │  ├─ brown_candle_three_candles.json
│  │     │  │  ├─ brown_candle_three_candles_lit.json
│  │     │  │  ├─ brown_candle_two_candles.json
│  │     │  │  ├─ brown_candle_two_candles_lit.json
│  │     │  │  ├─ brown_carpet.json
│  │     │  │  ├─ brown_concrete.json
│  │     │  │  ├─ brown_concrete_powder.json
│  │     │  │  ├─ brown_glazed_terracotta.json
│  │     │  │  ├─ brown_mushroom.json
│  │     │  │  ├─ brown_mushroom_block.json
│  │     │  │  ├─ brown_mushroom_block_inventory.json
│  │     │  │  ├─ brown_shulker_box.json
│  │     │  │  ├─ brown_stained_glass.json
│  │     │  │  ├─ brown_stained_glass_pane_noside.json
│  │     │  │  ├─ brown_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ brown_stained_glass_pane_post.json
│  │     │  │  ├─ brown_stained_glass_pane_side.json
│  │     │  │  ├─ brown_stained_glass_pane_side_alt.json
│  │     │  │  ├─ brown_terracotta.json
│  │     │  │  ├─ brown_wool.json
│  │     │  │  ├─ bubble_coral.json
│  │     │  │  ├─ bubble_coral_block.json
│  │     │  │  ├─ bubble_coral_fan.json
│  │     │  │  ├─ bubble_coral_wall_fan.json
│  │     │  │  ├─ budding_amethyst.json
│  │     │  │  ├─ bush.json
│  │     │  │  ├─ button.json
│  │     │  │  ├─ button_inventory.json
│  │     │  │  ├─ button_pressed.json
│  │     │  │  ├─ cactus.json
│  │     │  │  ├─ cactus_flower.json
│  │     │  │  ├─ cake.json
│  │     │  │  ├─ cake_slice1.json
│  │     │  │  ├─ cake_slice2.json
│  │     │  │  ├─ cake_slice3.json
│  │     │  │  ├─ cake_slice4.json
│  │     │  │  ├─ cake_slice5.json
│  │     │  │  ├─ cake_slice6.json
│  │     │  │  ├─ calcite.json
│  │     │  │  ├─ calibrated_sculk_sensor.json
│  │     │  │  ├─ calibrated_sculk_sensor_active.json
│  │     │  │  ├─ calibrated_sculk_sensor_inactive.json
│  │     │  │  ├─ campfire.json
│  │     │  │  ├─ campfire_off.json
│  │     │  │  ├─ candle_cake.json
│  │     │  │  ├─ candle_cake_lit.json
│  │     │  │  ├─ candle_four_candles.json
│  │     │  │  ├─ candle_four_candles_lit.json
│  │     │  │  ├─ candle_one_candle.json
│  │     │  │  ├─ candle_one_candle_lit.json
│  │     │  │  ├─ candle_three_candles.json
│  │     │  │  ├─ candle_three_candles_lit.json
│  │     │  │  ├─ candle_two_candles.json
│  │     │  │  ├─ candle_two_candles_lit.json
│  │     │  │  ├─ carpet.json
│  │     │  │  ├─ carrots_stage0.json
│  │     │  │  ├─ carrots_stage1.json
│  │     │  │  ├─ carrots_stage2.json
│  │     │  │  ├─ carrots_stage3.json
│  │     │  │  ├─ cartography_table.json
│  │     │  │  ├─ carved_pumpkin.json
│  │     │  │  ├─ cauldron.json
│  │     │  │  ├─ cave_vines.json
│  │     │  │  ├─ cave_vines_lit.json
│  │     │  │  ├─ cave_vines_plant.json
│  │     │  │  ├─ cave_vines_plant_lit.json
│  │     │  │  ├─ chain_command_block.json
│  │     │  │  ├─ chain_command_block_conditional.json
│  │     │  │  ├─ cherry_button.json
│  │     │  │  ├─ cherry_button_inventory.json
│  │     │  │  ├─ cherry_button_pressed.json
│  │     │  │  ├─ cherry_door_bottom_left.json
│  │     │  │  ├─ cherry_door_bottom_left_open.json
│  │     │  │  ├─ cherry_door_bottom_right.json
│  │     │  │  ├─ cherry_door_bottom_right_open.json
│  │     │  │  ├─ cherry_door_top_left.json
│  │     │  │  ├─ cherry_door_top_left_open.json
│  │     │  │  ├─ cherry_door_top_right.json
│  │     │  │  ├─ cherry_door_top_right_open.json
│  │     │  │  ├─ cherry_fence_gate.json
│  │     │  │  ├─ cherry_fence_gate_open.json
│  │     │  │  ├─ cherry_fence_gate_wall.json
│  │     │  │  ├─ cherry_fence_gate_wall_open.json
│  │     │  │  ├─ cherry_fence_inventory.json
│  │     │  │  ├─ cherry_fence_post.json
│  │     │  │  ├─ cherry_fence_side.json
│  │     │  │  ├─ cherry_hanging_sign.json
│  │     │  │  ├─ cherry_leaves.json
│  │     │  │  ├─ cherry_log.json
│  │     │  │  ├─ cherry_log_x.json
│  │     │  │  ├─ cherry_log_y.json
│  │     │  │  ├─ cherry_log_z.json
│  │     │  │  ├─ cherry_planks.json
│  │     │  │  ├─ cherry_pressure_plate.json
│  │     │  │  ├─ cherry_pressure_plate_down.json
│  │     │  │  ├─ cherry_sapling.json
│  │     │  │  ├─ cherry_shelf.json
│  │     │  │  ├─ cherry_shelf_center.json
│  │     │  │  ├─ cherry_shelf_inventory.json
│  │     │  │  ├─ cherry_shelf_left.json
│  │     │  │  ├─ cherry_shelf_right.json
│  │     │  │  ├─ cherry_shelf_unconnected.json
│  │     │  │  ├─ cherry_shelf_unpowered.json
│  │     │  │  ├─ cherry_sign.json
│  │     │  │  ├─ cherry_slab.json
│  │     │  │  ├─ cherry_slab_top.json
│  │     │  │  ├─ cherry_stairs.json
│  │     │  │  ├─ cherry_stairs_inner.json
│  │     │  │  ├─ cherry_stairs_outer.json
│  │     │  │  ├─ cherry_trapdoor_bottom.json
│  │     │  │  ├─ cherry_trapdoor_open.json
│  │     │  │  ├─ cherry_trapdoor_top.json
│  │     │  │  ├─ cherry_wood.json
│  │     │  │  ├─ chest.json
│  │     │  │  ├─ chipped_anvil.json
│  │     │  │  ├─ chiseled_bookshelf.json
│  │     │  │  ├─ chiseled_bookshelf_empty_slot_bottom_left.json
│  │     │  │  ├─ chiseled_bookshelf_empty_slot_bottom_mid.json
│  │     │  │  ├─ chiseled_bookshelf_empty_slot_bottom_right.json
│  │     │  │  ├─ chiseled_bookshelf_empty_slot_top_left.json
│  │     │  │  ├─ chiseled_bookshelf_empty_slot_top_mid.json
│  │     │  │  ├─ chiseled_bookshelf_empty_slot_top_right.json
│  │     │  │  ├─ chiseled_bookshelf_inventory.json
│  │     │  │  ├─ chiseled_bookshelf_occupied_slot_bottom_left.json
│  │     │  │  ├─ chiseled_bookshelf_occupied_slot_bottom_mid.json
│  │     │  │  ├─ chiseled_bookshelf_occupied_slot_bottom_right.json
│  │     │  │  ├─ chiseled_bookshelf_occupied_slot_top_left.json
│  │     │  │  ├─ chiseled_bookshelf_occupied_slot_top_mid.json
│  │     │  │  ├─ chiseled_bookshelf_occupied_slot_top_right.json
│  │     │  │  ├─ chiseled_copper.json
│  │     │  │  ├─ chiseled_deepslate.json
│  │     │  │  ├─ chiseled_nether_bricks.json
│  │     │  │  ├─ chiseled_polished_blackstone.json
│  │     │  │  ├─ chiseled_quartz_block.json
│  │     │  │  ├─ chiseled_red_sandstone.json
│  │     │  │  ├─ chiseled_resin_bricks.json
│  │     │  │  ├─ chiseled_sandstone.json
│  │     │  │  ├─ chiseled_stone_bricks.json
│  │     │  │  ├─ chiseled_tuff.json
│  │     │  │  ├─ chiseled_tuff_bricks.json
│  │     │  │  ├─ chorus_flower.json
│  │     │  │  ├─ chorus_flower_dead.json
│  │     │  │  ├─ chorus_plant.json
│  │     │  │  ├─ chorus_plant_noside.json
│  │     │  │  ├─ chorus_plant_noside1.json
│  │     │  │  ├─ chorus_plant_noside2.json
│  │     │  │  ├─ chorus_plant_noside3.json
│  │     │  │  ├─ chorus_plant_side.json
│  │     │  │  ├─ clay.json
│  │     │  │  ├─ closed_eyeblossom.json
│  │     │  │  ├─ coal_block.json
│  │     │  │  ├─ coal_ore.json
│  │     │  │  ├─ coarse_dirt.json
│  │     │  │  ├─ cobbled_deepslate.json
│  │     │  │  ├─ cobbled_deepslate_slab.json
│  │     │  │  ├─ cobbled_deepslate_slab_top.json
│  │     │  │  ├─ cobbled_deepslate_stairs.json
│  │     │  │  ├─ cobbled_deepslate_stairs_inner.json
│  │     │  │  ├─ cobbled_deepslate_stairs_outer.json
│  │     │  │  ├─ cobbled_deepslate_wall_inventory.json
│  │     │  │  ├─ cobbled_deepslate_wall_post.json
│  │     │  │  ├─ cobbled_deepslate_wall_side.json
│  │     │  │  ├─ cobbled_deepslate_wall_side_tall.json
│  │     │  │  ├─ cobblestone.json
│  │     │  │  ├─ cobblestone_slab.json
│  │     │  │  ├─ cobblestone_slab_top.json
│  │     │  │  ├─ cobblestone_stairs.json
│  │     │  │  ├─ cobblestone_stairs_inner.json
│  │     │  │  ├─ cobblestone_stairs_outer.json
│  │     │  │  ├─ cobblestone_wall_inventory.json
│  │     │  │  ├─ cobblestone_wall_post.json
│  │     │  │  ├─ cobblestone_wall_side.json
│  │     │  │  ├─ cobblestone_wall_side_tall.json
│  │     │  │  ├─ cobweb.json
│  │     │  │  ├─ cocoa_stage0.json
│  │     │  │  ├─ cocoa_stage1.json
│  │     │  │  ├─ cocoa_stage2.json
│  │     │  │  ├─ command_block.json
│  │     │  │  ├─ command_block_conditional.json
│  │     │  │  ├─ comparator.json
│  │     │  │  ├─ comparator_on.json
│  │     │  │  ├─ comparator_on_subtract.json
│  │     │  │  ├─ comparator_subtract.json
│  │     │  │  ├─ composter.json
│  │     │  │  ├─ composter_contents1.json
│  │     │  │  ├─ composter_contents2.json
│  │     │  │  ├─ composter_contents3.json
│  │     │  │  ├─ composter_contents4.json
│  │     │  │  ├─ composter_contents5.json
│  │     │  │  ├─ composter_contents6.json
│  │     │  │  ├─ composter_contents7.json
│  │     │  │  ├─ composter_contents_ready.json
│  │     │  │  ├─ conduit.json
│  │     │  │  ├─ copper_bars_cap.json
│  │     │  │  ├─ copper_bars_cap_alt.json
│  │     │  │  ├─ copper_bars_post.json
│  │     │  │  ├─ copper_bars_post_ends.json
│  │     │  │  ├─ copper_bars_side.json
│  │     │  │  ├─ copper_bars_side_alt.json
│  │     │  │  ├─ copper_block.json
│  │     │  │  ├─ copper_bulb.json
│  │     │  │  ├─ copper_bulb_lit.json
│  │     │  │  ├─ copper_bulb_lit_powered.json
│  │     │  │  ├─ copper_bulb_powered.json
│  │     │  │  ├─ copper_chain.json
│  │     │  │  ├─ copper_chest.json
│  │     │  │  ├─ copper_door_bottom_left.json
│  │     │  │  ├─ copper_door_bottom_left_open.json
│  │     │  │  ├─ copper_door_bottom_right.json
│  │     │  │  ├─ copper_door_bottom_right_open.json
│  │     │  │  ├─ copper_door_top_left.json
│  │     │  │  ├─ copper_door_top_left_open.json
│  │     │  │  ├─ copper_door_top_right.json
│  │     │  │  ├─ copper_door_top_right_open.json
│  │     │  │  ├─ copper_golem_statue.json
│  │     │  │  ├─ copper_grate.json
│  │     │  │  ├─ copper_lantern.json
│  │     │  │  ├─ copper_lantern_hanging.json
│  │     │  │  ├─ copper_ore.json
│  │     │  │  ├─ copper_torch.json
│  │     │  │  ├─ copper_trapdoor_bottom.json
│  │     │  │  ├─ copper_trapdoor_open.json
│  │     │  │  ├─ copper_trapdoor_top.json
│  │     │  │  ├─ copper_wall_torch.json
│  │     │  │  ├─ coral_fan.json
│  │     │  │  ├─ coral_wall_fan.json
│  │     │  │  ├─ cornflower.json
│  │     │  │  ├─ cracked_deepslate_bricks.json
│  │     │  │  ├─ cracked_deepslate_tiles.json
│  │     │  │  ├─ cracked_nether_bricks.json
│  │     │  │  ├─ cracked_polished_blackstone_bricks.json
│  │     │  │  ├─ cracked_stone_bricks.json
│  │     │  │  ├─ crafter.json
│  │     │  │  ├─ crafter_crafting.json
│  │     │  │  ├─ crafter_crafting_triggered.json
│  │     │  │  ├─ crafter_triggered.json
│  │     │  │  ├─ crafting_table.json
│  │     │  │  ├─ creaking_heart.json
│  │     │  │  ├─ creaking_heart_awake.json
│  │     │  │  ├─ creaking_heart_awake_horizontal.json
│  │     │  │  ├─ creaking_heart_dormant.json
│  │     │  │  ├─ creaking_heart_dormant_horizontal.json
│  │     │  │  ├─ creaking_heart_horizontal.json
│  │     │  │  ├─ crimson_button.json
│  │     │  │  ├─ crimson_button_inventory.json
│  │     │  │  ├─ crimson_button_pressed.json
│  │     │  │  ├─ crimson_door_bottom_left.json
│  │     │  │  ├─ crimson_door_bottom_left_open.json
│  │     │  │  ├─ crimson_door_bottom_right.json
│  │     │  │  ├─ crimson_door_bottom_right_open.json
│  │     │  │  ├─ crimson_door_top_left.json
│  │     │  │  ├─ crimson_door_top_left_open.json
│  │     │  │  ├─ crimson_door_top_right.json
│  │     │  │  ├─ crimson_door_top_right_open.json
│  │     │  │  ├─ crimson_fence_gate.json
│  │     │  │  ├─ crimson_fence_gate_open.json
│  │     │  │  ├─ crimson_fence_gate_wall.json
│  │     │  │  ├─ crimson_fence_gate_wall_open.json
│  │     │  │  ├─ crimson_fence_inventory.json
│  │     │  │  ├─ crimson_fence_post.json
│  │     │  │  ├─ crimson_fence_side.json
│  │     │  │  ├─ crimson_fungus.json
│  │     │  │  ├─ crimson_hanging_sign.json
│  │     │  │  ├─ crimson_hyphae.json
│  │     │  │  ├─ crimson_nylium.json
│  │     │  │  ├─ crimson_planks.json
│  │     │  │  ├─ crimson_pressure_plate.json
│  │     │  │  ├─ crimson_pressure_plate_down.json
│  │     │  │  ├─ crimson_roots.json
│  │     │  │  ├─ crimson_shelf.json
│  │     │  │  ├─ crimson_shelf_center.json
│  │     │  │  ├─ crimson_shelf_inventory.json
│  │     │  │  ├─ crimson_shelf_left.json
│  │     │  │  ├─ crimson_shelf_right.json
│  │     │  │  ├─ crimson_shelf_unconnected.json
│  │     │  │  ├─ crimson_shelf_unpowered.json
│  │     │  │  ├─ crimson_sign.json
│  │     │  │  ├─ crimson_slab.json
│  │     │  │  ├─ crimson_slab_top.json
│  │     │  │  ├─ crimson_stairs.json
│  │     │  │  ├─ crimson_stairs_inner.json
│  │     │  │  ├─ crimson_stairs_outer.json
│  │     │  │  ├─ crimson_stem.json
│  │     │  │  ├─ crimson_trapdoor_bottom.json
│  │     │  │  ├─ crimson_trapdoor_open.json
│  │     │  │  ├─ crimson_trapdoor_top.json
│  │     │  │  ├─ crop.json
│  │     │  │  ├─ cross.json
│  │     │  │  ├─ cross_emissive.json
│  │     │  │  ├─ crying_obsidian.json
│  │     │  │  ├─ cube.json
│  │     │  │  ├─ cube_all.json
│  │     │  │  ├─ cube_all_inner_faces.json
│  │     │  │  ├─ cube_bottom_top.json
│  │     │  │  ├─ cube_bottom_top_inner_faces.json
│  │     │  │  ├─ cube_column.json
│  │     │  │  ├─ cube_column_horizontal.json
│  │     │  │  ├─ cube_column_mirrored.json
│  │     │  │  ├─ cube_column_uv_locked_x.json
│  │     │  │  ├─ cube_column_uv_locked_y.json
│  │     │  │  ├─ cube_column_uv_locked_z.json
│  │     │  │  ├─ cube_directional.json
│  │     │  │  ├─ cube_mirrored.json
│  │     │  │  ├─ cube_mirrored_all.json
│  │     │  │  ├─ cube_north_west_mirrored.json
│  │     │  │  ├─ cube_north_west_mirrored_all.json
│  │     │  │  ├─ cube_top.json
│  │     │  │  ├─ custom_fence_inventory.json
│  │     │  │  ├─ custom_fence_post.json
│  │     │  │  ├─ custom_fence_side_east.json
│  │     │  │  ├─ custom_fence_side_north.json
│  │     │  │  ├─ custom_fence_side_south.json
│  │     │  │  ├─ custom_fence_side_west.json
│  │     │  │  ├─ cut_copper.json
│  │     │  │  ├─ cut_copper_slab.json
│  │     │  │  ├─ cut_copper_slab_top.json
│  │     │  │  ├─ cut_copper_stairs.json
│  │     │  │  ├─ cut_copper_stairs_inner.json
│  │     │  │  ├─ cut_copper_stairs_outer.json
│  │     │  │  ├─ cut_red_sandstone.json
│  │     │  │  ├─ cut_red_sandstone_slab.json
│  │     │  │  ├─ cut_red_sandstone_slab_top.json
│  │     │  │  ├─ cut_sandstone.json
│  │     │  │  ├─ cut_sandstone_slab.json
│  │     │  │  ├─ cut_sandstone_slab_top.json
│  │     │  │  ├─ cyan_candle_cake.json
│  │     │  │  ├─ cyan_candle_cake_lit.json
│  │     │  │  ├─ cyan_candle_four_candles.json
│  │     │  │  ├─ cyan_candle_four_candles_lit.json
│  │     │  │  ├─ cyan_candle_one_candle.json
│  │     │  │  ├─ cyan_candle_one_candle_lit.json
│  │     │  │  ├─ cyan_candle_three_candles.json
│  │     │  │  ├─ cyan_candle_three_candles_lit.json
│  │     │  │  ├─ cyan_candle_two_candles.json
│  │     │  │  ├─ cyan_candle_two_candles_lit.json
│  │     │  │  ├─ cyan_carpet.json
│  │     │  │  ├─ cyan_concrete.json
│  │     │  │  ├─ cyan_concrete_powder.json
│  │     │  │  ├─ cyan_glazed_terracotta.json
│  │     │  │  ├─ cyan_shulker_box.json
│  │     │  │  ├─ cyan_stained_glass.json
│  │     │  │  ├─ cyan_stained_glass_pane_noside.json
│  │     │  │  ├─ cyan_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ cyan_stained_glass_pane_post.json
│  │     │  │  ├─ cyan_stained_glass_pane_side.json
│  │     │  │  ├─ cyan_stained_glass_pane_side_alt.json
│  │     │  │  ├─ cyan_terracotta.json
│  │     │  │  ├─ cyan_wool.json
│  │     │  │  ├─ damaged_anvil.json
│  │     │  │  ├─ dandelion.json
│  │     │  │  ├─ dark_oak_button.json
│  │     │  │  ├─ dark_oak_button_inventory.json
│  │     │  │  ├─ dark_oak_button_pressed.json
│  │     │  │  ├─ dark_oak_door_bottom_left.json
│  │     │  │  ├─ dark_oak_door_bottom_left_open.json
│  │     │  │  ├─ dark_oak_door_bottom_right.json
│  │     │  │  ├─ dark_oak_door_bottom_right_open.json
│  │     │  │  ├─ dark_oak_door_top_left.json
│  │     │  │  ├─ dark_oak_door_top_left_open.json
│  │     │  │  ├─ dark_oak_door_top_right.json
│  │     │  │  ├─ dark_oak_door_top_right_open.json
│  │     │  │  ├─ dark_oak_fence_gate.json
│  │     │  │  ├─ dark_oak_fence_gate_open.json
│  │     │  │  ├─ dark_oak_fence_gate_wall.json
│  │     │  │  ├─ dark_oak_fence_gate_wall_open.json
│  │     │  │  ├─ dark_oak_fence_inventory.json
│  │     │  │  ├─ dark_oak_fence_post.json
│  │     │  │  ├─ dark_oak_fence_side.json
│  │     │  │  ├─ dark_oak_hanging_sign.json
│  │     │  │  ├─ dark_oak_leaves.json
│  │     │  │  ├─ dark_oak_log.json
│  │     │  │  ├─ dark_oak_log_horizontal.json
│  │     │  │  ├─ dark_oak_planks.json
│  │     │  │  ├─ dark_oak_pressure_plate.json
│  │     │  │  ├─ dark_oak_pressure_plate_down.json
│  │     │  │  ├─ dark_oak_sapling.json
│  │     │  │  ├─ dark_oak_shelf.json
│  │     │  │  ├─ dark_oak_shelf_center.json
│  │     │  │  ├─ dark_oak_shelf_inventory.json
│  │     │  │  ├─ dark_oak_shelf_left.json
│  │     │  │  ├─ dark_oak_shelf_right.json
│  │     │  │  ├─ dark_oak_shelf_unconnected.json
│  │     │  │  ├─ dark_oak_shelf_unpowered.json
│  │     │  │  ├─ dark_oak_sign.json
│  │     │  │  ├─ dark_oak_slab.json
│  │     │  │  ├─ dark_oak_slab_top.json
│  │     │  │  ├─ dark_oak_stairs.json
│  │     │  │  ├─ dark_oak_stairs_inner.json
│  │     │  │  ├─ dark_oak_stairs_outer.json
│  │     │  │  ├─ dark_oak_trapdoor_bottom.json
│  │     │  │  ├─ dark_oak_trapdoor_open.json
│  │     │  │  ├─ dark_oak_trapdoor_top.json
│  │     │  │  ├─ dark_oak_wood.json
│  │     │  │  ├─ dark_prismarine.json
│  │     │  │  ├─ dark_prismarine_slab.json
│  │     │  │  ├─ dark_prismarine_slab_top.json
│  │     │  │  ├─ dark_prismarine_stairs.json
│  │     │  │  ├─ dark_prismarine_stairs_inner.json
│  │     │  │  ├─ dark_prismarine_stairs_outer.json
│  │     │  │  ├─ daylight_detector.json
│  │     │  │  ├─ daylight_detector_inverted.json
│  │     │  │  ├─ dead_brain_coral.json
│  │     │  │  ├─ dead_brain_coral_block.json
│  │     │  │  ├─ dead_brain_coral_fan.json
│  │     │  │  ├─ dead_brain_coral_wall_fan.json
│  │     │  │  ├─ dead_bubble_coral.json
│  │     │  │  ├─ dead_bubble_coral_block.json
│  │     │  │  ├─ dead_bubble_coral_fan.json
│  │     │  │  ├─ dead_bubble_coral_wall_fan.json
│  │     │  │  ├─ dead_bush.json
│  │     │  │  ├─ dead_fire_coral.json
│  │     │  │  ├─ dead_fire_coral_block.json
│  │     │  │  ├─ dead_fire_coral_fan.json
│  │     │  │  ├─ dead_fire_coral_wall_fan.json
│  │     │  │  ├─ dead_horn_coral.json
│  │     │  │  ├─ dead_horn_coral_block.json
│  │     │  │  ├─ dead_horn_coral_fan.json
│  │     │  │  ├─ dead_horn_coral_wall_fan.json
│  │     │  │  ├─ dead_sea_pickle.json
│  │     │  │  ├─ dead_tube_coral.json
│  │     │  │  ├─ dead_tube_coral_block.json
│  │     │  │  ├─ dead_tube_coral_fan.json
│  │     │  │  ├─ dead_tube_coral_wall_fan.json
│  │     │  │  ├─ decorated_pot.json
│  │     │  │  ├─ deepslate.json
│  │     │  │  ├─ deepslate_bricks.json
│  │     │  │  ├─ deepslate_brick_slab.json
│  │     │  │  ├─ deepslate_brick_slab_top.json
│  │     │  │  ├─ deepslate_brick_stairs.json
│  │     │  │  ├─ deepslate_brick_stairs_inner.json
│  │     │  │  ├─ deepslate_brick_stairs_outer.json
│  │     │  │  ├─ deepslate_brick_wall_inventory.json
│  │     │  │  ├─ deepslate_brick_wall_post.json
│  │     │  │  ├─ deepslate_brick_wall_side.json
│  │     │  │  ├─ deepslate_brick_wall_side_tall.json
│  │     │  │  ├─ deepslate_coal_ore.json
│  │     │  │  ├─ deepslate_copper_ore.json
│  │     │  │  ├─ deepslate_diamond_ore.json
│  │     │  │  ├─ deepslate_emerald_ore.json
│  │     │  │  ├─ deepslate_gold_ore.json
│  │     │  │  ├─ deepslate_iron_ore.json
│  │     │  │  ├─ deepslate_lapis_ore.json
│  │     │  │  ├─ deepslate_mirrored.json
│  │     │  │  ├─ deepslate_redstone_ore.json
│  │     │  │  ├─ deepslate_tiles.json
│  │     │  │  ├─ deepslate_tile_slab.json
│  │     │  │  ├─ deepslate_tile_slab_top.json
│  │     │  │  ├─ deepslate_tile_stairs.json
│  │     │  │  ├─ deepslate_tile_stairs_inner.json
│  │     │  │  ├─ deepslate_tile_stairs_outer.json
│  │     │  │  ├─ deepslate_tile_wall_inventory.json
│  │     │  │  ├─ deepslate_tile_wall_post.json
│  │     │  │  ├─ deepslate_tile_wall_side.json
│  │     │  │  ├─ deepslate_tile_wall_side_tall.json
│  │     │  │  ├─ detector_rail.json
│  │     │  │  ├─ detector_rail_on.json
│  │     │  │  ├─ detector_rail_on_raised_ne.json
│  │     │  │  ├─ detector_rail_on_raised_sw.json
│  │     │  │  ├─ detector_rail_raised_ne.json
│  │     │  │  ├─ detector_rail_raised_sw.json
│  │     │  │  ├─ diamond_block.json
│  │     │  │  ├─ diamond_ore.json
│  │     │  │  ├─ diorite.json
│  │     │  │  ├─ diorite_slab.json
│  │     │  │  ├─ diorite_slab_top.json
│  │     │  │  ├─ diorite_stairs.json
│  │     │  │  ├─ diorite_stairs_inner.json
│  │     │  │  ├─ diorite_stairs_outer.json
│  │     │  │  ├─ diorite_wall_inventory.json
│  │     │  │  ├─ diorite_wall_post.json
│  │     │  │  ├─ diorite_wall_side.json
│  │     │  │  ├─ diorite_wall_side_tall.json
│  │     │  │  ├─ dirt.json
│  │     │  │  ├─ dirt_path.json
│  │     │  │  ├─ dispenser.json
│  │     │  │  ├─ dispenser_vertical.json
│  │     │  │  ├─ door_bottom_left.json
│  │     │  │  ├─ door_bottom_left_open.json
│  │     │  │  ├─ door_bottom_right.json
│  │     │  │  ├─ door_bottom_right_open.json
│  │     │  │  ├─ door_top_left.json
│  │     │  │  ├─ door_top_left_open.json
│  │     │  │  ├─ door_top_right.json
│  │     │  │  ├─ door_top_right_open.json
│  │     │  │  ├─ dragon_egg.json
│  │     │  │  ├─ dried_ghast.json
│  │     │  │  ├─ dried_ghast_hydration_0.json
│  │     │  │  ├─ dried_ghast_hydration_1.json
│  │     │  │  ├─ dried_ghast_hydration_2.json
│  │     │  │  ├─ dried_ghast_hydration_3.json
│  │     │  │  ├─ dried_kelp_block.json
│  │     │  │  ├─ dripstone_block.json
│  │     │  │  ├─ dropper.json
│  │     │  │  ├─ dropper_vertical.json
│  │     │  │  ├─ emerald_block.json
│  │     │  │  ├─ emerald_ore.json
│  │     │  │  ├─ enchanting_table.json
│  │     │  │  ├─ ender_chest.json
│  │     │  │  ├─ end_gateway.json
│  │     │  │  ├─ end_portal.json
│  │     │  │  ├─ end_portal_frame.json
│  │     │  │  ├─ end_portal_frame_filled.json
│  │     │  │  ├─ end_rod.json
│  │     │  │  ├─ end_stone.json
│  │     │  │  ├─ end_stone_bricks.json
│  │     │  │  ├─ end_stone_brick_slab.json
│  │     │  │  ├─ end_stone_brick_slab_top.json
│  │     │  │  ├─ end_stone_brick_stairs.json
│  │     │  │  ├─ end_stone_brick_stairs_inner.json
│  │     │  │  ├─ end_stone_brick_stairs_outer.json
│  │     │  │  ├─ end_stone_brick_wall_inventory.json
│  │     │  │  ├─ end_stone_brick_wall_post.json
│  │     │  │  ├─ end_stone_brick_wall_side.json
│  │     │  │  ├─ end_stone_brick_wall_side_tall.json
│  │     │  │  ├─ exposed_chiseled_copper.json
│  │     │  │  ├─ exposed_copper.json
│  │     │  │  ├─ exposed_copper_bars_cap.json
│  │     │  │  ├─ exposed_copper_bars_cap_alt.json
│  │     │  │  ├─ exposed_copper_bars_post.json
│  │     │  │  ├─ exposed_copper_bars_post_ends.json
│  │     │  │  ├─ exposed_copper_bars_side.json
│  │     │  │  ├─ exposed_copper_bars_side_alt.json
│  │     │  │  ├─ exposed_copper_bulb.json
│  │     │  │  ├─ exposed_copper_bulb_lit.json
│  │     │  │  ├─ exposed_copper_bulb_lit_powered.json
│  │     │  │  ├─ exposed_copper_bulb_powered.json
│  │     │  │  ├─ exposed_copper_chain.json
│  │     │  │  ├─ exposed_copper_chest.json
│  │     │  │  ├─ exposed_copper_door_bottom_left.json
│  │     │  │  ├─ exposed_copper_door_bottom_left_open.json
│  │     │  │  ├─ exposed_copper_door_bottom_right.json
│  │     │  │  ├─ exposed_copper_door_bottom_right_open.json
│  │     │  │  ├─ exposed_copper_door_top_left.json
│  │     │  │  ├─ exposed_copper_door_top_left_open.json
│  │     │  │  ├─ exposed_copper_door_top_right.json
│  │     │  │  ├─ exposed_copper_door_top_right_open.json
│  │     │  │  ├─ exposed_copper_golem_statue.json
│  │     │  │  ├─ exposed_copper_grate.json
│  │     │  │  ├─ exposed_copper_lantern.json
│  │     │  │  ├─ exposed_copper_lantern_hanging.json
│  │     │  │  ├─ exposed_copper_trapdoor_bottom.json
│  │     │  │  ├─ exposed_copper_trapdoor_open.json
│  │     │  │  ├─ exposed_copper_trapdoor_top.json
│  │     │  │  ├─ exposed_cut_copper.json
│  │     │  │  ├─ exposed_cut_copper_slab.json
│  │     │  │  ├─ exposed_cut_copper_slab_top.json
│  │     │  │  ├─ exposed_cut_copper_stairs.json
│  │     │  │  ├─ exposed_cut_copper_stairs_inner.json
│  │     │  │  ├─ exposed_cut_copper_stairs_outer.json
│  │     │  │  ├─ exposed_lightning_rod.json
│  │     │  │  ├─ farmland.json
│  │     │  │  ├─ farmland_moist.json
│  │     │  │  ├─ fence_inventory.json
│  │     │  │  ├─ fence_post.json
│  │     │  │  ├─ fence_side.json
│  │     │  │  ├─ fern.json
│  │     │  │  ├─ firefly_bush.json
│  │     │  │  ├─ fire_coral.json
│  │     │  │  ├─ fire_coral_block.json
│  │     │  │  ├─ fire_coral_fan.json
│  │     │  │  ├─ fire_coral_wall_fan.json
│  │     │  │  ├─ fire_floor0.json
│  │     │  │  ├─ fire_floor1.json
│  │     │  │  ├─ fire_side0.json
│  │     │  │  ├─ fire_side1.json
│  │     │  │  ├─ fire_side_alt0.json
│  │     │  │  ├─ fire_side_alt1.json
│  │     │  │  ├─ fire_up0.json
│  │     │  │  ├─ fire_up1.json
│  │     │  │  ├─ fire_up_alt0.json
│  │     │  │  ├─ fire_up_alt1.json
│  │     │  │  ├─ fletching_table.json
│  │     │  │  ├─ flowerbed_1.json
│  │     │  │  ├─ flowerbed_2.json
│  │     │  │  ├─ flowerbed_3.json
│  │     │  │  ├─ flowerbed_4.json
│  │     │  │  ├─ flowering_azalea.json
│  │     │  │  ├─ flowering_azalea_leaves.json
│  │     │  │  ├─ flower_pot.json
│  │     │  │  ├─ flower_pot_cross.json
│  │     │  │  ├─ flower_pot_cross_emissive.json
│  │     │  │  ├─ four_dead_sea_pickles.json
│  │     │  │  ├─ four_sea_pickles.json
│  │     │  │  ├─ four_slightly_cracked_turtle_eggs.json
│  │     │  │  ├─ four_turtle_eggs.json
│  │     │  │  ├─ four_very_cracked_turtle_eggs.json
│  │     │  │  ├─ frogspawn.json
│  │     │  │  ├─ frosted_ice_0.json
│  │     │  │  ├─ frosted_ice_1.json
│  │     │  │  ├─ frosted_ice_2.json
│  │     │  │  ├─ frosted_ice_3.json
│  │     │  │  ├─ furnace.json
│  │     │  │  ├─ furnace_on.json
│  │     │  │  ├─ gilded_blackstone.json
│  │     │  │  ├─ glass.json
│  │     │  │  ├─ glass_pane_noside.json
│  │     │  │  ├─ glass_pane_noside_alt.json
│  │     │  │  ├─ glass_pane_post.json
│  │     │  │  ├─ glass_pane_side.json
│  │     │  │  ├─ glass_pane_side_alt.json
│  │     │  │  ├─ glowstone.json
│  │     │  │  ├─ glow_item_frame.json
│  │     │  │  ├─ glow_item_frame_map.json
│  │     │  │  ├─ glow_lichen.json
│  │     │  │  ├─ gold_block.json
│  │     │  │  ├─ gold_ore.json
│  │     │  │  ├─ granite.json
│  │     │  │  ├─ granite_slab.json
│  │     │  │  ├─ granite_slab_top.json
│  │     │  │  ├─ granite_stairs.json
│  │     │  │  ├─ granite_stairs_inner.json
│  │     │  │  ├─ granite_stairs_outer.json
│  │     │  │  ├─ granite_wall_inventory.json
│  │     │  │  ├─ granite_wall_post.json
│  │     │  │  ├─ granite_wall_side.json
│  │     │  │  ├─ granite_wall_side_tall.json
│  │     │  │  ├─ grass_block.json
│  │     │  │  ├─ grass_block_snow.json
│  │     │  │  ├─ gravel.json
│  │     │  │  ├─ gray_candle_cake.json
│  │     │  │  ├─ gray_candle_cake_lit.json
│  │     │  │  ├─ gray_candle_four_candles.json
│  │     │  │  ├─ gray_candle_four_candles_lit.json
│  │     │  │  ├─ gray_candle_one_candle.json
│  │     │  │  ├─ gray_candle_one_candle_lit.json
│  │     │  │  ├─ gray_candle_three_candles.json
│  │     │  │  ├─ gray_candle_three_candles_lit.json
│  │     │  │  ├─ gray_candle_two_candles.json
│  │     │  │  ├─ gray_candle_two_candles_lit.json
│  │     │  │  ├─ gray_carpet.json
│  │     │  │  ├─ gray_concrete.json
│  │     │  │  ├─ gray_concrete_powder.json
│  │     │  │  ├─ gray_glazed_terracotta.json
│  │     │  │  ├─ gray_shulker_box.json
│  │     │  │  ├─ gray_stained_glass.json
│  │     │  │  ├─ gray_stained_glass_pane_noside.json
│  │     │  │  ├─ gray_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ gray_stained_glass_pane_post.json
│  │     │  │  ├─ gray_stained_glass_pane_side.json
│  │     │  │  ├─ gray_stained_glass_pane_side_alt.json
│  │     │  │  ├─ gray_terracotta.json
│  │     │  │  ├─ gray_wool.json
│  │     │  │  ├─ green_candle_cake.json
│  │     │  │  ├─ green_candle_cake_lit.json
│  │     │  │  ├─ green_candle_four_candles.json
│  │     │  │  ├─ green_candle_four_candles_lit.json
│  │     │  │  ├─ green_candle_one_candle.json
│  │     │  │  ├─ green_candle_one_candle_lit.json
│  │     │  │  ├─ green_candle_three_candles.json
│  │     │  │  ├─ green_candle_three_candles_lit.json
│  │     │  │  ├─ green_candle_two_candles.json
│  │     │  │  ├─ green_candle_two_candles_lit.json
│  │     │  │  ├─ green_carpet.json
│  │     │  │  ├─ green_concrete.json
│  │     │  │  ├─ green_concrete_powder.json
│  │     │  │  ├─ green_glazed_terracotta.json
│  │     │  │  ├─ green_shulker_box.json
│  │     │  │  ├─ green_stained_glass.json
│  │     │  │  ├─ green_stained_glass_pane_noside.json
│  │     │  │  ├─ green_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ green_stained_glass_pane_post.json
│  │     │  │  ├─ green_stained_glass_pane_side.json
│  │     │  │  ├─ green_stained_glass_pane_side_alt.json
│  │     │  │  ├─ green_terracotta.json
│  │     │  │  ├─ green_wool.json
│  │     │  │  ├─ grindstone.json
│  │     │  │  ├─ hanging_roots.json
│  │     │  │  ├─ hay_block.json
│  │     │  │  ├─ hay_block_horizontal.json
│  │     │  │  ├─ heavy_core.json
│  │     │  │  ├─ heavy_weighted_pressure_plate.json
│  │     │  │  ├─ heavy_weighted_pressure_plate_down.json
│  │     │  │  ├─ honeycomb_block.json
│  │     │  │  ├─ honey_block.json
│  │     │  │  ├─ hopper.json
│  │     │  │  ├─ hopper_side.json
│  │     │  │  ├─ horn_coral.json
│  │     │  │  ├─ horn_coral_block.json
│  │     │  │  ├─ horn_coral_fan.json
│  │     │  │  ├─ horn_coral_wall_fan.json
│  │     │  │  ├─ ice.json
│  │     │  │  ├─ inner_stairs.json
│  │     │  │  ├─ iron_bars_cap.json
│  │     │  │  ├─ iron_bars_cap_alt.json
│  │     │  │  ├─ iron_bars_post.json
│  │     │  │  ├─ iron_bars_post_ends.json
│  │     │  │  ├─ iron_bars_side.json
│  │     │  │  ├─ iron_bars_side_alt.json
│  │     │  │  ├─ iron_block.json
│  │     │  │  ├─ iron_chain.json
│  │     │  │  ├─ iron_door_bottom_left.json
│  │     │  │  ├─ iron_door_bottom_left_open.json
│  │     │  │  ├─ iron_door_bottom_right.json
│  │     │  │  ├─ iron_door_bottom_right_open.json
│  │     │  │  ├─ iron_door_top_left.json
│  │     │  │  ├─ iron_door_top_left_open.json
│  │     │  │  ├─ iron_door_top_right.json
│  │     │  │  ├─ iron_door_top_right_open.json
│  │     │  │  ├─ iron_ore.json
│  │     │  │  ├─ iron_trapdoor_bottom.json
│  │     │  │  ├─ iron_trapdoor_open.json
│  │     │  │  ├─ iron_trapdoor_top.json
│  │     │  │  ├─ item_frame.json
│  │     │  │  ├─ item_frame_map.json
│  │     │  │  ├─ jack_o_lantern.json
│  │     │  │  ├─ jigsaw.json
│  │     │  │  ├─ jukebox.json
│  │     │  │  ├─ jungle_button.json
│  │     │  │  ├─ jungle_button_inventory.json
│  │     │  │  ├─ jungle_button_pressed.json
│  │     │  │  ├─ jungle_door_bottom_left.json
│  │     │  │  ├─ jungle_door_bottom_left_open.json
│  │     │  │  ├─ jungle_door_bottom_right.json
│  │     │  │  ├─ jungle_door_bottom_right_open.json
│  │     │  │  ├─ jungle_door_top_left.json
│  │     │  │  ├─ jungle_door_top_left_open.json
│  │     │  │  ├─ jungle_door_top_right.json
│  │     │  │  ├─ jungle_door_top_right_open.json
│  │     │  │  ├─ jungle_fence_gate.json
│  │     │  │  ├─ jungle_fence_gate_open.json
│  │     │  │  ├─ jungle_fence_gate_wall.json
│  │     │  │  ├─ jungle_fence_gate_wall_open.json
│  │     │  │  ├─ jungle_fence_inventory.json
│  │     │  │  ├─ jungle_fence_post.json
│  │     │  │  ├─ jungle_fence_side.json
│  │     │  │  ├─ jungle_hanging_sign.json
│  │     │  │  ├─ jungle_leaves.json
│  │     │  │  ├─ jungle_log.json
│  │     │  │  ├─ jungle_log_horizontal.json
│  │     │  │  ├─ jungle_planks.json
│  │     │  │  ├─ jungle_pressure_plate.json
│  │     │  │  ├─ jungle_pressure_plate_down.json
│  │     │  │  ├─ jungle_sapling.json
│  │     │  │  ├─ jungle_shelf.json
│  │     │  │  ├─ jungle_shelf_center.json
│  │     │  │  ├─ jungle_shelf_inventory.json
│  │     │  │  ├─ jungle_shelf_left.json
│  │     │  │  ├─ jungle_shelf_right.json
│  │     │  │  ├─ jungle_shelf_unconnected.json
│  │     │  │  ├─ jungle_shelf_unpowered.json
│  │     │  │  ├─ jungle_sign.json
│  │     │  │  ├─ jungle_slab.json
│  │     │  │  ├─ jungle_slab_top.json
│  │     │  │  ├─ jungle_stairs.json
│  │     │  │  ├─ jungle_stairs_inner.json
│  │     │  │  ├─ jungle_stairs_outer.json
│  │     │  │  ├─ jungle_trapdoor_bottom.json
│  │     │  │  ├─ jungle_trapdoor_open.json
│  │     │  │  ├─ jungle_trapdoor_top.json
│  │     │  │  ├─ jungle_wood.json
│  │     │  │  ├─ kelp.json
│  │     │  │  ├─ kelp_plant.json
│  │     │  │  ├─ ladder.json
│  │     │  │  ├─ lantern.json
│  │     │  │  ├─ lantern_hanging.json
│  │     │  │  ├─ lapis_block.json
│  │     │  │  ├─ lapis_ore.json
│  │     │  │  ├─ large_amethyst_bud.json
│  │     │  │  ├─ large_fern_bottom.json
│  │     │  │  ├─ large_fern_top.json
│  │     │  │  ├─ lava.json
│  │     │  │  ├─ lava_cauldron.json
│  │     │  │  ├─ leaf_litter_1.json
│  │     │  │  ├─ leaf_litter_2.json
│  │     │  │  ├─ leaf_litter_3.json
│  │     │  │  ├─ leaf_litter_4.json
│  │     │  │  ├─ leaves.json
│  │     │  │  ├─ lectern.json
│  │     │  │  ├─ lever.json
│  │     │  │  ├─ lever_on.json
│  │     │  │  ├─ lightning_rod.json
│  │     │  │  ├─ lightning_rod_on.json
│  │     │  │  ├─ light_00.json
│  │     │  │  ├─ light_01.json
│  │     │  │  ├─ light_02.json
│  │     │  │  ├─ light_03.json
│  │     │  │  ├─ light_04.json
│  │     │  │  ├─ light_05.json
│  │     │  │  ├─ light_06.json
│  │     │  │  ├─ light_07.json
│  │     │  │  ├─ light_08.json
│  │     │  │  ├─ light_09.json
│  │     │  │  ├─ light_10.json
│  │     │  │  ├─ light_11.json
│  │     │  │  ├─ light_12.json
│  │     │  │  ├─ light_13.json
│  │     │  │  ├─ light_14.json
│  │     │  │  ├─ light_15.json
│  │     │  │  ├─ light_blue_candle_cake.json
│  │     │  │  ├─ light_blue_candle_cake_lit.json
│  │     │  │  ├─ light_blue_candle_four_candles.json
│  │     │  │  ├─ light_blue_candle_four_candles_lit.json
│  │     │  │  ├─ light_blue_candle_one_candle.json
│  │     │  │  ├─ light_blue_candle_one_candle_lit.json
│  │     │  │  ├─ light_blue_candle_three_candles.json
│  │     │  │  ├─ light_blue_candle_three_candles_lit.json
│  │     │  │  ├─ light_blue_candle_two_candles.json
│  │     │  │  ├─ light_blue_candle_two_candles_lit.json
│  │     │  │  ├─ light_blue_carpet.json
│  │     │  │  ├─ light_blue_concrete.json
│  │     │  │  ├─ light_blue_concrete_powder.json
│  │     │  │  ├─ light_blue_glazed_terracotta.json
│  │     │  │  ├─ light_blue_shulker_box.json
│  │     │  │  ├─ light_blue_stained_glass.json
│  │     │  │  ├─ light_blue_stained_glass_pane_noside.json
│  │     │  │  ├─ light_blue_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ light_blue_stained_glass_pane_post.json
│  │     │  │  ├─ light_blue_stained_glass_pane_side.json
│  │     │  │  ├─ light_blue_stained_glass_pane_side_alt.json
│  │     │  │  ├─ light_blue_terracotta.json
│  │     │  │  ├─ light_blue_wool.json
│  │     │  │  ├─ light_gray_candle_cake.json
│  │     │  │  ├─ light_gray_candle_cake_lit.json
│  │     │  │  ├─ light_gray_candle_four_candles.json
│  │     │  │  ├─ light_gray_candle_four_candles_lit.json
│  │     │  │  ├─ light_gray_candle_one_candle.json
│  │     │  │  ├─ light_gray_candle_one_candle_lit.json
│  │     │  │  ├─ light_gray_candle_three_candles.json
│  │     │  │  ├─ light_gray_candle_three_candles_lit.json
│  │     │  │  ├─ light_gray_candle_two_candles.json
│  │     │  │  ├─ light_gray_candle_two_candles_lit.json
│  │     │  │  ├─ light_gray_carpet.json
│  │     │  │  ├─ light_gray_concrete.json
│  │     │  │  ├─ light_gray_concrete_powder.json
│  │     │  │  ├─ light_gray_glazed_terracotta.json
│  │     │  │  ├─ light_gray_shulker_box.json
│  │     │  │  ├─ light_gray_stained_glass.json
│  │     │  │  ├─ light_gray_stained_glass_pane_noside.json
│  │     │  │  ├─ light_gray_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ light_gray_stained_glass_pane_post.json
│  │     │  │  ├─ light_gray_stained_glass_pane_side.json
│  │     │  │  ├─ light_gray_stained_glass_pane_side_alt.json
│  │     │  │  ├─ light_gray_terracotta.json
│  │     │  │  ├─ light_gray_wool.json
│  │     │  │  ├─ light_weighted_pressure_plate.json
│  │     │  │  ├─ light_weighted_pressure_plate_down.json
│  │     │  │  ├─ lilac_bottom.json
│  │     │  │  ├─ lilac_top.json
│  │     │  │  ├─ lily_of_the_valley.json
│  │     │  │  ├─ lily_pad.json
│  │     │  │  ├─ lime_candle_cake.json
│  │     │  │  ├─ lime_candle_cake_lit.json
│  │     │  │  ├─ lime_candle_four_candles.json
│  │     │  │  ├─ lime_candle_four_candles_lit.json
│  │     │  │  ├─ lime_candle_one_candle.json
│  │     │  │  ├─ lime_candle_one_candle_lit.json
│  │     │  │  ├─ lime_candle_three_candles.json
│  │     │  │  ├─ lime_candle_three_candles_lit.json
│  │     │  │  ├─ lime_candle_two_candles.json
│  │     │  │  ├─ lime_candle_two_candles_lit.json
│  │     │  │  ├─ lime_carpet.json
│  │     │  │  ├─ lime_concrete.json
│  │     │  │  ├─ lime_concrete_powder.json
│  │     │  │  ├─ lime_glazed_terracotta.json
│  │     │  │  ├─ lime_shulker_box.json
│  │     │  │  ├─ lime_stained_glass.json
│  │     │  │  ├─ lime_stained_glass_pane_noside.json
│  │     │  │  ├─ lime_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ lime_stained_glass_pane_post.json
│  │     │  │  ├─ lime_stained_glass_pane_side.json
│  │     │  │  ├─ lime_stained_glass_pane_side_alt.json
│  │     │  │  ├─ lime_terracotta.json
│  │     │  │  ├─ lime_wool.json
│  │     │  │  ├─ lodestone.json
│  │     │  │  ├─ loom.json
│  │     │  │  ├─ magenta_candle_cake.json
│  │     │  │  ├─ magenta_candle_cake_lit.json
│  │     │  │  ├─ magenta_candle_four_candles.json
│  │     │  │  ├─ magenta_candle_four_candles_lit.json
│  │     │  │  ├─ magenta_candle_one_candle.json
│  │     │  │  ├─ magenta_candle_one_candle_lit.json
│  │     │  │  ├─ magenta_candle_three_candles.json
│  │     │  │  ├─ magenta_candle_three_candles_lit.json
│  │     │  │  ├─ magenta_candle_two_candles.json
│  │     │  │  ├─ magenta_candle_two_candles_lit.json
│  │     │  │  ├─ magenta_carpet.json
│  │     │  │  ├─ magenta_concrete.json
│  │     │  │  ├─ magenta_concrete_powder.json
│  │     │  │  ├─ magenta_glazed_terracotta.json
│  │     │  │  ├─ magenta_shulker_box.json
│  │     │  │  ├─ magenta_stained_glass.json
│  │     │  │  ├─ magenta_stained_glass_pane_noside.json
│  │     │  │  ├─ magenta_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ magenta_stained_glass_pane_post.json
│  │     │  │  ├─ magenta_stained_glass_pane_side.json
│  │     │  │  ├─ magenta_stained_glass_pane_side_alt.json
│  │     │  │  ├─ magenta_terracotta.json
│  │     │  │  ├─ magenta_wool.json
│  │     │  │  ├─ magma_block.json
│  │     │  │  ├─ mangrove_button.json
│  │     │  │  ├─ mangrove_button_inventory.json
│  │     │  │  ├─ mangrove_button_pressed.json
│  │     │  │  ├─ mangrove_door_bottom_left.json
│  │     │  │  ├─ mangrove_door_bottom_left_open.json
│  │     │  │  ├─ mangrove_door_bottom_right.json
│  │     │  │  ├─ mangrove_door_bottom_right_open.json
│  │     │  │  ├─ mangrove_door_top_left.json
│  │     │  │  ├─ mangrove_door_top_left_open.json
│  │     │  │  ├─ mangrove_door_top_right.json
│  │     │  │  ├─ mangrove_door_top_right_open.json
│  │     │  │  ├─ mangrove_fence_gate.json
│  │     │  │  ├─ mangrove_fence_gate_open.json
│  │     │  │  ├─ mangrove_fence_gate_wall.json
│  │     │  │  ├─ mangrove_fence_gate_wall_open.json
│  │     │  │  ├─ mangrove_fence_inventory.json
│  │     │  │  ├─ mangrove_fence_post.json
│  │     │  │  ├─ mangrove_fence_side.json
│  │     │  │  ├─ mangrove_hanging_sign.json
│  │     │  │  ├─ mangrove_leaves.json
│  │     │  │  ├─ mangrove_log.json
│  │     │  │  ├─ mangrove_log_horizontal.json
│  │     │  │  ├─ mangrove_planks.json
│  │     │  │  ├─ mangrove_pressure_plate.json
│  │     │  │  ├─ mangrove_pressure_plate_down.json
│  │     │  │  ├─ mangrove_propagule.json
│  │     │  │  ├─ mangrove_propagule_hanging_0.json
│  │     │  │  ├─ mangrove_propagule_hanging_1.json
│  │     │  │  ├─ mangrove_propagule_hanging_2.json
│  │     │  │  ├─ mangrove_propagule_hanging_3.json
│  │     │  │  ├─ mangrove_propagule_hanging_4.json
│  │     │  │  ├─ mangrove_roots.json
│  │     │  │  ├─ mangrove_shelf.json
│  │     │  │  ├─ mangrove_shelf_center.json
│  │     │  │  ├─ mangrove_shelf_inventory.json
│  │     │  │  ├─ mangrove_shelf_left.json
│  │     │  │  ├─ mangrove_shelf_right.json
│  │     │  │  ├─ mangrove_shelf_unconnected.json
│  │     │  │  ├─ mangrove_shelf_unpowered.json
│  │     │  │  ├─ mangrove_sign.json
│  │     │  │  ├─ mangrove_slab.json
│  │     │  │  ├─ mangrove_slab_top.json
│  │     │  │  ├─ mangrove_stairs.json
│  │     │  │  ├─ mangrove_stairs_inner.json
│  │     │  │  ├─ mangrove_stairs_outer.json
│  │     │  │  ├─ mangrove_trapdoor_bottom.json
│  │     │  │  ├─ mangrove_trapdoor_open.json
│  │     │  │  ├─ mangrove_trapdoor_top.json
│  │     │  │  ├─ mangrove_wood.json
│  │     │  │  ├─ medium_amethyst_bud.json
│  │     │  │  ├─ melon.json
│  │     │  │  ├─ melon_stem_stage0.json
│  │     │  │  ├─ melon_stem_stage1.json
│  │     │  │  ├─ melon_stem_stage2.json
│  │     │  │  ├─ melon_stem_stage3.json
│  │     │  │  ├─ melon_stem_stage4.json
│  │     │  │  ├─ melon_stem_stage5.json
│  │     │  │  ├─ melon_stem_stage6.json
│  │     │  │  ├─ melon_stem_stage7.json
│  │     │  │  ├─ mossy_carpet_side.json
│  │     │  │  ├─ mossy_cobblestone.json
│  │     │  │  ├─ mossy_cobblestone_slab.json
│  │     │  │  ├─ mossy_cobblestone_slab_top.json
│  │     │  │  ├─ mossy_cobblestone_stairs.json
│  │     │  │  ├─ mossy_cobblestone_stairs_inner.json
│  │     │  │  ├─ mossy_cobblestone_stairs_outer.json
│  │     │  │  ├─ mossy_cobblestone_wall_inventory.json
│  │     │  │  ├─ mossy_cobblestone_wall_post.json
│  │     │  │  ├─ mossy_cobblestone_wall_side.json
│  │     │  │  ├─ mossy_cobblestone_wall_side_tall.json
│  │     │  │  ├─ mossy_stone_bricks.json
│  │     │  │  ├─ mossy_stone_brick_slab.json
│  │     │  │  ├─ mossy_stone_brick_slab_top.json
│  │     │  │  ├─ mossy_stone_brick_stairs.json
│  │     │  │  ├─ mossy_stone_brick_stairs_inner.json
│  │     │  │  ├─ mossy_stone_brick_stairs_outer.json
│  │     │  │  ├─ mossy_stone_brick_wall_inventory.json
│  │     │  │  ├─ mossy_stone_brick_wall_post.json
│  │     │  │  ├─ mossy_stone_brick_wall_side.json
│  │     │  │  ├─ mossy_stone_brick_wall_side_tall.json
│  │     │  │  ├─ moss_block.json
│  │     │  │  ├─ moss_carpet.json
│  │     │  │  ├─ moving_piston.json
│  │     │  │  ├─ mud.json
│  │     │  │  ├─ muddy_mangrove_roots.json
│  │     │  │  ├─ mud_bricks.json
│  │     │  │  ├─ mud_bricks_north_west_mirrored.json
│  │     │  │  ├─ mud_brick_slab.json
│  │     │  │  ├─ mud_brick_slab_top.json
│  │     │  │  ├─ mud_brick_stairs.json
│  │     │  │  ├─ mud_brick_stairs_inner.json
│  │     │  │  ├─ mud_brick_stairs_outer.json
│  │     │  │  ├─ mud_brick_wall_inventory.json
│  │     │  │  ├─ mud_brick_wall_post.json
│  │     │  │  ├─ mud_brick_wall_side.json
│  │     │  │  ├─ mud_brick_wall_side_tall.json
│  │     │  │  ├─ mushroom_block_inside.json
│  │     │  │  ├─ mushroom_stem.json
│  │     │  │  ├─ mushroom_stem_inventory.json
│  │     │  │  ├─ mycelium.json
│  │     │  │  ├─ netherite_block.json
│  │     │  │  ├─ netherrack.json
│  │     │  │  ├─ nether_bricks.json
│  │     │  │  ├─ nether_brick_fence_inventory.json
│  │     │  │  ├─ nether_brick_fence_post.json
│  │     │  │  ├─ nether_brick_fence_side.json
│  │     │  │  ├─ nether_brick_slab.json
│  │     │  │  ├─ nether_brick_slab_top.json
│  │     │  │  ├─ nether_brick_stairs.json
│  │     │  │  ├─ nether_brick_stairs_inner.json
│  │     │  │  ├─ nether_brick_stairs_outer.json
│  │     │  │  ├─ nether_brick_wall_inventory.json
│  │     │  │  ├─ nether_brick_wall_post.json
│  │     │  │  ├─ nether_brick_wall_side.json
│  │     │  │  ├─ nether_brick_wall_side_tall.json
│  │     │  │  ├─ nether_gold_ore.json
│  │     │  │  ├─ nether_portal_ew.json
│  │     │  │  ├─ nether_portal_ns.json
│  │     │  │  ├─ nether_quartz_ore.json
│  │     │  │  ├─ nether_sprouts.json
│  │     │  │  ├─ nether_wart_block.json
│  │     │  │  ├─ nether_wart_stage0.json
│  │     │  │  ├─ nether_wart_stage1.json
│  │     │  │  ├─ nether_wart_stage2.json
│  │     │  │  ├─ note_block.json
│  │     │  │  ├─ oak_button.json
│  │     │  │  ├─ oak_button_inventory.json
│  │     │  │  ├─ oak_button_pressed.json
│  │     │  │  ├─ oak_door_bottom_left.json
│  │     │  │  ├─ oak_door_bottom_left_open.json
│  │     │  │  ├─ oak_door_bottom_right.json
│  │     │  │  ├─ oak_door_bottom_right_open.json
│  │     │  │  ├─ oak_door_top_left.json
│  │     │  │  ├─ oak_door_top_left_open.json
│  │     │  │  ├─ oak_door_top_right.json
│  │     │  │  ├─ oak_door_top_right_open.json
│  │     │  │  ├─ oak_fence_gate.json
│  │     │  │  ├─ oak_fence_gate_open.json
│  │     │  │  ├─ oak_fence_gate_wall.json
│  │     │  │  ├─ oak_fence_gate_wall_open.json
│  │     │  │  ├─ oak_fence_inventory.json
│  │     │  │  ├─ oak_fence_post.json
│  │     │  │  ├─ oak_fence_side.json
│  │     │  │  ├─ oak_hanging_sign.json
│  │     │  │  ├─ oak_leaves.json
│  │     │  │  ├─ oak_log.json
│  │     │  │  ├─ oak_log_horizontal.json
│  │     │  │  ├─ oak_planks.json
│  │     │  │  ├─ oak_pressure_plate.json
│  │     │  │  ├─ oak_pressure_plate_down.json
│  │     │  │  ├─ oak_sapling.json
│  │     │  │  ├─ oak_shelf.json
│  │     │  │  ├─ oak_shelf_center.json
│  │     │  │  ├─ oak_shelf_inventory.json
│  │     │  │  ├─ oak_shelf_left.json
│  │     │  │  ├─ oak_shelf_right.json
│  │     │  │  ├─ oak_shelf_unconnected.json
│  │     │  │  ├─ oak_shelf_unpowered.json
│  │     │  │  ├─ oak_sign.json
│  │     │  │  ├─ oak_slab.json
│  │     │  │  ├─ oak_slab_top.json
│  │     │  │  ├─ oak_stairs.json
│  │     │  │  ├─ oak_stairs_inner.json
│  │     │  │  ├─ oak_stairs_outer.json
│  │     │  │  ├─ oak_trapdoor_bottom.json
│  │     │  │  ├─ oak_trapdoor_open.json
│  │     │  │  ├─ oak_trapdoor_top.json
│  │     │  │  ├─ oak_wood.json
│  │     │  │  ├─ observer.json
│  │     │  │  ├─ observer_on.json
│  │     │  │  ├─ obsidian.json
│  │     │  │  ├─ ochre_froglight.json
│  │     │  │  ├─ ochre_froglight_horizontal.json
│  │     │  │  ├─ open_eyeblossom.json
│  │     │  │  ├─ orange_candle_cake.json
│  │     │  │  ├─ orange_candle_cake_lit.json
│  │     │  │  ├─ orange_candle_four_candles.json
│  │     │  │  ├─ orange_candle_four_candles_lit.json
│  │     │  │  ├─ orange_candle_one_candle.json
│  │     │  │  ├─ orange_candle_one_candle_lit.json
│  │     │  │  ├─ orange_candle_three_candles.json
│  │     │  │  ├─ orange_candle_three_candles_lit.json
│  │     │  │  ├─ orange_candle_two_candles.json
│  │     │  │  ├─ orange_candle_two_candles_lit.json
│  │     │  │  ├─ orange_carpet.json
│  │     │  │  ├─ orange_concrete.json
│  │     │  │  ├─ orange_concrete_powder.json
│  │     │  │  ├─ orange_glazed_terracotta.json
│  │     │  │  ├─ orange_shulker_box.json
│  │     │  │  ├─ orange_stained_glass.json
│  │     │  │  ├─ orange_stained_glass_pane_noside.json
│  │     │  │  ├─ orange_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ orange_stained_glass_pane_post.json
│  │     │  │  ├─ orange_stained_glass_pane_side.json
│  │     │  │  ├─ orange_stained_glass_pane_side_alt.json
│  │     │  │  ├─ orange_terracotta.json
│  │     │  │  ├─ orange_tulip.json
│  │     │  │  ├─ orange_wool.json
│  │     │  │  ├─ orientable.json
│  │     │  │  ├─ orientable_vertical.json
│  │     │  │  ├─ orientable_with_bottom.json
│  │     │  │  ├─ outer_stairs.json
│  │     │  │  ├─ oxeye_daisy.json
│  │     │  │  ├─ oxidized_chiseled_copper.json
│  │     │  │  ├─ oxidized_copper.json
│  │     │  │  ├─ oxidized_copper_bars_cap.json
│  │     │  │  ├─ oxidized_copper_bars_cap_alt.json
│  │     │  │  ├─ oxidized_copper_bars_post.json
│  │     │  │  ├─ oxidized_copper_bars_post_ends.json
│  │     │  │  ├─ oxidized_copper_bars_side.json
│  │     │  │  ├─ oxidized_copper_bars_side_alt.json
│  │     │  │  ├─ oxidized_copper_bulb.json
│  │     │  │  ├─ oxidized_copper_bulb_lit.json
│  │     │  │  ├─ oxidized_copper_bulb_lit_powered.json
│  │     │  │  ├─ oxidized_copper_bulb_powered.json
│  │     │  │  ├─ oxidized_copper_chain.json
│  │     │  │  ├─ oxidized_copper_chest.json
│  │     │  │  ├─ oxidized_copper_door_bottom_left.json
│  │     │  │  ├─ oxidized_copper_door_bottom_left_open.json
│  │     │  │  ├─ oxidized_copper_door_bottom_right.json
│  │     │  │  ├─ oxidized_copper_door_bottom_right_open.json
│  │     │  │  ├─ oxidized_copper_door_top_left.json
│  │     │  │  ├─ oxidized_copper_door_top_left_open.json
│  │     │  │  ├─ oxidized_copper_door_top_right.json
│  │     │  │  ├─ oxidized_copper_door_top_right_open.json
│  │     │  │  ├─ oxidized_copper_golem_statue.json
│  │     │  │  ├─ oxidized_copper_grate.json
│  │     │  │  ├─ oxidized_copper_lantern.json
│  │     │  │  ├─ oxidized_copper_lantern_hanging.json
│  │     │  │  ├─ oxidized_copper_trapdoor_bottom.json
│  │     │  │  ├─ oxidized_copper_trapdoor_open.json
│  │     │  │  ├─ oxidized_copper_trapdoor_top.json
│  │     │  │  ├─ oxidized_cut_copper.json
│  │     │  │  ├─ oxidized_cut_copper_slab.json
│  │     │  │  ├─ oxidized_cut_copper_slab_top.json
│  │     │  │  ├─ oxidized_cut_copper_stairs.json
│  │     │  │  ├─ oxidized_cut_copper_stairs_inner.json
│  │     │  │  ├─ oxidized_cut_copper_stairs_outer.json
│  │     │  │  ├─ oxidized_lightning_rod.json
│  │     │  │  ├─ packed_ice.json
│  │     │  │  ├─ packed_mud.json
│  │     │  │  ├─ pale_hanging_moss.json
│  │     │  │  ├─ pale_hanging_moss_tip.json
│  │     │  │  ├─ pale_moss_block.json
│  │     │  │  ├─ pale_moss_carpet.json
│  │     │  │  ├─ pale_moss_carpet_side_small.json
│  │     │  │  ├─ pale_moss_carpet_side_tall.json
│  │     │  │  ├─ pale_oak_button.json
│  │     │  │  ├─ pale_oak_button_inventory.json
│  │     │  │  ├─ pale_oak_button_pressed.json
│  │     │  │  ├─ pale_oak_door_bottom_left.json
│  │     │  │  ├─ pale_oak_door_bottom_left_open.json
│  │     │  │  ├─ pale_oak_door_bottom_right.json
│  │     │  │  ├─ pale_oak_door_bottom_right_open.json
│  │     │  │  ├─ pale_oak_door_top_left.json
│  │     │  │  ├─ pale_oak_door_top_left_open.json
│  │     │  │  ├─ pale_oak_door_top_right.json
│  │     │  │  ├─ pale_oak_door_top_right_open.json
│  │     │  │  ├─ pale_oak_fence_gate.json
│  │     │  │  ├─ pale_oak_fence_gate_open.json
│  │     │  │  ├─ pale_oak_fence_gate_wall.json
│  │     │  │  ├─ pale_oak_fence_gate_wall_open.json
│  │     │  │  ├─ pale_oak_fence_inventory.json
│  │     │  │  ├─ pale_oak_fence_post.json
│  │     │  │  ├─ pale_oak_fence_side.json
│  │     │  │  ├─ pale_oak_hanging_sign.json
│  │     │  │  ├─ pale_oak_leaves.json
│  │     │  │  ├─ pale_oak_log.json
│  │     │  │  ├─ pale_oak_log_horizontal.json
│  │     │  │  ├─ pale_oak_planks.json
│  │     │  │  ├─ pale_oak_pressure_plate.json
│  │     │  │  ├─ pale_oak_pressure_plate_down.json
│  │     │  │  ├─ pale_oak_sapling.json
│  │     │  │  ├─ pale_oak_shelf.json
│  │     │  │  ├─ pale_oak_shelf_center.json
│  │     │  │  ├─ pale_oak_shelf_inventory.json
│  │     │  │  ├─ pale_oak_shelf_left.json
│  │     │  │  ├─ pale_oak_shelf_right.json
│  │     │  │  ├─ pale_oak_shelf_unconnected.json
│  │     │  │  ├─ pale_oak_shelf_unpowered.json
│  │     │  │  ├─ pale_oak_sign.json
│  │     │  │  ├─ pale_oak_slab.json
│  │     │  │  ├─ pale_oak_slab_top.json
│  │     │  │  ├─ pale_oak_stairs.json
│  │     │  │  ├─ pale_oak_stairs_inner.json
│  │     │  │  ├─ pale_oak_stairs_outer.json
│  │     │  │  ├─ pale_oak_trapdoor_bottom.json
│  │     │  │  ├─ pale_oak_trapdoor_open.json
│  │     │  │  ├─ pale_oak_trapdoor_top.json
│  │     │  │  ├─ pale_oak_wood.json
│  │     │  │  ├─ pearlescent_froglight.json
│  │     │  │  ├─ pearlescent_froglight_horizontal.json
│  │     │  │  ├─ peony_bottom.json
│  │     │  │  ├─ peony_top.json
│  │     │  │  ├─ petrified_oak_slab.json
│  │     │  │  ├─ petrified_oak_slab_top.json
│  │     │  │  ├─ pink_candle_cake.json
│  │     │  │  ├─ pink_candle_cake_lit.json
│  │     │  │  ├─ pink_candle_four_candles.json
│  │     │  │  ├─ pink_candle_four_candles_lit.json
│  │     │  │  ├─ pink_candle_one_candle.json
│  │     │  │  ├─ pink_candle_one_candle_lit.json
│  │     │  │  ├─ pink_candle_three_candles.json
│  │     │  │  ├─ pink_candle_three_candles_lit.json
│  │     │  │  ├─ pink_candle_two_candles.json
│  │     │  │  ├─ pink_candle_two_candles_lit.json
│  │     │  │  ├─ pink_carpet.json
│  │     │  │  ├─ pink_concrete.json
│  │     │  │  ├─ pink_concrete_powder.json
│  │     │  │  ├─ pink_glazed_terracotta.json
│  │     │  │  ├─ pink_petals_1.json
│  │     │  │  ├─ pink_petals_2.json
│  │     │  │  ├─ pink_petals_3.json
│  │     │  │  ├─ pink_petals_4.json
│  │     │  │  ├─ pink_shulker_box.json
│  │     │  │  ├─ pink_stained_glass.json
│  │     │  │  ├─ pink_stained_glass_pane_noside.json
│  │     │  │  ├─ pink_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ pink_stained_glass_pane_post.json
│  │     │  │  ├─ pink_stained_glass_pane_side.json
│  │     │  │  ├─ pink_stained_glass_pane_side_alt.json
│  │     │  │  ├─ pink_terracotta.json
│  │     │  │  ├─ pink_tulip.json
│  │     │  │  ├─ pink_wool.json
│  │     │  │  ├─ piston.json
│  │     │  │  ├─ piston_base.json
│  │     │  │  ├─ piston_extended.json
│  │     │  │  ├─ piston_head.json
│  │     │  │  ├─ piston_head_short.json
│  │     │  │  ├─ piston_head_short_sticky.json
│  │     │  │  ├─ piston_head_sticky.json
│  │     │  │  ├─ piston_inventory.json
│  │     │  │  ├─ pitcher_crop_bottom_stage_0.json
│  │     │  │  ├─ pitcher_crop_bottom_stage_1.json
│  │     │  │  ├─ pitcher_crop_bottom_stage_2.json
│  │     │  │  ├─ pitcher_crop_bottom_stage_3.json
│  │     │  │  ├─ pitcher_crop_bottom_stage_4.json
│  │     │  │  ├─ pitcher_crop_top_stage_0.json
│  │     │  │  ├─ pitcher_crop_top_stage_1.json
│  │     │  │  ├─ pitcher_crop_top_stage_2.json
│  │     │  │  ├─ pitcher_crop_top_stage_3.json
│  │     │  │  ├─ pitcher_crop_top_stage_4.json
│  │     │  │  ├─ pitcher_plant_bottom.json
│  │     │  │  ├─ pitcher_plant_top.json
│  │     │  │  ├─ podzol.json
│  │     │  │  ├─ pointed_dripstone.json
│  │     │  │  ├─ pointed_dripstone_down_base.json
│  │     │  │  ├─ pointed_dripstone_down_frustum.json
│  │     │  │  ├─ pointed_dripstone_down_middle.json
│  │     │  │  ├─ pointed_dripstone_down_tip.json
│  │     │  │  ├─ pointed_dripstone_down_tip_merge.json
│  │     │  │  ├─ pointed_dripstone_up_base.json
│  │     │  │  ├─ pointed_dripstone_up_frustum.json
│  │     │  │  ├─ pointed_dripstone_up_middle.json
│  │     │  │  ├─ pointed_dripstone_up_tip.json
│  │     │  │  ├─ pointed_dripstone_up_tip_merge.json
│  │     │  │  ├─ polished_andesite.json
│  │     │  │  ├─ polished_andesite_slab.json
│  │     │  │  ├─ polished_andesite_slab_top.json
│  │     │  │  ├─ polished_andesite_stairs.json
│  │     │  │  ├─ polished_andesite_stairs_inner.json
│  │     │  │  ├─ polished_andesite_stairs_outer.json
│  │     │  │  ├─ polished_basalt.json
│  │     │  │  ├─ polished_blackstone.json
│  │     │  │  ├─ polished_blackstone_bricks.json
│  │     │  │  ├─ polished_blackstone_brick_slab.json
│  │     │  │  ├─ polished_blackstone_brick_slab_top.json
│  │     │  │  ├─ polished_blackstone_brick_stairs.json
│  │     │  │  ├─ polished_blackstone_brick_stairs_inner.json
│  │     │  │  ├─ polished_blackstone_brick_stairs_outer.json
│  │     │  │  ├─ polished_blackstone_brick_wall_inventory.json
│  │     │  │  ├─ polished_blackstone_brick_wall_post.json
│  │     │  │  ├─ polished_blackstone_brick_wall_side.json
│  │     │  │  ├─ polished_blackstone_brick_wall_side_tall.json
│  │     │  │  ├─ polished_blackstone_button.json
│  │     │  │  ├─ polished_blackstone_button_inventory.json
│  │     │  │  ├─ polished_blackstone_button_pressed.json
│  │     │  │  ├─ polished_blackstone_pressure_plate.json
│  │     │  │  ├─ polished_blackstone_pressure_plate_down.json
│  │     │  │  ├─ polished_blackstone_slab.json
│  │     │  │  ├─ polished_blackstone_slab_top.json
│  │     │  │  ├─ polished_blackstone_stairs.json
│  │     │  │  ├─ polished_blackstone_stairs_inner.json
│  │     │  │  ├─ polished_blackstone_stairs_outer.json
│  │     │  │  ├─ polished_blackstone_wall_inventory.json
│  │     │  │  ├─ polished_blackstone_wall_post.json
│  │     │  │  ├─ polished_blackstone_wall_side.json
│  │     │  │  ├─ polished_blackstone_wall_side_tall.json
│  │     │  │  ├─ polished_deepslate.json
│  │     │  │  ├─ polished_deepslate_slab.json
│  │     │  │  ├─ polished_deepslate_slab_top.json
│  │     │  │  ├─ polished_deepslate_stairs.json
│  │     │  │  ├─ polished_deepslate_stairs_inner.json
│  │     │  │  ├─ polished_deepslate_stairs_outer.json
│  │     │  │  ├─ polished_deepslate_wall_inventory.json
│  │     │  │  ├─ polished_deepslate_wall_post.json
│  │     │  │  ├─ polished_deepslate_wall_side.json
│  │     │  │  ├─ polished_deepslate_wall_side_tall.json
│  │     │  │  ├─ polished_diorite.json
│  │     │  │  ├─ polished_diorite_slab.json
│  │     │  │  ├─ polished_diorite_slab_top.json
│  │     │  │  ├─ polished_diorite_stairs.json
│  │     │  │  ├─ polished_diorite_stairs_inner.json
│  │     │  │  ├─ polished_diorite_stairs_outer.json
│  │     │  │  ├─ polished_granite.json
│  │     │  │  ├─ polished_granite_slab.json
│  │     │  │  ├─ polished_granite_slab_top.json
│  │     │  │  ├─ polished_granite_stairs.json
│  │     │  │  ├─ polished_granite_stairs_inner.json
│  │     │  │  ├─ polished_granite_stairs_outer.json
│  │     │  │  ├─ polished_tuff.json
│  │     │  │  ├─ polished_tuff_slab.json
│  │     │  │  ├─ polished_tuff_slab_top.json
│  │     │  │  ├─ polished_tuff_stairs.json
│  │     │  │  ├─ polished_tuff_stairs_inner.json
│  │     │  │  ├─ polished_tuff_stairs_outer.json
│  │     │  │  ├─ polished_tuff_wall_inventory.json
│  │     │  │  ├─ polished_tuff_wall_post.json
│  │     │  │  ├─ polished_tuff_wall_side.json
│  │     │  │  ├─ polished_tuff_wall_side_tall.json
│  │     │  │  ├─ poppy.json
│  │     │  │  ├─ potatoes_stage0.json
│  │     │  │  ├─ potatoes_stage1.json
│  │     │  │  ├─ potatoes_stage2.json
│  │     │  │  ├─ potatoes_stage3.json
│  │     │  │  ├─ potted_acacia_sapling.json
│  │     │  │  ├─ potted_allium.json
│  │     │  │  ├─ potted_azalea_bush.json
│  │     │  │  ├─ potted_azure_bluet.json
│  │     │  │  ├─ potted_bamboo.json
│  │     │  │  ├─ potted_birch_sapling.json
│  │     │  │  ├─ potted_blue_orchid.json
│  │     │  │  ├─ potted_brown_mushroom.json
│  │     │  │  ├─ potted_cactus.json
│  │     │  │  ├─ potted_cherry_sapling.json
│  │     │  │  ├─ potted_closed_eyeblossom.json
│  │     │  │  ├─ potted_cornflower.json
│  │     │  │  ├─ potted_crimson_fungus.json
│  │     │  │  ├─ potted_crimson_roots.json
│  │     │  │  ├─ potted_dandelion.json
│  │     │  │  ├─ potted_dark_oak_sapling.json
│  │     │  │  ├─ potted_dead_bush.json
│  │     │  │  ├─ potted_fern.json
│  │     │  │  ├─ potted_flowering_azalea_bush.json
│  │     │  │  ├─ potted_jungle_sapling.json
│  │     │  │  ├─ potted_lily_of_the_valley.json
│  │     │  │  ├─ potted_mangrove_propagule.json
│  │     │  │  ├─ potted_oak_sapling.json
│  │     │  │  ├─ potted_open_eyeblossom.json
│  │     │  │  ├─ potted_orange_tulip.json
│  │     │  │  ├─ potted_oxeye_daisy.json
│  │     │  │  ├─ potted_pale_oak_sapling.json
│  │     │  │  ├─ potted_pink_tulip.json
│  │     │  │  ├─ potted_poppy.json
│  │     │  │  ├─ potted_red_mushroom.json
│  │     │  │  ├─ potted_red_tulip.json
│  │     │  │  ├─ potted_spruce_sapling.json
│  │     │  │  ├─ potted_torchflower.json
│  │     │  │  ├─ potted_warped_fungus.json
│  │     │  │  ├─ potted_warped_roots.json
│  │     │  │  ├─ potted_white_tulip.json
│  │     │  │  ├─ potted_wither_rose.json
│  │     │  │  ├─ powder_snow.json
│  │     │  │  ├─ powder_snow_cauldron_full.json
│  │     │  │  ├─ powder_snow_cauldron_level1.json
│  │     │  │  ├─ powder_snow_cauldron_level2.json
│  │     │  │  ├─ powered_rail.json
│  │     │  │  ├─ powered_rail_on.json
│  │     │  │  ├─ powered_rail_on_raised_ne.json
│  │     │  │  ├─ powered_rail_on_raised_sw.json
│  │     │  │  ├─ powered_rail_raised_ne.json
│  │     │  │  ├─ powered_rail_raised_sw.json
│  │     │  │  ├─ pressure_plate_down.json
│  │     │  │  ├─ pressure_plate_up.json
│  │     │  │  ├─ prismarine.json
│  │     │  │  ├─ prismarine_bricks.json
│  │     │  │  ├─ prismarine_brick_slab.json
│  │     │  │  ├─ prismarine_brick_slab_top.json
│  │     │  │  ├─ prismarine_brick_stairs.json
│  │     │  │  ├─ prismarine_brick_stairs_inner.json
│  │     │  │  ├─ prismarine_brick_stairs_outer.json
│  │     │  │  ├─ prismarine_slab.json
│  │     │  │  ├─ prismarine_slab_top.json
│  │     │  │  ├─ prismarine_stairs.json
│  │     │  │  ├─ prismarine_stairs_inner.json
│  │     │  │  ├─ prismarine_stairs_outer.json
│  │     │  │  ├─ prismarine_wall_inventory.json
│  │     │  │  ├─ prismarine_wall_post.json
│  │     │  │  ├─ prismarine_wall_side.json
│  │     │  │  ├─ prismarine_wall_side_tall.json
│  │     │  │  ├─ pumpkin.json
│  │     │  │  ├─ pumpkin_stem_stage0.json
│  │     │  │  ├─ pumpkin_stem_stage1.json
│  │     │  │  ├─ pumpkin_stem_stage2.json
│  │     │  │  ├─ pumpkin_stem_stage3.json
│  │     │  │  ├─ pumpkin_stem_stage4.json
│  │     │  │  ├─ pumpkin_stem_stage5.json
│  │     │  │  ├─ pumpkin_stem_stage6.json
│  │     │  │  ├─ pumpkin_stem_stage7.json
│  │     │  │  ├─ purple_candle_cake.json
│  │     │  │  ├─ purple_candle_cake_lit.json
│  │     │  │  ├─ purple_candle_four_candles.json
│  │     │  │  ├─ purple_candle_four_candles_lit.json
│  │     │  │  ├─ purple_candle_one_candle.json
│  │     │  │  ├─ purple_candle_one_candle_lit.json
│  │     │  │  ├─ purple_candle_three_candles.json
│  │     │  │  ├─ purple_candle_three_candles_lit.json
│  │     │  │  ├─ purple_candle_two_candles.json
│  │     │  │  ├─ purple_candle_two_candles_lit.json
│  │     │  │  ├─ purple_carpet.json
│  │     │  │  ├─ purple_concrete.json
│  │     │  │  ├─ purple_concrete_powder.json
│  │     │  │  ├─ purple_glazed_terracotta.json
│  │     │  │  ├─ purple_shulker_box.json
│  │     │  │  ├─ purple_stained_glass.json
│  │     │  │  ├─ purple_stained_glass_pane_noside.json
│  │     │  │  ├─ purple_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ purple_stained_glass_pane_post.json
│  │     │  │  ├─ purple_stained_glass_pane_side.json
│  │     │  │  ├─ purple_stained_glass_pane_side_alt.json
│  │     │  │  ├─ purple_terracotta.json
│  │     │  │  ├─ purple_wool.json
│  │     │  │  ├─ purpur_block.json
│  │     │  │  ├─ purpur_pillar.json
│  │     │  │  ├─ purpur_pillar_horizontal.json
│  │     │  │  ├─ purpur_slab.json
│  │     │  │  ├─ purpur_slab_top.json
│  │     │  │  ├─ purpur_stairs.json
│  │     │  │  ├─ purpur_stairs_inner.json
│  │     │  │  ├─ purpur_stairs_outer.json
│  │     │  │  ├─ quartz_block.json
│  │     │  │  ├─ quartz_bricks.json
│  │     │  │  ├─ quartz_pillar.json
│  │     │  │  ├─ quartz_pillar_horizontal.json
│  │     │  │  ├─ quartz_slab.json
│  │     │  │  ├─ quartz_slab_top.json
│  │     │  │  ├─ quartz_stairs.json
│  │     │  │  ├─ quartz_stairs_inner.json
│  │     │  │  ├─ quartz_stairs_outer.json
│  │     │  │  ├─ rail.json
│  │     │  │  ├─ rail_corner.json
│  │     │  │  ├─ rail_curved.json
│  │     │  │  ├─ rail_flat.json
│  │     │  │  ├─ rail_raised_ne.json
│  │     │  │  ├─ rail_raised_sw.json
│  │     │  │  ├─ raw_copper_block.json
│  │     │  │  ├─ raw_gold_block.json
│  │     │  │  ├─ raw_iron_block.json
│  │     │  │  ├─ redstone_block.json
│  │     │  │  ├─ redstone_dust_dot.json
│  │     │  │  ├─ redstone_dust_side.json
│  │     │  │  ├─ redstone_dust_side0.json
│  │     │  │  ├─ redstone_dust_side1.json
│  │     │  │  ├─ redstone_dust_side_alt.json
│  │     │  │  ├─ redstone_dust_side_alt0.json
│  │     │  │  ├─ redstone_dust_side_alt1.json
│  │     │  │  ├─ redstone_dust_up.json
│  │     │  │  ├─ redstone_lamp.json
│  │     │  │  ├─ redstone_lamp_on.json
│  │     │  │  ├─ redstone_ore.json
│  │     │  │  ├─ redstone_torch.json
│  │     │  │  ├─ redstone_torch_off.json
│  │     │  │  ├─ redstone_wall_torch.json
│  │     │  │  ├─ redstone_wall_torch_off.json
│  │     │  │  ├─ red_candle_cake.json
│  │     │  │  ├─ red_candle_cake_lit.json
│  │     │  │  ├─ red_candle_four_candles.json
│  │     │  │  ├─ red_candle_four_candles_lit.json
│  │     │  │  ├─ red_candle_one_candle.json
│  │     │  │  ├─ red_candle_one_candle_lit.json
│  │     │  │  ├─ red_candle_three_candles.json
│  │     │  │  ├─ red_candle_three_candles_lit.json
│  │     │  │  ├─ red_candle_two_candles.json
│  │     │  │  ├─ red_candle_two_candles_lit.json
│  │     │  │  ├─ red_carpet.json
│  │     │  │  ├─ red_concrete.json
│  │     │  │  ├─ red_concrete_powder.json
│  │     │  │  ├─ red_glazed_terracotta.json
│  │     │  │  ├─ red_mushroom.json
│  │     │  │  ├─ red_mushroom_block.json
│  │     │  │  ├─ red_mushroom_block_inventory.json
│  │     │  │  ├─ red_nether_bricks.json
│  │     │  │  ├─ red_nether_brick_slab.json
│  │     │  │  ├─ red_nether_brick_slab_top.json
│  │     │  │  ├─ red_nether_brick_stairs.json
│  │     │  │  ├─ red_nether_brick_stairs_inner.json
│  │     │  │  ├─ red_nether_brick_stairs_outer.json
│  │     │  │  ├─ red_nether_brick_wall_inventory.json
│  │     │  │  ├─ red_nether_brick_wall_post.json
│  │     │  │  ├─ red_nether_brick_wall_side.json
│  │     │  │  ├─ red_nether_brick_wall_side_tall.json
│  │     │  │  ├─ red_sand.json
│  │     │  │  ├─ red_sandstone.json
│  │     │  │  ├─ red_sandstone_slab.json
│  │     │  │  ├─ red_sandstone_slab_top.json
│  │     │  │  ├─ red_sandstone_stairs.json
│  │     │  │  ├─ red_sandstone_stairs_inner.json
│  │     │  │  ├─ red_sandstone_stairs_outer.json
│  │     │  │  ├─ red_sandstone_wall_inventory.json
│  │     │  │  ├─ red_sandstone_wall_post.json
│  │     │  │  ├─ red_sandstone_wall_side.json
│  │     │  │  ├─ red_sandstone_wall_side_tall.json
│  │     │  │  ├─ red_shulker_box.json
│  │     │  │  ├─ red_stained_glass.json
│  │     │  │  ├─ red_stained_glass_pane_noside.json
│  │     │  │  ├─ red_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ red_stained_glass_pane_post.json
│  │     │  │  ├─ red_stained_glass_pane_side.json
│  │     │  │  ├─ red_stained_glass_pane_side_alt.json
│  │     │  │  ├─ red_terracotta.json
│  │     │  │  ├─ red_tulip.json
│  │     │  │  ├─ red_wool.json
│  │     │  │  ├─ reinforced_deepslate.json
│  │     │  │  ├─ repeater_1tick.json
│  │     │  │  ├─ repeater_1tick_locked.json
│  │     │  │  ├─ repeater_1tick_on.json
│  │     │  │  ├─ repeater_1tick_on_locked.json
│  │     │  │  ├─ repeater_2tick.json
│  │     │  │  ├─ repeater_2tick_locked.json
│  │     │  │  ├─ repeater_2tick_on.json
│  │     │  │  ├─ repeater_2tick_on_locked.json
│  │     │  │  ├─ repeater_3tick.json
│  │     │  │  ├─ repeater_3tick_locked.json
│  │     │  │  ├─ repeater_3tick_on.json
│  │     │  │  ├─ repeater_3tick_on_locked.json
│  │     │  │  ├─ repeater_4tick.json
│  │     │  │  ├─ repeater_4tick_locked.json
│  │     │  │  ├─ repeater_4tick_on.json
│  │     │  │  ├─ repeater_4tick_on_locked.json
│  │     │  │  ├─ repeating_command_block.json
│  │     │  │  ├─ repeating_command_block_conditional.json
│  │     │  │  ├─ resin_block.json
│  │     │  │  ├─ resin_bricks.json
│  │     │  │  ├─ resin_brick_slab.json
│  │     │  │  ├─ resin_brick_slab_top.json
│  │     │  │  ├─ resin_brick_stairs.json
│  │     │  │  ├─ resin_brick_stairs_inner.json
│  │     │  │  ├─ resin_brick_stairs_outer.json
│  │     │  │  ├─ resin_brick_wall_inventory.json
│  │     │  │  ├─ resin_brick_wall_post.json
│  │     │  │  ├─ resin_brick_wall_side.json
│  │     │  │  ├─ resin_brick_wall_side_tall.json
│  │     │  │  ├─ resin_clump.json
│  │     │  │  ├─ respawn_anchor_0.json
│  │     │  │  ├─ respawn_anchor_1.json
│  │     │  │  ├─ respawn_anchor_2.json
│  │     │  │  ├─ respawn_anchor_3.json
│  │     │  │  ├─ respawn_anchor_4.json
│  │     │  │  ├─ rooted_dirt.json
│  │     │  │  ├─ rose_bush_bottom.json
│  │     │  │  ├─ rose_bush_top.json
│  │     │  │  ├─ sand.json
│  │     │  │  ├─ sandstone.json
│  │     │  │  ├─ sandstone_slab.json
│  │     │  │  ├─ sandstone_slab_top.json
│  │     │  │  ├─ sandstone_stairs.json
│  │     │  │  ├─ sandstone_stairs_inner.json
│  │     │  │  ├─ sandstone_stairs_outer.json
│  │     │  │  ├─ sandstone_wall_inventory.json
│  │     │  │  ├─ sandstone_wall_post.json
│  │     │  │  ├─ sandstone_wall_side.json
│  │     │  │  ├─ sandstone_wall_side_tall.json
│  │     │  │  ├─ scaffolding_stable.json
│  │     │  │  ├─ scaffolding_unstable.json
│  │     │  │  ├─ sculk.json
│  │     │  │  ├─ sculk_catalyst.json
│  │     │  │  ├─ sculk_catalyst_bloom.json
│  │     │  │  ├─ sculk_mirrored.json
│  │     │  │  ├─ sculk_sensor.json
│  │     │  │  ├─ sculk_sensor_active.json
│  │     │  │  ├─ sculk_sensor_inactive.json
│  │     │  │  ├─ sculk_shrieker.json
│  │     │  │  ├─ sculk_shrieker_can_summon.json
│  │     │  │  ├─ sculk_vein.json
│  │     │  │  ├─ seagrass.json
│  │     │  │  ├─ sea_lantern.json
│  │     │  │  ├─ sea_pickle.json
│  │     │  │  ├─ short_dry_grass.json
│  │     │  │  ├─ short_grass.json
│  │     │  │  ├─ shroomlight.json
│  │     │  │  ├─ shulker_box.json
│  │     │  │  ├─ skull.json
│  │     │  │  ├─ slab.json
│  │     │  │  ├─ slab_top.json
│  │     │  │  ├─ slightly_cracked_turtle_egg.json
│  │     │  │  ├─ slime_block.json
│  │     │  │  ├─ small_amethyst_bud.json
│  │     │  │  ├─ small_dripleaf_bottom.json
│  │     │  │  ├─ small_dripleaf_top.json
│  │     │  │  ├─ smithing_table.json
│  │     │  │  ├─ smoker.json
│  │     │  │  ├─ smoker_on.json
│  │     │  │  ├─ smooth_basalt.json
│  │     │  │  ├─ smooth_quartz.json
│  │     │  │  ├─ smooth_quartz_slab.json
│  │     │  │  ├─ smooth_quartz_slab_top.json
│  │     │  │  ├─ smooth_quartz_stairs.json
│  │     │  │  ├─ smooth_quartz_stairs_inner.json
│  │     │  │  ├─ smooth_quartz_stairs_outer.json
│  │     │  │  ├─ smooth_red_sandstone.json
│  │     │  │  ├─ smooth_red_sandstone_slab.json
│  │     │  │  ├─ smooth_red_sandstone_slab_top.json
│  │     │  │  ├─ smooth_red_sandstone_stairs.json
│  │     │  │  ├─ smooth_red_sandstone_stairs_inner.json
│  │     │  │  ├─ smooth_red_sandstone_stairs_outer.json
│  │     │  │  ├─ smooth_sandstone.json
│  │     │  │  ├─ smooth_sandstone_slab.json
│  │     │  │  ├─ smooth_sandstone_slab_top.json
│  │     │  │  ├─ smooth_sandstone_stairs.json
│  │     │  │  ├─ smooth_sandstone_stairs_inner.json
│  │     │  │  ├─ smooth_sandstone_stairs_outer.json
│  │     │  │  ├─ smooth_stone.json
│  │     │  │  ├─ smooth_stone_slab.json
│  │     │  │  ├─ smooth_stone_slab_double.json
│  │     │  │  ├─ smooth_stone_slab_top.json
│  │     │  │  ├─ sniffer_egg.json
│  │     │  │  ├─ sniffer_egg_not_cracked.json
│  │     │  │  ├─ sniffer_egg_slightly_cracked.json
│  │     │  │  ├─ sniffer_egg_very_cracked.json
│  │     │  │  ├─ snow_block.json
│  │     │  │  ├─ snow_height10.json
│  │     │  │  ├─ snow_height12.json
│  │     │  │  ├─ snow_height14.json
│  │     │  │  ├─ snow_height2.json
│  │     │  │  ├─ snow_height4.json
│  │     │  │  ├─ snow_height6.json
│  │     │  │  ├─ snow_height8.json
│  │     │  │  ├─ soul_campfire.json
│  │     │  │  ├─ soul_fire_floor0.json
│  │     │  │  ├─ soul_fire_floor1.json
│  │     │  │  ├─ soul_fire_side0.json
│  │     │  │  ├─ soul_fire_side1.json
│  │     │  │  ├─ soul_fire_side_alt0.json
│  │     │  │  ├─ soul_fire_side_alt1.json
│  │     │  │  ├─ soul_lantern.json
│  │     │  │  ├─ soul_lantern_hanging.json
│  │     │  │  ├─ soul_sand.json
│  │     │  │  ├─ soul_soil.json
│  │     │  │  ├─ soul_torch.json
│  │     │  │  ├─ soul_wall_torch.json
│  │     │  │  ├─ spawner.json
│  │     │  │  ├─ sponge.json
│  │     │  │  ├─ spore_blossom.json
│  │     │  │  ├─ spruce_button.json
│  │     │  │  ├─ spruce_button_inventory.json
│  │     │  │  ├─ spruce_button_pressed.json
│  │     │  │  ├─ spruce_door_bottom_left.json
│  │     │  │  ├─ spruce_door_bottom_left_open.json
│  │     │  │  ├─ spruce_door_bottom_right.json
│  │     │  │  ├─ spruce_door_bottom_right_open.json
│  │     │  │  ├─ spruce_door_top_left.json
│  │     │  │  ├─ spruce_door_top_left_open.json
│  │     │  │  ├─ spruce_door_top_right.json
│  │     │  │  ├─ spruce_door_top_right_open.json
│  │     │  │  ├─ spruce_fence_gate.json
│  │     │  │  ├─ spruce_fence_gate_open.json
│  │     │  │  ├─ spruce_fence_gate_wall.json
│  │     │  │  ├─ spruce_fence_gate_wall_open.json
│  │     │  │  ├─ spruce_fence_inventory.json
│  │     │  │  ├─ spruce_fence_post.json
│  │     │  │  ├─ spruce_fence_side.json
│  │     │  │  ├─ spruce_hanging_sign.json
│  │     │  │  ├─ spruce_leaves.json
│  │     │  │  ├─ spruce_log.json
│  │     │  │  ├─ spruce_log_horizontal.json
│  │     │  │  ├─ spruce_planks.json
│  │     │  │  ├─ spruce_pressure_plate.json
│  │     │  │  ├─ spruce_pressure_plate_down.json
│  │     │  │  ├─ spruce_sapling.json
│  │     │  │  ├─ spruce_shelf.json
│  │     │  │  ├─ spruce_shelf_center.json
│  │     │  │  ├─ spruce_shelf_inventory.json
│  │     │  │  ├─ spruce_shelf_left.json
│  │     │  │  ├─ spruce_shelf_right.json
│  │     │  │  ├─ spruce_shelf_unconnected.json
│  │     │  │  ├─ spruce_shelf_unpowered.json
│  │     │  │  ├─ spruce_sign.json
│  │     │  │  ├─ spruce_slab.json
│  │     │  │  ├─ spruce_slab_top.json
│  │     │  │  ├─ spruce_stairs.json
│  │     │  │  ├─ spruce_stairs_inner.json
│  │     │  │  ├─ spruce_stairs_outer.json
│  │     │  │  ├─ spruce_trapdoor_bottom.json
│  │     │  │  ├─ spruce_trapdoor_open.json
│  │     │  │  ├─ spruce_trapdoor_top.json
│  │     │  │  ├─ spruce_wood.json
│  │     │  │  ├─ stairs.json
│  │     │  │  ├─ stem_fruit.json
│  │     │  │  ├─ stem_growth0.json
│  │     │  │  ├─ stem_growth1.json
│  │     │  │  ├─ stem_growth2.json
│  │     │  │  ├─ stem_growth3.json
│  │     │  │  ├─ stem_growth4.json
│  │     │  │  ├─ stem_growth5.json
│  │     │  │  ├─ stem_growth6.json
│  │     │  │  ├─ stem_growth7.json
│  │     │  │  ├─ sticky_piston.json
│  │     │  │  ├─ sticky_piston_inventory.json
│  │     │  │  ├─ stone.json
│  │     │  │  ├─ stonecutter.json
│  │     │  │  ├─ stone_bricks.json
│  │     │  │  ├─ stone_brick_slab.json
│  │     │  │  ├─ stone_brick_slab_top.json
│  │     │  │  ├─ stone_brick_stairs.json
│  │     │  │  ├─ stone_brick_stairs_inner.json
│  │     │  │  ├─ stone_brick_stairs_outer.json
│  │     │  │  ├─ stone_brick_wall_inventory.json
│  │     │  │  ├─ stone_brick_wall_post.json
│  │     │  │  ├─ stone_brick_wall_side.json
│  │     │  │  ├─ stone_brick_wall_side_tall.json
│  │     │  │  ├─ stone_button.json
│  │     │  │  ├─ stone_button_inventory.json
│  │     │  │  ├─ stone_button_pressed.json
│  │     │  │  ├─ stone_mirrored.json
│  │     │  │  ├─ stone_pressure_plate.json
│  │     │  │  ├─ stone_pressure_plate_down.json
│  │     │  │  ├─ stone_slab.json
│  │     │  │  ├─ stone_slab_top.json
│  │     │  │  ├─ stone_stairs.json
│  │     │  │  ├─ stone_stairs_inner.json
│  │     │  │  ├─ stone_stairs_outer.json
│  │     │  │  ├─ stripped_acacia_log.json
│  │     │  │  ├─ stripped_acacia_log_horizontal.json
│  │     │  │  ├─ stripped_acacia_wood.json
│  │     │  │  ├─ stripped_bamboo_block.json
│  │     │  │  ├─ stripped_bamboo_block_x.json
│  │     │  │  ├─ stripped_bamboo_block_y.json
│  │     │  │  ├─ stripped_bamboo_block_z.json
│  │     │  │  ├─ stripped_birch_log.json
│  │     │  │  ├─ stripped_birch_log_horizontal.json
│  │     │  │  ├─ stripped_birch_wood.json
│  │     │  │  ├─ stripped_cherry_log.json
│  │     │  │  ├─ stripped_cherry_log_x.json
│  │     │  │  ├─ stripped_cherry_log_y.json
│  │     │  │  ├─ stripped_cherry_log_z.json
│  │     │  │  ├─ stripped_cherry_wood.json
│  │     │  │  ├─ stripped_crimson_hyphae.json
│  │     │  │  ├─ stripped_crimson_stem.json
│  │     │  │  ├─ stripped_dark_oak_log.json
│  │     │  │  ├─ stripped_dark_oak_log_horizontal.json
│  │     │  │  ├─ stripped_dark_oak_wood.json
│  │     │  │  ├─ stripped_jungle_log.json
│  │     │  │  ├─ stripped_jungle_log_horizontal.json
│  │     │  │  ├─ stripped_jungle_wood.json
│  │     │  │  ├─ stripped_mangrove_log.json
│  │     │  │  ├─ stripped_mangrove_log_horizontal.json
│  │     │  │  ├─ stripped_mangrove_wood.json
│  │     │  │  ├─ stripped_oak_log.json
│  │     │  │  ├─ stripped_oak_log_horizontal.json
│  │     │  │  ├─ stripped_oak_wood.json
│  │     │  │  ├─ stripped_pale_oak_log.json
│  │     │  │  ├─ stripped_pale_oak_log_horizontal.json
│  │     │  │  ├─ stripped_pale_oak_wood.json
│  │     │  │  ├─ stripped_spruce_log.json
│  │     │  │  ├─ stripped_spruce_log_horizontal.json
│  │     │  │  ├─ stripped_spruce_wood.json
│  │     │  │  ├─ stripped_warped_hyphae.json
│  │     │  │  ├─ stripped_warped_stem.json
│  │     │  │  ├─ structure_block.json
│  │     │  │  ├─ structure_block_corner.json
│  │     │  │  ├─ structure_block_data.json
│  │     │  │  ├─ structure_block_load.json
│  │     │  │  ├─ structure_block_save.json
│  │     │  │  ├─ structure_void.json
│  │     │  │  ├─ sugar_cane.json
│  │     │  │  ├─ sunflower_bottom.json
│  │     │  │  ├─ sunflower_top.json
│  │     │  │  ├─ suspicious_gravel_0.json
│  │     │  │  ├─ suspicious_gravel_1.json
│  │     │  │  ├─ suspicious_gravel_2.json
│  │     │  │  ├─ suspicious_gravel_3.json
│  │     │  │  ├─ suspicious_sand_0.json
│  │     │  │  ├─ suspicious_sand_1.json
│  │     │  │  ├─ suspicious_sand_2.json
│  │     │  │  ├─ suspicious_sand_3.json
│  │     │  │  ├─ sweet_berry_bush_stage0.json
│  │     │  │  ├─ sweet_berry_bush_stage1.json
│  │     │  │  ├─ sweet_berry_bush_stage2.json
│  │     │  │  ├─ sweet_berry_bush_stage3.json
│  │     │  │  ├─ tall_dry_grass.json
│  │     │  │  ├─ tall_grass_bottom.json
│  │     │  │  ├─ tall_grass_top.json
│  │     │  │  ├─ tall_seagrass_bottom.json
│  │     │  │  ├─ tall_seagrass_top.json
│  │     │  │  ├─ target.json
│  │     │  │  ├─ template_anvil.json
│  │     │  │  ├─ template_azalea.json
│  │     │  │  ├─ template_bars_cap.json
│  │     │  │  ├─ template_bars_cap_alt.json
│  │     │  │  ├─ template_bars_post.json
│  │     │  │  ├─ template_bars_post_ends.json
│  │     │  │  ├─ template_bars_side.json
│  │     │  │  ├─ template_bars_side_alt.json
│  │     │  │  ├─ template_cake_with_candle.json
│  │     │  │  ├─ template_campfire.json
│  │     │  │  ├─ template_candle.json
│  │     │  │  ├─ template_cauldron_full.json
│  │     │  │  ├─ template_cauldron_level1.json
│  │     │  │  ├─ template_cauldron_level2.json
│  │     │  │  ├─ template_chain.json
│  │     │  │  ├─ template_chiseled_bookshelf_slot_bottom_left.json
│  │     │  │  ├─ template_chiseled_bookshelf_slot_bottom_mid.json
│  │     │  │  ├─ template_chiseled_bookshelf_slot_bottom_right.json
│  │     │  │  ├─ template_chiseled_bookshelf_slot_top_left.json
│  │     │  │  ├─ template_chiseled_bookshelf_slot_top_mid.json
│  │     │  │  ├─ template_chiseled_bookshelf_slot_top_right.json
│  │     │  │  ├─ template_chorus_flower.json
│  │     │  │  ├─ template_command_block.json
│  │     │  │  ├─ template_custom_fence_gate.json
│  │     │  │  ├─ template_custom_fence_gate_open.json
│  │     │  │  ├─ template_custom_fence_gate_wall.json
│  │     │  │  ├─ template_custom_fence_gate_wall_open.json
│  │     │  │  ├─ template_daylight_detector.json
│  │     │  │  ├─ template_farmland.json
│  │     │  │  ├─ template_fence_gate.json
│  │     │  │  ├─ template_fence_gate_open.json
│  │     │  │  ├─ template_fence_gate_wall.json
│  │     │  │  ├─ template_fence_gate_wall_open.json
│  │     │  │  ├─ template_fire_floor.json
│  │     │  │  ├─ template_fire_side.json
│  │     │  │  ├─ template_fire_side_alt.json
│  │     │  │  ├─ template_fire_up.json
│  │     │  │  ├─ template_fire_up_alt.json
│  │     │  │  ├─ template_four_candles.json
│  │     │  │  ├─ template_four_turtle_eggs.json
│  │     │  │  ├─ template_glass_pane_noside.json
│  │     │  │  ├─ template_glass_pane_noside_alt.json
│  │     │  │  ├─ template_glass_pane_post.json
│  │     │  │  ├─ template_glass_pane_side.json
│  │     │  │  ├─ template_glass_pane_side_alt.json
│  │     │  │  ├─ template_glazed_terracotta.json
│  │     │  │  ├─ template_hanging_lantern.json
│  │     │  │  ├─ template_item_frame.json
│  │     │  │  ├─ template_item_frame_map.json
│  │     │  │  ├─ template_lantern.json
│  │     │  │  ├─ template_leaf_litter_1.json
│  │     │  │  ├─ template_leaf_litter_2.json
│  │     │  │  ├─ template_leaf_litter_3.json
│  │     │  │  ├─ template_leaf_litter_4.json
│  │     │  │  ├─ template_lightning_rod.json
│  │     │  │  ├─ template_orientable_trapdoor_bottom.json
│  │     │  │  ├─ template_orientable_trapdoor_open.json
│  │     │  │  ├─ template_orientable_trapdoor_top.json
│  │     │  │  ├─ template_piston.json
│  │     │  │  ├─ template_piston_head.json
│  │     │  │  ├─ template_piston_head_short.json
│  │     │  │  ├─ template_potted_azalea_bush.json
│  │     │  │  ├─ template_rail_raised_ne.json
│  │     │  │  ├─ template_rail_raised_sw.json
│  │     │  │  ├─ template_redstone_torch.json
│  │     │  │  ├─ template_redstone_torch_wall.json
│  │     │  │  ├─ template_sculk_shrieker.json
│  │     │  │  ├─ template_seagrass.json
│  │     │  │  ├─ template_shelf_body.json
│  │     │  │  ├─ template_shelf_center.json
│  │     │  │  ├─ template_shelf_inventory.json
│  │     │  │  ├─ template_shelf_left.json
│  │     │  │  ├─ template_shelf_right.json
│  │     │  │  ├─ template_shelf_unconnected.json
│  │     │  │  ├─ template_shelf_unpowered.json
│  │     │  │  ├─ template_single_face.json
│  │     │  │  ├─ template_three_candles.json
│  │     │  │  ├─ template_three_turtle_eggs.json
│  │     │  │  ├─ template_torch.json
│  │     │  │  ├─ template_torch_unlit.json
│  │     │  │  ├─ template_torch_wall.json
│  │     │  │  ├─ template_torch_wall_unlit.json
│  │     │  │  ├─ template_trapdoor_bottom.json
│  │     │  │  ├─ template_trapdoor_open.json
│  │     │  │  ├─ template_trapdoor_top.json
│  │     │  │  ├─ template_turtle_egg.json
│  │     │  │  ├─ template_two_candles.json
│  │     │  │  ├─ template_two_turtle_eggs.json
│  │     │  │  ├─ template_vault.json
│  │     │  │  ├─ template_wall_post.json
│  │     │  │  ├─ template_wall_side.json
│  │     │  │  ├─ template_wall_side_tall.json
│  │     │  │  ├─ terracotta.json
│  │     │  │  ├─ test_block_accept.json
│  │     │  │  ├─ test_block_fail.json
│  │     │  │  ├─ test_block_log.json
│  │     │  │  ├─ test_block_start.json
│  │     │  │  ├─ test_instance_block.json
│  │     │  │  ├─ thin_block.json
│  │     │  │  ├─ three_dead_sea_pickles.json
│  │     │  │  ├─ three_sea_pickles.json
│  │     │  │  ├─ three_slightly_cracked_turtle_eggs.json
│  │     │  │  ├─ three_turtle_eggs.json
│  │     │  │  ├─ three_very_cracked_turtle_eggs.json
│  │     │  │  ├─ tinted_cross.json
│  │     │  │  ├─ tinted_flower_pot_cross.json
│  │     │  │  ├─ tinted_glass.json
│  │     │  │  ├─ tnt.json
│  │     │  │  ├─ torch.json
│  │     │  │  ├─ torchflower.json
│  │     │  │  ├─ torchflower_crop_stage0.json
│  │     │  │  ├─ torchflower_crop_stage1.json
│  │     │  │  ├─ trapped_chest.json
│  │     │  │  ├─ trial_spawner.json
│  │     │  │  ├─ trial_spawner_active.json
│  │     │  │  ├─ trial_spawner_active_ominous.json
│  │     │  │  ├─ trial_spawner_ejecting_reward.json
│  │     │  │  ├─ trial_spawner_ejecting_reward_ominous.json
│  │     │  │  ├─ trial_spawner_inactive_ominous.json
│  │     │  │  ├─ tripwire_attached_n.json
│  │     │  │  ├─ tripwire_attached_ne.json
│  │     │  │  ├─ tripwire_attached_ns.json
│  │     │  │  ├─ tripwire_attached_nse.json
│  │     │  │  ├─ tripwire_attached_nsew.json
│  │     │  │  ├─ tripwire_hook.json
│  │     │  │  ├─ tripwire_hook_attached.json
│  │     │  │  ├─ tripwire_hook_attached_on.json
│  │     │  │  ├─ tripwire_hook_on.json
│  │     │  │  ├─ tripwire_n.json
│  │     │  │  ├─ tripwire_ne.json
│  │     │  │  ├─ tripwire_ns.json
│  │     │  │  ├─ tripwire_nse.json
│  │     │  │  ├─ tripwire_nsew.json
│  │     │  │  ├─ tube_coral.json
│  │     │  │  ├─ tube_coral_block.json
│  │     │  │  ├─ tube_coral_fan.json
│  │     │  │  ├─ tube_coral_wall_fan.json
│  │     │  │  ├─ tuff.json
│  │     │  │  ├─ tuff_bricks.json
│  │     │  │  ├─ tuff_brick_slab.json
│  │     │  │  ├─ tuff_brick_slab_top.json
│  │     │  │  ├─ tuff_brick_stairs.json
│  │     │  │  ├─ tuff_brick_stairs_inner.json
│  │     │  │  ├─ tuff_brick_stairs_outer.json
│  │     │  │  ├─ tuff_brick_wall_inventory.json
│  │     │  │  ├─ tuff_brick_wall_post.json
│  │     │  │  ├─ tuff_brick_wall_side.json
│  │     │  │  ├─ tuff_brick_wall_side_tall.json
│  │     │  │  ├─ tuff_slab.json
│  │     │  │  ├─ tuff_slab_top.json
│  │     │  │  ├─ tuff_stairs.json
│  │     │  │  ├─ tuff_stairs_inner.json
│  │     │  │  ├─ tuff_stairs_outer.json
│  │     │  │  ├─ tuff_wall_inventory.json
│  │     │  │  ├─ tuff_wall_post.json
│  │     │  │  ├─ tuff_wall_side.json
│  │     │  │  ├─ tuff_wall_side_tall.json
│  │     │  │  ├─ turtle_egg.json
│  │     │  │  ├─ twisting_vines.json
│  │     │  │  ├─ twisting_vines_plant.json
│  │     │  │  ├─ two_dead_sea_pickles.json
│  │     │  │  ├─ two_sea_pickles.json
│  │     │  │  ├─ two_slightly_cracked_turtle_eggs.json
│  │     │  │  ├─ two_turtle_eggs.json
│  │     │  │  ├─ two_very_cracked_turtle_eggs.json
│  │     │  │  ├─ vault.json
│  │     │  │  ├─ vault_active.json
│  │     │  │  ├─ vault_active_ominous.json
│  │     │  │  ├─ vault_ejecting_reward.json
│  │     │  │  ├─ vault_ejecting_reward_ominous.json
│  │     │  │  ├─ vault_ominous.json
│  │     │  │  ├─ vault_unlocking.json
│  │     │  │  ├─ vault_unlocking_ominous.json
│  │     │  │  ├─ verdant_froglight.json
│  │     │  │  ├─ verdant_froglight_horizontal.json
│  │     │  │  ├─ very_cracked_turtle_egg.json
│  │     │  │  ├─ vine.json
│  │     │  │  ├─ wall_inventory.json
│  │     │  │  ├─ wall_torch.json
│  │     │  │  ├─ warped_button.json
│  │     │  │  ├─ warped_button_inventory.json
│  │     │  │  ├─ warped_button_pressed.json
│  │     │  │  ├─ warped_door_bottom_left.json
│  │     │  │  ├─ warped_door_bottom_left_open.json
│  │     │  │  ├─ warped_door_bottom_right.json
│  │     │  │  ├─ warped_door_bottom_right_open.json
│  │     │  │  ├─ warped_door_top_left.json
│  │     │  │  ├─ warped_door_top_left_open.json
│  │     │  │  ├─ warped_door_top_right.json
│  │     │  │  ├─ warped_door_top_right_open.json
│  │     │  │  ├─ warped_fence_gate.json
│  │     │  │  ├─ warped_fence_gate_open.json
│  │     │  │  ├─ warped_fence_gate_wall.json
│  │     │  │  ├─ warped_fence_gate_wall_open.json
│  │     │  │  ├─ warped_fence_inventory.json
│  │     │  │  ├─ warped_fence_post.json
│  │     │  │  ├─ warped_fence_side.json
│  │     │  │  ├─ warped_fungus.json
│  │     │  │  ├─ warped_hanging_sign.json
│  │     │  │  ├─ warped_hyphae.json
│  │     │  │  ├─ warped_nylium.json
│  │     │  │  ├─ warped_planks.json
│  │     │  │  ├─ warped_pressure_plate.json
│  │     │  │  ├─ warped_pressure_plate_down.json
│  │     │  │  ├─ warped_roots.json
│  │     │  │  ├─ warped_shelf.json
│  │     │  │  ├─ warped_shelf_center.json
│  │     │  │  ├─ warped_shelf_inventory.json
│  │     │  │  ├─ warped_shelf_left.json
│  │     │  │  ├─ warped_shelf_right.json
│  │     │  │  ├─ warped_shelf_unconnected.json
│  │     │  │  ├─ warped_shelf_unpowered.json
│  │     │  │  ├─ warped_sign.json
│  │     │  │  ├─ warped_slab.json
│  │     │  │  ├─ warped_slab_top.json
│  │     │  │  ├─ warped_stairs.json
│  │     │  │  ├─ warped_stairs_inner.json
│  │     │  │  ├─ warped_stairs_outer.json
│  │     │  │  ├─ warped_stem.json
│  │     │  │  ├─ warped_trapdoor_bottom.json
│  │     │  │  ├─ warped_trapdoor_open.json
│  │     │  │  ├─ warped_trapdoor_top.json
│  │     │  │  ├─ warped_wart_block.json
│  │     │  │  ├─ water.json
│  │     │  │  ├─ water_cauldron_full.json
│  │     │  │  ├─ water_cauldron_level1.json
│  │     │  │  ├─ water_cauldron_level2.json
│  │     │  │  ├─ weathered_chiseled_copper.json
│  │     │  │  ├─ weathered_copper.json
│  │     │  │  ├─ weathered_copper_bars_cap.json
│  │     │  │  ├─ weathered_copper_bars_cap_alt.json
│  │     │  │  ├─ weathered_copper_bars_post.json
│  │     │  │  ├─ weathered_copper_bars_post_ends.json
│  │     │  │  ├─ weathered_copper_bars_side.json
│  │     │  │  ├─ weathered_copper_bars_side_alt.json
│  │     │  │  ├─ weathered_copper_bulb.json
│  │     │  │  ├─ weathered_copper_bulb_lit.json
│  │     │  │  ├─ weathered_copper_bulb_lit_powered.json
│  │     │  │  ├─ weathered_copper_bulb_powered.json
│  │     │  │  ├─ weathered_copper_chain.json
│  │     │  │  ├─ weathered_copper_chest.json
│  │     │  │  ├─ weathered_copper_door_bottom_left.json
│  │     │  │  ├─ weathered_copper_door_bottom_left_open.json
│  │     │  │  ├─ weathered_copper_door_bottom_right.json
│  │     │  │  ├─ weathered_copper_door_bottom_right_open.json
│  │     │  │  ├─ weathered_copper_door_top_left.json
│  │     │  │  ├─ weathered_copper_door_top_left_open.json
│  │     │  │  ├─ weathered_copper_door_top_right.json
│  │     │  │  ├─ weathered_copper_door_top_right_open.json
│  │     │  │  ├─ weathered_copper_golem_statue.json
│  │     │  │  ├─ weathered_copper_grate.json
│  │     │  │  ├─ weathered_copper_lantern.json
│  │     │  │  ├─ weathered_copper_lantern_hanging.json
│  │     │  │  ├─ weathered_copper_trapdoor_bottom.json
│  │     │  │  ├─ weathered_copper_trapdoor_open.json
│  │     │  │  ├─ weathered_copper_trapdoor_top.json
│  │     │  │  ├─ weathered_cut_copper.json
│  │     │  │  ├─ weathered_cut_copper_slab.json
│  │     │  │  ├─ weathered_cut_copper_slab_top.json
│  │     │  │  ├─ weathered_cut_copper_stairs.json
│  │     │  │  ├─ weathered_cut_copper_stairs_inner.json
│  │     │  │  ├─ weathered_cut_copper_stairs_outer.json
│  │     │  │  ├─ weathered_lightning_rod.json
│  │     │  │  ├─ weeping_vines.json
│  │     │  │  ├─ weeping_vines_plant.json
│  │     │  │  ├─ wet_sponge.json
│  │     │  │  ├─ wheat_stage0.json
│  │     │  │  ├─ wheat_stage1.json
│  │     │  │  ├─ wheat_stage2.json
│  │     │  │  ├─ wheat_stage3.json
│  │     │  │  ├─ wheat_stage4.json
│  │     │  │  ├─ wheat_stage5.json
│  │     │  │  ├─ wheat_stage6.json
│  │     │  │  ├─ wheat_stage7.json
│  │     │  │  ├─ white_candle_cake.json
│  │     │  │  ├─ white_candle_cake_lit.json
│  │     │  │  ├─ white_candle_four_candles.json
│  │     │  │  ├─ white_candle_four_candles_lit.json
│  │     │  │  ├─ white_candle_one_candle.json
│  │     │  │  ├─ white_candle_one_candle_lit.json
│  │     │  │  ├─ white_candle_three_candles.json
│  │     │  │  ├─ white_candle_three_candles_lit.json
│  │     │  │  ├─ white_candle_two_candles.json
│  │     │  │  ├─ white_candle_two_candles_lit.json
│  │     │  │  ├─ white_carpet.json
│  │     │  │  ├─ white_concrete.json
│  │     │  │  ├─ white_concrete_powder.json
│  │     │  │  ├─ white_glazed_terracotta.json
│  │     │  │  ├─ white_shulker_box.json
│  │     │  │  ├─ white_stained_glass.json
│  │     │  │  ├─ white_stained_glass_pane_noside.json
│  │     │  │  ├─ white_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ white_stained_glass_pane_post.json
│  │     │  │  ├─ white_stained_glass_pane_side.json
│  │     │  │  ├─ white_stained_glass_pane_side_alt.json
│  │     │  │  ├─ white_terracotta.json
│  │     │  │  ├─ white_tulip.json
│  │     │  │  ├─ white_wool.json
│  │     │  │  ├─ wildflowers_1.json
│  │     │  │  ├─ wildflowers_2.json
│  │     │  │  ├─ wildflowers_3.json
│  │     │  │  ├─ wildflowers_4.json
│  │     │  │  ├─ wither_rose.json
│  │     │  │  ├─ yellow_candle_cake.json
│  │     │  │  ├─ yellow_candle_cake_lit.json
│  │     │  │  ├─ yellow_candle_four_candles.json
│  │     │  │  ├─ yellow_candle_four_candles_lit.json
│  │     │  │  ├─ yellow_candle_one_candle.json
│  │     │  │  ├─ yellow_candle_one_candle_lit.json
│  │     │  │  ├─ yellow_candle_three_candles.json
│  │     │  │  ├─ yellow_candle_three_candles_lit.json
│  │     │  │  ├─ yellow_candle_two_candles.json
│  │     │  │  ├─ yellow_candle_two_candles_lit.json
│  │     │  │  ├─ yellow_carpet.json
│  │     │  │  ├─ yellow_concrete.json
│  │     │  │  ├─ yellow_concrete_powder.json
│  │     │  │  ├─ yellow_glazed_terracotta.json
│  │     │  │  ├─ yellow_shulker_box.json
│  │     │  │  ├─ yellow_stained_glass.json
│  │     │  │  ├─ yellow_stained_glass_pane_noside.json
│  │     │  │  ├─ yellow_stained_glass_pane_noside_alt.json
│  │     │  │  ├─ yellow_stained_glass_pane_post.json
│  │     │  │  ├─ yellow_stained_glass_pane_side.json
│  │     │  │  ├─ yellow_stained_glass_pane_side_alt.json
│  │     │  │  ├─ yellow_terracotta.json
│  │     │  │  └─ yellow_wool.json
│  │     │  └─ item
│  │     │     ├─ acacia_boat.json
│  │     │     ├─ acacia_chest_boat.json
│  │     │     ├─ acacia_door.json
│  │     │     ├─ acacia_hanging_sign.json
│  │     │     ├─ acacia_sapling.json
│  │     │     ├─ acacia_sign.json
│  │     │     ├─ activator_rail.json
│  │     │     ├─ air.json
│  │     │     ├─ allay_spawn_egg.json
│  │     │     ├─ allium.json
│  │     │     ├─ amethyst_bud.json
│  │     │     ├─ amethyst_cluster.json
│  │     │     ├─ amethyst_shard.json
│  │     │     ├─ angler_pottery_sherd.json
│  │     │     ├─ apple.json
│  │     │     ├─ archer_pottery_sherd.json
│  │     │     ├─ armadillo_scute.json
│  │     │     ├─ armadillo_spawn_egg.json
│  │     │     ├─ armor_stand.json
│  │     │     ├─ arms_up_pottery_sherd.json
│  │     │     ├─ arrow.json
│  │     │     ├─ axolotl_bucket.json
│  │     │     ├─ axolotl_spawn_egg.json
│  │     │     ├─ azure_bluet.json
│  │     │     ├─ baked_potato.json
│  │     │     ├─ bamboo.json
│  │     │     ├─ bamboo_chest_raft.json
│  │     │     ├─ bamboo_door.json
│  │     │     ├─ bamboo_hanging_sign.json
│  │     │     ├─ bamboo_raft.json
│  │     │     ├─ bamboo_sign.json
│  │     │     ├─ barrier.json
│  │     │     ├─ bat_spawn_egg.json
│  │     │     ├─ beef.json
│  │     │     ├─ beetroot.json
│  │     │     ├─ beetroot_seeds.json
│  │     │     ├─ beetroot_soup.json
│  │     │     ├─ bee_spawn_egg.json
│  │     │     ├─ bell.json
│  │     │     ├─ big_dripleaf.json
│  │     │     ├─ birch_boat.json
│  │     │     ├─ birch_chest_boat.json
│  │     │     ├─ birch_door.json
│  │     │     ├─ birch_hanging_sign.json
│  │     │     ├─ birch_sapling.json
│  │     │     ├─ birch_sign.json
│  │     │     ├─ black_bed.json
│  │     │     ├─ black_bundle.json
│  │     │     ├─ black_bundle_open_back.json
│  │     │     ├─ black_bundle_open_front.json
│  │     │     ├─ black_candle.json
│  │     │     ├─ black_dye.json
│  │     │     ├─ black_harness.json
│  │     │     ├─ black_shulker_box.json
│  │     │     ├─ black_stained_glass_pane.json
│  │     │     ├─ blade_pottery_sherd.json
│  │     │     ├─ blaze_powder.json
│  │     │     ├─ blaze_rod.json
│  │     │     ├─ blaze_spawn_egg.json
│  │     │     ├─ blue_bed.json
│  │     │     ├─ blue_bundle.json
│  │     │     ├─ blue_bundle_open_back.json
│  │     │     ├─ blue_bundle_open_front.json
│  │     │     ├─ blue_candle.json
│  │     │     ├─ blue_dye.json
│  │     │     ├─ blue_egg.json
│  │     │     ├─ blue_harness.json
│  │     │     ├─ blue_orchid.json
│  │     │     ├─ blue_shulker_box.json
│  │     │     ├─ blue_stained_glass_pane.json
│  │     │     ├─ bogged_spawn_egg.json
│  │     │     ├─ bolt_armor_trim_smithing_template.json
│  │     │     ├─ bone.json
│  │     │     ├─ bone_meal.json
│  │     │     ├─ book.json
│  │     │     ├─ bordure_indented_banner_pattern.json
│  │     │     ├─ bow.json
│  │     │     ├─ bowl.json
│  │     │     ├─ bow_pulling_0.json
│  │     │     ├─ bow_pulling_1.json
│  │     │     ├─ bow_pulling_2.json
│  │     │     ├─ brain_coral.json
│  │     │     ├─ brain_coral_fan.json
│  │     │     ├─ bread.json
│  │     │     ├─ breeze_rod.json
│  │     │     ├─ breeze_spawn_egg.json
│  │     │     ├─ brewer_pottery_sherd.json
│  │     │     ├─ brewing_stand.json
│  │     │     ├─ brick.json
│  │     │     ├─ brown_bed.json
│  │     │     ├─ brown_bundle.json
│  │     │     ├─ brown_bundle_open_back.json
│  │     │     ├─ brown_bundle_open_front.json
│  │     │     ├─ brown_candle.json
│  │     │     ├─ brown_dye.json
│  │     │     ├─ brown_egg.json
│  │     │     ├─ brown_harness.json
│  │     │     ├─ brown_mushroom.json
│  │     │     ├─ brown_shulker_box.json
│  │     │     ├─ brown_stained_glass_pane.json
│  │     │     ├─ brush.json
│  │     │     ├─ brush_brushing_0.json
│  │     │     ├─ brush_brushing_1.json
│  │     │     ├─ brush_brushing_2.json
│  │     │     ├─ bubble_coral.json
│  │     │     ├─ bubble_coral_fan.json
│  │     │     ├─ bucket.json
│  │     │     ├─ bundle.json
│  │     │     ├─ bundle_open_back.json
│  │     │     ├─ bundle_open_front.json
│  │     │     ├─ burn_pottery_sherd.json
│  │     │     ├─ bush.json
│  │     │     ├─ cactus_flower.json
│  │     │     ├─ cake.json
│  │     │     ├─ camel_husk_spawn_egg.json
│  │     │     ├─ camel_spawn_egg.json
│  │     │     ├─ campfire.json
│  │     │     ├─ candle.json
│  │     │     ├─ carrot.json
│  │     │     ├─ carrot_on_a_stick.json
│  │     │     ├─ cat_spawn_egg.json
│  │     │     ├─ cauldron.json
│  │     │     ├─ cave_spider_spawn_egg.json
│  │     │     ├─ chainmail_boots.json
│  │     │     ├─ chainmail_boots_amethyst_trim.json
│  │     │     ├─ chainmail_boots_copper_trim.json
│  │     │     ├─ chainmail_boots_diamond_trim.json
│  │     │     ├─ chainmail_boots_emerald_trim.json
│  │     │     ├─ chainmail_boots_gold_trim.json
│  │     │     ├─ chainmail_boots_iron_trim.json
│  │     │     ├─ chainmail_boots_lapis_trim.json
│  │     │     ├─ chainmail_boots_netherite_trim.json
│  │     │     ├─ chainmail_boots_quartz_trim.json
│  │     │     ├─ chainmail_boots_redstone_trim.json
│  │     │     ├─ chainmail_boots_resin_trim.json
│  │     │     ├─ chainmail_chestplate.json
│  │     │     ├─ chainmail_chestplate_amethyst_trim.json
│  │     │     ├─ chainmail_chestplate_copper_trim.json
│  │     │     ├─ chainmail_chestplate_diamond_trim.json
│  │     │     ├─ chainmail_chestplate_emerald_trim.json
│  │     │     ├─ chainmail_chestplate_gold_trim.json
│  │     │     ├─ chainmail_chestplate_iron_trim.json
│  │     │     ├─ chainmail_chestplate_lapis_trim.json
│  │     │     ├─ chainmail_chestplate_netherite_trim.json
│  │     │     ├─ chainmail_chestplate_quartz_trim.json
│  │     │     ├─ chainmail_chestplate_redstone_trim.json
│  │     │     ├─ chainmail_chestplate_resin_trim.json
│  │     │     ├─ chainmail_helmet.json
│  │     │     ├─ chainmail_helmet_amethyst_trim.json
│  │     │     ├─ chainmail_helmet_copper_trim.json
│  │     │     ├─ chainmail_helmet_diamond_trim.json
│  │     │     ├─ chainmail_helmet_emerald_trim.json
│  │     │     ├─ chainmail_helmet_gold_trim.json
│  │     │     ├─ chainmail_helmet_iron_trim.json
│  │     │     ├─ chainmail_helmet_lapis_trim.json
│  │     │     ├─ chainmail_helmet_netherite_trim.json
│  │     │     ├─ chainmail_helmet_quartz_trim.json
│  │     │     ├─ chainmail_helmet_redstone_trim.json
│  │     │     ├─ chainmail_helmet_resin_trim.json
│  │     │     ├─ chainmail_leggings.json
│  │     │     ├─ chainmail_leggings_amethyst_trim.json
│  │     │     ├─ chainmail_leggings_copper_trim.json
│  │     │     ├─ chainmail_leggings_diamond_trim.json
│  │     │     ├─ chainmail_leggings_emerald_trim.json
│  │     │     ├─ chainmail_leggings_gold_trim.json
│  │     │     ├─ chainmail_leggings_iron_trim.json
│  │     │     ├─ chainmail_leggings_lapis_trim.json
│  │     │     ├─ chainmail_leggings_netherite_trim.json
│  │     │     ├─ chainmail_leggings_quartz_trim.json
│  │     │     ├─ chainmail_leggings_redstone_trim.json
│  │     │     ├─ chainmail_leggings_resin_trim.json
│  │     │     ├─ charcoal.json
│  │     │     ├─ cherry_boat.json
│  │     │     ├─ cherry_chest_boat.json
│  │     │     ├─ cherry_door.json
│  │     │     ├─ cherry_hanging_sign.json
│  │     │     ├─ cherry_sapling.json
│  │     │     ├─ cherry_sign.json
│  │     │     ├─ chest.json
│  │     │     ├─ chest_minecart.json
│  │     │     ├─ chicken.json
│  │     │     ├─ chicken_spawn_egg.json
│  │     │     ├─ chorus_fruit.json
│  │     │     ├─ clay_ball.json
│  │     │     ├─ clock_00.json
│  │     │     ├─ clock_01.json
│  │     │     ├─ clock_02.json
│  │     │     ├─ clock_03.json
│  │     │     ├─ clock_04.json
│  │     │     ├─ clock_05.json
│  │     │     ├─ clock_06.json
│  │     │     ├─ clock_07.json
│  │     │     ├─ clock_08.json
│  │     │     ├─ clock_09.json
│  │     │     ├─ clock_10.json
│  │     │     ├─ clock_11.json
│  │     │     ├─ clock_12.json
│  │     │     ├─ clock_13.json
│  │     │     ├─ clock_14.json
│  │     │     ├─ clock_15.json
│  │     │     ├─ clock_16.json
│  │     │     ├─ clock_17.json
│  │     │     ├─ clock_18.json
│  │     │     ├─ clock_19.json
│  │     │     ├─ clock_20.json
│  │     │     ├─ clock_21.json
│  │     │     ├─ clock_22.json
│  │     │     ├─ clock_23.json
│  │     │     ├─ clock_24.json
│  │     │     ├─ clock_25.json
│  │     │     ├─ clock_26.json
│  │     │     ├─ clock_27.json
│  │     │     ├─ clock_28.json
│  │     │     ├─ clock_29.json
│  │     │     ├─ clock_30.json
│  │     │     ├─ clock_31.json
│  │     │     ├─ clock_32.json
│  │     │     ├─ clock_33.json
│  │     │     ├─ clock_34.json
│  │     │     ├─ clock_35.json
│  │     │     ├─ clock_36.json
│  │     │     ├─ clock_37.json
│  │     │     ├─ clock_38.json
│  │     │     ├─ clock_39.json
│  │     │     ├─ clock_40.json
│  │     │     ├─ clock_41.json
│  │     │     ├─ clock_42.json
│  │     │     ├─ clock_43.json
│  │     │     ├─ clock_44.json
│  │     │     ├─ clock_45.json
│  │     │     ├─ clock_46.json
│  │     │     ├─ clock_47.json
│  │     │     ├─ clock_48.json
│  │     │     ├─ clock_49.json
│  │     │     ├─ clock_50.json
│  │     │     ├─ clock_51.json
│  │     │     ├─ clock_52.json
│  │     │     ├─ clock_53.json
│  │     │     ├─ clock_54.json
│  │     │     ├─ clock_55.json
│  │     │     ├─ clock_56.json
│  │     │     ├─ clock_57.json
│  │     │     ├─ clock_58.json
│  │     │     ├─ clock_59.json
│  │     │     ├─ clock_60.json
│  │     │     ├─ clock_61.json
│  │     │     ├─ clock_62.json
│  │     │     ├─ clock_63.json
│  │     │     ├─ closed_eyeblossom.json
│  │     │     ├─ coal.json
│  │     │     ├─ coast_armor_trim_smithing_template.json
│  │     │     ├─ cobweb.json
│  │     │     ├─ cocoa_beans.json
│  │     │     ├─ cod.json
│  │     │     ├─ cod_bucket.json
│  │     │     ├─ cod_spawn_egg.json
│  │     │     ├─ command_block_minecart.json
│  │     │     ├─ comparator.json
│  │     │     ├─ compass_00.json
│  │     │     ├─ compass_01.json
│  │     │     ├─ compass_02.json
│  │     │     ├─ compass_03.json
│  │     │     ├─ compass_04.json
│  │     │     ├─ compass_05.json
│  │     │     ├─ compass_06.json
│  │     │     ├─ compass_07.json
│  │     │     ├─ compass_08.json
│  │     │     ├─ compass_09.json
│  │     │     ├─ compass_10.json
│  │     │     ├─ compass_11.json
│  │     │     ├─ compass_12.json
│  │     │     ├─ compass_13.json
│  │     │     ├─ compass_14.json
│  │     │     ├─ compass_15.json
│  │     │     ├─ compass_16.json
│  │     │     ├─ compass_17.json
│  │     │     ├─ compass_18.json
│  │     │     ├─ compass_19.json
│  │     │     ├─ compass_20.json
│  │     │     ├─ compass_21.json
│  │     │     ├─ compass_22.json
│  │     │     ├─ compass_23.json
│  │     │     ├─ compass_24.json
│  │     │     ├─ compass_25.json
│  │     │     ├─ compass_26.json
│  │     │     ├─ compass_27.json
│  │     │     ├─ compass_28.json
│  │     │     ├─ compass_29.json
│  │     │     ├─ compass_30.json
│  │     │     ├─ compass_31.json
│  │     │     ├─ conduit.json
│  │     │     ├─ cooked_beef.json
│  │     │     ├─ cooked_chicken.json
│  │     │     ├─ cooked_cod.json
│  │     │     ├─ cooked_mutton.json
│  │     │     ├─ cooked_porkchop.json
│  │     │     ├─ cooked_rabbit.json
│  │     │     ├─ cooked_salmon.json
│  │     │     ├─ cookie.json
│  │     │     ├─ copper_axe.json
│  │     │     ├─ copper_bars.json
│  │     │     ├─ copper_boots.json
│  │     │     ├─ copper_boots_amethyst_trim.json
│  │     │     ├─ copper_boots_copper_trim.json
│  │     │     ├─ copper_boots_diamond_trim.json
│  │     │     ├─ copper_boots_emerald_trim.json
│  │     │     ├─ copper_boots_gold_trim.json
│  │     │     ├─ copper_boots_iron_trim.json
│  │     │     ├─ copper_boots_lapis_trim.json
│  │     │     ├─ copper_boots_netherite_trim.json
│  │     │     ├─ copper_boots_quartz_trim.json
│  │     │     ├─ copper_boots_redstone_trim.json
│  │     │     ├─ copper_boots_resin_trim.json
│  │     │     ├─ copper_chain.json
│  │     │     ├─ copper_chest.json
│  │     │     ├─ copper_chestplate.json
│  │     │     ├─ copper_chestplate_amethyst_trim.json
│  │     │     ├─ copper_chestplate_copper_trim.json
│  │     │     ├─ copper_chestplate_diamond_trim.json
│  │     │     ├─ copper_chestplate_emerald_trim.json
│  │     │     ├─ copper_chestplate_gold_trim.json
│  │     │     ├─ copper_chestplate_iron_trim.json
│  │     │     ├─ copper_chestplate_lapis_trim.json
│  │     │     ├─ copper_chestplate_netherite_trim.json
│  │     │     ├─ copper_chestplate_quartz_trim.json
│  │     │     ├─ copper_chestplate_redstone_trim.json
│  │     │     ├─ copper_chestplate_resin_trim.json
│  │     │     ├─ copper_door.json
│  │     │     ├─ copper_golem_spawn_egg.json
│  │     │     ├─ copper_helmet.json
│  │     │     ├─ copper_helmet_amethyst_trim.json
│  │     │     ├─ copper_helmet_copper_trim.json
│  │     │     ├─ copper_helmet_diamond_trim.json
│  │     │     ├─ copper_helmet_emerald_trim.json
│  │     │     ├─ copper_helmet_gold_trim.json
│  │     │     ├─ copper_helmet_iron_trim.json
│  │     │     ├─ copper_helmet_lapis_trim.json
│  │     │     ├─ copper_helmet_netherite_trim.json
│  │     │     ├─ copper_helmet_quartz_trim.json
│  │     │     ├─ copper_helmet_redstone_trim.json
│  │     │     ├─ copper_helmet_resin_trim.json
│  │     │     ├─ copper_hoe.json
│  │     │     ├─ copper_horse_armor.json
│  │     │     ├─ copper_ingot.json
│  │     │     ├─ copper_lantern.json
│  │     │     ├─ copper_leggings.json
│  │     │     ├─ copper_leggings_amethyst_trim.json
│  │     │     ├─ copper_leggings_copper_trim.json
│  │     │     ├─ copper_leggings_diamond_trim.json
│  │     │     ├─ copper_leggings_emerald_trim.json
│  │     │     ├─ copper_leggings_gold_trim.json
│  │     │     ├─ copper_leggings_iron_trim.json
│  │     │     ├─ copper_leggings_lapis_trim.json
│  │     │     ├─ copper_leggings_netherite_trim.json
│  │     │     ├─ copper_leggings_quartz_trim.json
│  │     │     ├─ copper_leggings_redstone_trim.json
│  │     │     ├─ copper_leggings_resin_trim.json
│  │     │     ├─ copper_nautilus_armor.json
│  │     │     ├─ copper_nugget.json
│  │     │     ├─ copper_pickaxe.json
│  │     │     ├─ copper_shovel.json
│  │     │     ├─ copper_spear.json
│  │     │     ├─ copper_spear_in_hand.json
│  │     │     ├─ copper_sword.json
│  │     │     ├─ copper_torch.json
│  │     │     ├─ cornflower.json
│  │     │     ├─ cow_spawn_egg.json
│  │     │     ├─ creaking_spawn_egg.json
│  │     │     ├─ creeper_banner_pattern.json
│  │     │     ├─ creeper_spawn_egg.json
│  │     │     ├─ crimson_door.json
│  │     │     ├─ crimson_fungus.json
│  │     │     ├─ crimson_hanging_sign.json
│  │     │     ├─ crimson_roots.json
│  │     │     ├─ crimson_sign.json
│  │     │     ├─ crossbow.json
│  │     │     ├─ crossbow_arrow.json
│  │     │     ├─ crossbow_firework.json
│  │     │     ├─ crossbow_pulling_0.json
│  │     │     ├─ crossbow_pulling_1.json
│  │     │     ├─ crossbow_pulling_2.json
│  │     │     ├─ cyan_bed.json
│  │     │     ├─ cyan_bundle.json
│  │     │     ├─ cyan_bundle_open_back.json
│  │     │     ├─ cyan_bundle_open_front.json
│  │     │     ├─ cyan_candle.json
│  │     │     ├─ cyan_dye.json
│  │     │     ├─ cyan_harness.json
│  │     │     ├─ cyan_shulker_box.json
│  │     │     ├─ cyan_stained_glass_pane.json
│  │     │     ├─ dandelion.json
│  │     │     ├─ danger_pottery_sherd.json
│  │     │     ├─ dark_oak_boat.json
│  │     │     ├─ dark_oak_chest_boat.json
│  │     │     ├─ dark_oak_door.json
│  │     │     ├─ dark_oak_hanging_sign.json
│  │     │     ├─ dark_oak_sapling.json
│  │     │     ├─ dark_oak_sign.json
│  │     │     ├─ dead_brain_coral.json
│  │     │     ├─ dead_brain_coral_fan.json
│  │     │     ├─ dead_bubble_coral.json
│  │     │     ├─ dead_bubble_coral_fan.json
│  │     │     ├─ dead_bush.json
│  │     │     ├─ dead_fire_coral.json
│  │     │     ├─ dead_fire_coral_fan.json
│  │     │     ├─ dead_horn_coral.json
│  │     │     ├─ dead_horn_coral_fan.json
│  │     │     ├─ dead_tube_coral.json
│  │     │     ├─ dead_tube_coral_fan.json
│  │     │     ├─ debug_stick.json
│  │     │     ├─ decorated_pot.json
│  │     │     ├─ detector_rail.json
│  │     │     ├─ diamond.json
│  │     │     ├─ diamond_axe.json
│  │     │     ├─ diamond_boots.json
│  │     │     ├─ diamond_boots_amethyst_trim.json
│  │     │     ├─ diamond_boots_copper_trim.json
│  │     │     ├─ diamond_boots_diamond_trim.json
│  │     │     ├─ diamond_boots_emerald_trim.json
│  │     │     ├─ diamond_boots_gold_trim.json
│  │     │     ├─ diamond_boots_iron_trim.json
│  │     │     ├─ diamond_boots_lapis_trim.json
│  │     │     ├─ diamond_boots_netherite_trim.json
│  │     │     ├─ diamond_boots_quartz_trim.json
│  │     │     ├─ diamond_boots_redstone_trim.json
│  │     │     ├─ diamond_boots_resin_trim.json
│  │     │     ├─ diamond_chestplate.json
│  │     │     ├─ diamond_chestplate_amethyst_trim.json
│  │     │     ├─ diamond_chestplate_copper_trim.json
│  │     │     ├─ diamond_chestplate_diamond_trim.json
│  │     │     ├─ diamond_chestplate_emerald_trim.json
│  │     │     ├─ diamond_chestplate_gold_trim.json
│  │     │     ├─ diamond_chestplate_iron_trim.json
│  │     │     ├─ diamond_chestplate_lapis_trim.json
│  │     │     ├─ diamond_chestplate_netherite_trim.json
│  │     │     ├─ diamond_chestplate_quartz_trim.json
│  │     │     ├─ diamond_chestplate_redstone_trim.json
│  │     │     ├─ diamond_chestplate_resin_trim.json
│  │     │     ├─ diamond_helmet.json
│  │     │     ├─ diamond_helmet_amethyst_trim.json
│  │     │     ├─ diamond_helmet_copper_trim.json
│  │     │     ├─ diamond_helmet_diamond_trim.json
│  │     │     ├─ diamond_helmet_emerald_trim.json
│  │     │     ├─ diamond_helmet_gold_trim.json
│  │     │     ├─ diamond_helmet_iron_trim.json
│  │     │     ├─ diamond_helmet_lapis_trim.json
│  │     │     ├─ diamond_helmet_netherite_trim.json
│  │     │     ├─ diamond_helmet_quartz_trim.json
│  │     │     ├─ diamond_helmet_redstone_trim.json
│  │     │     ├─ diamond_helmet_resin_trim.json
│  │     │     ├─ diamond_hoe.json
│  │     │     ├─ diamond_horse_armor.json
│  │     │     ├─ diamond_leggings.json
│  │     │     ├─ diamond_leggings_amethyst_trim.json
│  │     │     ├─ diamond_leggings_copper_trim.json
│  │     │     ├─ diamond_leggings_diamond_trim.json
│  │     │     ├─ diamond_leggings_emerald_trim.json
│  │     │     ├─ diamond_leggings_gold_trim.json
│  │     │     ├─ diamond_leggings_iron_trim.json
│  │     │     ├─ diamond_leggings_lapis_trim.json
│  │     │     ├─ diamond_leggings_netherite_trim.json
│  │     │     ├─ diamond_leggings_quartz_trim.json
│  │     │     ├─ diamond_leggings_redstone_trim.json
│  │     │     ├─ diamond_leggings_resin_trim.json
│  │     │     ├─ diamond_nautilus_armor.json
│  │     │     ├─ diamond_pickaxe.json
│  │     │     ├─ diamond_shovel.json
│  │     │     ├─ diamond_spear.json
│  │     │     ├─ diamond_spear_in_hand.json
│  │     │     ├─ diamond_sword.json
│  │     │     ├─ disc_fragment_5.json
│  │     │     ├─ dolphin_spawn_egg.json
│  │     │     ├─ donkey_spawn_egg.json
│  │     │     ├─ dragon_breath.json
│  │     │     ├─ dragon_head.json
│  │     │     ├─ dried_kelp.json
│  │     │     ├─ drowned_spawn_egg.json
│  │     │     ├─ dune_armor_trim_smithing_template.json
│  │     │     ├─ echo_shard.json
│  │     │     ├─ egg.json
│  │     │     ├─ elder_guardian_spawn_egg.json
│  │     │     ├─ elytra.json
│  │     │     ├─ elytra_broken.json
│  │     │     ├─ emerald.json
│  │     │     ├─ enchanted_book.json
│  │     │     ├─ enchanted_golden_apple.json
│  │     │     ├─ enderman_spawn_egg.json
│  │     │     ├─ endermite_spawn_egg.json
│  │     │     ├─ ender_chest.json
│  │     │     ├─ ender_dragon_spawn_egg.json
│  │     │     ├─ ender_eye.json
│  │     │     ├─ ender_pearl.json
│  │     │     ├─ end_crystal.json
│  │     │     ├─ evoker_spawn_egg.json
│  │     │     ├─ experience_bottle.json
│  │     │     ├─ explorer_pottery_sherd.json
│  │     │     ├─ exposed_copper_bars.json
│  │     │     ├─ exposed_copper_chain.json
│  │     │     ├─ exposed_copper_chest.json
│  │     │     ├─ exposed_copper_door.json
│  │     │     ├─ exposed_copper_lantern.json
│  │     │     ├─ eye_armor_trim_smithing_template.json
│  │     │     ├─ feather.json
│  │     │     ├─ fermented_spider_eye.json
│  │     │     ├─ fern.json
│  │     │     ├─ field_masoned_banner_pattern.json
│  │     │     ├─ filled_map.json
│  │     │     ├─ firefly_bush.json
│  │     │     ├─ firework_rocket.json
│  │     │     ├─ firework_star.json
│  │     │     ├─ fire_charge.json
│  │     │     ├─ fire_coral.json
│  │     │     ├─ fire_coral_fan.json
│  │     │     ├─ fishing_rod.json
│  │     │     ├─ fishing_rod_cast.json
│  │     │     ├─ flint.json
│  │     │     ├─ flint_and_steel.json
│  │     │     ├─ flower_banner_pattern.json
│  │     │     ├─ flower_pot.json
│  │     │     ├─ flow_armor_trim_smithing_template.json
│  │     │     ├─ flow_banner_pattern.json
│  │     │     ├─ flow_pottery_sherd.json
│  │     │     ├─ fox_spawn_egg.json
│  │     │     ├─ friend_pottery_sherd.json
│  │     │     ├─ frogspawn.json
│  │     │     ├─ frog_spawn_egg.json
│  │     │     ├─ furnace_minecart.json
│  │     │     ├─ generated.json
│  │     │     ├─ ghast_spawn_egg.json
│  │     │     ├─ ghast_tear.json
│  │     │     ├─ glass_bottle.json
│  │     │     ├─ glass_pane.json
│  │     │     ├─ glistering_melon_slice.json
│  │     │     ├─ globe_banner_pattern.json
│  │     │     ├─ glowstone_dust.json
│  │     │     ├─ glow_berries.json
│  │     │     ├─ glow_ink_sac.json
│  │     │     ├─ glow_item_frame.json
│  │     │     ├─ glow_lichen.json
│  │     │     ├─ glow_squid_spawn_egg.json
│  │     │     ├─ goat_horn.json
│  │     │     ├─ goat_spawn_egg.json
│  │     │     ├─ golden_apple.json
│  │     │     ├─ golden_axe.json
│  │     │     ├─ golden_boots.json
│  │     │     ├─ golden_boots_amethyst_trim.json
│  │     │     ├─ golden_boots_copper_trim.json
│  │     │     ├─ golden_boots_diamond_trim.json
│  │     │     ├─ golden_boots_emerald_trim.json
│  │     │     ├─ golden_boots_gold_trim.json
│  │     │     ├─ golden_boots_iron_trim.json
│  │     │     ├─ golden_boots_lapis_trim.json
│  │     │     ├─ golden_boots_netherite_trim.json
│  │     │     ├─ golden_boots_quartz_trim.json
│  │     │     ├─ golden_boots_redstone_trim.json
│  │     │     ├─ golden_boots_resin_trim.json
│  │     │     ├─ golden_carrot.json
│  │     │     ├─ golden_chestplate.json
│  │     │     ├─ golden_chestplate_amethyst_trim.json
│  │     │     ├─ golden_chestplate_copper_trim.json
│  │     │     ├─ golden_chestplate_diamond_trim.json
│  │     │     ├─ golden_chestplate_emerald_trim.json
│  │     │     ├─ golden_chestplate_gold_trim.json
│  │     │     ├─ golden_chestplate_iron_trim.json
│  │     │     ├─ golden_chestplate_lapis_trim.json
│  │     │     ├─ golden_chestplate_netherite_trim.json
│  │     │     ├─ golden_chestplate_quartz_trim.json
│  │     │     ├─ golden_chestplate_redstone_trim.json
│  │     │     ├─ golden_chestplate_resin_trim.json
│  │     │     ├─ golden_helmet.json
│  │     │     ├─ golden_helmet_amethyst_trim.json
│  │     │     ├─ golden_helmet_copper_trim.json
│  │     │     ├─ golden_helmet_diamond_trim.json
│  │     │     ├─ golden_helmet_emerald_trim.json
│  │     │     ├─ golden_helmet_gold_trim.json
│  │     │     ├─ golden_helmet_iron_trim.json
│  │     │     ├─ golden_helmet_lapis_trim.json
│  │     │     ├─ golden_helmet_netherite_trim.json
│  │     │     ├─ golden_helmet_quartz_trim.json
│  │     │     ├─ golden_helmet_redstone_trim.json
│  │     │     ├─ golden_helmet_resin_trim.json
│  │     │     ├─ golden_hoe.json
│  │     │     ├─ golden_horse_armor.json
│  │     │     ├─ golden_leggings.json
│  │     │     ├─ golden_leggings_amethyst_trim.json
│  │     │     ├─ golden_leggings_copper_trim.json
│  │     │     ├─ golden_leggings_diamond_trim.json
│  │     │     ├─ golden_leggings_emerald_trim.json
│  │     │     ├─ golden_leggings_gold_trim.json
│  │     │     ├─ golden_leggings_iron_trim.json
│  │     │     ├─ golden_leggings_lapis_trim.json
│  │     │     ├─ golden_leggings_netherite_trim.json
│  │     │     ├─ golden_leggings_quartz_trim.json
│  │     │     ├─ golden_leggings_redstone_trim.json
│  │     │     ├─ golden_leggings_resin_trim.json
│  │     │     ├─ golden_nautilus_armor.json
│  │     │     ├─ golden_pickaxe.json
│  │     │     ├─ golden_shovel.json
│  │     │     ├─ golden_spear.json
│  │     │     ├─ golden_spear_in_hand.json
│  │     │     ├─ golden_sword.json
│  │     │     ├─ gold_ingot.json
│  │     │     ├─ gold_nugget.json
│  │     │     ├─ gray_bed.json
│  │     │     ├─ gray_bundle.json
│  │     │     ├─ gray_bundle_open_back.json
│  │     │     ├─ gray_bundle_open_front.json
│  │     │     ├─ gray_candle.json
│  │     │     ├─ gray_dye.json
│  │     │     ├─ gray_harness.json
│  │     │     ├─ gray_shulker_box.json
│  │     │     ├─ gray_stained_glass_pane.json
│  │     │     ├─ green_bed.json
│  │     │     ├─ green_bundle.json
│  │     │     ├─ green_bundle_open_back.json
│  │     │     ├─ green_bundle_open_front.json
│  │     │     ├─ green_candle.json
│  │     │     ├─ green_dye.json
│  │     │     ├─ green_harness.json
│  │     │     ├─ green_shulker_box.json
│  │     │     ├─ green_stained_glass_pane.json
│  │     │     ├─ guardian_spawn_egg.json
│  │     │     ├─ gunpowder.json
│  │     │     ├─ guster_banner_pattern.json
│  │     │     ├─ guster_pottery_sherd.json
│  │     │     ├─ handheld.json
│  │     │     ├─ handheld_mace.json
│  │     │     ├─ handheld_rod.json
│  │     │     ├─ hanging_roots.json
│  │     │     ├─ happy_ghast_spawn_egg.json
│  │     │     ├─ heartbreak_pottery_sherd.json
│  │     │     ├─ heart_of_the_sea.json
│  │     │     ├─ heart_pottery_sherd.json
│  │     │     ├─ hoglin_spawn_egg.json
│  │     │     ├─ honeycomb.json
│  │     │     ├─ honey_bottle.json
│  │     │     ├─ hopper.json
│  │     │     ├─ hopper_minecart.json
│  │     │     ├─ horn_coral.json
│  │     │     ├─ horn_coral_fan.json
│  │     │     ├─ horse_spawn_egg.json
│  │     │     ├─ host_armor_trim_smithing_template.json
│  │     │     ├─ howl_pottery_sherd.json
│  │     │     ├─ husk_spawn_egg.json
│  │     │     ├─ ink_sac.json
│  │     │     ├─ iron_axe.json
│  │     │     ├─ iron_bars.json
│  │     │     ├─ iron_boots.json
│  │     │     ├─ iron_boots_amethyst_trim.json
│  │     │     ├─ iron_boots_copper_trim.json
│  │     │     ├─ iron_boots_diamond_trim.json
│  │     │     ├─ iron_boots_emerald_trim.json
│  │     │     ├─ iron_boots_gold_trim.json
│  │     │     ├─ iron_boots_iron_trim.json
│  │     │     ├─ iron_boots_lapis_trim.json
│  │     │     ├─ iron_boots_netherite_trim.json
│  │     │     ├─ iron_boots_quartz_trim.json
│  │     │     ├─ iron_boots_redstone_trim.json
│  │     │     ├─ iron_boots_resin_trim.json
│  │     │     ├─ iron_chain.json
│  │     │     ├─ iron_chestplate.json
│  │     │     ├─ iron_chestplate_amethyst_trim.json
│  │     │     ├─ iron_chestplate_copper_trim.json
│  │     │     ├─ iron_chestplate_diamond_trim.json
│  │     │     ├─ iron_chestplate_emerald_trim.json
│  │     │     ├─ iron_chestplate_gold_trim.json
│  │     │     ├─ iron_chestplate_iron_trim.json
│  │     │     ├─ iron_chestplate_lapis_trim.json
│  │     │     ├─ iron_chestplate_netherite_trim.json
│  │     │     ├─ iron_chestplate_quartz_trim.json
│  │     │     ├─ iron_chestplate_redstone_trim.json
│  │     │     ├─ iron_chestplate_resin_trim.json
│  │     │     ├─ iron_door.json
│  │     │     ├─ iron_golem_spawn_egg.json
│  │     │     ├─ iron_helmet.json
│  │     │     ├─ iron_helmet_amethyst_trim.json
│  │     │     ├─ iron_helmet_copper_trim.json
│  │     │     ├─ iron_helmet_diamond_trim.json
│  │     │     ├─ iron_helmet_emerald_trim.json
│  │     │     ├─ iron_helmet_gold_trim.json
│  │     │     ├─ iron_helmet_iron_trim.json
│  │     │     ├─ iron_helmet_lapis_trim.json
│  │     │     ├─ iron_helmet_netherite_trim.json
│  │     │     ├─ iron_helmet_quartz_trim.json
│  │     │     ├─ iron_helmet_redstone_trim.json
│  │     │     ├─ iron_helmet_resin_trim.json
│  │     │     ├─ iron_hoe.json
│  │     │     ├─ iron_horse_armor.json
│  │     │     ├─ iron_ingot.json
│  │     │     ├─ iron_leggings.json
│  │     │     ├─ iron_leggings_amethyst_trim.json
│  │     │     ├─ iron_leggings_copper_trim.json
│  │     │     ├─ iron_leggings_diamond_trim.json
│  │     │     ├─ iron_leggings_emerald_trim.json
│  │     │     ├─ iron_leggings_gold_trim.json
│  │     │     ├─ iron_leggings_iron_trim.json
│  │     │     ├─ iron_leggings_lapis_trim.json
│  │     │     ├─ iron_leggings_netherite_trim.json
│  │     │     ├─ iron_leggings_quartz_trim.json
│  │     │     ├─ iron_leggings_redstone_trim.json
│  │     │     ├─ iron_leggings_resin_trim.json
│  │     │     ├─ iron_nautilus_armor.json
│  │     │     ├─ iron_nugget.json
│  │     │     ├─ iron_pickaxe.json
│  │     │     ├─ iron_shovel.json
│  │     │     ├─ iron_spear.json
│  │     │     ├─ iron_spear_in_hand.json
│  │     │     ├─ iron_sword.json
│  │     │     ├─ item_frame.json
│  │     │     ├─ jungle_boat.json
│  │     │     ├─ jungle_chest_boat.json
│  │     │     ├─ jungle_door.json
│  │     │     ├─ jungle_hanging_sign.json
│  │     │     ├─ jungle_sapling.json
│  │     │     ├─ jungle_sign.json
│  │     │     ├─ kelp.json
│  │     │     ├─ knowledge_book.json
│  │     │     ├─ ladder.json
│  │     │     ├─ lantern.json
│  │     │     ├─ lapis_lazuli.json
│  │     │     ├─ large_amethyst_bud.json
│  │     │     ├─ large_fern.json
│  │     │     ├─ lava_bucket.json
│  │     │     ├─ lead.json
│  │     │     ├─ leaf_litter.json
│  │     │     ├─ leather.json
│  │     │     ├─ leather_boots.json
│  │     │     ├─ leather_boots_amethyst_trim.json
│  │     │     ├─ leather_boots_copper_trim.json
│  │     │     ├─ leather_boots_diamond_trim.json
│  │     │     ├─ leather_boots_emerald_trim.json
│  │     │     ├─ leather_boots_gold_trim.json
│  │     │     ├─ leather_boots_iron_trim.json
│  │     │     ├─ leather_boots_lapis_trim.json
│  │     │     ├─ leather_boots_netherite_trim.json
│  │     │     ├─ leather_boots_quartz_trim.json
│  │     │     ├─ leather_boots_redstone_trim.json
│  │     │     ├─ leather_boots_resin_trim.json
│  │     │     ├─ leather_chestplate.json
│  │     │     ├─ leather_chestplate_amethyst_trim.json
│  │     │     ├─ leather_chestplate_copper_trim.json
│  │     │     ├─ leather_chestplate_diamond_trim.json
│  │     │     ├─ leather_chestplate_emerald_trim.json
│  │     │     ├─ leather_chestplate_gold_trim.json
│  │     │     ├─ leather_chestplate_iron_trim.json
│  │     │     ├─ leather_chestplate_lapis_trim.json
│  │     │     ├─ leather_chestplate_netherite_trim.json
│  │     │     ├─ leather_chestplate_quartz_trim.json
│  │     │     ├─ leather_chestplate_redstone_trim.json
│  │     │     ├─ leather_chestplate_resin_trim.json
│  │     │     ├─ leather_helmet.json
│  │     │     ├─ leather_helmet_amethyst_trim.json
│  │     │     ├─ leather_helmet_copper_trim.json
│  │     │     ├─ leather_helmet_diamond_trim.json
│  │     │     ├─ leather_helmet_emerald_trim.json
│  │     │     ├─ leather_helmet_gold_trim.json
│  │     │     ├─ leather_helmet_iron_trim.json
│  │     │     ├─ leather_helmet_lapis_trim.json
│  │     │     ├─ leather_helmet_netherite_trim.json
│  │     │     ├─ leather_helmet_quartz_trim.json
│  │     │     ├─ leather_helmet_redstone_trim.json
│  │     │     ├─ leather_helmet_resin_trim.json
│  │     │     ├─ leather_horse_armor.json
│  │     │     ├─ leather_leggings.json
│  │     │     ├─ leather_leggings_amethyst_trim.json
│  │     │     ├─ leather_leggings_copper_trim.json
│  │     │     ├─ leather_leggings_diamond_trim.json
│  │     │     ├─ leather_leggings_emerald_trim.json
│  │     │     ├─ leather_leggings_gold_trim.json
│  │     │     ├─ leather_leggings_iron_trim.json
│  │     │     ├─ leather_leggings_lapis_trim.json
│  │     │     ├─ leather_leggings_netherite_trim.json
│  │     │     ├─ leather_leggings_quartz_trim.json
│  │     │     ├─ leather_leggings_redstone_trim.json
│  │     │     ├─ leather_leggings_resin_trim.json
│  │     │     ├─ lever.json
│  │     │     ├─ light.json
│  │     │     ├─ light_00.json
│  │     │     ├─ light_01.json
│  │     │     ├─ light_02.json
│  │     │     ├─ light_03.json
│  │     │     ├─ light_04.json
│  │     │     ├─ light_05.json
│  │     │     ├─ light_06.json
│  │     │     ├─ light_07.json
│  │     │     ├─ light_08.json
│  │     │     ├─ light_09.json
│  │     │     ├─ light_10.json
│  │     │     ├─ light_11.json
│  │     │     ├─ light_12.json
│  │     │     ├─ light_13.json
│  │     │     ├─ light_14.json
│  │     │     ├─ light_15.json
│  │     │     ├─ light_blue_bed.json
│  │     │     ├─ light_blue_bundle.json
│  │     │     ├─ light_blue_bundle_open_back.json
│  │     │     ├─ light_blue_bundle_open_front.json
│  │     │     ├─ light_blue_candle.json
│  │     │     ├─ light_blue_dye.json
│  │     │     ├─ light_blue_harness.json
│  │     │     ├─ light_blue_shulker_box.json
│  │     │     ├─ light_blue_stained_glass_pane.json
│  │     │     ├─ light_gray_bed.json
│  │     │     ├─ light_gray_bundle.json
│  │     │     ├─ light_gray_bundle_open_back.json
│  │     │     ├─ light_gray_bundle_open_front.json
│  │     │     ├─ light_gray_candle.json
│  │     │     ├─ light_gray_dye.json
│  │     │     ├─ light_gray_harness.json
│  │     │     ├─ light_gray_shulker_box.json
│  │     │     ├─ light_gray_stained_glass_pane.json
│  │     │     ├─ lilac.json
│  │     │     ├─ lily_of_the_valley.json
│  │     │     ├─ lily_pad.json
│  │     │     ├─ lime_bed.json
│  │     │     ├─ lime_bundle.json
│  │     │     ├─ lime_bundle_open_back.json
│  │     │     ├─ lime_bundle_open_front.json
│  │     │     ├─ lime_candle.json
│  │     │     ├─ lime_dye.json
│  │     │     ├─ lime_harness.json
│  │     │     ├─ lime_shulker_box.json
│  │     │     ├─ lime_stained_glass_pane.json
│  │     │     ├─ lingering_potion.json
│  │     │     ├─ llama_spawn_egg.json
│  │     │     ├─ mace.json
│  │     │     ├─ magenta_bed.json
│  │     │     ├─ magenta_bundle.json
│  │     │     ├─ magenta_bundle_open_back.json
│  │     │     ├─ magenta_bundle_open_front.json
│  │     │     ├─ magenta_candle.json
│  │     │     ├─ magenta_dye.json
│  │     │     ├─ magenta_harness.json
│  │     │     ├─ magenta_shulker_box.json
│  │     │     ├─ magenta_stained_glass_pane.json
│  │     │     ├─ magma_cream.json
│  │     │     ├─ magma_cube_spawn_egg.json
│  │     │     ├─ mangrove_boat.json
│  │     │     ├─ mangrove_chest_boat.json
│  │     │     ├─ mangrove_door.json
│  │     │     ├─ mangrove_hanging_sign.json
│  │     │     ├─ mangrove_propagule.json
│  │     │     ├─ mangrove_sign.json
│  │     │     ├─ map.json
│  │     │     ├─ medium_amethyst_bud.json
│  │     │     ├─ melon_seeds.json
│  │     │     ├─ melon_slice.json
│  │     │     ├─ milk_bucket.json
│  │     │     ├─ minecart.json
│  │     │     ├─ miner_pottery_sherd.json
│  │     │     ├─ mojang_banner_pattern.json
│  │     │     ├─ mooshroom_spawn_egg.json
│  │     │     ├─ mourner_pottery_sherd.json
│  │     │     ├─ mule_spawn_egg.json
│  │     │     ├─ mushroom_stew.json
│  │     │     ├─ music_disc_11.json
│  │     │     ├─ music_disc_13.json
│  │     │     ├─ music_disc_5.json
│  │     │     ├─ music_disc_blocks.json
│  │     │     ├─ music_disc_cat.json
│  │     │     ├─ music_disc_chirp.json
│  │     │     ├─ music_disc_creator.json
│  │     │     ├─ music_disc_creator_music_box.json
│  │     │     ├─ music_disc_far.json
│  │     │     ├─ music_disc_lava_chicken.json
│  │     │     ├─ music_disc_mall.json
│  │     │     ├─ music_disc_mellohi.json
│  │     │     ├─ music_disc_otherside.json
│  │     │     ├─ music_disc_pigstep.json
│  │     │     ├─ music_disc_precipice.json
│  │     │     ├─ music_disc_relic.json
│  │     │     ├─ music_disc_stal.json
│  │     │     ├─ music_disc_strad.json
│  │     │     ├─ music_disc_tears.json
│  │     │     ├─ music_disc_wait.json
│  │     │     ├─ music_disc_ward.json
│  │     │     ├─ mutton.json
│  │     │     ├─ name_tag.json
│  │     │     ├─ nautilus_shell.json
│  │     │     ├─ nautilus_spawn_egg.json
│  │     │     ├─ netherite_axe.json
│  │     │     ├─ netherite_boots.json
│  │     │     ├─ netherite_boots_amethyst_trim.json
│  │     │     ├─ netherite_boots_copper_trim.json
│  │     │     ├─ netherite_boots_diamond_trim.json
│  │     │     ├─ netherite_boots_emerald_trim.json
│  │     │     ├─ netherite_boots_gold_trim.json
│  │     │     ├─ netherite_boots_iron_trim.json
│  │     │     ├─ netherite_boots_lapis_trim.json
│  │     │     ├─ netherite_boots_netherite_trim.json
│  │     │     ├─ netherite_boots_quartz_trim.json
│  │     │     ├─ netherite_boots_redstone_trim.json
│  │     │     ├─ netherite_boots_resin_trim.json
│  │     │     ├─ netherite_chestplate.json
│  │     │     ├─ netherite_chestplate_amethyst_trim.json
│  │     │     ├─ netherite_chestplate_copper_trim.json
│  │     │     ├─ netherite_chestplate_diamond_trim.json
│  │     │     ├─ netherite_chestplate_emerald_trim.json
│  │     │     ├─ netherite_chestplate_gold_trim.json
│  │     │     ├─ netherite_chestplate_iron_trim.json
│  │     │     ├─ netherite_chestplate_lapis_trim.json
│  │     │     ├─ netherite_chestplate_netherite_trim.json
│  │     │     ├─ netherite_chestplate_quartz_trim.json
│  │     │     ├─ netherite_chestplate_redstone_trim.json
│  │     │     ├─ netherite_chestplate_resin_trim.json
│  │     │     ├─ netherite_helmet.json
│  │     │     ├─ netherite_helmet_amethyst_trim.json
│  │     │     ├─ netherite_helmet_copper_trim.json
│  │     │     ├─ netherite_helmet_diamond_trim.json
│  │     │     ├─ netherite_helmet_emerald_trim.json
│  │     │     ├─ netherite_helmet_gold_trim.json
│  │     │     ├─ netherite_helmet_iron_trim.json
│  │     │     ├─ netherite_helmet_lapis_trim.json
│  │     │     ├─ netherite_helmet_netherite_trim.json
│  │     │     ├─ netherite_helmet_quartz_trim.json
│  │     │     ├─ netherite_helmet_redstone_trim.json
│  │     │     ├─ netherite_helmet_resin_trim.json
│  │     │     ├─ netherite_hoe.json
│  │     │     ├─ netherite_horse_armor.json
│  │     │     ├─ netherite_ingot.json
│  │     │     ├─ netherite_leggings.json
│  │     │     ├─ netherite_leggings_amethyst_trim.json
│  │     │     ├─ netherite_leggings_copper_trim.json
│  │     │     ├─ netherite_leggings_diamond_trim.json
│  │     │     ├─ netherite_leggings_emerald_trim.json
│  │     │     ├─ netherite_leggings_gold_trim.json
│  │     │     ├─ netherite_leggings_iron_trim.json
│  │     │     ├─ netherite_leggings_lapis_trim.json
│  │     │     ├─ netherite_leggings_netherite_trim.json
│  │     │     ├─ netherite_leggings_quartz_trim.json
│  │     │     ├─ netherite_leggings_redstone_trim.json
│  │     │     ├─ netherite_leggings_resin_trim.json
│  │     │     ├─ netherite_nautilus_armor.json
│  │     │     ├─ netherite_pickaxe.json
│  │     │     ├─ netherite_scrap.json
│  │     │     ├─ netherite_shovel.json
│  │     │     ├─ netherite_spear.json
│  │     │     ├─ netherite_spear_in_hand.json
│  │     │     ├─ netherite_sword.json
│  │     │     ├─ netherite_upgrade_smithing_template.json
│  │     │     ├─ nether_brick.json
│  │     │     ├─ nether_sprouts.json
│  │     │     ├─ nether_star.json
│  │     │     ├─ nether_wart.json
│  │     │     ├─ oak_boat.json
│  │     │     ├─ oak_chest_boat.json
│  │     │     ├─ oak_door.json
│  │     │     ├─ oak_hanging_sign.json
│  │     │     ├─ oak_sapling.json
│  │     │     ├─ oak_sign.json
│  │     │     ├─ ocelot_spawn_egg.json
│  │     │     ├─ ominous_bottle.json
│  │     │     ├─ ominous_trial_key.json
│  │     │     ├─ open_eyeblossom.json
│  │     │     ├─ orange_bed.json
│  │     │     ├─ orange_bundle.json
│  │     │     ├─ orange_bundle_open_back.json
│  │     │     ├─ orange_bundle_open_front.json
│  │     │     ├─ orange_candle.json
│  │     │     ├─ orange_dye.json
│  │     │     ├─ orange_harness.json
│  │     │     ├─ orange_shulker_box.json
│  │     │     ├─ orange_stained_glass_pane.json
│  │     │     ├─ orange_tulip.json
│  │     │     ├─ oxeye_daisy.json
│  │     │     ├─ oxidized_copper_bars.json
│  │     │     ├─ oxidized_copper_chain.json
│  │     │     ├─ oxidized_copper_chest.json
│  │     │     ├─ oxidized_copper_door.json
│  │     │     ├─ oxidized_copper_lantern.json
│  │     │     ├─ painting.json
│  │     │     ├─ pale_hanging_moss.json
│  │     │     ├─ pale_oak_boat.json
│  │     │     ├─ pale_oak_chest_boat.json
│  │     │     ├─ pale_oak_door.json
│  │     │     ├─ pale_oak_hanging_sign.json
│  │     │     ├─ pale_oak_sapling.json
│  │     │     ├─ pale_oak_sign.json
│  │     │     ├─ panda_spawn_egg.json
│  │     │     ├─ paper.json
│  │     │     ├─ parched_spawn_egg.json
│  │     │     ├─ parrot_spawn_egg.json
│  │     │     ├─ peony.json
│  │     │     ├─ phantom_membrane.json
│  │     │     ├─ phantom_spawn_egg.json
│  │     │     ├─ piglin_banner_pattern.json
│  │     │     ├─ piglin_brute_spawn_egg.json
│  │     │     ├─ piglin_spawn_egg.json
│  │     │     ├─ pig_spawn_egg.json
│  │     │     ├─ pillager_spawn_egg.json
│  │     │     ├─ pink_bed.json
│  │     │     ├─ pink_bundle.json
│  │     │     ├─ pink_bundle_open_back.json
│  │     │     ├─ pink_bundle_open_front.json
│  │     │     ├─ pink_candle.json
│  │     │     ├─ pink_dye.json
│  │     │     ├─ pink_harness.json
│  │     │     ├─ pink_petals.json
│  │     │     ├─ pink_shulker_box.json
│  │     │     ├─ pink_stained_glass_pane.json
│  │     │     ├─ pink_tulip.json
│  │     │     ├─ pitcher_plant.json
│  │     │     ├─ pitcher_pod.json
│  │     │     ├─ plenty_pottery_sherd.json
│  │     │     ├─ pointed_dripstone.json
│  │     │     ├─ poisonous_potato.json
│  │     │     ├─ polar_bear_spawn_egg.json
│  │     │     ├─ popped_chorus_fruit.json
│  │     │     ├─ poppy.json
│  │     │     ├─ porkchop.json
│  │     │     ├─ potato.json
│  │     │     ├─ potion.json
│  │     │     ├─ powder_snow_bucket.json
│  │     │     ├─ powered_rail.json
│  │     │     ├─ prismarine_crystals.json
│  │     │     ├─ prismarine_shard.json
│  │     │     ├─ prize_pottery_sherd.json
│  │     │     ├─ pufferfish.json
│  │     │     ├─ pufferfish_bucket.json
│  │     │     ├─ pufferfish_spawn_egg.json
│  │     │     ├─ pumpkin_pie.json
│  │     │     ├─ pumpkin_seeds.json
│  │     │     ├─ purple_bed.json
│  │     │     ├─ purple_bundle.json
│  │     │     ├─ purple_bundle_open_back.json
│  │     │     ├─ purple_bundle_open_front.json
│  │     │     ├─ purple_candle.json
│  │     │     ├─ purple_dye.json
│  │     │     ├─ purple_harness.json
│  │     │     ├─ purple_shulker_box.json
│  │     │     ├─ purple_stained_glass_pane.json
│  │     │     ├─ quartz.json
│  │     │     ├─ rabbit.json
│  │     │     ├─ rabbit_foot.json
│  │     │     ├─ rabbit_hide.json
│  │     │     ├─ rabbit_spawn_egg.json
│  │     │     ├─ rabbit_stew.json
│  │     │     ├─ rail.json
│  │     │     ├─ raiser_armor_trim_smithing_template.json
│  │     │     ├─ ravager_spawn_egg.json
│  │     │     ├─ raw_copper.json
│  │     │     ├─ raw_gold.json
│  │     │     ├─ raw_iron.json
│  │     │     ├─ recovery_compass_00.json
│  │     │     ├─ recovery_compass_01.json
│  │     │     ├─ recovery_compass_02.json
│  │     │     ├─ recovery_compass_03.json
│  │     │     ├─ recovery_compass_04.json
│  │     │     ├─ recovery_compass_05.json
│  │     │     ├─ recovery_compass_06.json
│  │     │     ├─ recovery_compass_07.json
│  │     │     ├─ recovery_compass_08.json
│  │     │     ├─ recovery_compass_09.json
│  │     │     ├─ recovery_compass_10.json
│  │     │     ├─ recovery_compass_11.json
│  │     │     ├─ recovery_compass_12.json
│  │     │     ├─ recovery_compass_13.json
│  │     │     ├─ recovery_compass_14.json
│  │     │     ├─ recovery_compass_15.json
│  │     │     ├─ recovery_compass_16.json
│  │     │     ├─ recovery_compass_17.json
│  │     │     ├─ recovery_compass_18.json
│  │     │     ├─ recovery_compass_19.json
│  │     │     ├─ recovery_compass_20.json
│  │     │     ├─ recovery_compass_21.json
│  │     │     ├─ recovery_compass_22.json
│  │     │     ├─ recovery_compass_23.json
│  │     │     ├─ recovery_compass_24.json
│  │     │     ├─ recovery_compass_25.json
│  │     │     ├─ recovery_compass_26.json
│  │     │     ├─ recovery_compass_27.json
│  │     │     ├─ recovery_compass_28.json
│  │     │     ├─ recovery_compass_29.json
│  │     │     ├─ recovery_compass_30.json
│  │     │     ├─ recovery_compass_31.json
│  │     │     ├─ redstone.json
│  │     │     ├─ redstone_torch.json
│  │     │     ├─ red_bed.json
│  │     │     ├─ red_bundle.json
│  │     │     ├─ red_bundle_open_back.json
│  │     │     ├─ red_bundle_open_front.json
│  │     │     ├─ red_candle.json
│  │     │     ├─ red_dye.json
│  │     │     ├─ red_harness.json
│  │     │     ├─ red_mushroom.json
│  │     │     ├─ red_shulker_box.json
│  │     │     ├─ red_stained_glass_pane.json
│  │     │     ├─ red_tulip.json
│  │     │     ├─ repeater.json
│  │     │     ├─ resin_brick.json
│  │     │     ├─ resin_clump.json
│  │     │     ├─ rib_armor_trim_smithing_template.json
│  │     │     ├─ rose_bush.json
│  │     │     ├─ rotten_flesh.json
│  │     │     ├─ saddle.json
│  │     │     ├─ salmon.json
│  │     │     ├─ salmon_bucket.json
│  │     │     ├─ salmon_spawn_egg.json
│  │     │     ├─ scrape_pottery_sherd.json
│  │     │     ├─ sculk_vein.json
│  │     │     ├─ seagrass.json
│  │     │     ├─ sea_pickle.json
│  │     │     ├─ sentry_armor_trim_smithing_template.json
│  │     │     ├─ shaper_armor_trim_smithing_template.json
│  │     │     ├─ sheaf_pottery_sherd.json
│  │     │     ├─ shears.json
│  │     │     ├─ sheep_spawn_egg.json
│  │     │     ├─ shelter_pottery_sherd.json
│  │     │     ├─ shield.json
│  │     │     ├─ shield_blocking.json
│  │     │     ├─ short_dry_grass.json
│  │     │     ├─ short_grass.json
│  │     │     ├─ shulker_box.json
│  │     │     ├─ shulker_shell.json
│  │     │     ├─ shulker_spawn_egg.json
│  │     │     ├─ silence_armor_trim_smithing_template.json
│  │     │     ├─ silverfish_spawn_egg.json
│  │     │     ├─ skeleton_horse_spawn_egg.json
│  │     │     ├─ skeleton_spawn_egg.json
│  │     │     ├─ skull_banner_pattern.json
│  │     │     ├─ skull_pottery_sherd.json
│  │     │     ├─ slime_ball.json
│  │     │     ├─ slime_spawn_egg.json
│  │     │     ├─ small_amethyst_bud.json
│  │     │     ├─ small_dripleaf.json
│  │     │     ├─ sniffer_egg.json
│  │     │     ├─ sniffer_spawn_egg.json
│  │     │     ├─ snort_pottery_sherd.json
│  │     │     ├─ snout_armor_trim_smithing_template.json
│  │     │     ├─ snowball.json
│  │     │     ├─ snow_golem_spawn_egg.json
│  │     │     ├─ soul_campfire.json
│  │     │     ├─ soul_lantern.json
│  │     │     ├─ soul_torch.json
│  │     │     ├─ spear_in_hand.json
│  │     │     ├─ spectral_arrow.json
│  │     │     ├─ spider_eye.json
│  │     │     ├─ spider_spawn_egg.json
│  │     │     ├─ spire_armor_trim_smithing_template.json
│  │     │     ├─ splash_potion.json
│  │     │     ├─ spruce_boat.json
│  │     │     ├─ spruce_chest_boat.json
│  │     │     ├─ spruce_door.json
│  │     │     ├─ spruce_hanging_sign.json
│  │     │     ├─ spruce_sapling.json
│  │     │     ├─ spruce_sign.json
│  │     │     ├─ spyglass.json
│  │     │     ├─ spyglass_in_hand.json
│  │     │     ├─ squid_spawn_egg.json
│  │     │     ├─ stick.json
│  │     │     ├─ stone_axe.json
│  │     │     ├─ stone_hoe.json
│  │     │     ├─ stone_pickaxe.json
│  │     │     ├─ stone_shovel.json
│  │     │     ├─ stone_spear.json
│  │     │     ├─ stone_spear_in_hand.json
│  │     │     ├─ stone_sword.json
│  │     │     ├─ stray_spawn_egg.json
│  │     │     ├─ strider_spawn_egg.json
│  │     │     ├─ string.json
│  │     │     ├─ structure_void.json
│  │     │     ├─ sugar.json
│  │     │     ├─ sugar_cane.json
│  │     │     ├─ sunflower.json
│  │     │     ├─ suspicious_stew.json
│  │     │     ├─ sweet_berries.json
│  │     │     ├─ tadpole_bucket.json
│  │     │     ├─ tadpole_spawn_egg.json
│  │     │     ├─ tall_dry_grass.json
│  │     │     ├─ tall_grass.json
│  │     │     ├─ template_banner.json
│  │     │     ├─ template_bed.json
│  │     │     ├─ template_bundle_open_back.json
│  │     │     ├─ template_bundle_open_front.json
│  │     │     ├─ template_chest.json
│  │     │     ├─ template_copper_golem_statue.json
│  │     │     ├─ template_music_disc.json
│  │     │     ├─ template_shulker_box.json
│  │     │     ├─ template_skull.json
│  │     │     ├─ tide_armor_trim_smithing_template.json
│  │     │     ├─ tipped_arrow.json
│  │     │     ├─ tnt_minecart.json
│  │     │     ├─ tooting_goat_horn.json
│  │     │     ├─ torch.json
│  │     │     ├─ torchflower.json
│  │     │     ├─ torchflower_seeds.json
│  │     │     ├─ totem_of_undying.json
│  │     │     ├─ trader_llama_spawn_egg.json
│  │     │     ├─ trapped_chest.json
│  │     │     ├─ trial_key.json
│  │     │     ├─ trident.json
│  │     │     ├─ trident_in_hand.json
│  │     │     ├─ trident_throwing.json
│  │     │     ├─ tripwire_hook.json
│  │     │     ├─ tropical_fish.json
│  │     │     ├─ tropical_fish_bucket.json
│  │     │     ├─ tropical_fish_spawn_egg.json
│  │     │     ├─ tube_coral.json
│  │     │     ├─ tube_coral_fan.json
│  │     │     ├─ turtle_egg.json
│  │     │     ├─ turtle_helmet.json
│  │     │     ├─ turtle_helmet_amethyst_trim.json
│  │     │     ├─ turtle_helmet_copper_trim.json
│  │     │     ├─ turtle_helmet_diamond_trim.json
│  │     │     ├─ turtle_helmet_emerald_trim.json
│  │     │     ├─ turtle_helmet_gold_trim.json
│  │     │     ├─ turtle_helmet_iron_trim.json
│  │     │     ├─ turtle_helmet_lapis_trim.json
│  │     │     ├─ turtle_helmet_netherite_trim.json
│  │     │     ├─ turtle_helmet_quartz_trim.json
│  │     │     ├─ turtle_helmet_redstone_trim.json
│  │     │     ├─ turtle_helmet_resin_trim.json
│  │     │     ├─ turtle_scute.json
│  │     │     ├─ turtle_spawn_egg.json
│  │     │     ├─ twisting_vines.json
│  │     │     ├─ vex_armor_trim_smithing_template.json
│  │     │     ├─ vex_spawn_egg.json
│  │     │     ├─ villager_spawn_egg.json
│  │     │     ├─ vindicator_spawn_egg.json
│  │     │     ├─ vine.json
│  │     │     ├─ wandering_trader_spawn_egg.json
│  │     │     ├─ warden_spawn_egg.json
│  │     │     ├─ ward_armor_trim_smithing_template.json
│  │     │     ├─ warped_door.json
│  │     │     ├─ warped_fungus.json
│  │     │     ├─ warped_fungus_on_a_stick.json
│  │     │     ├─ warped_hanging_sign.json
│  │     │     ├─ warped_roots.json
│  │     │     ├─ warped_sign.json
│  │     │     ├─ water_bucket.json
│  │     │     ├─ wayfinder_armor_trim_smithing_template.json
│  │     │     ├─ weathered_copper_bars.json
│  │     │     ├─ weathered_copper_chain.json
│  │     │     ├─ weathered_copper_chest.json
│  │     │     ├─ weathered_copper_door.json
│  │     │     ├─ weathered_copper_lantern.json
│  │     │     ├─ weeping_vines.json
│  │     │     ├─ wheat.json
│  │     │     ├─ wheat_seeds.json
│  │     │     ├─ white_bed.json
│  │     │     ├─ white_bundle.json
│  │     │     ├─ white_bundle_open_back.json
│  │     │     ├─ white_bundle_open_front.json
│  │     │     ├─ white_candle.json
│  │     │     ├─ white_dye.json
│  │     │     ├─ white_harness.json
│  │     │     ├─ white_shulker_box.json
│  │     │     ├─ white_stained_glass_pane.json
│  │     │     ├─ white_tulip.json
│  │     │     ├─ wildflowers.json
│  │     │     ├─ wild_armor_trim_smithing_template.json
│  │     │     ├─ wind_charge.json
│  │     │     ├─ witch_spawn_egg.json
│  │     │     ├─ wither_rose.json
│  │     │     ├─ wither_skeleton_spawn_egg.json
│  │     │     ├─ wither_spawn_egg.json
│  │     │     ├─ wolf_armor.json
│  │     │     ├─ wolf_armor_dyed.json
│  │     │     ├─ wolf_spawn_egg.json
│  │     │     ├─ wooden_axe.json
│  │     │     ├─ wooden_hoe.json
│  │     │     ├─ wooden_pickaxe.json
│  │     │     ├─ wooden_shovel.json
│  │     │     ├─ wooden_spear.json
│  │     │     ├─ wooden_spear_in_hand.json
│  │     │     ├─ wooden_sword.json
│  │     │     ├─ writable_book.json
│  │     │     ├─ written_book.json
│  │     │     ├─ yellow_bed.json
│  │     │     ├─ yellow_bundle.json
│  │     │     ├─ yellow_bundle_open_back.json
│  │     │     ├─ yellow_bundle_open_front.json
│  │     │     ├─ yellow_candle.json
│  │     │     ├─ yellow_dye.json
│  │     │     ├─ yellow_harness.json
│  │     │     ├─ yellow_shulker_box.json
│  │     │     ├─ yellow_stained_glass_pane.json
│  │     │     ├─ zoglin_spawn_egg.json
│  │     │     ├─ zombie_horse_spawn_egg.json
│  │     │     ├─ zombie_nautilus_spawn_egg.json
│  │     │     ├─ zombie_spawn_egg.json
│  │     │     ├─ zombie_villager_spawn_egg.json
│  │     │     └─ zombified_piglin_spawn_egg.json
│  │     ├─ particles
│  │     │  ├─ ambient_entity_effect.json
│  │     │  ├─ angry_villager.json
│  │     │  ├─ ash.json
│  │     │  ├─ bubble.json
│  │     │  ├─ bubble_column_up.json
│  │     │  ├─ bubble_pop.json
│  │     │  ├─ campfire_cosy_smoke.json
│  │     │  ├─ campfire_signal_smoke.json
│  │     │  ├─ cherry_leaves.json
│  │     │  ├─ cloud.json
│  │     │  ├─ composter.json
│  │     │  ├─ copper_fire_flame.json
│  │     │  ├─ crimson_spore.json
│  │     │  ├─ crit.json
│  │     │  ├─ current_down.json
│  │     │  ├─ damage_indicator.json
│  │     │  ├─ dolphin.json
│  │     │  ├─ dragon_breath.json
│  │     │  ├─ dripping_dripstone_lava.json
│  │     │  ├─ dripping_dripstone_water.json
│  │     │  ├─ dripping_honey.json
│  │     │  ├─ dripping_lava.json
│  │     │  ├─ dripping_obsidian_tear.json
│  │     │  ├─ dripping_water.json
│  │     │  ├─ dust.json
│  │     │  ├─ dust_color_transition.json
│  │     │  ├─ dust_plume.json
│  │     │  ├─ effect.json
│  │     │  ├─ egg_crack.json
│  │     │  ├─ electric_spark.json
│  │     │  ├─ enchant.json
│  │     │  ├─ enchanted_hit.json
│  │     │  ├─ end_rod.json
│  │     │  ├─ entity_effect.json
│  │     │  ├─ explosion.json
│  │     │  ├─ falling_dripstone_lava.json
│  │     │  ├─ falling_dripstone_water.json
│  │     │  ├─ falling_dust.json
│  │     │  ├─ falling_honey.json
│  │     │  ├─ falling_lava.json
│  │     │  ├─ falling_nectar.json
│  │     │  ├─ falling_obsidian_tear.json
│  │     │  ├─ falling_spore_blossom.json
│  │     │  ├─ falling_water.json
│  │     │  ├─ firefly.json
│  │     │  ├─ firework.json
│  │     │  ├─ fishing.json
│  │     │  ├─ flame.json
│  │     │  ├─ flash.json
│  │     │  ├─ glow.json
│  │     │  ├─ glow_squid_ink.json
│  │     │  ├─ gust.json
│  │     │  ├─ happy_villager.json
│  │     │  ├─ heart.json
│  │     │  ├─ infested.json
│  │     │  ├─ instant_effect.json
│  │     │  ├─ landing_honey.json
│  │     │  ├─ landing_lava.json
│  │     │  ├─ landing_obsidian_tear.json
│  │     │  ├─ large_smoke.json
│  │     │  ├─ lava.json
│  │     │  ├─ mycelium.json
│  │     │  ├─ nautilus.json
│  │     │  ├─ note.json
│  │     │  ├─ ominous_spawning.json
│  │     │  ├─ pale_oak_leaves.json
│  │     │  ├─ poof.json
│  │     │  ├─ portal.json
│  │     │  ├─ raid_omen.json
│  │     │  ├─ rain.json
│  │     │  ├─ reverse_portal.json
│  │     │  ├─ scrape.json
│  │     │  ├─ sculk_charge.json
│  │     │  ├─ sculk_charge_pop.json
│  │     │  ├─ sculk_soul.json
│  │     │  ├─ shriek.json
│  │     │  ├─ small_flame.json
│  │     │  ├─ small_gust.json
│  │     │  ├─ smoke.json
│  │     │  ├─ sneeze.json
│  │     │  ├─ snowflake.json
│  │     │  ├─ sonic_boom.json
│  │     │  ├─ soul.json
│  │     │  ├─ soul_fire_flame.json
│  │     │  ├─ spit.json
│  │     │  ├─ splash.json
│  │     │  ├─ spore_blossom_air.json
│  │     │  ├─ squid_ink.json
│  │     │  ├─ sweep_attack.json
│  │     │  ├─ tinted_leaves.json
│  │     │  ├─ totem_of_undying.json
│  │     │  ├─ trail.json
│  │     │  ├─ trial_omen.json
│  │     │  ├─ trial_spawner_detection.json
│  │     │  ├─ trial_spawner_detection_ominous.json
│  │     │  ├─ underwater.json
│  │     │  ├─ vault_connection.json
│  │     │  ├─ vibration.json
│  │     │  ├─ warped_spore.json
│  │     │  ├─ wax_off.json
│  │     │  ├─ wax_on.json
│  │     │  ├─ white_ash.json
│  │     │  ├─ white_smoke.json
│  │     │  └─ witch.json
│  │     ├─ post_effect
│  │     │  ├─ blur.json
│  │     │  ├─ creeper.json
│  │     │  ├─ entity_outline.json
│  │     │  ├─ invert.json
│  │     │  ├─ spider.json
│  │     │  └─ transparency.json
│  │     ├─ regional_compliancies.json
│  │     ├─ shaders
│  │     │  ├─ core
│  │     │  │  ├─ animate_sprite.vsh
│  │     │  │  ├─ animate_sprite_blit.fsh
│  │     │  │  ├─ animate_sprite_interpolate.fsh
│  │     │  │  ├─ blit_screen.fsh
│  │     │  │  ├─ block.fsh
│  │     │  │  ├─ block.vsh
│  │     │  │  ├─ debug_point.vsh
│  │     │  │  ├─ entity.fsh
│  │     │  │  ├─ entity.vsh
│  │     │  │  ├─ glint.fsh
│  │     │  │  ├─ glint.vsh
│  │     │  │  ├─ gui.fsh
│  │     │  │  ├─ gui.vsh
│  │     │  │  ├─ lightmap.fsh
│  │     │  │  ├─ panorama.fsh
│  │     │  │  ├─ panorama.vsh
│  │     │  │  ├─ particle.fsh
│  │     │  │  ├─ particle.vsh
│  │     │  │  ├─ position.fsh
│  │     │  │  ├─ position.vsh
│  │     │  │  ├─ position_color.fsh
│  │     │  │  ├─ position_color.vsh
│  │     │  │  ├─ position_tex.fsh
│  │     │  │  ├─ position_tex.vsh
│  │     │  │  ├─ position_tex_color.fsh
│  │     │  │  ├─ position_tex_color.vsh
│  │     │  │  ├─ rendertype_beacon_beam.fsh
│  │     │  │  ├─ rendertype_beacon_beam.vsh
│  │     │  │  ├─ rendertype_clouds.fsh
│  │     │  │  ├─ rendertype_clouds.vsh
│  │     │  │  ├─ rendertype_crumbling.fsh
│  │     │  │  ├─ rendertype_crumbling.vsh
│  │     │  │  ├─ rendertype_end_portal.fsh
│  │     │  │  ├─ rendertype_end_portal.vsh
│  │     │  │  ├─ rendertype_entity_alpha.fsh
│  │     │  │  ├─ rendertype_entity_alpha.vsh
│  │     │  │  ├─ rendertype_entity_decal.fsh
│  │     │  │  ├─ rendertype_entity_decal.vsh
│  │     │  │  ├─ rendertype_entity_shadow.fsh
│  │     │  │  ├─ rendertype_entity_shadow.vsh
│  │     │  │  ├─ rendertype_item_entity_translucent_cull.fsh
│  │     │  │  ├─ rendertype_item_entity_translucent_cull.vsh
│  │     │  │  ├─ rendertype_leash.fsh
│  │     │  │  ├─ rendertype_leash.vsh
│  │     │  │  ├─ rendertype_lightning.fsh
│  │     │  │  ├─ rendertype_lightning.vsh
│  │     │  │  ├─ rendertype_lines.fsh
│  │     │  │  ├─ rendertype_lines.vsh
│  │     │  │  ├─ rendertype_outline.fsh
│  │     │  │  ├─ rendertype_outline.vsh
│  │     │  │  ├─ rendertype_text.fsh
│  │     │  │  ├─ rendertype_text.vsh
│  │     │  │  ├─ rendertype_text_background.fsh
│  │     │  │  ├─ rendertype_text_background.vsh
│  │     │  │  ├─ rendertype_text_background_see_through.fsh
│  │     │  │  ├─ rendertype_text_background_see_through.vsh
│  │     │  │  ├─ rendertype_text_intensity.fsh
│  │     │  │  ├─ rendertype_text_intensity.vsh
│  │     │  │  ├─ rendertype_text_intensity_see_through.fsh
│  │     │  │  ├─ rendertype_text_intensity_see_through.vsh
│  │     │  │  ├─ rendertype_text_see_through.fsh
│  │     │  │  ├─ rendertype_text_see_through.vsh
│  │     │  │  ├─ rendertype_translucent_moving_block.fsh
│  │     │  │  ├─ rendertype_translucent_moving_block.vsh
│  │     │  │  ├─ rendertype_water_mask.fsh
│  │     │  │  ├─ rendertype_water_mask.vsh
│  │     │  │  ├─ rendertype_world_border.fsh
│  │     │  │  ├─ rendertype_world_border.vsh
│  │     │  │  ├─ screenquad.vsh
│  │     │  │  ├─ sky.fsh
│  │     │  │  ├─ sky.vsh
│  │     │  │  ├─ stars.fsh
│  │     │  │  ├─ stars.vsh
│  │     │  │  ├─ terrain.fsh
│  │     │  │  └─ terrain.vsh
│  │     │  ├─ include
│  │     │  │  ├─ animation_sprite.glsl
│  │     │  │  ├─ chunksection.glsl
│  │     │  │  ├─ dynamictransforms.glsl
│  │     │  │  ├─ fog.glsl
│  │     │  │  ├─ globals.glsl
│  │     │  │  ├─ light.glsl
│  │     │  │  ├─ matrix.glsl
│  │     │  │  └─ projection.glsl
│  │     │  └─ post
│  │     │     ├─ bits.fsh
│  │     │     ├─ blit.fsh
│  │     │     ├─ box_blur.fsh
│  │     │     ├─ color_convolve.fsh
│  │     │     ├─ entity_outline_box_blur.fsh
│  │     │     ├─ entity_sobel.fsh
│  │     │     ├─ invert.fsh
│  │     │     ├─ rotscale.vsh
│  │     │     ├─ spiderclip.fsh
│  │     │     └─ transparency.fsh
│  │     ├─ texts
│  │     │  ├─ credits.json
│  │     │  ├─ end.txt
│  │     │  ├─ postcredits.txt
│  │     │  └─ splashes.txt
│  │     ├─ textures
│  │     │  ├─ block
│  │     │  │  ├─ acacia_door_bottom.png
│  │     │  │  ├─ acacia_door_top.png
│  │     │  │  ├─ acacia_leaves.png
│  │     │  │  ├─ acacia_leaves.png.mcmeta
│  │     │  │  ├─ acacia_log.png
│  │     │  │  ├─ acacia_log_top.png
│  │     │  │  ├─ acacia_planks.png
│  │     │  │  ├─ acacia_sapling.png
│  │     │  │  ├─ acacia_shelf.png
│  │     │  │  ├─ acacia_trapdoor.png
│  │     │  │  ├─ activator_rail.png
│  │     │  │  ├─ activator_rail_on.png
│  │     │  │  ├─ allium.png
│  │     │  │  ├─ allium.png.mcmeta
│  │     │  │  ├─ amethyst_block.png
│  │     │  │  ├─ amethyst_cluster.png
│  │     │  │  ├─ amethyst_cluster.png.mcmeta
│  │     │  │  ├─ ancient_debris_side.png
│  │     │  │  ├─ ancient_debris_top.png
│  │     │  │  ├─ andesite.png
│  │     │  │  ├─ anvil.png
│  │     │  │  ├─ anvil_top.png
│  │     │  │  ├─ attached_melon_stem.png
│  │     │  │  ├─ attached_pumpkin_stem.png
│  │     │  │  ├─ azalea_leaves.png
│  │     │  │  ├─ azalea_leaves.png.mcmeta
│  │     │  │  ├─ azalea_plant.png
│  │     │  │  ├─ azalea_side.png
│  │     │  │  ├─ azalea_top.png
│  │     │  │  ├─ azure_bluet.png
│  │     │  │  ├─ azure_bluet.png.mcmeta
│  │     │  │  ├─ bamboo_block.png
│  │     │  │  ├─ bamboo_block_top.png
│  │     │  │  ├─ bamboo_door_bottom.png
│  │     │  │  ├─ bamboo_door_top.png
│  │     │  │  ├─ bamboo_fence.png
│  │     │  │  ├─ bamboo_fence_gate.png
│  │     │  │  ├─ bamboo_fence_gate_particle.png
│  │     │  │  ├─ bamboo_fence_particle.png
│  │     │  │  ├─ bamboo_large_leaves.png
│  │     │  │  ├─ bamboo_mosaic.png
│  │     │  │  ├─ bamboo_planks.png
│  │     │  │  ├─ bamboo_shelf.png
│  │     │  │  ├─ bamboo_singleleaf.png
│  │     │  │  ├─ bamboo_small_leaves.png
│  │     │  │  ├─ bamboo_stage0.png
│  │     │  │  ├─ bamboo_stalk.png
│  │     │  │  ├─ bamboo_trapdoor.png
│  │     │  │  ├─ barrel_bottom.png
│  │     │  │  ├─ barrel_side.png
│  │     │  │  ├─ barrel_top.png
│  │     │  │  ├─ barrel_top_open.png
│  │     │  │  ├─ basalt_side.png
│  │     │  │  ├─ basalt_top.png
│  │     │  │  ├─ beacon.png
│  │     │  │  ├─ bedrock.png
│  │     │  │  ├─ beehive_end.png
│  │     │  │  ├─ beehive_front.png
│  │     │  │  ├─ beehive_front_honey.png
│  │     │  │  ├─ beehive_side.png
│  │     │  │  ├─ beetroots_stage0.png
│  │     │  │  ├─ beetroots_stage1.png
│  │     │  │  ├─ beetroots_stage2.png
│  │     │  │  ├─ beetroots_stage3.png
│  │     │  │  ├─ bee_nest_bottom.png
│  │     │  │  ├─ bee_nest_front.png
│  │     │  │  ├─ bee_nest_front_honey.png
│  │     │  │  ├─ bee_nest_side.png
│  │     │  │  ├─ bee_nest_top.png
│  │     │  │  ├─ bell_bottom.png
│  │     │  │  ├─ bell_side.png
│  │     │  │  ├─ bell_top.png
│  │     │  │  ├─ big_dripleaf_side.png
│  │     │  │  ├─ big_dripleaf_stem.png
│  │     │  │  ├─ big_dripleaf_tip.png
│  │     │  │  ├─ big_dripleaf_top.png
│  │     │  │  ├─ birch_door_bottom.png
│  │     │  │  ├─ birch_door_top.png
│  │     │  │  ├─ birch_leaves.png
│  │     │  │  ├─ birch_leaves.png.mcmeta
│  │     │  │  ├─ birch_log.png
│  │     │  │  ├─ birch_log_top.png
│  │     │  │  ├─ birch_planks.png
│  │     │  │  ├─ birch_sapling.png
│  │     │  │  ├─ birch_shelf.png
│  │     │  │  ├─ birch_trapdoor.png
│  │     │  │  ├─ blackstone.png
│  │     │  │  ├─ blackstone_top.png
│  │     │  │  ├─ black_candle.png
│  │     │  │  ├─ black_candle_lit.png
│  │     │  │  ├─ black_concrete.png
│  │     │  │  ├─ black_concrete_powder.png
│  │     │  │  ├─ black_glazed_terracotta.png
│  │     │  │  ├─ black_shulker_box.png
│  │     │  │  ├─ black_stained_glass.png
│  │     │  │  ├─ black_stained_glass_pane_top.png
│  │     │  │  ├─ black_terracotta.png
│  │     │  │  ├─ black_wool.png
│  │     │  │  ├─ blast_furnace_front.png
│  │     │  │  ├─ blast_furnace_front_on.png
│  │     │  │  ├─ blast_furnace_front_on.png.mcmeta
│  │     │  │  ├─ blast_furnace_side.png
│  │     │  │  ├─ blast_furnace_top.png
│  │     │  │  ├─ blue_candle.png
│  │     │  │  ├─ blue_candle_lit.png
│  │     │  │  ├─ blue_concrete.png
│  │     │  │  ├─ blue_concrete_powder.png
│  │     │  │  ├─ blue_glazed_terracotta.png
│  │     │  │  ├─ blue_ice.png
│  │     │  │  ├─ blue_orchid.png
│  │     │  │  ├─ blue_orchid.png.mcmeta
│  │     │  │  ├─ blue_shulker_box.png
│  │     │  │  ├─ blue_stained_glass.png
│  │     │  │  ├─ blue_stained_glass_pane_top.png
│  │     │  │  ├─ blue_terracotta.png
│  │     │  │  ├─ blue_wool.png
│  │     │  │  ├─ bone_block_side.png
│  │     │  │  ├─ bone_block_top.png
│  │     │  │  ├─ bookshelf.png
│  │     │  │  ├─ brain_coral.png
│  │     │  │  ├─ brain_coral_block.png
│  │     │  │  ├─ brain_coral_fan.png
│  │     │  │  ├─ brewing_stand.png
│  │     │  │  ├─ brewing_stand_base.png
│  │     │  │  ├─ bricks.png
│  │     │  │  ├─ brown_candle.png
│  │     │  │  ├─ brown_candle_lit.png
│  │     │  │  ├─ brown_concrete.png
│  │     │  │  ├─ brown_concrete_powder.png
│  │     │  │  ├─ brown_glazed_terracotta.png
│  │     │  │  ├─ brown_mushroom.png
│  │     │  │  ├─ brown_mushroom.png.mcmeta
│  │     │  │  ├─ brown_mushroom_block.png
│  │     │  │  ├─ brown_shulker_box.png
│  │     │  │  ├─ brown_stained_glass.png
│  │     │  │  ├─ brown_stained_glass_pane_top.png
│  │     │  │  ├─ brown_terracotta.png
│  │     │  │  ├─ brown_wool.png
│  │     │  │  ├─ bubble_coral.png
│  │     │  │  ├─ bubble_coral_block.png
│  │     │  │  ├─ bubble_coral_fan.png
│  │     │  │  ├─ budding_amethyst.png
│  │     │  │  ├─ bush.png
│  │     │  │  ├─ cactus_bottom.png
│  │     │  │  ├─ cactus_flower.png
│  │     │  │  ├─ cactus_flower.png.mcmeta
│  │     │  │  ├─ cactus_side.png
│  │     │  │  ├─ cactus_top.png
│  │     │  │  ├─ cake_bottom.png
│  │     │  │  ├─ cake_inner.png
│  │     │  │  ├─ cake_side.png
│  │     │  │  ├─ cake_top.png
│  │     │  │  ├─ calcite.png
│  │     │  │  ├─ calibrated_sculk_sensor_amethyst.png
│  │     │  │  ├─ calibrated_sculk_sensor_input_side.png
│  │     │  │  ├─ calibrated_sculk_sensor_top.png
│  │     │  │  ├─ campfire_fire.png
│  │     │  │  ├─ campfire_fire.png.mcmeta
│  │     │  │  ├─ campfire_log.png
│  │     │  │  ├─ campfire_log_lit.png
│  │     │  │  ├─ campfire_log_lit.png.mcmeta
│  │     │  │  ├─ candle.png
│  │     │  │  ├─ candle_lit.png
│  │     │  │  ├─ carrots_stage0.png
│  │     │  │  ├─ carrots_stage1.png
│  │     │  │  ├─ carrots_stage2.png
│  │     │  │  ├─ carrots_stage3.png
│  │     │  │  ├─ cartography_table_side1.png
│  │     │  │  ├─ cartography_table_side2.png
│  │     │  │  ├─ cartography_table_side3.png
│  │     │  │  ├─ cartography_table_top.png
│  │     │  │  ├─ carved_pumpkin.png
│  │     │  │  ├─ cauldron_bottom.png
│  │     │  │  ├─ cauldron_inner.png
│  │     │  │  ├─ cauldron_side.png
│  │     │  │  ├─ cauldron_top.png
│  │     │  │  ├─ cave_vines.png
│  │     │  │  ├─ cave_vines_lit.png
│  │     │  │  ├─ cave_vines_plant.png
│  │     │  │  ├─ cave_vines_plant_lit.png
│  │     │  │  ├─ chain_command_block_back.png
│  │     │  │  ├─ chain_command_block_back.png.mcmeta
│  │     │  │  ├─ chain_command_block_conditional.png
│  │     │  │  ├─ chain_command_block_conditional.png.mcmeta
│  │     │  │  ├─ chain_command_block_front.png
│  │     │  │  ├─ chain_command_block_front.png.mcmeta
│  │     │  │  ├─ chain_command_block_side.png
│  │     │  │  ├─ chain_command_block_side.png.mcmeta
│  │     │  │  ├─ cherry_door_bottom.png
│  │     │  │  ├─ cherry_door_top.png
│  │     │  │  ├─ cherry_leaves.png
│  │     │  │  ├─ cherry_leaves.png.mcmeta
│  │     │  │  ├─ cherry_log.png
│  │     │  │  ├─ cherry_log_top.png
│  │     │  │  ├─ cherry_planks.png
│  │     │  │  ├─ cherry_sapling.png
│  │     │  │  ├─ cherry_shelf.png
│  │     │  │  ├─ cherry_trapdoor.png
│  │     │  │  ├─ chipped_anvil_top.png
│  │     │  │  ├─ chiseled_bookshelf_empty.png
│  │     │  │  ├─ chiseled_bookshelf_occupied.png
│  │     │  │  ├─ chiseled_bookshelf_side.png
│  │     │  │  ├─ chiseled_bookshelf_top.png
│  │     │  │  ├─ chiseled_copper.png
│  │     │  │  ├─ chiseled_deepslate.png
│  │     │  │  ├─ chiseled_nether_bricks.png
│  │     │  │  ├─ chiseled_polished_blackstone.png
│  │     │  │  ├─ chiseled_quartz_block.png
│  │     │  │  ├─ chiseled_quartz_block_top.png
│  │     │  │  ├─ chiseled_red_sandstone.png
│  │     │  │  ├─ chiseled_resin_bricks.png
│  │     │  │  ├─ chiseled_sandstone.png
│  │     │  │  ├─ chiseled_stone_bricks.png
│  │     │  │  ├─ chiseled_tuff.png
│  │     │  │  ├─ chiseled_tuff_bricks.png
│  │     │  │  ├─ chiseled_tuff_bricks_top.png
│  │     │  │  ├─ chiseled_tuff_top.png
│  │     │  │  ├─ chorus_flower.png
│  │     │  │  ├─ chorus_flower_dead.png
│  │     │  │  ├─ chorus_plant.png
│  │     │  │  ├─ clay.png
│  │     │  │  ├─ closed_eyeblossom.png
│  │     │  │  ├─ closed_eyeblossom.png.mcmeta
│  │     │  │  ├─ coal_block.png
│  │     │  │  ├─ coal_ore.png
│  │     │  │  ├─ coarse_dirt.png
│  │     │  │  ├─ cobbled_deepslate.png
│  │     │  │  ├─ cobblestone.png
│  │     │  │  ├─ cobweb.png
│  │     │  │  ├─ cocoa_stage0.png
│  │     │  │  ├─ cocoa_stage1.png
│  │     │  │  ├─ cocoa_stage2.png
│  │     │  │  ├─ command_block_back.png
│  │     │  │  ├─ command_block_back.png.mcmeta
│  │     │  │  ├─ command_block_conditional.png
│  │     │  │  ├─ command_block_conditional.png.mcmeta
│  │     │  │  ├─ command_block_front.png
│  │     │  │  ├─ command_block_front.png.mcmeta
│  │     │  │  ├─ command_block_side.png
│  │     │  │  ├─ command_block_side.png.mcmeta
│  │     │  │  ├─ comparator.png
│  │     │  │  ├─ comparator_on.png
│  │     │  │  ├─ composter_bottom.png
│  │     │  │  ├─ composter_compost.png
│  │     │  │  ├─ composter_ready.png
│  │     │  │  ├─ composter_side.png
│  │     │  │  ├─ composter_top.png
│  │     │  │  ├─ conduit.png
│  │     │  │  ├─ copper_bars.png
│  │     │  │  ├─ copper_block.png
│  │     │  │  ├─ copper_bulb.png
│  │     │  │  ├─ copper_bulb_lit.png
│  │     │  │  ├─ copper_bulb_lit_powered.png
│  │     │  │  ├─ copper_bulb_powered.png
│  │     │  │  ├─ copper_chain.png
│  │     │  │  ├─ copper_door_bottom.png
│  │     │  │  ├─ copper_door_top.png
│  │     │  │  ├─ copper_grate.png
│  │     │  │  ├─ copper_lantern.png
│  │     │  │  ├─ copper_lantern.png.mcmeta
│  │     │  │  ├─ copper_ore.png
│  │     │  │  ├─ copper_torch.png
│  │     │  │  ├─ copper_trapdoor.png
│  │     │  │  ├─ cornflower.png
│  │     │  │  ├─ cornflower.png.mcmeta
│  │     │  │  ├─ cracked_deepslate_bricks.png
│  │     │  │  ├─ cracked_deepslate_tiles.png
│  │     │  │  ├─ cracked_nether_bricks.png
│  │     │  │  ├─ cracked_polished_blackstone_bricks.png
│  │     │  │  ├─ cracked_stone_bricks.png
│  │     │  │  ├─ crafter_bottom.png
│  │     │  │  ├─ crafter_east.png
│  │     │  │  ├─ crafter_east_crafting.png
│  │     │  │  ├─ crafter_east_triggered.png
│  │     │  │  ├─ crafter_north.png
│  │     │  │  ├─ crafter_north_crafting.png
│  │     │  │  ├─ crafter_south.png
│  │     │  │  ├─ crafter_south_triggered.png
│  │     │  │  ├─ crafter_top.png
│  │     │  │  ├─ crafter_top_crafting.png
│  │     │  │  ├─ crafter_top_triggered.png
│  │     │  │  ├─ crafter_west.png
│  │     │  │  ├─ crafter_west_crafting.png
│  │     │  │  ├─ crafter_west_triggered.png
│  │     │  │  ├─ crafting_table_front.png
│  │     │  │  ├─ crafting_table_side.png
│  │     │  │  ├─ crafting_table_top.png
│  │     │  │  ├─ creaking_heart.png
│  │     │  │  ├─ creaking_heart_awake.png
│  │     │  │  ├─ creaking_heart_dormant.png
│  │     │  │  ├─ creaking_heart_top.png
│  │     │  │  ├─ creaking_heart_top_awake.png
│  │     │  │  ├─ creaking_heart_top_dormant.png
│  │     │  │  ├─ crimson_door_bottom.png
│  │     │  │  ├─ crimson_door_top.png
│  │     │  │  ├─ crimson_fungus.png
│  │     │  │  ├─ crimson_fungus.png.mcmeta
│  │     │  │  ├─ crimson_nylium.png
│  │     │  │  ├─ crimson_nylium_side.png
│  │     │  │  ├─ crimson_planks.png
│  │     │  │  ├─ crimson_roots.png
│  │     │  │  ├─ crimson_roots_pot.png
│  │     │  │  ├─ crimson_shelf.png
│  │     │  │  ├─ crimson_stem.png
│  │     │  │  ├─ crimson_stem.png.mcmeta
│  │     │  │  ├─ crimson_stem_top.png
│  │     │  │  ├─ crimson_trapdoor.png
│  │     │  │  ├─ crying_obsidian.png
│  │     │  │  ├─ cut_copper.png
│  │     │  │  ├─ cut_red_sandstone.png
│  │     │  │  ├─ cut_sandstone.png
│  │     │  │  ├─ cyan_candle.png
│  │     │  │  ├─ cyan_candle_lit.png
│  │     │  │  ├─ cyan_concrete.png
│  │     │  │  ├─ cyan_concrete_powder.png
│  │     │  │  ├─ cyan_glazed_terracotta.png
│  │     │  │  ├─ cyan_shulker_box.png
│  │     │  │  ├─ cyan_stained_glass.png
│  │     │  │  ├─ cyan_stained_glass_pane_top.png
│  │     │  │  ├─ cyan_terracotta.png
│  │     │  │  ├─ cyan_wool.png
│  │     │  │  ├─ damaged_anvil_top.png
│  │     │  │  ├─ dandelion.png
│  │     │  │  ├─ dandelion.png.mcmeta
│  │     │  │  ├─ dark_oak_door_bottom.png
│  │     │  │  ├─ dark_oak_door_top.png
│  │     │  │  ├─ dark_oak_leaves.png
│  │     │  │  ├─ dark_oak_leaves.png.mcmeta
│  │     │  │  ├─ dark_oak_log.png
│  │     │  │  ├─ dark_oak_log_top.png
│  │     │  │  ├─ dark_oak_planks.png
│  │     │  │  ├─ dark_oak_sapling.png
│  │     │  │  ├─ dark_oak_shelf.png
│  │     │  │  ├─ dark_oak_trapdoor.png
│  │     │  │  ├─ dark_prismarine.png
│  │     │  │  ├─ daylight_detector_inverted_top.png
│  │     │  │  ├─ daylight_detector_side.png
│  │     │  │  ├─ daylight_detector_top.png
│  │     │  │  ├─ dead_brain_coral.png
│  │     │  │  ├─ dead_brain_coral_block.png
│  │     │  │  ├─ dead_brain_coral_fan.png
│  │     │  │  ├─ dead_bubble_coral.png
│  │     │  │  ├─ dead_bubble_coral_block.png
│  │     │  │  ├─ dead_bubble_coral_fan.png
│  │     │  │  ├─ dead_bush.png
│  │     │  │  ├─ dead_fire_coral.png
│  │     │  │  ├─ dead_fire_coral_block.png
│  │     │  │  ├─ dead_fire_coral_fan.png
│  │     │  │  ├─ dead_horn_coral.png
│  │     │  │  ├─ dead_horn_coral_block.png
│  │     │  │  ├─ dead_horn_coral_fan.png
│  │     │  │  ├─ dead_tube_coral.png
│  │     │  │  ├─ dead_tube_coral_block.png
│  │     │  │  ├─ dead_tube_coral_fan.png
│  │     │  │  ├─ debug.png
│  │     │  │  ├─ debug2.png
│  │     │  │  ├─ deepslate.png
│  │     │  │  ├─ deepslate_bricks.png
│  │     │  │  ├─ deepslate_coal_ore.png
│  │     │  │  ├─ deepslate_copper_ore.png
│  │     │  │  ├─ deepslate_diamond_ore.png
│  │     │  │  ├─ deepslate_emerald_ore.png
│  │     │  │  ├─ deepslate_gold_ore.png
│  │     │  │  ├─ deepslate_iron_ore.png
│  │     │  │  ├─ deepslate_lapis_ore.png
│  │     │  │  ├─ deepslate_redstone_ore.png
│  │     │  │  ├─ deepslate_tiles.png
│  │     │  │  ├─ deepslate_top.png
│  │     │  │  ├─ destroy_stage_0.png
│  │     │  │  ├─ destroy_stage_1.png
│  │     │  │  ├─ destroy_stage_2.png
│  │     │  │  ├─ destroy_stage_3.png
│  │     │  │  ├─ destroy_stage_4.png
│  │     │  │  ├─ destroy_stage_5.png
│  │     │  │  ├─ destroy_stage_6.png
│  │     │  │  ├─ destroy_stage_7.png
│  │     │  │  ├─ destroy_stage_8.png
│  │     │  │  ├─ destroy_stage_9.png
│  │     │  │  ├─ detector_rail.png
│  │     │  │  ├─ detector_rail_on.png
│  │     │  │  ├─ diamond_block.png
│  │     │  │  ├─ diamond_ore.png
│  │     │  │  ├─ diorite.png
│  │     │  │  ├─ dirt.png
│  │     │  │  ├─ dirt_path_side.png
│  │     │  │  ├─ dirt_path_top.png
│  │     │  │  ├─ dispenser_front.png
│  │     │  │  ├─ dispenser_front_vertical.png
│  │     │  │  ├─ dragon_egg.png
│  │     │  │  ├─ dried_ghast_hydration_0_bottom.png
│  │     │  │  ├─ dried_ghast_hydration_0_east.png
│  │     │  │  ├─ dried_ghast_hydration_0_north.png
│  │     │  │  ├─ dried_ghast_hydration_0_south.png
│  │     │  │  ├─ dried_ghast_hydration_0_tentacles.png
│  │     │  │  ├─ dried_ghast_hydration_0_top.png
│  │     │  │  ├─ dried_ghast_hydration_0_west.png
│  │     │  │  ├─ dried_ghast_hydration_1_bottom.png
│  │     │  │  ├─ dried_ghast_hydration_1_east.png
│  │     │  │  ├─ dried_ghast_hydration_1_north.png
│  │     │  │  ├─ dried_ghast_hydration_1_south.png
│  │     │  │  ├─ dried_ghast_hydration_1_tentacles.png
│  │     │  │  ├─ dried_ghast_hydration_1_top.png
│  │     │  │  ├─ dried_ghast_hydration_1_west.png
│  │     │  │  ├─ dried_ghast_hydration_2_bottom.png
│  │     │  │  ├─ dried_ghast_hydration_2_east.png
│  │     │  │  ├─ dried_ghast_hydration_2_north.png
│  │     │  │  ├─ dried_ghast_hydration_2_south.png
│  │     │  │  ├─ dried_ghast_hydration_2_tentacles.png
│  │     │  │  ├─ dried_ghast_hydration_2_top.png
│  │     │  │  ├─ dried_ghast_hydration_2_west.png
│  │     │  │  ├─ dried_ghast_hydration_3_bottom.png
│  │     │  │  ├─ dried_ghast_hydration_3_east.png
│  │     │  │  ├─ dried_ghast_hydration_3_north.png
│  │     │  │  ├─ dried_ghast_hydration_3_south.png
│  │     │  │  ├─ dried_ghast_hydration_3_tentacles.png
│  │     │  │  ├─ dried_ghast_hydration_3_top.png
│  │     │  │  ├─ dried_ghast_hydration_3_west.png
│  │     │  │  ├─ dried_kelp_bottom.png
│  │     │  │  ├─ dried_kelp_side.png
│  │     │  │  ├─ dried_kelp_top.png
│  │     │  │  ├─ dripstone_block.png
│  │     │  │  ├─ dropper_front.png
│  │     │  │  ├─ dropper_front_vertical.png
│  │     │  │  ├─ emerald_block.png
│  │     │  │  ├─ emerald_ore.png
│  │     │  │  ├─ enchanting_table_bottom.png
│  │     │  │  ├─ enchanting_table_side.png
│  │     │  │  ├─ enchanting_table_top.png
│  │     │  │  ├─ end_portal_frame_eye.png
│  │     │  │  ├─ end_portal_frame_side.png
│  │     │  │  ├─ end_portal_frame_top.png
│  │     │  │  ├─ end_rod.png
│  │     │  │  ├─ end_stone.png
│  │     │  │  ├─ end_stone_bricks.png
│  │     │  │  ├─ exposed_chiseled_copper.png
│  │     │  │  ├─ exposed_copper.png
│  │     │  │  ├─ exposed_copper_bars.png
│  │     │  │  ├─ exposed_copper_bulb.png
│  │     │  │  ├─ exposed_copper_bulb_lit.png
│  │     │  │  ├─ exposed_copper_bulb_lit_powered.png
│  │     │  │  ├─ exposed_copper_bulb_powered.png
│  │     │  │  ├─ exposed_copper_chain.png
│  │     │  │  ├─ exposed_copper_door_bottom.png
│  │     │  │  ├─ exposed_copper_door_top.png
│  │     │  │  ├─ exposed_copper_grate.png
│  │     │  │  ├─ exposed_copper_lantern.png
│  │     │  │  ├─ exposed_copper_lantern.png.mcmeta
│  │     │  │  ├─ exposed_copper_trapdoor.png
│  │     │  │  ├─ exposed_cut_copper.png
│  │     │  │  ├─ exposed_lightning_rod.png
│  │     │  │  ├─ farmland.png
│  │     │  │  ├─ farmland_moist.png
│  │     │  │  ├─ fern.png
│  │     │  │  ├─ firefly_bush.png
│  │     │  │  ├─ firefly_bush_emissive.png
│  │     │  │  ├─ firefly_bush_emissive.png.mcmeta
│  │     │  │  ├─ fire_0.png
│  │     │  │  ├─ fire_0.png.mcmeta
│  │     │  │  ├─ fire_1.png
│  │     │  │  ├─ fire_1.png.mcmeta
│  │     │  │  ├─ fire_coral.png
│  │     │  │  ├─ fire_coral_block.png
│  │     │  │  ├─ fire_coral_fan.png
│  │     │  │  ├─ fletching_table_front.png
│  │     │  │  ├─ fletching_table_side.png
│  │     │  │  ├─ fletching_table_top.png
│  │     │  │  ├─ flowering_azalea_leaves.png
│  │     │  │  ├─ flowering_azalea_leaves.png.mcmeta
│  │     │  │  ├─ flowering_azalea_side.png
│  │     │  │  ├─ flowering_azalea_top.png
│  │     │  │  ├─ flower_pot.png
│  │     │  │  ├─ frogspawn.png
│  │     │  │  ├─ frosted_ice_0.png
│  │     │  │  ├─ frosted_ice_1.png
│  │     │  │  ├─ frosted_ice_2.png
│  │     │  │  ├─ frosted_ice_3.png
│  │     │  │  ├─ furnace_front.png
│  │     │  │  ├─ furnace_front_on.png
│  │     │  │  ├─ furnace_side.png
│  │     │  │  ├─ furnace_top.png
│  │     │  │  ├─ gilded_blackstone.png
│  │     │  │  ├─ glass.png
│  │     │  │  ├─ glass.png.mcmeta
│  │     │  │  ├─ glass_pane_top.png
│  │     │  │  ├─ glowstone.png
│  │     │  │  ├─ glow_item_frame.png
│  │     │  │  ├─ glow_lichen.png
│  │     │  │  ├─ gold_block.png
│  │     │  │  ├─ gold_ore.png
│  │     │  │  ├─ granite.png
│  │     │  │  ├─ grass_block_side.png
│  │     │  │  ├─ grass_block_side_overlay.png
│  │     │  │  ├─ grass_block_snow.png
│  │     │  │  ├─ grass_block_top.png
│  │     │  │  ├─ gravel.png
│  │     │  │  ├─ gray_candle.png
│  │     │  │  ├─ gray_candle_lit.png
│  │     │  │  ├─ gray_concrete.png
│  │     │  │  ├─ gray_concrete_powder.png
│  │     │  │  ├─ gray_glazed_terracotta.png
│  │     │  │  ├─ gray_shulker_box.png
│  │     │  │  ├─ gray_stained_glass.png
│  │     │  │  ├─ gray_stained_glass_pane_top.png
│  │     │  │  ├─ gray_terracotta.png
│  │     │  │  ├─ gray_wool.png
│  │     │  │  ├─ green_candle.png
│  │     │  │  ├─ green_candle_lit.png
│  │     │  │  ├─ green_concrete.png
│  │     │  │  ├─ green_concrete_powder.png
│  │     │  │  ├─ green_glazed_terracotta.png
│  │     │  │  ├─ green_shulker_box.png
│  │     │  │  ├─ green_stained_glass.png
│  │     │  │  ├─ green_stained_glass_pane_top.png
│  │     │  │  ├─ green_terracotta.png
│  │     │  │  ├─ green_wool.png
│  │     │  │  ├─ grindstone_pivot.png
│  │     │  │  ├─ grindstone_round.png
│  │     │  │  ├─ grindstone_side.png
│  │     │  │  ├─ hanging_roots.png
│  │     │  │  ├─ hay_block_side.png
│  │     │  │  ├─ hay_block_top.png
│  │     │  │  ├─ heavy_core.png
│  │     │  │  ├─ honeycomb_block.png
│  │     │  │  ├─ honey_block_bottom.png
│  │     │  │  ├─ honey_block_side.png
│  │     │  │  ├─ honey_block_top.png
│  │     │  │  ├─ hopper_inside.png
│  │     │  │  ├─ hopper_outside.png
│  │     │  │  ├─ hopper_top.png
│  │     │  │  ├─ horn_coral.png
│  │     │  │  ├─ horn_coral_block.png
│  │     │  │  ├─ horn_coral_fan.png
│  │     │  │  ├─ ice.png
│  │     │  │  ├─ iron_bars.png
│  │     │  │  ├─ iron_block.png
│  │     │  │  ├─ iron_chain.png
│  │     │  │  ├─ iron_door_bottom.png
│  │     │  │  ├─ iron_door_top.png
│  │     │  │  ├─ iron_ore.png
│  │     │  │  ├─ iron_trapdoor.png
│  │     │  │  ├─ item_frame.png
│  │     │  │  ├─ jack_o_lantern.png
│  │     │  │  ├─ jigsaw_bottom.png
│  │     │  │  ├─ jigsaw_lock.png
│  │     │  │  ├─ jigsaw_side.png
│  │     │  │  ├─ jigsaw_top.png
│  │     │  │  ├─ jukebox_side.png
│  │     │  │  ├─ jukebox_top.png
│  │     │  │  ├─ jungle_door_bottom.png
│  │     │  │  ├─ jungle_door_top.png
│  │     │  │  ├─ jungle_leaves.png
│  │     │  │  ├─ jungle_leaves.png.mcmeta
│  │     │  │  ├─ jungle_log.png
│  │     │  │  ├─ jungle_log_top.png
│  │     │  │  ├─ jungle_planks.png
│  │     │  │  ├─ jungle_sapling.png
│  │     │  │  ├─ jungle_shelf.png
│  │     │  │  ├─ jungle_trapdoor.png
│  │     │  │  ├─ kelp.png
│  │     │  │  ├─ kelp.png.mcmeta
│  │     │  │  ├─ kelp_plant.png
│  │     │  │  ├─ kelp_plant.png.mcmeta
│  │     │  │  ├─ ladder.png
│  │     │  │  ├─ lantern.png
│  │     │  │  ├─ lantern.png.mcmeta
│  │     │  │  ├─ lapis_block.png
│  │     │  │  ├─ lapis_ore.png
│  │     │  │  ├─ large_amethyst_bud.png
│  │     │  │  ├─ large_amethyst_bud.png.mcmeta
│  │     │  │  ├─ large_fern_bottom.png
│  │     │  │  ├─ large_fern_top.png
│  │     │  │  ├─ lava_flow.png
│  │     │  │  ├─ lava_flow.png.mcmeta
│  │     │  │  ├─ lava_still.png
│  │     │  │  ├─ lava_still.png.mcmeta
│  │     │  │  ├─ leaf_litter.png
│  │     │  │  ├─ lectern_base.png
│  │     │  │  ├─ lectern_front.png
│  │     │  │  ├─ lectern_sides.png
│  │     │  │  ├─ lectern_top.png
│  │     │  │  ├─ lever.png
│  │     │  │  ├─ lightning_rod.png
│  │     │  │  ├─ lightning_rod_on.png
│  │     │  │  ├─ light_blue_candle.png
│  │     │  │  ├─ light_blue_candle_lit.png
│  │     │  │  ├─ light_blue_concrete.png
│  │     │  │  ├─ light_blue_concrete_powder.png
│  │     │  │  ├─ light_blue_glazed_terracotta.png
│  │     │  │  ├─ light_blue_shulker_box.png
│  │     │  │  ├─ light_blue_stained_glass.png
│  │     │  │  ├─ light_blue_stained_glass_pane_top.png
│  │     │  │  ├─ light_blue_terracotta.png
│  │     │  │  ├─ light_blue_wool.png
│  │     │  │  ├─ light_gray_candle.png
│  │     │  │  ├─ light_gray_candle_lit.png
│  │     │  │  ├─ light_gray_concrete.png
│  │     │  │  ├─ light_gray_concrete_powder.png
│  │     │  │  ├─ light_gray_glazed_terracotta.png
│  │     │  │  ├─ light_gray_shulker_box.png
│  │     │  │  ├─ light_gray_stained_glass.png
│  │     │  │  ├─ light_gray_stained_glass_pane_top.png
│  │     │  │  ├─ light_gray_terracotta.png
│  │     │  │  ├─ light_gray_wool.png
│  │     │  │  ├─ lilac_bottom.png
│  │     │  │  ├─ lilac_top.png
│  │     │  │  ├─ lily_of_the_valley.png
│  │     │  │  ├─ lily_of_the_valley.png.mcmeta
│  │     │  │  ├─ lily_pad.png
│  │     │  │  ├─ lime_candle.png
│  │     │  │  ├─ lime_candle_lit.png
│  │     │  │  ├─ lime_concrete.png
│  │     │  │  ├─ lime_concrete_powder.png
│  │     │  │  ├─ lime_glazed_terracotta.png
│  │     │  │  ├─ lime_shulker_box.png
│  │     │  │  ├─ lime_stained_glass.png
│  │     │  │  ├─ lime_stained_glass_pane_top.png
│  │     │  │  ├─ lime_terracotta.png
│  │     │  │  ├─ lime_wool.png
│  │     │  │  ├─ lodestone_side.png
│  │     │  │  ├─ lodestone_top.png
│  │     │  │  ├─ loom_bottom.png
│  │     │  │  ├─ loom_front.png
│  │     │  │  ├─ loom_side.png
│  │     │  │  ├─ loom_top.png
│  │     │  │  ├─ magenta_candle.png
│  │     │  │  ├─ magenta_candle_lit.png
│  │     │  │  ├─ magenta_concrete.png
│  │     │  │  ├─ magenta_concrete_powder.png
│  │     │  │  ├─ magenta_glazed_terracotta.png
│  │     │  │  ├─ magenta_shulker_box.png
│  │     │  │  ├─ magenta_stained_glass.png
│  │     │  │  ├─ magenta_stained_glass_pane_top.png
│  │     │  │  ├─ magenta_terracotta.png
│  │     │  │  ├─ magenta_wool.png
│  │     │  │  ├─ magma.png
│  │     │  │  ├─ magma.png.mcmeta
│  │     │  │  ├─ mangrove_door_bottom.png
│  │     │  │  ├─ mangrove_door_top.png
│  │     │  │  ├─ mangrove_leaves.png
│  │     │  │  ├─ mangrove_leaves.png.mcmeta
│  │     │  │  ├─ mangrove_log.png
│  │     │  │  ├─ mangrove_log_top.png
│  │     │  │  ├─ mangrove_planks.png
│  │     │  │  ├─ mangrove_propagule.png
│  │     │  │  ├─ mangrove_propagule_hanging.png
│  │     │  │  ├─ mangrove_roots_side.png
│  │     │  │  ├─ mangrove_roots_side.png.mcmeta
│  │     │  │  ├─ mangrove_roots_top.png
│  │     │  │  ├─ mangrove_roots_top.png.mcmeta
│  │     │  │  ├─ mangrove_shelf.png
│  │     │  │  ├─ mangrove_trapdoor.png
│  │     │  │  ├─ medium_amethyst_bud.png
│  │     │  │  ├─ medium_amethyst_bud.png.mcmeta
│  │     │  │  ├─ melon_side.png
│  │     │  │  ├─ melon_stem.png
│  │     │  │  ├─ melon_top.png
│  │     │  │  ├─ mossy_cobblestone.png
│  │     │  │  ├─ mossy_stone_bricks.png
│  │     │  │  ├─ moss_block.png
│  │     │  │  ├─ mud.png
│  │     │  │  ├─ muddy_mangrove_roots_side.png
│  │     │  │  ├─ muddy_mangrove_roots_top.png
│  │     │  │  ├─ mud_bricks.png
│  │     │  │  ├─ mushroom_block_inside.png
│  │     │  │  ├─ mushroom_stem.png
│  │     │  │  ├─ mycelium_side.png
│  │     │  │  ├─ mycelium_top.png
│  │     │  │  ├─ netherite_block.png
│  │     │  │  ├─ netherrack.png
│  │     │  │  ├─ nether_bricks.png
│  │     │  │  ├─ nether_gold_ore.png
│  │     │  │  ├─ nether_portal.png
│  │     │  │  ├─ nether_portal.png.mcmeta
│  │     │  │  ├─ nether_quartz_ore.png
│  │     │  │  ├─ nether_sprouts.png
│  │     │  │  ├─ nether_sprouts.png.mcmeta
│  │     │  │  ├─ nether_wart_block.png
│  │     │  │  ├─ nether_wart_stage0.png
│  │     │  │  ├─ nether_wart_stage1.png
│  │     │  │  ├─ nether_wart_stage2.png
│  │     │  │  ├─ note_block.png
│  │     │  │  ├─ oak_door_bottom.png
│  │     │  │  ├─ oak_door_top.png
│  │     │  │  ├─ oak_leaves.png
│  │     │  │  ├─ oak_leaves.png.mcmeta
│  │     │  │  ├─ oak_log.png
│  │     │  │  ├─ oak_log_top.png
│  │     │  │  ├─ oak_planks.png
│  │     │  │  ├─ oak_sapling.png
│  │     │  │  ├─ oak_shelf.png
│  │     │  │  ├─ oak_trapdoor.png
│  │     │  │  ├─ observer_back.png
│  │     │  │  ├─ observer_back_on.png
│  │     │  │  ├─ observer_front.png
│  │     │  │  ├─ observer_side.png
│  │     │  │  ├─ observer_top.png
│  │     │  │  ├─ obsidian.png
│  │     │  │  ├─ ochre_froglight_side.png
│  │     │  │  ├─ ochre_froglight_top.png
│  │     │  │  ├─ open_eyeblossom.png
│  │     │  │  ├─ open_eyeblossom.png.mcmeta
│  │     │  │  ├─ open_eyeblossom_emissive.png
│  │     │  │  ├─ orange_candle.png
│  │     │  │  ├─ orange_candle_lit.png
│  │     │  │  ├─ orange_concrete.png
│  │     │  │  ├─ orange_concrete_powder.png
│  │     │  │  ├─ orange_glazed_terracotta.png
│  │     │  │  ├─ orange_shulker_box.png
│  │     │  │  ├─ orange_stained_glass.png
│  │     │  │  ├─ orange_stained_glass_pane_top.png
│  │     │  │  ├─ orange_terracotta.png
│  │     │  │  ├─ orange_tulip.png
│  │     │  │  ├─ orange_tulip.png.mcmeta
│  │     │  │  ├─ orange_wool.png
│  │     │  │  ├─ oxeye_daisy.png
│  │     │  │  ├─ oxeye_daisy.png.mcmeta
│  │     │  │  ├─ oxidized_chiseled_copper.png
│  │     │  │  ├─ oxidized_copper.png
│  │     │  │  ├─ oxidized_copper_bars.png
│  │     │  │  ├─ oxidized_copper_bulb.png
│  │     │  │  ├─ oxidized_copper_bulb_lit.png
│  │     │  │  ├─ oxidized_copper_bulb_lit_powered.png
│  │     │  │  ├─ oxidized_copper_bulb_powered.png
│  │     │  │  ├─ oxidized_copper_chain.png
│  │     │  │  ├─ oxidized_copper_door_bottom.png
│  │     │  │  ├─ oxidized_copper_door_top.png
│  │     │  │  ├─ oxidized_copper_grate.png
│  │     │  │  ├─ oxidized_copper_lantern.png
│  │     │  │  ├─ oxidized_copper_lantern.png.mcmeta
│  │     │  │  ├─ oxidized_copper_trapdoor.png
│  │     │  │  ├─ oxidized_cut_copper.png
│  │     │  │  ├─ oxidized_lightning_rod.png
│  │     │  │  ├─ packed_ice.png
│  │     │  │  ├─ packed_mud.png
│  │     │  │  ├─ pale_hanging_moss.png
│  │     │  │  ├─ pale_hanging_moss_tip.png
│  │     │  │  ├─ pale_moss_block.png
│  │     │  │  ├─ pale_moss_carpet.png
│  │     │  │  ├─ pale_moss_carpet_side_small.png
│  │     │  │  ├─ pale_moss_carpet_side_tall.png
│  │     │  │  ├─ pale_oak_door_bottom.png
│  │     │  │  ├─ pale_oak_door_top.png
│  │     │  │  ├─ pale_oak_leaves.png
│  │     │  │  ├─ pale_oak_leaves.png.mcmeta
│  │     │  │  ├─ pale_oak_log.png
│  │     │  │  ├─ pale_oak_log_top.png
│  │     │  │  ├─ pale_oak_planks.png
│  │     │  │  ├─ pale_oak_sapling.png
│  │     │  │  ├─ pale_oak_shelf.png
│  │     │  │  ├─ pale_oak_trapdoor.png
│  │     │  │  ├─ pearlescent_froglight_side.png
│  │     │  │  ├─ pearlescent_froglight_top.png
│  │     │  │  ├─ peony_bottom.png
│  │     │  │  ├─ peony_top.png
│  │     │  │  ├─ pink_candle.png
│  │     │  │  ├─ pink_candle_lit.png
│  │     │  │  ├─ pink_concrete.png
│  │     │  │  ├─ pink_concrete_powder.png
│  │     │  │  ├─ pink_glazed_terracotta.png
│  │     │  │  ├─ pink_petals.png
│  │     │  │  ├─ pink_petals_stem.png
│  │     │  │  ├─ pink_shulker_box.png
│  │     │  │  ├─ pink_stained_glass.png
│  │     │  │  ├─ pink_stained_glass_pane_top.png
│  │     │  │  ├─ pink_terracotta.png
│  │     │  │  ├─ pink_tulip.png
│  │     │  │  ├─ pink_tulip.png.mcmeta
│  │     │  │  ├─ pink_wool.png
│  │     │  │  ├─ piston_bottom.png
│  │     │  │  ├─ piston_inner.png
│  │     │  │  ├─ piston_side.png
│  │     │  │  ├─ piston_top.png
│  │     │  │  ├─ piston_top_sticky.png
│  │     │  │  ├─ pitcher_crop_bottom.png
│  │     │  │  ├─ pitcher_crop_bottom_stage_1.png
│  │     │  │  ├─ pitcher_crop_bottom_stage_2.png
│  │     │  │  ├─ pitcher_crop_bottom_stage_3.png
│  │     │  │  ├─ pitcher_crop_bottom_stage_4.png
│  │     │  │  ├─ pitcher_crop_side.png
│  │     │  │  ├─ pitcher_crop_top.png
│  │     │  │  ├─ pitcher_crop_top_stage_3.png
│  │     │  │  ├─ pitcher_crop_top_stage_4.png
│  │     │  │  ├─ podzol_side.png
│  │     │  │  ├─ podzol_top.png
│  │     │  │  ├─ pointed_dripstone_down_base.png
│  │     │  │  ├─ pointed_dripstone_down_frustum.png
│  │     │  │  ├─ pointed_dripstone_down_middle.png
│  │     │  │  ├─ pointed_dripstone_down_tip.png
│  │     │  │  ├─ pointed_dripstone_down_tip_merge.png
│  │     │  │  ├─ pointed_dripstone_up_base.png
│  │     │  │  ├─ pointed_dripstone_up_frustum.png
│  │     │  │  ├─ pointed_dripstone_up_middle.png
│  │     │  │  ├─ pointed_dripstone_up_tip.png
│  │     │  │  ├─ pointed_dripstone_up_tip_merge.png
│  │     │  │  ├─ polished_andesite.png
│  │     │  │  ├─ polished_basalt_side.png
│  │     │  │  ├─ polished_basalt_top.png
│  │     │  │  ├─ polished_blackstone.png
│  │     │  │  ├─ polished_blackstone_bricks.png
│  │     │  │  ├─ polished_deepslate.png
│  │     │  │  ├─ polished_diorite.png
│  │     │  │  ├─ polished_granite.png
│  │     │  │  ├─ polished_tuff.png
│  │     │  │  ├─ poppy.png
│  │     │  │  ├─ poppy.png.mcmeta
│  │     │  │  ├─ potatoes_stage0.png
│  │     │  │  ├─ potatoes_stage1.png
│  │     │  │  ├─ potatoes_stage2.png
│  │     │  │  ├─ potatoes_stage3.png
│  │     │  │  ├─ potted_azalea_bush_plant.png
│  │     │  │  ├─ potted_azalea_bush_side.png
│  │     │  │  ├─ potted_azalea_bush_top.png
│  │     │  │  ├─ potted_flowering_azalea_bush_plant.png
│  │     │  │  ├─ potted_flowering_azalea_bush_side.png
│  │     │  │  ├─ potted_flowering_azalea_bush_top.png
│  │     │  │  ├─ powder_snow.png
│  │     │  │  ├─ powered_rail.png
│  │     │  │  ├─ powered_rail_on.png
│  │     │  │  ├─ prismarine.png
│  │     │  │  ├─ prismarine.png.mcmeta
│  │     │  │  ├─ prismarine_bricks.png
│  │     │  │  ├─ pumpkin_side.png
│  │     │  │  ├─ pumpkin_stem.png
│  │     │  │  ├─ pumpkin_top.png
│  │     │  │  ├─ purple_candle.png
│  │     │  │  ├─ purple_candle_lit.png
│  │     │  │  ├─ purple_concrete.png
│  │     │  │  ├─ purple_concrete_powder.png
│  │     │  │  ├─ purple_glazed_terracotta.png
│  │     │  │  ├─ purple_shulker_box.png
│  │     │  │  ├─ purple_stained_glass.png
│  │     │  │  ├─ purple_stained_glass_pane_top.png
│  │     │  │  ├─ purple_terracotta.png
│  │     │  │  ├─ purple_wool.png
│  │     │  │  ├─ purpur_block.png
│  │     │  │  ├─ purpur_pillar.png
│  │     │  │  ├─ purpur_pillar_top.png
│  │     │  │  ├─ quartz_block_bottom.png
│  │     │  │  ├─ quartz_block_side.png
│  │     │  │  ├─ quartz_block_top.png
│  │     │  │  ├─ quartz_bricks.png
│  │     │  │  ├─ quartz_pillar.png
│  │     │  │  ├─ quartz_pillar_top.png
│  │     │  │  ├─ rail.png
│  │     │  │  ├─ rail_corner.png
│  │     │  │  ├─ raw_copper_block.png
│  │     │  │  ├─ raw_gold_block.png
│  │     │  │  ├─ raw_iron_block.png
│  │     │  │  ├─ redstone_block.png
│  │     │  │  ├─ redstone_dust_dot.png
│  │     │  │  ├─ redstone_dust_dot.png.mcmeta
│  │     │  │  ├─ redstone_dust_line0.png
│  │     │  │  ├─ redstone_dust_line0.png.mcmeta
│  │     │  │  ├─ redstone_dust_line1.png
│  │     │  │  ├─ redstone_dust_line1.png.mcmeta
│  │     │  │  ├─ redstone_dust_overlay.png
│  │     │  │  ├─ redstone_dust_overlay.png.mcmeta
│  │     │  │  ├─ redstone_lamp.png
│  │     │  │  ├─ redstone_lamp_on.png
│  │     │  │  ├─ redstone_ore.png
│  │     │  │  ├─ redstone_torch.png
│  │     │  │  ├─ redstone_torch_off.png
│  │     │  │  ├─ red_candle.png
│  │     │  │  ├─ red_candle_lit.png
│  │     │  │  ├─ red_concrete.png
│  │     │  │  ├─ red_concrete_powder.png
│  │     │  │  ├─ red_glazed_terracotta.png
│  │     │  │  ├─ red_mushroom.png
│  │     │  │  ├─ red_mushroom.png.mcmeta
│  │     │  │  ├─ red_mushroom_block.png
│  │     │  │  ├─ red_nether_bricks.png
│  │     │  │  ├─ red_sand.png
│  │     │  │  ├─ red_sandstone.png
│  │     │  │  ├─ red_sandstone_bottom.png
│  │     │  │  ├─ red_sandstone_top.png
│  │     │  │  ├─ red_shulker_box.png
│  │     │  │  ├─ red_stained_glass.png
│  │     │  │  ├─ red_stained_glass_pane_top.png
│  │     │  │  ├─ red_terracotta.png
│  │     │  │  ├─ red_tulip.png
│  │     │  │  ├─ red_tulip.png.mcmeta
│  │     │  │  ├─ red_wool.png
│  │     │  │  ├─ reinforced_deepslate_bottom.png
│  │     │  │  ├─ reinforced_deepslate_side.png
│  │     │  │  ├─ reinforced_deepslate_top.png
│  │     │  │  ├─ repeater.png
│  │     │  │  ├─ repeater_on.png
│  │     │  │  ├─ repeating_command_block_back.png
│  │     │  │  ├─ repeating_command_block_back.png.mcmeta
│  │     │  │  ├─ repeating_command_block_conditional.png
│  │     │  │  ├─ repeating_command_block_conditional.png.mcmeta
│  │     │  │  ├─ repeating_command_block_front.png
│  │     │  │  ├─ repeating_command_block_front.png.mcmeta
│  │     │  │  ├─ repeating_command_block_side.png
│  │     │  │  ├─ repeating_command_block_side.png.mcmeta
│  │     │  │  ├─ resin_block.png
│  │     │  │  ├─ resin_bricks.png
│  │     │  │  ├─ resin_clump.png
│  │     │  │  ├─ respawn_anchor_bottom.png
│  │     │  │  ├─ respawn_anchor_side0.png
│  │     │  │  ├─ respawn_anchor_side1.png
│  │     │  │  ├─ respawn_anchor_side2.png
│  │     │  │  ├─ respawn_anchor_side3.png
│  │     │  │  ├─ respawn_anchor_side4.png
│  │     │  │  ├─ respawn_anchor_top.png
│  │     │  │  ├─ respawn_anchor_top.png.mcmeta
│  │     │  │  ├─ respawn_anchor_top_off.png
│  │     │  │  ├─ rooted_dirt.png
│  │     │  │  ├─ rose_bush_bottom.png
│  │     │  │  ├─ rose_bush_top.png
│  │     │  │  ├─ sand.png
│  │     │  │  ├─ sandstone.png
│  │     │  │  ├─ sandstone_bottom.png
│  │     │  │  ├─ sandstone_top.png
│  │     │  │  ├─ scaffolding_bottom.png
│  │     │  │  ├─ scaffolding_side.png
│  │     │  │  ├─ scaffolding_top.png
│  │     │  │  ├─ sculk.png
│  │     │  │  ├─ sculk.png.mcmeta
│  │     │  │  ├─ sculk_catalyst_bottom.png
│  │     │  │  ├─ sculk_catalyst_side.png
│  │     │  │  ├─ sculk_catalyst_side_bloom.png
│  │     │  │  ├─ sculk_catalyst_side_bloom.png.mcmeta
│  │     │  │  ├─ sculk_catalyst_top.png
│  │     │  │  ├─ sculk_catalyst_top_bloom.png
│  │     │  │  ├─ sculk_catalyst_top_bloom.png.mcmeta
│  │     │  │  ├─ sculk_sensor_bottom.png
│  │     │  │  ├─ sculk_sensor_side.png
│  │     │  │  ├─ sculk_sensor_tendril_active.png
│  │     │  │  ├─ sculk_sensor_tendril_active.png.mcmeta
│  │     │  │  ├─ sculk_sensor_tendril_inactive.png
│  │     │  │  ├─ sculk_sensor_tendril_inactive.png.mcmeta
│  │     │  │  ├─ sculk_sensor_top.png
│  │     │  │  ├─ sculk_shrieker_bottom.png
│  │     │  │  ├─ sculk_shrieker_can_summon_inner_top.png
│  │     │  │  ├─ sculk_shrieker_can_summon_inner_top.png.mcmeta
│  │     │  │  ├─ sculk_shrieker_inner_top.png
│  │     │  │  ├─ sculk_shrieker_inner_top.png.mcmeta
│  │     │  │  ├─ sculk_shrieker_side.png
│  │     │  │  ├─ sculk_shrieker_top.png
│  │     │  │  ├─ sculk_vein.png
│  │     │  │  ├─ sculk_vein.png.mcmeta
│  │     │  │  ├─ seagrass.png
│  │     │  │  ├─ seagrass.png.mcmeta
│  │     │  │  ├─ sea_lantern.png
│  │     │  │  ├─ sea_lantern.png.mcmeta
│  │     │  │  ├─ sea_pickle.png
│  │     │  │  ├─ short_dry_grass.png
│  │     │  │  ├─ short_grass.png
│  │     │  │  ├─ shroomlight.png
│  │     │  │  ├─ shulker_box.png
│  │     │  │  ├─ slime_block.png
│  │     │  │  ├─ small_amethyst_bud.png
│  │     │  │  ├─ small_amethyst_bud.png.mcmeta
│  │     │  │  ├─ small_dripleaf_side.png
│  │     │  │  ├─ small_dripleaf_stem_bottom.png
│  │     │  │  ├─ small_dripleaf_stem_top.png
│  │     │  │  ├─ small_dripleaf_top.png
│  │     │  │  ├─ smithing_table_bottom.png
│  │     │  │  ├─ smithing_table_front.png
│  │     │  │  ├─ smithing_table_side.png
│  │     │  │  ├─ smithing_table_top.png
│  │     │  │  ├─ smoker_bottom.png
│  │     │  │  ├─ smoker_front.png
│  │     │  │  ├─ smoker_front_on.png
│  │     │  │  ├─ smoker_front_on.png.mcmeta
│  │     │  │  ├─ smoker_side.png
│  │     │  │  ├─ smoker_top.png
│  │     │  │  ├─ smooth_basalt.png
│  │     │  │  ├─ smooth_stone.png
│  │     │  │  ├─ smooth_stone_slab_side.png
│  │     │  │  ├─ sniffer_egg_not_cracked_bottom.png
│  │     │  │  ├─ sniffer_egg_not_cracked_east.png
│  │     │  │  ├─ sniffer_egg_not_cracked_north.png
│  │     │  │  ├─ sniffer_egg_not_cracked_south.png
│  │     │  │  ├─ sniffer_egg_not_cracked_top.png
│  │     │  │  ├─ sniffer_egg_not_cracked_west.png
│  │     │  │  ├─ sniffer_egg_slightly_cracked_bottom.png
│  │     │  │  ├─ sniffer_egg_slightly_cracked_east.png
│  │     │  │  ├─ sniffer_egg_slightly_cracked_north.png
│  │     │  │  ├─ sniffer_egg_slightly_cracked_south.png
│  │     │  │  ├─ sniffer_egg_slightly_cracked_top.png
│  │     │  │  ├─ sniffer_egg_slightly_cracked_west.png
│  │     │  │  ├─ sniffer_egg_very_cracked_bottom.png
│  │     │  │  ├─ sniffer_egg_very_cracked_east.png
│  │     │  │  ├─ sniffer_egg_very_cracked_north.png
│  │     │  │  ├─ sniffer_egg_very_cracked_south.png
│  │     │  │  ├─ sniffer_egg_very_cracked_top.png
│  │     │  │  ├─ sniffer_egg_very_cracked_west.png
│  │     │  │  ├─ snow.png
│  │     │  │  ├─ soul_campfire_fire.png
│  │     │  │  ├─ soul_campfire_fire.png.mcmeta
│  │     │  │  ├─ soul_campfire_log_lit.png
│  │     │  │  ├─ soul_campfire_log_lit.png.mcmeta
│  │     │  │  ├─ soul_fire_0.png
│  │     │  │  ├─ soul_fire_0.png.mcmeta
│  │     │  │  ├─ soul_fire_1.png
│  │     │  │  ├─ soul_fire_1.png.mcmeta
│  │     │  │  ├─ soul_lantern.png
│  │     │  │  ├─ soul_lantern.png.mcmeta
│  │     │  │  ├─ soul_sand.png
│  │     │  │  ├─ soul_soil.png
│  │     │  │  ├─ soul_torch.png
│  │     │  │  ├─ spawner.png
│  │     │  │  ├─ sponge.png
│  │     │  │  ├─ spore_blossom.png
│  │     │  │  ├─ spore_blossom_base.png
│  │     │  │  ├─ spruce_door_bottom.png
│  │     │  │  ├─ spruce_door_top.png
│  │     │  │  ├─ spruce_leaves.png
│  │     │  │  ├─ spruce_leaves.png.mcmeta
│  │     │  │  ├─ spruce_log.png
│  │     │  │  ├─ spruce_log_top.png
│  │     │  │  ├─ spruce_planks.png
│  │     │  │  ├─ spruce_sapling.png
│  │     │  │  ├─ spruce_shelf.png
│  │     │  │  ├─ spruce_trapdoor.png
│  │     │  │  ├─ stone.png
│  │     │  │  ├─ stonecutter_bottom.png
│  │     │  │  ├─ stonecutter_saw.png
│  │     │  │  ├─ stonecutter_saw.png.mcmeta
│  │     │  │  ├─ stonecutter_side.png
│  │     │  │  ├─ stonecutter_top.png
│  │     │  │  ├─ stone_bricks.png
│  │     │  │  ├─ stripped_acacia_log.png
│  │     │  │  ├─ stripped_acacia_log_top.png
│  │     │  │  ├─ stripped_bamboo_block.png
│  │     │  │  ├─ stripped_bamboo_block_top.png
│  │     │  │  ├─ stripped_birch_log.png
│  │     │  │  ├─ stripped_birch_log_top.png
│  │     │  │  ├─ stripped_cherry_log.png
│  │     │  │  ├─ stripped_cherry_log_top.png
│  │     │  │  ├─ stripped_crimson_stem.png
│  │     │  │  ├─ stripped_crimson_stem_top.png
│  │     │  │  ├─ stripped_dark_oak_log.png
│  │     │  │  ├─ stripped_dark_oak_log_top.png
│  │     │  │  ├─ stripped_jungle_log.png
│  │     │  │  ├─ stripped_jungle_log_top.png
│  │     │  │  ├─ stripped_mangrove_log.png
│  │     │  │  ├─ stripped_mangrove_log_top.png
│  │     │  │  ├─ stripped_oak_log.png
│  │     │  │  ├─ stripped_oak_log_top.png
│  │     │  │  ├─ stripped_pale_oak_log.png
│  │     │  │  ├─ stripped_pale_oak_log_top.png
│  │     │  │  ├─ stripped_spruce_log.png
│  │     │  │  ├─ stripped_spruce_log_top.png
│  │     │  │  ├─ stripped_warped_stem.png
│  │     │  │  ├─ stripped_warped_stem_top.png
│  │     │  │  ├─ structure_block.png
│  │     │  │  ├─ structure_block_corner.png
│  │     │  │  ├─ structure_block_data.png
│  │     │  │  ├─ structure_block_load.png
│  │     │  │  ├─ structure_block_save.png
│  │     │  │  ├─ sugar_cane.png
│  │     │  │  ├─ sunflower_back.png
│  │     │  │  ├─ sunflower_bottom.png
│  │     │  │  ├─ sunflower_front.png
│  │     │  │  ├─ sunflower_top.png
│  │     │  │  ├─ suspicious_gravel_0.png
│  │     │  │  ├─ suspicious_gravel_1.png
│  │     │  │  ├─ suspicious_gravel_2.png
│  │     │  │  ├─ suspicious_gravel_3.png
│  │     │  │  ├─ suspicious_sand_0.png
│  │     │  │  ├─ suspicious_sand_1.png
│  │     │  │  ├─ suspicious_sand_2.png
│  │     │  │  ├─ suspicious_sand_3.png
│  │     │  │  ├─ sweet_berry_bush_stage0.png
│  │     │  │  ├─ sweet_berry_bush_stage0.png.mcmeta
│  │     │  │  ├─ sweet_berry_bush_stage1.png
│  │     │  │  ├─ sweet_berry_bush_stage2.png
│  │     │  │  ├─ sweet_berry_bush_stage3.png
│  │     │  │  ├─ tall_dry_grass.png
│  │     │  │  ├─ tall_grass_bottom.png
│  │     │  │  ├─ tall_grass_top.png
│  │     │  │  ├─ tall_seagrass_bottom.png
│  │     │  │  ├─ tall_seagrass_bottom.png.mcmeta
│  │     │  │  ├─ tall_seagrass_top.png
│  │     │  │  ├─ tall_seagrass_top.png.mcmeta
│  │     │  │  ├─ target_side.png
│  │     │  │  ├─ target_top.png
│  │     │  │  ├─ terracotta.png
│  │     │  │  ├─ test_block_accept.png
│  │     │  │  ├─ test_block_fail.png
│  │     │  │  ├─ test_block_log.png
│  │     │  │  ├─ test_block_start.png
│  │     │  │  ├─ test_instance_block.png
│  │     │  │  ├─ tinted_glass.png
│  │     │  │  ├─ tnt_bottom.png
│  │     │  │  ├─ tnt_side.png
│  │     │  │  ├─ tnt_top.png
│  │     │  │  ├─ torch.png
│  │     │  │  ├─ torchflower.png
│  │     │  │  ├─ torchflower.png.mcmeta
│  │     │  │  ├─ torchflower_crop_stage0.png
│  │     │  │  ├─ torchflower_crop_stage1.png
│  │     │  │  ├─ trial_spawner_bottom.png
│  │     │  │  ├─ trial_spawner_side_active.png
│  │     │  │  ├─ trial_spawner_side_active_ominous.png
│  │     │  │  ├─ trial_spawner_side_inactive.png
│  │     │  │  ├─ trial_spawner_side_inactive_ominous.png
│  │     │  │  ├─ trial_spawner_top_active.png
│  │     │  │  ├─ trial_spawner_top_active_ominous.png
│  │     │  │  ├─ trial_spawner_top_ejecting_reward.png
│  │     │  │  ├─ trial_spawner_top_ejecting_reward_ominous.png
│  │     │  │  ├─ trial_spawner_top_inactive.png
│  │     │  │  ├─ trial_spawner_top_inactive_ominous.png
│  │     │  │  ├─ tripwire.png
│  │     │  │  ├─ tripwire_hook.png
│  │     │  │  ├─ tube_coral.png
│  │     │  │  ├─ tube_coral_block.png
│  │     │  │  ├─ tube_coral_fan.png
│  │     │  │  ├─ tuff.png
│  │     │  │  ├─ tuff_bricks.png
│  │     │  │  ├─ turtle_egg.png
│  │     │  │  ├─ turtle_egg_slightly_cracked.png
│  │     │  │  ├─ turtle_egg_very_cracked.png
│  │     │  │  ├─ twisting_vines.png
│  │     │  │  ├─ twisting_vines_plant.png
│  │     │  │  ├─ vault_bottom.png
│  │     │  │  ├─ vault_bottom_ominous.png
│  │     │  │  ├─ vault_front_ejecting.png
│  │     │  │  ├─ vault_front_ejecting_ominous.png
│  │     │  │  ├─ vault_front_off.png
│  │     │  │  ├─ vault_front_off_ominous.png
│  │     │  │  ├─ vault_front_on.png
│  │     │  │  ├─ vault_front_on_ominous.png
│  │     │  │  ├─ vault_side_off.png
│  │     │  │  ├─ vault_side_off_ominous.png
│  │     │  │  ├─ vault_side_on.png
│  │     │  │  ├─ vault_side_on_ominous.png
│  │     │  │  ├─ vault_top.png
│  │     │  │  ├─ vault_top_ejecting.png
│  │     │  │  ├─ vault_top_ejecting_ominous.png
│  │     │  │  ├─ vault_top_ominous.png
│  │     │  │  ├─ verdant_froglight_side.png
│  │     │  │  ├─ verdant_froglight_top.png
│  │     │  │  ├─ vine.png
│  │     │  │  ├─ warped_door_bottom.png
│  │     │  │  ├─ warped_door_top.png
│  │     │  │  ├─ warped_fungus.png
│  │     │  │  ├─ warped_fungus.png.mcmeta
│  │     │  │  ├─ warped_nylium.png
│  │     │  │  ├─ warped_nylium_side.png
│  │     │  │  ├─ warped_planks.png
│  │     │  │  ├─ warped_roots.png
│  │     │  │  ├─ warped_roots_pot.png
│  │     │  │  ├─ warped_shelf.png
│  │     │  │  ├─ warped_stem.png
│  │     │  │  ├─ warped_stem.png.mcmeta
│  │     │  │  ├─ warped_stem_top.png
│  │     │  │  ├─ warped_trapdoor.png
│  │     │  │  ├─ warped_wart_block.png
│  │     │  │  ├─ water_flow.png
│  │     │  │  ├─ water_flow.png.mcmeta
│  │     │  │  ├─ water_overlay.png
│  │     │  │  ├─ water_still.png
│  │     │  │  ├─ water_still.png.mcmeta
│  │     │  │  ├─ weathered_chiseled_copper.png
│  │     │  │  ├─ weathered_copper.png
│  │     │  │  ├─ weathered_copper_bars.png
│  │     │  │  ├─ weathered_copper_bulb.png
│  │     │  │  ├─ weathered_copper_bulb_lit.png
│  │     │  │  ├─ weathered_copper_bulb_lit_powered.png
│  │     │  │  ├─ weathered_copper_bulb_powered.png
│  │     │  │  ├─ weathered_copper_chain.png
│  │     │  │  ├─ weathered_copper_door_bottom.png
│  │     │  │  ├─ weathered_copper_door_top.png
│  │     │  │  ├─ weathered_copper_grate.png
│  │     │  │  ├─ weathered_copper_lantern.png
│  │     │  │  ├─ weathered_copper_lantern.png.mcmeta
│  │     │  │  ├─ weathered_copper_trapdoor.png
│  │     │  │  ├─ weathered_cut_copper.png
│  │     │  │  ├─ weathered_lightning_rod.png
│  │     │  │  ├─ weeping_vines.png
│  │     │  │  ├─ weeping_vines_plant.png
│  │     │  │  ├─ wet_sponge.png
│  │     │  │  ├─ wheat_stage0.png
│  │     │  │  ├─ wheat_stage1.png
│  │     │  │  ├─ wheat_stage2.png
│  │     │  │  ├─ wheat_stage3.png
│  │     │  │  ├─ wheat_stage4.png
│  │     │  │  ├─ wheat_stage5.png
│  │     │  │  ├─ wheat_stage6.png
│  │     │  │  ├─ wheat_stage7.png
│  │     │  │  ├─ white_candle.png
│  │     │  │  ├─ white_candle_lit.png
│  │     │  │  ├─ white_concrete.png
│  │     │  │  ├─ white_concrete_powder.png
│  │     │  │  ├─ white_glazed_terracotta.png
│  │     │  │  ├─ white_shulker_box.png
│  │     │  │  ├─ white_stained_glass.png
│  │     │  │  ├─ white_stained_glass_pane_top.png
│  │     │  │  ├─ white_terracotta.png
│  │     │  │  ├─ white_tulip.png
│  │     │  │  ├─ white_tulip.png.mcmeta
│  │     │  │  ├─ white_wool.png
│  │     │  │  ├─ wildflowers.png
│  │     │  │  ├─ wildflowers_stem.png
│  │     │  │  ├─ wither_rose.png
│  │     │  │  ├─ wither_rose.png.mcmeta
│  │     │  │  ├─ yellow_candle.png
│  │     │  │  ├─ yellow_candle_lit.png
│  │     │  │  ├─ yellow_concrete.png
│  │     │  │  ├─ yellow_concrete_powder.png
│  │     │  │  ├─ yellow_glazed_terracotta.png
│  │     │  │  ├─ yellow_shulker_box.png
│  │     │  │  ├─ yellow_stained_glass.png
│  │     │  │  ├─ yellow_stained_glass_pane_top.png
│  │     │  │  ├─ yellow_terracotta.png
│  │     │  │  └─ yellow_wool.png
│  │     │  ├─ colormap
│  │     │  │  ├─ dry_foliage.png
│  │     │  │  ├─ foliage.png
│  │     │  │  └─ grass.png
│  │     │  ├─ effect
│  │     │  │  └─ dither.png
│  │     │  ├─ entity
│  │     │  │  ├─ allay
│  │     │  │  │  └─ allay.png
│  │     │  │  ├─ armadillo.png
│  │     │  │  ├─ armorstand
│  │     │  │  │  └─ wood.png
│  │     │  │  ├─ axolotl
│  │     │  │  │  ├─ axolotl_blue.png
│  │     │  │  │  ├─ axolotl_cyan.png
│  │     │  │  │  ├─ axolotl_gold.png
│  │     │  │  │  ├─ axolotl_lucy.png
│  │     │  │  │  └─ axolotl_wild.png
│  │     │  │  ├─ banner
│  │     │  │  │  ├─ base.png
│  │     │  │  │  ├─ border.png
│  │     │  │  │  ├─ bricks.png
│  │     │  │  │  ├─ circle.png
│  │     │  │  │  ├─ creeper.png
│  │     │  │  │  ├─ cross.png
│  │     │  │  │  ├─ curly_border.png
│  │     │  │  │  ├─ diagonal_left.png
│  │     │  │  │  ├─ diagonal_right.png
│  │     │  │  │  ├─ diagonal_up_left.png
│  │     │  │  │  ├─ diagonal_up_right.png
│  │     │  │  │  ├─ flow.png
│  │     │  │  │  ├─ flower.png
│  │     │  │  │  ├─ globe.png
│  │     │  │  │  ├─ gradient.png
│  │     │  │  │  ├─ gradient_up.png
│  │     │  │  │  ├─ guster.png
│  │     │  │  │  ├─ half_horizontal.png
│  │     │  │  │  ├─ half_horizontal_bottom.png
│  │     │  │  │  ├─ half_vertical.png
│  │     │  │  │  ├─ half_vertical_right.png
│  │     │  │  │  ├─ mojang.png
│  │     │  │  │  ├─ piglin.png
│  │     │  │  │  ├─ rhombus.png
│  │     │  │  │  ├─ skull.png
│  │     │  │  │  ├─ small_stripes.png
│  │     │  │  │  ├─ square_bottom_left.png
│  │     │  │  │  ├─ square_bottom_right.png
│  │     │  │  │  ├─ square_top_left.png
│  │     │  │  │  ├─ square_top_right.png
│  │     │  │  │  ├─ straight_cross.png
│  │     │  │  │  ├─ stripe_bottom.png
│  │     │  │  │  ├─ stripe_center.png
│  │     │  │  │  ├─ stripe_downleft.png
│  │     │  │  │  ├─ stripe_downright.png
│  │     │  │  │  ├─ stripe_left.png
│  │     │  │  │  ├─ stripe_middle.png
│  │     │  │  │  ├─ stripe_right.png
│  │     │  │  │  ├─ stripe_top.png
│  │     │  │  │  ├─ triangles_bottom.png
│  │     │  │  │  ├─ triangles_top.png
│  │     │  │  │  ├─ triangle_bottom.png
│  │     │  │  │  └─ triangle_top.png
│  │     │  │  ├─ banner_base.png
│  │     │  │  ├─ bat.png
│  │     │  │  ├─ beacon_beam.png
│  │     │  │  ├─ bear
│  │     │  │  │  └─ polarbear.png
│  │     │  │  ├─ bed
│  │     │  │  │  ├─ black.png
│  │     │  │  │  ├─ blue.png
│  │     │  │  │  ├─ brown.png
│  │     │  │  │  ├─ cyan.png
│  │     │  │  │  ├─ gray.png
│  │     │  │  │  ├─ green.png
│  │     │  │  │  ├─ light_blue.png
│  │     │  │  │  ├─ light_gray.png
│  │     │  │  │  ├─ lime.png
│  │     │  │  │  ├─ magenta.png
│  │     │  │  │  ├─ orange.png
│  │     │  │  │  ├─ pink.png
│  │     │  │  │  ├─ purple.png
│  │     │  │  │  ├─ red.png
│  │     │  │  │  ├─ white.png
│  │     │  │  │  └─ yellow.png
│  │     │  │  ├─ bee
│  │     │  │  │  ├─ bee.png
│  │     │  │  │  ├─ bee_angry.png
│  │     │  │  │  ├─ bee_angry_nectar.png
│  │     │  │  │  ├─ bee_nectar.png
│  │     │  │  │  └─ bee_stinger.png
│  │     │  │  ├─ bell
│  │     │  │  │  └─ bell_body.png
│  │     │  │  ├─ blaze.png
│  │     │  │  ├─ boat
│  │     │  │  │  ├─ acacia.png
│  │     │  │  │  ├─ bamboo.png
│  │     │  │  │  ├─ birch.png
│  │     │  │  │  ├─ cherry.png
│  │     │  │  │  ├─ dark_oak.png
│  │     │  │  │  ├─ jungle.png
│  │     │  │  │  ├─ mangrove.png
│  │     │  │  │  ├─ oak.png
│  │     │  │  │  ├─ pale_oak.png
│  │     │  │  │  └─ spruce.png
│  │     │  │  ├─ breeze
│  │     │  │  │  ├─ breeze.png
│  │     │  │  │  ├─ breeze_eyes.png
│  │     │  │  │  └─ breeze_wind.png
│  │     │  │  ├─ camel
│  │     │  │  │  ├─ camel.png
│  │     │  │  │  └─ camel_husk.png
│  │     │  │  ├─ cat
│  │     │  │  │  ├─ all_black.png
│  │     │  │  │  ├─ black.png
│  │     │  │  │  ├─ british_shorthair.png
│  │     │  │  │  ├─ calico.png
│  │     │  │  │  ├─ cat_collar.png
│  │     │  │  │  ├─ jellie.png
│  │     │  │  │  ├─ ocelot.png
│  │     │  │  │  ├─ persian.png
│  │     │  │  │  ├─ ragdoll.png
│  │     │  │  │  ├─ red.png
│  │     │  │  │  ├─ siamese.png
│  │     │  │  │  ├─ tabby.png
│  │     │  │  │  └─ white.png
│  │     │  │  ├─ chest
│  │     │  │  │  ├─ christmas.png
│  │     │  │  │  ├─ christmas_left.png
│  │     │  │  │  ├─ christmas_right.png
│  │     │  │  │  ├─ copper.png
│  │     │  │  │  ├─ copper_exposed.png
│  │     │  │  │  ├─ copper_exposed_left.png
│  │     │  │  │  ├─ copper_exposed_right.png
│  │     │  │  │  ├─ copper_left.png
│  │     │  │  │  ├─ copper_oxidized.png
│  │     │  │  │  ├─ copper_oxidized_left.png
│  │     │  │  │  ├─ copper_oxidized_right.png
│  │     │  │  │  ├─ copper_right.png
│  │     │  │  │  ├─ copper_weathered.png
│  │     │  │  │  ├─ copper_weathered_left.png
│  │     │  │  │  ├─ copper_weathered_right.png
│  │     │  │  │  ├─ ender.png
│  │     │  │  │  ├─ normal.png
│  │     │  │  │  ├─ normal_left.png
│  │     │  │  │  ├─ normal_right.png
│  │     │  │  │  ├─ trapped.png
│  │     │  │  │  ├─ trapped_left.png
│  │     │  │  │  └─ trapped_right.png
│  │     │  │  ├─ chest_boat
│  │     │  │  │  ├─ acacia.png
│  │     │  │  │  ├─ bamboo.png
│  │     │  │  │  ├─ birch.png
│  │     │  │  │  ├─ cherry.png
│  │     │  │  │  ├─ dark_oak.png
│  │     │  │  │  ├─ jungle.png
│  │     │  │  │  ├─ mangrove.png
│  │     │  │  │  ├─ oak.png
│  │     │  │  │  ├─ pale_oak.png
│  │     │  │  │  └─ spruce.png
│  │     │  │  ├─ chicken
│  │     │  │  │  ├─ cold_chicken.png
│  │     │  │  │  ├─ temperate_chicken.png
│  │     │  │  │  └─ warm_chicken.png
│  │     │  │  ├─ conduit
│  │     │  │  │  ├─ base.png
│  │     │  │  │  ├─ break_particle.png
│  │     │  │  │  ├─ cage.png
│  │     │  │  │  ├─ closed_eye.png
│  │     │  │  │  ├─ open_eye.png
│  │     │  │  │  ├─ wind.png
│  │     │  │  │  ├─ wind.png.mcmeta
│  │     │  │  │  ├─ wind_vertical.png
│  │     │  │  │  └─ wind_vertical.png.mcmeta
│  │     │  │  ├─ copper_golem
│  │     │  │  │  ├─ copper_golem.png
│  │     │  │  │  ├─ copper_golem_eyes.png
│  │     │  │  │  ├─ exposed_copper_golem.png
│  │     │  │  │  ├─ exposed_copper_golem_eyes.png
│  │     │  │  │  ├─ oxidized_copper_golem.png
│  │     │  │  │  ├─ oxidized_copper_golem_eyes.png
│  │     │  │  │  ├─ weathered_copper_golem.png
│  │     │  │  │  └─ weathered_copper_golem_eyes.png
│  │     │  │  ├─ cow
│  │     │  │  │  ├─ brown_mooshroom.png
│  │     │  │  │  ├─ cold_cow.png
│  │     │  │  │  ├─ red_mooshroom.png
│  │     │  │  │  ├─ temperate_cow.png
│  │     │  │  │  └─ warm_cow.png
│  │     │  │  ├─ creaking
│  │     │  │  │  ├─ creaking.png
│  │     │  │  │  └─ creaking_eyes.png
│  │     │  │  ├─ creeper
│  │     │  │  │  ├─ creeper.png
│  │     │  │  │  └─ creeper_armor.png
│  │     │  │  ├─ decorated_pot
│  │     │  │  │  ├─ angler_pottery_pattern.png
│  │     │  │  │  ├─ archer_pottery_pattern.png
│  │     │  │  │  ├─ arms_up_pottery_pattern.png
│  │     │  │  │  ├─ blade_pottery_pattern.png
│  │     │  │  │  ├─ brewer_pottery_pattern.png
│  │     │  │  │  ├─ burn_pottery_pattern.png
│  │     │  │  │  ├─ danger_pottery_pattern.png
│  │     │  │  │  ├─ decorated_pot_base.png
│  │     │  │  │  ├─ decorated_pot_side.png
│  │     │  │  │  ├─ explorer_pottery_pattern.png
│  │     │  │  │  ├─ flow_pottery_pattern.png
│  │     │  │  │  ├─ friend_pottery_pattern.png
│  │     │  │  │  ├─ guster_pottery_pattern.png
│  │     │  │  │  ├─ heartbreak_pottery_pattern.png
│  │     │  │  │  ├─ heart_pottery_pattern.png
│  │     │  │  │  ├─ howl_pottery_pattern.png
│  │     │  │  │  ├─ miner_pottery_pattern.png
│  │     │  │  │  ├─ mourner_pottery_pattern.png
│  │     │  │  │  ├─ plenty_pottery_pattern.png
│  │     │  │  │  ├─ prize_pottery_pattern.png
│  │     │  │  │  ├─ scrape_pottery_pattern.png
│  │     │  │  │  ├─ sheaf_pottery_pattern.png
│  │     │  │  │  ├─ shelter_pottery_pattern.png
│  │     │  │  │  ├─ skull_pottery_pattern.png
│  │     │  │  │  └─ snort_pottery_pattern.png
│  │     │  │  ├─ dolphin.png
│  │     │  │  ├─ enchanting_table_book.png
│  │     │  │  ├─ enderdragon
│  │     │  │  │  ├─ dragon.png
│  │     │  │  │  ├─ dragon_exploding.png
│  │     │  │  │  ├─ dragon_eyes.png
│  │     │  │  │  └─ dragon_fireball.png
│  │     │  │  ├─ enderman
│  │     │  │  │  ├─ enderman.png
│  │     │  │  │  └─ enderman_eyes.png
│  │     │  │  ├─ endermite.png
│  │     │  │  ├─ end_crystal
│  │     │  │  │  ├─ end_crystal.png
│  │     │  │  │  └─ end_crystal_beam.png
│  │     │  │  ├─ end_gateway_beam.png
│  │     │  │  ├─ end_portal.png
│  │     │  │  ├─ equipment
│  │     │  │  │  ├─ camel_husk_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ camel_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ donkey_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ happy_ghast_body
│  │     │  │  │  │  ├─ black_harness.png
│  │     │  │  │  │  ├─ blue_harness.png
│  │     │  │  │  │  ├─ brown_harness.png
│  │     │  │  │  │  ├─ cyan_harness.png
│  │     │  │  │  │  ├─ gray_harness.png
│  │     │  │  │  │  ├─ green_harness.png
│  │     │  │  │  │  ├─ light_blue_harness.png
│  │     │  │  │  │  ├─ light_gray_harness.png
│  │     │  │  │  │  ├─ lime_harness.png
│  │     │  │  │  │  ├─ magenta_harness.png
│  │     │  │  │  │  ├─ orange_harness.png
│  │     │  │  │  │  ├─ pink_harness.png
│  │     │  │  │  │  ├─ purple_harness.png
│  │     │  │  │  │  ├─ red_harness.png
│  │     │  │  │  │  ├─ white_harness.png
│  │     │  │  │  │  └─ yellow_harness.png
│  │     │  │  │  ├─ horse_body
│  │     │  │  │  │  ├─ copper.png
│  │     │  │  │  │  ├─ diamond.png
│  │     │  │  │  │  ├─ gold.png
│  │     │  │  │  │  ├─ iron.png
│  │     │  │  │  │  ├─ leather.png
│  │     │  │  │  │  ├─ leather_overlay.png
│  │     │  │  │  │  └─ netherite.png
│  │     │  │  │  ├─ horse_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ humanoid
│  │     │  │  │  │  ├─ chainmail.png
│  │     │  │  │  │  ├─ copper.png
│  │     │  │  │  │  ├─ diamond.png
│  │     │  │  │  │  ├─ gold.png
│  │     │  │  │  │  ├─ iron.png
│  │     │  │  │  │  ├─ leather.png
│  │     │  │  │  │  ├─ leather_overlay.png
│  │     │  │  │  │  ├─ netherite.png
│  │     │  │  │  │  └─ turtle_scute.png
│  │     │  │  │  ├─ humanoid_leggings
│  │     │  │  │  │  ├─ chainmail.png
│  │     │  │  │  │  ├─ copper.png
│  │     │  │  │  │  ├─ diamond.png
│  │     │  │  │  │  ├─ gold.png
│  │     │  │  │  │  ├─ iron.png
│  │     │  │  │  │  ├─ leather.png
│  │     │  │  │  │  ├─ leather_overlay.png
│  │     │  │  │  │  └─ netherite.png
│  │     │  │  │  ├─ llama_body
│  │     │  │  │  │  ├─ black.png
│  │     │  │  │  │  ├─ blue.png
│  │     │  │  │  │  ├─ brown.png
│  │     │  │  │  │  ├─ cyan.png
│  │     │  │  │  │  ├─ gray.png
│  │     │  │  │  │  ├─ green.png
│  │     │  │  │  │  ├─ light_blue.png
│  │     │  │  │  │  ├─ light_gray.png
│  │     │  │  │  │  ├─ lime.png
│  │     │  │  │  │  ├─ magenta.png
│  │     │  │  │  │  ├─ orange.png
│  │     │  │  │  │  ├─ pink.png
│  │     │  │  │  │  ├─ purple.png
│  │     │  │  │  │  ├─ red.png
│  │     │  │  │  │  ├─ trader_llama.png
│  │     │  │  │  │  ├─ white.png
│  │     │  │  │  │  └─ yellow.png
│  │     │  │  │  ├─ mule_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ nautilus_body
│  │     │  │  │  │  ├─ copper.png
│  │     │  │  │  │  ├─ diamond.png
│  │     │  │  │  │  ├─ gold.png
│  │     │  │  │  │  ├─ iron.png
│  │     │  │  │  │  └─ netherite.png
│  │     │  │  │  ├─ nautilus_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ pig_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ skeleton_horse_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ strider_saddle
│  │     │  │  │  │  └─ saddle.png
│  │     │  │  │  ├─ wings
│  │     │  │  │  │  └─ elytra.png
│  │     │  │  │  ├─ wolf_body
│  │     │  │  │  │  ├─ armadillo_scute.png
│  │     │  │  │  │  └─ armadillo_scute_overlay.png
│  │     │  │  │  └─ zombie_horse_saddle
│  │     │  │  │     └─ saddle.png
│  │     │  │  ├─ experience_orb.png
│  │     │  │  ├─ fish
│  │     │  │  │  ├─ cod.png
│  │     │  │  │  ├─ pufferfish.png
│  │     │  │  │  ├─ salmon.png
│  │     │  │  │  ├─ tropical_a.png
│  │     │  │  │  ├─ tropical_a_pattern_1.png
│  │     │  │  │  ├─ tropical_a_pattern_2.png
│  │     │  │  │  ├─ tropical_a_pattern_3.png
│  │     │  │  │  ├─ tropical_a_pattern_4.png
│  │     │  │  │  ├─ tropical_a_pattern_5.png
│  │     │  │  │  ├─ tropical_a_pattern_6.png
│  │     │  │  │  ├─ tropical_b.png
│  │     │  │  │  ├─ tropical_b_pattern_1.png
│  │     │  │  │  ├─ tropical_b_pattern_2.png
│  │     │  │  │  ├─ tropical_b_pattern_3.png
│  │     │  │  │  ├─ tropical_b_pattern_4.png
│  │     │  │  │  ├─ tropical_b_pattern_5.png
│  │     │  │  │  └─ tropical_b_pattern_6.png
│  │     │  │  ├─ fishing_hook.png
│  │     │  │  ├─ fox
│  │     │  │  │  ├─ fox.png
│  │     │  │  │  ├─ fox_sleep.png
│  │     │  │  │  ├─ snow_fox.png
│  │     │  │  │  └─ snow_fox_sleep.png
│  │     │  │  ├─ frog
│  │     │  │  │  ├─ cold_frog.png
│  │     │  │  │  ├─ temperate_frog.png
│  │     │  │  │  └─ warm_frog.png
│  │     │  │  ├─ ghast
│  │     │  │  │  ├─ ghast.png
│  │     │  │  │  ├─ ghast_shooting.png
│  │     │  │  │  ├─ happy_ghast.png
│  │     │  │  │  ├─ happy_ghast_baby.png
│  │     │  │  │  └─ happy_ghast_ropes.png
│  │     │  │  ├─ goat
│  │     │  │  │  └─ goat.png
│  │     │  │  ├─ guardian.png
│  │     │  │  ├─ guardian_beam.png
│  │     │  │  ├─ guardian_elder.png
│  │     │  │  ├─ hoglin
│  │     │  │  │  ├─ hoglin.png
│  │     │  │  │  └─ zoglin.png
│  │     │  │  ├─ horse
│  │     │  │  │  ├─ donkey.png
│  │     │  │  │  ├─ horse_black.png
│  │     │  │  │  ├─ horse_brown.png
│  │     │  │  │  ├─ horse_chestnut.png
│  │     │  │  │  ├─ horse_creamy.png
│  │     │  │  │  ├─ horse_darkbrown.png
│  │     │  │  │  ├─ horse_gray.png
│  │     │  │  │  ├─ horse_markings_blackdots.png
│  │     │  │  │  ├─ horse_markings_white.png
│  │     │  │  │  ├─ horse_markings_whitedots.png
│  │     │  │  │  ├─ horse_markings_whitefield.png
│  │     │  │  │  ├─ horse_skeleton.png
│  │     │  │  │  ├─ horse_white.png
│  │     │  │  │  ├─ horse_zombie.png
│  │     │  │  │  └─ mule.png
│  │     │  │  ├─ illager
│  │     │  │  │  ├─ evoker.png
│  │     │  │  │  ├─ evoker_fangs.png
│  │     │  │  │  ├─ illusioner.png
│  │     │  │  │  ├─ pillager.png
│  │     │  │  │  ├─ ravager.png
│  │     │  │  │  ├─ vex.png
│  │     │  │  │  ├─ vex_charging.png
│  │     │  │  │  └─ vindicator.png
│  │     │  │  ├─ iron_golem
│  │     │  │  │  ├─ iron_golem.png
│  │     │  │  │  ├─ iron_golem_crackiness_high.png
│  │     │  │  │  ├─ iron_golem_crackiness_low.png
│  │     │  │  │  └─ iron_golem_crackiness_medium.png
│  │     │  │  ├─ lead_knot.png
│  │     │  │  ├─ llama
│  │     │  │  │  ├─ brown.png
│  │     │  │  │  ├─ creamy.png
│  │     │  │  │  ├─ gray.png
│  │     │  │  │  ├─ spit.png
│  │     │  │  │  └─ white.png
│  │     │  │  ├─ minecart.png
│  │     │  │  ├─ nautilus
│  │     │  │  │  ├─ nautilus.png
│  │     │  │  │  ├─ nautilus_baby.png
│  │     │  │  │  ├─ zombie_nautilus.png
│  │     │  │  │  └─ zombie_nautilus_coral.png
│  │     │  │  ├─ panda
│  │     │  │  │  ├─ aggressive_panda.png
│  │     │  │  │  ├─ brown_panda.png
│  │     │  │  │  ├─ lazy_panda.png
│  │     │  │  │  ├─ panda.png
│  │     │  │  │  ├─ playful_panda.png
│  │     │  │  │  ├─ weak_panda.png
│  │     │  │  │  └─ worried_panda.png
│  │     │  │  ├─ parrot
│  │     │  │  │  ├─ parrot_blue.png
│  │     │  │  │  ├─ parrot_green.png
│  │     │  │  │  ├─ parrot_grey.png
│  │     │  │  │  ├─ parrot_red_blue.png
│  │     │  │  │  └─ parrot_yellow_blue.png
│  │     │  │  ├─ phantom.png
│  │     │  │  ├─ phantom_eyes.png
│  │     │  │  ├─ pig
│  │     │  │  │  ├─ cold_pig.png
│  │     │  │  │  ├─ temperate_pig.png
│  │     │  │  │  └─ warm_pig.png
│  │     │  │  ├─ piglin
│  │     │  │  │  ├─ piglin.png
│  │     │  │  │  ├─ piglin_brute.png
│  │     │  │  │  └─ zombified_piglin.png
│  │     │  │  ├─ player
│  │     │  │  │  ├─ slim
│  │     │  │  │  │  ├─ alex.png
│  │     │  │  │  │  ├─ ari.png
│  │     │  │  │  │  ├─ efe.png
│  │     │  │  │  │  ├─ kai.png
│  │     │  │  │  │  ├─ makena.png
│  │     │  │  │  │  ├─ noor.png
│  │     │  │  │  │  ├─ steve.png
│  │     │  │  │  │  ├─ sunny.png
│  │     │  │  │  │  └─ zuri.png
│  │     │  │  │  └─ wide
│  │     │  │  │     ├─ alex.png
│  │     │  │  │     ├─ ari.png
│  │     │  │  │     ├─ efe.png
│  │     │  │  │     ├─ kai.png
│  │     │  │  │     ├─ makena.png
│  │     │  │  │     ├─ noor.png
│  │     │  │  │     ├─ steve.png
│  │     │  │  │     ├─ sunny.png
│  │     │  │  │     └─ zuri.png
│  │     │  │  ├─ projectiles
│  │     │  │  │  ├─ arrow.png
│  │     │  │  │  ├─ spectral_arrow.png
│  │     │  │  │  ├─ tipped_arrow.png
│  │     │  │  │  └─ wind_charge.png
│  │     │  │  ├─ rabbit
│  │     │  │  │  ├─ black.png
│  │     │  │  │  ├─ brown.png
│  │     │  │  │  ├─ caerbannog.png
│  │     │  │  │  ├─ gold.png
│  │     │  │  │  ├─ salt.png
│  │     │  │  │  ├─ toast.png
│  │     │  │  │  ├─ white.png
│  │     │  │  │  └─ white_splotched.png
│  │     │  │  ├─ sheep
│  │     │  │  │  ├─ sheep.png
│  │     │  │  │  ├─ sheep_wool.png
│  │     │  │  │  └─ sheep_wool_undercoat.png
│  │     │  │  ├─ shield
│  │     │  │  │  ├─ base.png
│  │     │  │  │  ├─ border.png
│  │     │  │  │  ├─ bricks.png
│  │     │  │  │  ├─ circle.png
│  │     │  │  │  ├─ creeper.png
│  │     │  │  │  ├─ cross.png
│  │     │  │  │  ├─ curly_border.png
│  │     │  │  │  ├─ diagonal_left.png
│  │     │  │  │  ├─ diagonal_right.png
│  │     │  │  │  ├─ diagonal_up_left.png
│  │     │  │  │  ├─ diagonal_up_right.png
│  │     │  │  │  ├─ flow.png
│  │     │  │  │  ├─ flower.png
│  │     │  │  │  ├─ globe.png
│  │     │  │  │  ├─ gradient.png
│  │     │  │  │  ├─ gradient_up.png
│  │     │  │  │  ├─ guster.png
│  │     │  │  │  ├─ half_horizontal.png
│  │     │  │  │  ├─ half_horizontal_bottom.png
│  │     │  │  │  ├─ half_vertical.png
│  │     │  │  │  ├─ half_vertical_right.png
│  │     │  │  │  ├─ mojang.png
│  │     │  │  │  ├─ piglin.png
│  │     │  │  │  ├─ rhombus.png
│  │     │  │  │  ├─ skull.png
│  │     │  │  │  ├─ small_stripes.png
│  │     │  │  │  ├─ square_bottom_left.png
│  │     │  │  │  ├─ square_bottom_right.png
│  │     │  │  │  ├─ square_top_left.png
│  │     │  │  │  ├─ square_top_right.png
│  │     │  │  │  ├─ straight_cross.png
│  │     │  │  │  ├─ stripe_bottom.png
│  │     │  │  │  ├─ stripe_center.png
│  │     │  │  │  ├─ stripe_downleft.png
│  │     │  │  │  ├─ stripe_downright.png
│  │     │  │  │  ├─ stripe_left.png
│  │     │  │  │  ├─ stripe_middle.png
│  │     │  │  │  ├─ stripe_right.png
│  │     │  │  │  ├─ stripe_top.png
│  │     │  │  │  ├─ triangles_bottom.png
│  │     │  │  │  ├─ triangles_top.png
│  │     │  │  │  ├─ triangle_bottom.png
│  │     │  │  │  └─ triangle_top.png
│  │     │  │  ├─ shield_base.png
│  │     │  │  ├─ shield_base_nopattern.png
│  │     │  │  ├─ shulker
│  │     │  │  │  ├─ shulker.png
│  │     │  │  │  ├─ shulker_black.png
│  │     │  │  │  ├─ shulker_blue.png
│  │     │  │  │  ├─ shulker_brown.png
│  │     │  │  │  ├─ shulker_cyan.png
│  │     │  │  │  ├─ shulker_gray.png
│  │     │  │  │  ├─ shulker_green.png
│  │     │  │  │  ├─ shulker_light_blue.png
│  │     │  │  │  ├─ shulker_light_gray.png
│  │     │  │  │  ├─ shulker_lime.png
│  │     │  │  │  ├─ shulker_magenta.png
│  │     │  │  │  ├─ shulker_orange.png
│  │     │  │  │  ├─ shulker_pink.png
│  │     │  │  │  ├─ shulker_purple.png
│  │     │  │  │  ├─ shulker_red.png
│  │     │  │  │  ├─ shulker_white.png
│  │     │  │  │  ├─ shulker_yellow.png
│  │     │  │  │  └─ spark.png
│  │     │  │  ├─ signs
│  │     │  │  │  ├─ acacia.png
│  │     │  │  │  ├─ bamboo.png
│  │     │  │  │  ├─ birch.png
│  │     │  │  │  ├─ cherry.png
│  │     │  │  │  ├─ crimson.png
│  │     │  │  │  ├─ dark_oak.png
│  │     │  │  │  ├─ hanging
│  │     │  │  │  │  ├─ acacia.png
│  │     │  │  │  │  ├─ bamboo.png
│  │     │  │  │  │  ├─ birch.png
│  │     │  │  │  │  ├─ cherry.png
│  │     │  │  │  │  ├─ crimson.png
│  │     │  │  │  │  ├─ dark_oak.png
│  │     │  │  │  │  ├─ jungle.png
│  │     │  │  │  │  ├─ mangrove.png
│  │     │  │  │  │  ├─ oak.png
│  │     │  │  │  │  ├─ pale_oak.png
│  │     │  │  │  │  ├─ spruce.png
│  │     │  │  │  │  └─ warped.png
│  │     │  │  │  ├─ jungle.png
│  │     │  │  │  ├─ mangrove.png
│  │     │  │  │  ├─ oak.png
│  │     │  │  │  ├─ pale_oak.png
│  │     │  │  │  ├─ spruce.png
│  │     │  │  │  └─ warped.png
│  │     │  │  ├─ silverfish.png
│  │     │  │  ├─ skeleton
│  │     │  │  │  ├─ bogged.png
│  │     │  │  │  ├─ bogged_overlay.png
│  │     │  │  │  ├─ parched.png
│  │     │  │  │  ├─ skeleton.png
│  │     │  │  │  ├─ stray.png
│  │     │  │  │  ├─ stray_overlay.png
│  │     │  │  │  └─ wither_skeleton.png
│  │     │  │  ├─ slime
│  │     │  │  │  ├─ magmacube.png
│  │     │  │  │  └─ slime.png
│  │     │  │  ├─ sniffer
│  │     │  │  │  └─ sniffer.png
│  │     │  │  ├─ snow_golem.png
│  │     │  │  ├─ spider
│  │     │  │  │  ├─ cave_spider.png
│  │     │  │  │  └─ spider.png
│  │     │  │  ├─ spider_eyes.png
│  │     │  │  ├─ squid
│  │     │  │  │  ├─ glow_squid.png
│  │     │  │  │  └─ squid.png
│  │     │  │  ├─ strider
│  │     │  │  │  ├─ strider.png
│  │     │  │  │  └─ strider_cold.png
│  │     │  │  ├─ tadpole
│  │     │  │  │  └─ tadpole.png
│  │     │  │  ├─ trident.png
│  │     │  │  ├─ trident_riptide.png
│  │     │  │  ├─ turtle
│  │     │  │  │  └─ big_sea_turtle.png
│  │     │  │  ├─ villager
│  │     │  │  │  ├─ profession
│  │     │  │  │  │  ├─ armorer.png
│  │     │  │  │  │  ├─ butcher.png
│  │     │  │  │  │  ├─ butcher.png.mcmeta
│  │     │  │  │  │  ├─ cartographer.png
│  │     │  │  │  │  ├─ cleric.png
│  │     │  │  │  │  ├─ farmer.png
│  │     │  │  │  │  ├─ farmer.png.mcmeta
│  │     │  │  │  │  ├─ fisherman.png
│  │     │  │  │  │  ├─ fisherman.png.mcmeta
│  │     │  │  │  │  ├─ fletcher.png
│  │     │  │  │  │  ├─ fletcher.png.mcmeta
│  │     │  │  │  │  ├─ leatherworker.png
│  │     │  │  │  │  ├─ librarian.png
│  │     │  │  │  │  ├─ librarian.png.mcmeta
│  │     │  │  │  │  ├─ mason.png
│  │     │  │  │  │  ├─ nitwit.png
│  │     │  │  │  │  ├─ shepherd.png
│  │     │  │  │  │  ├─ shepherd.png.mcmeta
│  │     │  │  │  │  ├─ toolsmith.png
│  │     │  │  │  │  └─ weaponsmith.png
│  │     │  │  │  ├─ profession_level
│  │     │  │  │  │  ├─ diamond.png
│  │     │  │  │  │  ├─ emerald.png
│  │     │  │  │  │  ├─ gold.png
│  │     │  │  │  │  ├─ iron.png
│  │     │  │  │  │  └─ stone.png
│  │     │  │  │  ├─ type
│  │     │  │  │  │  ├─ desert.png
│  │     │  │  │  │  ├─ desert.png.mcmeta
│  │     │  │  │  │  ├─ jungle.png
│  │     │  │  │  │  ├─ plains.png
│  │     │  │  │  │  ├─ savanna.png
│  │     │  │  │  │  ├─ snow.png
│  │     │  │  │  │  ├─ snow.png.mcmeta
│  │     │  │  │  │  ├─ swamp.png
│  │     │  │  │  │  └─ taiga.png
│  │     │  │  │  └─ villager.png
│  │     │  │  ├─ wandering_trader.png
│  │     │  │  ├─ warden
│  │     │  │  │  ├─ warden.png
│  │     │  │  │  ├─ warden_bioluminescent_layer.png
│  │     │  │  │  ├─ warden_heart.png
│  │     │  │  │  ├─ warden_pulsating_spots_1.png
│  │     │  │  │  └─ warden_pulsating_spots_2.png
│  │     │  │  ├─ witch.png
│  │     │  │  ├─ wither
│  │     │  │  │  ├─ wither.png
│  │     │  │  │  ├─ wither_armor.png
│  │     │  │  │  └─ wither_invulnerable.png
│  │     │  │  ├─ wolf
│  │     │  │  │  ├─ wolf.png
│  │     │  │  │  ├─ wolf_angry.png
│  │     │  │  │  ├─ wolf_armor_crackiness_high.png
│  │     │  │  │  ├─ wolf_armor_crackiness_low.png
│  │     │  │  │  ├─ wolf_armor_crackiness_medium.png
│  │     │  │  │  ├─ wolf_ashen.png
│  │     │  │  │  ├─ wolf_ashen_angry.png
│  │     │  │  │  ├─ wolf_ashen_tame.png
│  │     │  │  │  ├─ wolf_black.png
│  │     │  │  │  ├─ wolf_black_angry.png
│  │     │  │  │  ├─ wolf_black_tame.png
│  │     │  │  │  ├─ wolf_chestnut.png
│  │     │  │  │  ├─ wolf_chestnut_angry.png
│  │     │  │  │  ├─ wolf_chestnut_tame.png
│  │     │  │  │  ├─ wolf_collar.png
│  │     │  │  │  ├─ wolf_rusty.png
│  │     │  │  │  ├─ wolf_rusty_angry.png
│  │     │  │  │  ├─ wolf_rusty_tame.png
│  │     │  │  │  ├─ wolf_snowy.png
│  │     │  │  │  ├─ wolf_snowy_angry.png
│  │     │  │  │  ├─ wolf_snowy_tame.png
│  │     │  │  │  ├─ wolf_spotted.png
│  │     │  │  │  ├─ wolf_spotted_angry.png
│  │     │  │  │  ├─ wolf_spotted_tame.png
│  │     │  │  │  ├─ wolf_striped.png
│  │     │  │  │  ├─ wolf_striped_angry.png
│  │     │  │  │  ├─ wolf_striped_tame.png
│  │     │  │  │  ├─ wolf_tame.png
│  │     │  │  │  ├─ wolf_woods.png
│  │     │  │  │  ├─ wolf_woods_angry.png
│  │     │  │  │  └─ wolf_woods_tame.png
│  │     │  │  ├─ zombie
│  │     │  │  │  ├─ drowned.png
│  │     │  │  │  ├─ drowned_outer_layer.png
│  │     │  │  │  ├─ husk.png
│  │     │  │  │  └─ zombie.png
│  │     │  │  └─ zombie_villager
│  │     │  │     ├─ profession
│  │     │  │     │  ├─ armorer.png
│  │     │  │     │  ├─ butcher.png
│  │     │  │     │  ├─ butcher.png.mcmeta
│  │     │  │     │  ├─ cartographer.png
│  │     │  │     │  ├─ cleric.png
│  │     │  │     │  ├─ farmer.png
│  │     │  │     │  ├─ farmer.png.mcmeta
│  │     │  │     │  ├─ fisherman.png
│  │     │  │     │  ├─ fisherman.png.mcmeta
│  │     │  │     │  ├─ fletcher.png
│  │     │  │     │  ├─ fletcher.png.mcmeta
│  │     │  │     │  ├─ leatherworker.png
│  │     │  │     │  ├─ librarian.png
│  │     │  │     │  ├─ librarian.png.mcmeta
│  │     │  │     │  ├─ mason.png
│  │     │  │     │  ├─ nitwit.png
│  │     │  │     │  ├─ shepherd.png
│  │     │  │     │  ├─ shepherd.png.mcmeta
│  │     │  │     │  ├─ toolsmith.png
│  │     │  │     │  └─ weaponsmith.png
│  │     │  │     ├─ profession_level
│  │     │  │     │  ├─ diamond.png
│  │     │  │     │  ├─ emerald.png
│  │     │  │     │  ├─ gold.png
│  │     │  │     │  ├─ iron.png
│  │     │  │     │  └─ stone.png
│  │     │  │     ├─ type
│  │     │  │     │  ├─ desert.png
│  │     │  │     │  ├─ jungle.png
│  │     │  │     │  ├─ plains.png
│  │     │  │     │  ├─ savanna.png
│  │     │  │     │  ├─ snow.png
│  │     │  │     │  ├─ swamp.png
│  │     │  │     │  └─ taiga.png
│  │     │  │     └─ zombie_villager.png
│  │     │  ├─ environment
│  │     │  │  ├─ celestial
│  │     │  │  │  ├─ end_flash.png
│  │     │  │  │  ├─ moon
│  │     │  │  │  │  ├─ first_quarter.png
│  │     │  │  │  │  ├─ full_moon.png
│  │     │  │  │  │  ├─ new_moon.png
│  │     │  │  │  │  ├─ third_quarter.png
│  │     │  │  │  │  ├─ waning_crescent.png
│  │     │  │  │  │  ├─ waning_gibbous.png
│  │     │  │  │  │  ├─ waxing_crescent.png
│  │     │  │  │  │  └─ waxing_gibbous.png
│  │     │  │  │  └─ sun.png
│  │     │  │  ├─ clouds.png
│  │     │  │  ├─ end_sky.png
│  │     │  │  ├─ rain.png
│  │     │  │  └─ snow.png
│  │     │  ├─ font
│  │     │  │  ├─ accented.png
│  │     │  │  ├─ ascii.png
│  │     │  │  ├─ asciillager.png
│  │     │  │  ├─ ascii_sga.png
│  │     │  │  └─ nonlatin_european.png
│  │     │  ├─ gui
│  │     │  │  ├─ advancements
│  │     │  │  │  ├─ backgrounds
│  │     │  │  │  │  ├─ adventure.png
│  │     │  │  │  │  ├─ end.png
│  │     │  │  │  │  ├─ husbandry.png
│  │     │  │  │  │  ├─ nether.png
│  │     │  │  │  │  └─ stone.png
│  │     │  │  │  └─ window.png
│  │     │  │  ├─ book.png
│  │     │  │  ├─ container
│  │     │  │  │  ├─ anvil.png
│  │     │  │  │  ├─ beacon.png
│  │     │  │  │  ├─ blast_furnace.png
│  │     │  │  │  ├─ brewing_stand.png
│  │     │  │  │  ├─ cartography_table.png
│  │     │  │  │  ├─ crafter.png
│  │     │  │  │  ├─ crafting_table.png
│  │     │  │  │  ├─ creative_inventory
│  │     │  │  │  │  ├─ tab_inventory.png
│  │     │  │  │  │  ├─ tab_items.png
│  │     │  │  │  │  └─ tab_item_search.png
│  │     │  │  │  ├─ dispenser.png
│  │     │  │  │  ├─ enchanting_table.png
│  │     │  │  │  ├─ furnace.png
│  │     │  │  │  ├─ gamemode_switcher.png
│  │     │  │  │  ├─ generic_54.png
│  │     │  │  │  ├─ grindstone.png
│  │     │  │  │  ├─ hopper.png
│  │     │  │  │  ├─ horse.png
│  │     │  │  │  ├─ inventory.png
│  │     │  │  │  ├─ loom.png
│  │     │  │  │  ├─ nautilus.png
│  │     │  │  │  ├─ shulker_box.png
│  │     │  │  │  ├─ smithing.png
│  │     │  │  │  ├─ smoker.png
│  │     │  │  │  ├─ stonecutter.png
│  │     │  │  │  └─ villager.png
│  │     │  │  ├─ demo_background.png
│  │     │  │  ├─ footer_separator.png
│  │     │  │  ├─ hanging_signs
│  │     │  │  │  ├─ acacia.png
│  │     │  │  │  ├─ bamboo.png
│  │     │  │  │  ├─ birch.png
│  │     │  │  │  ├─ cherry.png
│  │     │  │  │  ├─ crimson.png
│  │     │  │  │  ├─ dark_oak.png
│  │     │  │  │  ├─ jungle.png
│  │     │  │  │  ├─ mangrove.png
│  │     │  │  │  ├─ oak.png
│  │     │  │  │  ├─ pale_oak.png
│  │     │  │  │  ├─ spruce.png
│  │     │  │  │  └─ warped.png
│  │     │  │  ├─ header_separator.png
│  │     │  │  ├─ inworld_footer_separator.png
│  │     │  │  ├─ inworld_header_separator.png
│  │     │  │  ├─ inworld_menu_background.png
│  │     │  │  ├─ inworld_menu_list_background.png
│  │     │  │  ├─ menu_background.png
│  │     │  │  ├─ menu_list_background.png
│  │     │  │  ├─ presets
│  │     │  │  │  └─ isles.png
│  │     │  │  ├─ realms
│  │     │  │  │  ├─ adventure.png
│  │     │  │  │  ├─ empty_frame.png
│  │     │  │  │  ├─ experience.png
│  │     │  │  │  ├─ inspiration.png
│  │     │  │  │  ├─ new_world.png
│  │     │  │  │  ├─ no_realms.png
│  │     │  │  │  ├─ snapshot_realms.png
│  │     │  │  │  ├─ survival_spawn.png
│  │     │  │  │  └─ upload.png
│  │     │  │  ├─ recipe_book.png
│  │     │  │  ├─ sprites
│  │     │  │  │  ├─ advancements
│  │     │  │  │  │  ├─ box_obtained.png
│  │     │  │  │  │  ├─ box_obtained.png.mcmeta
│  │     │  │  │  │  ├─ box_unobtained.png
│  │     │  │  │  │  ├─ box_unobtained.png.mcmeta
│  │     │  │  │  │  ├─ challenge_frame_obtained.png
│  │     │  │  │  │  ├─ challenge_frame_unobtained.png
│  │     │  │  │  │  ├─ goal_frame_obtained.png
│  │     │  │  │  │  ├─ goal_frame_unobtained.png
│  │     │  │  │  │  ├─ tab_above_left.png
│  │     │  │  │  │  ├─ tab_above_left_selected.png
│  │     │  │  │  │  ├─ tab_above_middle.png
│  │     │  │  │  │  ├─ tab_above_middle_selected.png
│  │     │  │  │  │  ├─ tab_above_right.png
│  │     │  │  │  │  ├─ tab_above_right_selected.png
│  │     │  │  │  │  ├─ tab_below_left.png
│  │     │  │  │  │  ├─ tab_below_left_selected.png
│  │     │  │  │  │  ├─ tab_below_middle.png
│  │     │  │  │  │  ├─ tab_below_middle_selected.png
│  │     │  │  │  │  ├─ tab_below_right.png
│  │     │  │  │  │  ├─ tab_below_right_selected.png
│  │     │  │  │  │  ├─ tab_left_bottom.png
│  │     │  │  │  │  ├─ tab_left_bottom_selected.png
│  │     │  │  │  │  ├─ tab_left_middle.png
│  │     │  │  │  │  ├─ tab_left_middle_selected.png
│  │     │  │  │  │  ├─ tab_left_top.png
│  │     │  │  │  │  ├─ tab_left_top_selected.png
│  │     │  │  │  │  ├─ tab_right_bottom.png
│  │     │  │  │  │  ├─ tab_right_bottom_selected.png
│  │     │  │  │  │  ├─ tab_right_middle.png
│  │     │  │  │  │  ├─ tab_right_middle_selected.png
│  │     │  │  │  │  ├─ tab_right_top.png
│  │     │  │  │  │  ├─ tab_right_top_selected.png
│  │     │  │  │  │  ├─ task_frame_obtained.png
│  │     │  │  │  │  ├─ task_frame_unobtained.png
│  │     │  │  │  │  ├─ title_box.png
│  │     │  │  │  │  └─ title_box.png.mcmeta
│  │     │  │  │  ├─ boss_bar
│  │     │  │  │  │  ├─ blue_background.png
│  │     │  │  │  │  ├─ blue_progress.png
│  │     │  │  │  │  ├─ green_background.png
│  │     │  │  │  │  ├─ green_progress.png
│  │     │  │  │  │  ├─ notched_10_background.png
│  │     │  │  │  │  ├─ notched_10_progress.png
│  │     │  │  │  │  ├─ notched_12_background.png
│  │     │  │  │  │  ├─ notched_12_progress.png
│  │     │  │  │  │  ├─ notched_20_background.png
│  │     │  │  │  │  ├─ notched_20_progress.png
│  │     │  │  │  │  ├─ notched_6_background.png
│  │     │  │  │  │  ├─ notched_6_progress.png
│  │     │  │  │  │  ├─ pink_background.png
│  │     │  │  │  │  ├─ pink_progress.png
│  │     │  │  │  │  ├─ purple_background.png
│  │     │  │  │  │  ├─ purple_progress.png
│  │     │  │  │  │  ├─ red_background.png
│  │     │  │  │  │  ├─ red_progress.png
│  │     │  │  │  │  ├─ white_background.png
│  │     │  │  │  │  ├─ white_progress.png
│  │     │  │  │  │  ├─ yellow_background.png
│  │     │  │  │  │  └─ yellow_progress.png
│  │     │  │  │  ├─ container
│  │     │  │  │  │  ├─ anvil
│  │     │  │  │  │  │  ├─ error.png
│  │     │  │  │  │  │  ├─ text_field.png
│  │     │  │  │  │  │  └─ text_field_disabled.png
│  │     │  │  │  │  ├─ beacon
│  │     │  │  │  │  │  ├─ button.png
│  │     │  │  │  │  │  ├─ button_disabled.png
│  │     │  │  │  │  │  ├─ button_highlighted.png
│  │     │  │  │  │  │  ├─ button_selected.png
│  │     │  │  │  │  │  ├─ cancel.png
│  │     │  │  │  │  │  └─ confirm.png
│  │     │  │  │  │  ├─ blast_furnace
│  │     │  │  │  │  │  ├─ burn_progress.png
│  │     │  │  │  │  │  └─ lit_progress.png
│  │     │  │  │  │  ├─ brewing_stand
│  │     │  │  │  │  │  ├─ brew_progress.png
│  │     │  │  │  │  │  ├─ bubbles.png
│  │     │  │  │  │  │  └─ fuel_length.png
│  │     │  │  │  │  ├─ bundle
│  │     │  │  │  │  │  ├─ bundle_progressbar_border.png
│  │     │  │  │  │  │  ├─ bundle_progressbar_border.png.mcmeta
│  │     │  │  │  │  │  ├─ bundle_progressbar_fill.png
│  │     │  │  │  │  │  ├─ bundle_progressbar_fill.png.mcmeta
│  │     │  │  │  │  │  ├─ bundle_progressbar_full.png
│  │     │  │  │  │  │  ├─ bundle_progressbar_full.png.mcmeta
│  │     │  │  │  │  │  ├─ slot_background.png
│  │     │  │  │  │  │  ├─ slot_background.png.mcmeta
│  │     │  │  │  │  │  ├─ slot_highlight_back.png
│  │     │  │  │  │  │  ├─ slot_highlight_back.png.mcmeta
│  │     │  │  │  │  │  ├─ slot_highlight_front.png
│  │     │  │  │  │  │  └─ slot_highlight_front.png.mcmeta
│  │     │  │  │  │  ├─ cartography_table
│  │     │  │  │  │  │  ├─ duplicated_map.png
│  │     │  │  │  │  │  ├─ error.png
│  │     │  │  │  │  │  ├─ locked.png
│  │     │  │  │  │  │  ├─ map.png
│  │     │  │  │  │  │  └─ scaled_map.png
│  │     │  │  │  │  ├─ crafter
│  │     │  │  │  │  │  ├─ disabled_slot.png
│  │     │  │  │  │  │  ├─ powered_redstone.png
│  │     │  │  │  │  │  └─ unpowered_redstone.png
│  │     │  │  │  │  ├─ creative_inventory
│  │     │  │  │  │  │  ├─ scroller.png
│  │     │  │  │  │  │  ├─ scroller_disabled.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_1.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_2.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_3.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_4.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_5.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_6.png
│  │     │  │  │  │  │  ├─ tab_bottom_selected_7.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_1.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_2.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_3.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_4.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_5.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_6.png
│  │     │  │  │  │  │  ├─ tab_bottom_unselected_7.png
│  │     │  │  │  │  │  ├─ tab_top_selected_1.png
│  │     │  │  │  │  │  ├─ tab_top_selected_2.png
│  │     │  │  │  │  │  ├─ tab_top_selected_3.png
│  │     │  │  │  │  │  ├─ tab_top_selected_4.png
│  │     │  │  │  │  │  ├─ tab_top_selected_5.png
│  │     │  │  │  │  │  ├─ tab_top_selected_6.png
│  │     │  │  │  │  │  ├─ tab_top_selected_7.png
│  │     │  │  │  │  │  ├─ tab_top_unselected_1.png
│  │     │  │  │  │  │  ├─ tab_top_unselected_2.png
│  │     │  │  │  │  │  ├─ tab_top_unselected_3.png
│  │     │  │  │  │  │  ├─ tab_top_unselected_4.png
│  │     │  │  │  │  │  ├─ tab_top_unselected_5.png
│  │     │  │  │  │  │  ├─ tab_top_unselected_6.png
│  │     │  │  │  │  │  └─ tab_top_unselected_7.png
│  │     │  │  │  │  ├─ enchanting_table
│  │     │  │  │  │  │  ├─ enchantment_slot.png
│  │     │  │  │  │  │  ├─ enchantment_slot_disabled.png
│  │     │  │  │  │  │  ├─ enchantment_slot_highlighted.png
│  │     │  │  │  │  │  ├─ level_1.png
│  │     │  │  │  │  │  ├─ level_1_disabled.png
│  │     │  │  │  │  │  ├─ level_2.png
│  │     │  │  │  │  │  ├─ level_2_disabled.png
│  │     │  │  │  │  │  ├─ level_3.png
│  │     │  │  │  │  │  └─ level_3_disabled.png
│  │     │  │  │  │  ├─ furnace
│  │     │  │  │  │  │  ├─ burn_progress.png
│  │     │  │  │  │  │  └─ lit_progress.png
│  │     │  │  │  │  ├─ grindstone
│  │     │  │  │  │  │  └─ error.png
│  │     │  │  │  │  ├─ horse
│  │     │  │  │  │  │  └─ chest_slots.png
│  │     │  │  │  │  ├─ inventory
│  │     │  │  │  │  │  ├─ effect_background.png
│  │     │  │  │  │  │  ├─ effect_background.png.mcmeta
│  │     │  │  │  │  │  ├─ effect_background_ambient.png
│  │     │  │  │  │  │  └─ effect_background_ambient.png.mcmeta
│  │     │  │  │  │  ├─ loom
│  │     │  │  │  │  │  ├─ error.png
│  │     │  │  │  │  │  ├─ pattern.png
│  │     │  │  │  │  │  ├─ pattern_highlighted.png
│  │     │  │  │  │  │  ├─ pattern_selected.png
│  │     │  │  │  │  │  ├─ scroller.png
│  │     │  │  │  │  │  └─ scroller_disabled.png
│  │     │  │  │  │  ├─ slot
│  │     │  │  │  │  │  ├─ amethyst_shard.png
│  │     │  │  │  │  │  ├─ axe.png
│  │     │  │  │  │  │  ├─ banner.png
│  │     │  │  │  │  │  ├─ banner_pattern.png
│  │     │  │  │  │  │  ├─ boots.png
│  │     │  │  │  │  │  ├─ brewing_fuel.png
│  │     │  │  │  │  │  ├─ chestplate.png
│  │     │  │  │  │  │  ├─ diamond.png
│  │     │  │  │  │  │  ├─ dye.png
│  │     │  │  │  │  │  ├─ emerald.png
│  │     │  │  │  │  │  ├─ helmet.png
│  │     │  │  │  │  │  ├─ hoe.png
│  │     │  │  │  │  │  ├─ horse_armor.png
│  │     │  │  │  │  │  ├─ ingot.png
│  │     │  │  │  │  │  ├─ lapis_lazuli.png
│  │     │  │  │  │  │  ├─ leggings.png
│  │     │  │  │  │  │  ├─ llama_armor.png
│  │     │  │  │  │  │  ├─ nautilus_armor.png
│  │     │  │  │  │  │  ├─ nautilus_armor_inventory.png
│  │     │  │  │  │  │  ├─ pickaxe.png
│  │     │  │  │  │  │  ├─ potion.png
│  │     │  │  │  │  │  ├─ quartz.png
│  │     │  │  │  │  │  ├─ redstone_dust.png
│  │     │  │  │  │  │  ├─ saddle.png
│  │     │  │  │  │  │  ├─ shield.png
│  │     │  │  │  │  │  ├─ shovel.png
│  │     │  │  │  │  │  ├─ smithing_template_armor_trim.png
│  │     │  │  │  │  │  ├─ smithing_template_netherite_upgrade.png
│  │     │  │  │  │  │  ├─ spear.png
│  │     │  │  │  │  │  └─ sword.png
│  │     │  │  │  │  ├─ slot.png
│  │     │  │  │  │  ├─ slot_highlight_back.png
│  │     │  │  │  │  ├─ slot_highlight_back.png.mcmeta
│  │     │  │  │  │  ├─ slot_highlight_front.png
│  │     │  │  │  │  ├─ slot_highlight_front.png.mcmeta
│  │     │  │  │  │  ├─ smithing
│  │     │  │  │  │  │  └─ error.png
│  │     │  │  │  │  ├─ smoker
│  │     │  │  │  │  │  ├─ burn_progress.png
│  │     │  │  │  │  │  └─ lit_progress.png
│  │     │  │  │  │  ├─ stonecutter
│  │     │  │  │  │  │  ├─ recipe.png
│  │     │  │  │  │  │  ├─ recipe_highlighted.png
│  │     │  │  │  │  │  ├─ recipe_selected.png
│  │     │  │  │  │  │  ├─ scroller.png
│  │     │  │  │  │  │  └─ scroller_disabled.png
│  │     │  │  │  │  └─ villager
│  │     │  │  │  │     ├─ discount_strikethrough.png
│  │     │  │  │  │     ├─ experience_bar_background.png
│  │     │  │  │  │     ├─ experience_bar_current.png
│  │     │  │  │  │     ├─ experience_bar_result.png
│  │     │  │  │  │     ├─ out_of_stock.png
│  │     │  │  │  │     ├─ scroller.png
│  │     │  │  │  │     ├─ scroller_disabled.png
│  │     │  │  │  │     ├─ trade_arrow.png
│  │     │  │  │  │     └─ trade_arrow_out_of_stock.png
│  │     │  │  │  ├─ dialog
│  │     │  │  │  │  ├─ warning_button.png
│  │     │  │  │  │  ├─ warning_button_disabled.png
│  │     │  │  │  │  └─ warning_button_highlighted.png
│  │     │  │  │  ├─ gamemode_switcher
│  │     │  │  │  │  ├─ selection.png
│  │     │  │  │  │  └─ slot.png
│  │     │  │  │  ├─ hud
│  │     │  │  │  │  ├─ air.png
│  │     │  │  │  │  ├─ air_bursting.png
│  │     │  │  │  │  ├─ air_empty.png
│  │     │  │  │  │  ├─ armor_empty.png
│  │     │  │  │  │  ├─ armor_full.png
│  │     │  │  │  │  ├─ armor_half.png
│  │     │  │  │  │  ├─ crosshair.png
│  │     │  │  │  │  ├─ crosshair_attack_indicator_background.png
│  │     │  │  │  │  ├─ crosshair_attack_indicator_full.png
│  │     │  │  │  │  ├─ crosshair_attack_indicator_progress.png
│  │     │  │  │  │  ├─ effect_background.png
│  │     │  │  │  │  ├─ effect_background_ambient.png
│  │     │  │  │  │  ├─ experience_bar_background.png
│  │     │  │  │  │  ├─ experience_bar_progress.png
│  │     │  │  │  │  ├─ food_empty.png
│  │     │  │  │  │  ├─ food_empty_hunger.png
│  │     │  │  │  │  ├─ food_full.png
│  │     │  │  │  │  ├─ food_full_hunger.png
│  │     │  │  │  │  ├─ food_half.png
│  │     │  │  │  │  ├─ food_half_hunger.png
│  │     │  │  │  │  ├─ heart
│  │     │  │  │  │  │  ├─ absorbing_full.png
│  │     │  │  │  │  │  ├─ absorbing_full_blinking.png
│  │     │  │  │  │  │  ├─ absorbing_half.png
│  │     │  │  │  │  │  ├─ absorbing_half_blinking.png
│  │     │  │  │  │  │  ├─ absorbing_hardcore_full.png
│  │     │  │  │  │  │  ├─ absorbing_hardcore_full_blinking.png
│  │     │  │  │  │  │  ├─ absorbing_hardcore_half.png
│  │     │  │  │  │  │  ├─ absorbing_hardcore_half_blinking.png
│  │     │  │  │  │  │  ├─ container.png
│  │     │  │  │  │  │  ├─ container_blinking.png
│  │     │  │  │  │  │  ├─ container_hardcore.png
│  │     │  │  │  │  │  ├─ container_hardcore_blinking.png
│  │     │  │  │  │  │  ├─ frozen_full.png
│  │     │  │  │  │  │  ├─ frozen_full_blinking.png
│  │     │  │  │  │  │  ├─ frozen_half.png
│  │     │  │  │  │  │  ├─ frozen_half_blinking.png
│  │     │  │  │  │  │  ├─ frozen_hardcore_full.png
│  │     │  │  │  │  │  ├─ frozen_hardcore_full_blinking.png
│  │     │  │  │  │  │  ├─ frozen_hardcore_half.png
│  │     │  │  │  │  │  ├─ frozen_hardcore_half_blinking.png
│  │     │  │  │  │  │  ├─ full.png
│  │     │  │  │  │  │  ├─ full_blinking.png
│  │     │  │  │  │  │  ├─ half.png
│  │     │  │  │  │  │  ├─ half_blinking.png
│  │     │  │  │  │  │  ├─ hardcore_full.png
│  │     │  │  │  │  │  ├─ hardcore_full_blinking.png
│  │     │  │  │  │  │  ├─ hardcore_half.png
│  │     │  │  │  │  │  ├─ hardcore_half_blinking.png
│  │     │  │  │  │  │  ├─ poisoned_full.png
│  │     │  │  │  │  │  ├─ poisoned_full_blinking.png
│  │     │  │  │  │  │  ├─ poisoned_half.png
│  │     │  │  │  │  │  ├─ poisoned_half_blinking.png
│  │     │  │  │  │  │  ├─ poisoned_hardcore_full.png
│  │     │  │  │  │  │  ├─ poisoned_hardcore_full_blinking.png
│  │     │  │  │  │  │  ├─ poisoned_hardcore_half.png
│  │     │  │  │  │  │  ├─ poisoned_hardcore_half_blinking.png
│  │     │  │  │  │  │  ├─ vehicle_container.png
│  │     │  │  │  │  │  ├─ vehicle_full.png
│  │     │  │  │  │  │  ├─ vehicle_half.png
│  │     │  │  │  │  │  ├─ withered_full.png
│  │     │  │  │  │  │  ├─ withered_full_blinking.png
│  │     │  │  │  │  │  ├─ withered_half.png
│  │     │  │  │  │  │  ├─ withered_half_blinking.png
│  │     │  │  │  │  │  ├─ withered_hardcore_full.png
│  │     │  │  │  │  │  ├─ withered_hardcore_full_blinking.png
│  │     │  │  │  │  │  ├─ withered_hardcore_half.png
│  │     │  │  │  │  │  └─ withered_hardcore_half_blinking.png
│  │     │  │  │  │  ├─ hotbar.png
│  │     │  │  │  │  ├─ hotbar_attack_indicator_background.png
│  │     │  │  │  │  ├─ hotbar_attack_indicator_progress.png
│  │     │  │  │  │  ├─ hotbar_offhand_left.png
│  │     │  │  │  │  ├─ hotbar_offhand_right.png
│  │     │  │  │  │  ├─ hotbar_selection.png
│  │     │  │  │  │  ├─ jump_bar_background.png
│  │     │  │  │  │  ├─ jump_bar_cooldown.png
│  │     │  │  │  │  ├─ jump_bar_progress.png
│  │     │  │  │  │  ├─ locator_bar_arrow_down.png
│  │     │  │  │  │  ├─ locator_bar_arrow_down.png.mcmeta
│  │     │  │  │  │  ├─ locator_bar_arrow_up.png
│  │     │  │  │  │  ├─ locator_bar_arrow_up.png.mcmeta
│  │     │  │  │  │  ├─ locator_bar_background.png
│  │     │  │  │  │  ├─ locator_bar_background.png.mcmeta
│  │     │  │  │  │  └─ locator_bar_dot
│  │     │  │  │  │     ├─ bowtie.png
│  │     │  │  │  │     ├─ default_0.png
│  │     │  │  │  │     ├─ default_1.png
│  │     │  │  │  │     ├─ default_2.png
│  │     │  │  │  │     └─ default_3.png
│  │     │  │  │  ├─ icon
│  │     │  │  │  │  ├─ accessibility.png
│  │     │  │  │  │  ├─ chat_modified.png
│  │     │  │  │  │  ├─ checkmark.png
│  │     │  │  │  │  ├─ draft_report.png
│  │     │  │  │  │  ├─ info.png
│  │     │  │  │  │  ├─ invite.png
│  │     │  │  │  │  ├─ language.png
│  │     │  │  │  │  ├─ link.png
│  │     │  │  │  │  ├─ link_highlighted.png
│  │     │  │  │  │  ├─ music_notes.png
│  │     │  │  │  │  ├─ music_notes.png.mcmeta
│  │     │  │  │  │  ├─ news.png
│  │     │  │  │  │  ├─ new_realm.png
│  │     │  │  │  │  ├─ ping_1.png
│  │     │  │  │  │  ├─ ping_2.png
│  │     │  │  │  │  ├─ ping_3.png
│  │     │  │  │  │  ├─ ping_4.png
│  │     │  │  │  │  ├─ ping_5.png
│  │     │  │  │  │  ├─ ping_unknown.png
│  │     │  │  │  │  ├─ search.png
│  │     │  │  │  │  ├─ trial_available.png
│  │     │  │  │  │  ├─ trial_available.png.mcmeta
│  │     │  │  │  │  ├─ unseen_notification.png
│  │     │  │  │  │  ├─ video_link.png
│  │     │  │  │  │  └─ video_link_highlighted.png
│  │     │  │  │  ├─ notification
│  │     │  │  │  │  ├─ 1.png
│  │     │  │  │  │  ├─ 2.png
│  │     │  │  │  │  ├─ 3.png
│  │     │  │  │  │  ├─ 4.png
│  │     │  │  │  │  ├─ 5.png
│  │     │  │  │  │  └─ more.png
│  │     │  │  │  ├─ pending_invite
│  │     │  │  │  │  ├─ accept.png
│  │     │  │  │  │  ├─ accept_highlighted.png
│  │     │  │  │  │  ├─ reject.png
│  │     │  │  │  │  └─ reject_highlighted.png
│  │     │  │  │  ├─ player_list
│  │     │  │  │  │  ├─ make_operator.png
│  │     │  │  │  │  ├─ remove_operator.png
│  │     │  │  │  │  └─ remove_player.png
│  │     │  │  │  ├─ popup
│  │     │  │  │  │  ├─ background.png
│  │     │  │  │  │  └─ background.png.mcmeta
│  │     │  │  │  ├─ realm_status
│  │     │  │  │  │  ├─ closed.png
│  │     │  │  │  │  ├─ expired.png
│  │     │  │  │  │  ├─ expires_soon.png
│  │     │  │  │  │  ├─ expires_soon.png.mcmeta
│  │     │  │  │  │  └─ open.png
│  │     │  │  │  ├─ recipe_book
│  │     │  │  │  │  ├─ button.png
│  │     │  │  │  │  ├─ button_highlighted.png
│  │     │  │  │  │  ├─ crafting_overlay.png
│  │     │  │  │  │  ├─ crafting_overlay_disabled.png
│  │     │  │  │  │  ├─ crafting_overlay_disabled_highlighted.png
│  │     │  │  │  │  ├─ crafting_overlay_highlighted.png
│  │     │  │  │  │  ├─ filter_disabled.png
│  │     │  │  │  │  ├─ filter_disabled_highlighted.png
│  │     │  │  │  │  ├─ filter_enabled.png
│  │     │  │  │  │  ├─ filter_enabled_highlighted.png
│  │     │  │  │  │  ├─ furnace_filter_disabled.png
│  │     │  │  │  │  ├─ furnace_filter_disabled_highlighted.png
│  │     │  │  │  │  ├─ furnace_filter_enabled.png
│  │     │  │  │  │  ├─ furnace_filter_enabled_highlighted.png
│  │     │  │  │  │  ├─ furnace_overlay.png
│  │     │  │  │  │  ├─ furnace_overlay_disabled.png
│  │     │  │  │  │  ├─ furnace_overlay_disabled_highlighted.png
│  │     │  │  │  │  ├─ furnace_overlay_highlighted.png
│  │     │  │  │  │  ├─ overlay_recipe.png
│  │     │  │  │  │  ├─ overlay_recipe.png.mcmeta
│  │     │  │  │  │  ├─ page_backward.png
│  │     │  │  │  │  ├─ page_backward_highlighted.png
│  │     │  │  │  │  ├─ page_forward.png
│  │     │  │  │  │  ├─ page_forward_highlighted.png
│  │     │  │  │  │  ├─ slot_craftable.png
│  │     │  │  │  │  ├─ slot_many_craftable.png
│  │     │  │  │  │  ├─ slot_many_uncraftable.png
│  │     │  │  │  │  ├─ slot_uncraftable.png
│  │     │  │  │  │  ├─ tab.png
│  │     │  │  │  │  └─ tab_selected.png
│  │     │  │  │  ├─ server_list
│  │     │  │  │  │  ├─ incompatible.png
│  │     │  │  │  │  ├─ join.png
│  │     │  │  │  │  ├─ join_highlighted.png
│  │     │  │  │  │  ├─ move_down.png
│  │     │  │  │  │  ├─ move_down_highlighted.png
│  │     │  │  │  │  ├─ move_up.png
│  │     │  │  │  │  ├─ move_up_highlighted.png
│  │     │  │  │  │  ├─ pinging_1.png
│  │     │  │  │  │  ├─ pinging_2.png
│  │     │  │  │  │  ├─ pinging_3.png
│  │     │  │  │  │  ├─ pinging_4.png
│  │     │  │  │  │  ├─ pinging_5.png
│  │     │  │  │  │  ├─ ping_1.png
│  │     │  │  │  │  ├─ ping_2.png
│  │     │  │  │  │  ├─ ping_3.png
│  │     │  │  │  │  ├─ ping_4.png
│  │     │  │  │  │  ├─ ping_5.png
│  │     │  │  │  │  └─ unreachable.png
│  │     │  │  │  ├─ social_interactions
│  │     │  │  │  │  ├─ background.png
│  │     │  │  │  │  ├─ background.png.mcmeta
│  │     │  │  │  │  ├─ mute_button.png
│  │     │  │  │  │  ├─ mute_button_highlighted.png
│  │     │  │  │  │  ├─ report_button.png
│  │     │  │  │  │  ├─ report_button_disabled.png
│  │     │  │  │  │  ├─ report_button_highlighted.png
│  │     │  │  │  │  ├─ unmute_button.png
│  │     │  │  │  │  └─ unmute_button_highlighted.png
│  │     │  │  │  ├─ spectator
│  │     │  │  │  │  ├─ close.png
│  │     │  │  │  │  ├─ scroll_left.png
│  │     │  │  │  │  ├─ scroll_right.png
│  │     │  │  │  │  ├─ teleport_to_player.png
│  │     │  │  │  │  └─ teleport_to_team.png
│  │     │  │  │  ├─ statistics
│  │     │  │  │  │  ├─ block_mined.png
│  │     │  │  │  │  ├─ header.png
│  │     │  │  │  │  ├─ item_broken.png
│  │     │  │  │  │  ├─ item_crafted.png
│  │     │  │  │  │  ├─ item_dropped.png
│  │     │  │  │  │  ├─ item_picked_up.png
│  │     │  │  │  │  ├─ item_used.png
│  │     │  │  │  │  ├─ sort_down.png
│  │     │  │  │  │  └─ sort_up.png
│  │     │  │  │  ├─ toast
│  │     │  │  │  │  ├─ advancement.png
│  │     │  │  │  │  ├─ mouse.png
│  │     │  │  │  │  ├─ movement_keys.png
│  │     │  │  │  │  ├─ now_playing.png
│  │     │  │  │  │  ├─ now_playing.png.mcmeta
│  │     │  │  │  │  ├─ recipe.png
│  │     │  │  │  │  ├─ recipe_book.png
│  │     │  │  │  │  ├─ right_click.png
│  │     │  │  │  │  ├─ social_interactions.png
│  │     │  │  │  │  ├─ system.png
│  │     │  │  │  │  ├─ system.png.mcmeta
│  │     │  │  │  │  ├─ tree.png
│  │     │  │  │  │  ├─ tutorial.png
│  │     │  │  │  │  ├─ tutorial.png.mcmeta
│  │     │  │  │  │  └─ wooden_planks.png
│  │     │  │  │  ├─ tooltip
│  │     │  │  │  │  ├─ background.png
│  │     │  │  │  │  ├─ background.png.mcmeta
│  │     │  │  │  │  ├─ frame.png
│  │     │  │  │  │  └─ frame.png.mcmeta
│  │     │  │  │  ├─ transferable_list
│  │     │  │  │  │  ├─ move_down.png
│  │     │  │  │  │  ├─ move_down_highlighted.png
│  │     │  │  │  │  ├─ move_up.png
│  │     │  │  │  │  ├─ move_up_highlighted.png
│  │     │  │  │  │  ├─ select.png
│  │     │  │  │  │  ├─ select_highlighted.png
│  │     │  │  │  │  ├─ unselect.png
│  │     │  │  │  │  └─ unselect_highlighted.png
│  │     │  │  │  ├─ widget
│  │     │  │  │  │  ├─ button.png
│  │     │  │  │  │  ├─ button.png.mcmeta
│  │     │  │  │  │  ├─ button_disabled.png
│  │     │  │  │  │  ├─ button_disabled.png.mcmeta
│  │     │  │  │  │  ├─ button_highlighted.png
│  │     │  │  │  │  ├─ button_highlighted.png.mcmeta
│  │     │  │  │  │  ├─ checkbox.png
│  │     │  │  │  │  ├─ checkbox_highlighted.png
│  │     │  │  │  │  ├─ checkbox_selected.png
│  │     │  │  │  │  ├─ checkbox_selected_highlighted.png
│  │     │  │  │  │  ├─ cross_button.png
│  │     │  │  │  │  ├─ cross_button_highlighted.png
│  │     │  │  │  │  ├─ locked_button.png
│  │     │  │  │  │  ├─ locked_button_disabled.png
│  │     │  │  │  │  ├─ locked_button_highlighted.png
│  │     │  │  │  │  ├─ page_backward.png
│  │     │  │  │  │  ├─ page_backward_highlighted.png
│  │     │  │  │  │  ├─ page_forward.png
│  │     │  │  │  │  ├─ page_forward_highlighted.png
│  │     │  │  │  │  ├─ scroller.png
│  │     │  │  │  │  ├─ scroller.png.mcmeta
│  │     │  │  │  │  ├─ scroller_background.png
│  │     │  │  │  │  ├─ scroller_background.png.mcmeta
│  │     │  │  │  │  ├─ slider.png
│  │     │  │  │  │  ├─ slider.png.mcmeta
│  │     │  │  │  │  ├─ slider_handle.png
│  │     │  │  │  │  ├─ slider_handle.png.mcmeta
│  │     │  │  │  │  ├─ slider_handle_highlighted.png
│  │     │  │  │  │  ├─ slider_handle_highlighted.png.mcmeta
│  │     │  │  │  │  ├─ slider_highlighted.png
│  │     │  │  │  │  ├─ slider_highlighted.png.mcmeta
│  │     │  │  │  │  ├─ slot_frame.png
│  │     │  │  │  │  ├─ tab.png
│  │     │  │  │  │  ├─ tab.png.mcmeta
│  │     │  │  │  │  ├─ tab_highlighted.png
│  │     │  │  │  │  ├─ tab_highlighted.png.mcmeta
│  │     │  │  │  │  ├─ tab_selected.png
│  │     │  │  │  │  ├─ tab_selected.png.mcmeta
│  │     │  │  │  │  ├─ tab_selected_highlighted.png
│  │     │  │  │  │  ├─ tab_selected_highlighted.png.mcmeta
│  │     │  │  │  │  ├─ text_field.png
│  │     │  │  │  │  ├─ text_field.png.mcmeta
│  │     │  │  │  │  ├─ text_field_highlighted.png
│  │     │  │  │  │  ├─ text_field_highlighted.png.mcmeta
│  │     │  │  │  │  ├─ unlocked_button.png
│  │     │  │  │  │  ├─ unlocked_button_disabled.png
│  │     │  │  │  │  └─ unlocked_button_highlighted.png
│  │     │  │  │  └─ world_list
│  │     │  │  │     ├─ error.png
│  │     │  │  │     ├─ error_highlighted.png
│  │     │  │  │     ├─ join.png
│  │     │  │  │     ├─ join_highlighted.png
│  │     │  │  │     ├─ marked_join.png
│  │     │  │  │     ├─ marked_join_highlighted.png
│  │     │  │  │     ├─ warning.png
│  │     │  │  │     └─ warning_highlighted.png
│  │     │  │  ├─ tab_header_background.png
│  │     │  │  └─ title
│  │     │  │     ├─ background
│  │     │  │     │  ├─ panorama_0.png
│  │     │  │     │  ├─ panorama_1.png
│  │     │  │     │  ├─ panorama_2.png
│  │     │  │     │  ├─ panorama_3.png
│  │     │  │     │  ├─ panorama_4.png
│  │     │  │     │  ├─ panorama_5.png
│  │     │  │     │  └─ panorama_overlay.png
│  │     │  │     ├─ edition.png
│  │     │  │     ├─ minceraft.png
│  │     │  │     ├─ minecraft.png
│  │     │  │     ├─ mojangstudios.png
│  │     │  │     └─ realms.png
│  │     │  ├─ item
│  │     │  │  ├─ acacia_boat.png
│  │     │  │  ├─ acacia_chest_boat.png
│  │     │  │  ├─ acacia_door.png
│  │     │  │  ├─ acacia_hanging_sign.png
│  │     │  │  ├─ acacia_sign.png
│  │     │  │  ├─ allay_spawn_egg.png
│  │     │  │  ├─ amethyst_shard.png
│  │     │  │  ├─ angler_pottery_sherd.png
│  │     │  │  ├─ apple.png
│  │     │  │  ├─ archer_pottery_sherd.png
│  │     │  │  ├─ armadillo_scute.png
│  │     │  │  ├─ armadillo_spawn_egg.png
│  │     │  │  ├─ armor_stand.png
│  │     │  │  ├─ arms_up_pottery_sherd.png
│  │     │  │  ├─ arrow.png
│  │     │  │  ├─ axolotl_bucket.png
│  │     │  │  ├─ axolotl_spawn_egg.png
│  │     │  │  ├─ baked_potato.png
│  │     │  │  ├─ bamboo.png
│  │     │  │  ├─ bamboo_chest_raft.png
│  │     │  │  ├─ bamboo_door.png
│  │     │  │  ├─ bamboo_hanging_sign.png
│  │     │  │  ├─ bamboo_raft.png
│  │     │  │  ├─ bamboo_sign.png
│  │     │  │  ├─ barrier.png
│  │     │  │  ├─ bat_spawn_egg.png
│  │     │  │  ├─ beef.png
│  │     │  │  ├─ beetroot.png
│  │     │  │  ├─ beetroot_seeds.png
│  │     │  │  ├─ beetroot_soup.png
│  │     │  │  ├─ bee_spawn_egg.png
│  │     │  │  ├─ bell.png
│  │     │  │  ├─ birch_boat.png
│  │     │  │  ├─ birch_chest_boat.png
│  │     │  │  ├─ birch_door.png
│  │     │  │  ├─ birch_hanging_sign.png
│  │     │  │  ├─ birch_sign.png
│  │     │  │  ├─ black_bundle.png
│  │     │  │  ├─ black_bundle_open_back.png
│  │     │  │  ├─ black_bundle_open_front.png
│  │     │  │  ├─ black_candle.png
│  │     │  │  ├─ black_dye.png
│  │     │  │  ├─ black_harness.png
│  │     │  │  ├─ blade_pottery_sherd.png
│  │     │  │  ├─ blaze_powder.png
│  │     │  │  ├─ blaze_rod.png
│  │     │  │  ├─ blaze_spawn_egg.png
│  │     │  │  ├─ blue_bundle.png
│  │     │  │  ├─ blue_bundle_open_back.png
│  │     │  │  ├─ blue_bundle_open_front.png
│  │     │  │  ├─ blue_candle.png
│  │     │  │  ├─ blue_dye.png
│  │     │  │  ├─ blue_egg.png
│  │     │  │  ├─ blue_harness.png
│  │     │  │  ├─ bogged_spawn_egg.png
│  │     │  │  ├─ bolt_armor_trim_smithing_template.png
│  │     │  │  ├─ bone.png
│  │     │  │  ├─ bone_meal.png
│  │     │  │  ├─ book.png
│  │     │  │  ├─ bordure_indented_banner_pattern.png
│  │     │  │  ├─ bow.png
│  │     │  │  ├─ bowl.png
│  │     │  │  ├─ bow_pulling_0.png
│  │     │  │  ├─ bow_pulling_1.png
│  │     │  │  ├─ bow_pulling_2.png
│  │     │  │  ├─ bread.png
│  │     │  │  ├─ breeze_rod.png
│  │     │  │  ├─ breeze_spawn_egg.png
│  │     │  │  ├─ brewer_pottery_sherd.png
│  │     │  │  ├─ brewing_stand.png
│  │     │  │  ├─ brick.png
│  │     │  │  ├─ brown_bundle.png
│  │     │  │  ├─ brown_bundle_open_back.png
│  │     │  │  ├─ brown_bundle_open_front.png
│  │     │  │  ├─ brown_candle.png
│  │     │  │  ├─ brown_dye.png
│  │     │  │  ├─ brown_egg.png
│  │     │  │  ├─ brown_harness.png
│  │     │  │  ├─ brush.png
│  │     │  │  ├─ bucket.png
│  │     │  │  ├─ bundle.png
│  │     │  │  ├─ bundle_open_back.png
│  │     │  │  ├─ bundle_open_front.png
│  │     │  │  ├─ burn_pottery_sherd.png
│  │     │  │  ├─ cake.png
│  │     │  │  ├─ camel_husk_spawn_egg.png
│  │     │  │  ├─ camel_spawn_egg.png
│  │     │  │  ├─ campfire.png
│  │     │  │  ├─ candle.png
│  │     │  │  ├─ carrot.png
│  │     │  │  ├─ carrot_on_a_stick.png
│  │     │  │  ├─ cat_spawn_egg.png
│  │     │  │  ├─ cauldron.png
│  │     │  │  ├─ cave_spider_spawn_egg.png
│  │     │  │  ├─ chainmail_boots.png
│  │     │  │  ├─ chainmail_chestplate.png
│  │     │  │  ├─ chainmail_helmet.png
│  │     │  │  ├─ chainmail_leggings.png
│  │     │  │  ├─ charcoal.png
│  │     │  │  ├─ cherry_boat.png
│  │     │  │  ├─ cherry_chest_boat.png
│  │     │  │  ├─ cherry_door.png
│  │     │  │  ├─ cherry_hanging_sign.png
│  │     │  │  ├─ cherry_sign.png
│  │     │  │  ├─ chest_minecart.png
│  │     │  │  ├─ chicken.png
│  │     │  │  ├─ chicken_spawn_egg.png
│  │     │  │  ├─ chorus_fruit.png
│  │     │  │  ├─ clay_ball.png
│  │     │  │  ├─ clock_00.png
│  │     │  │  ├─ clock_01.png
│  │     │  │  ├─ clock_02.png
│  │     │  │  ├─ clock_03.png
│  │     │  │  ├─ clock_04.png
│  │     │  │  ├─ clock_05.png
│  │     │  │  ├─ clock_06.png
│  │     │  │  ├─ clock_07.png
│  │     │  │  ├─ clock_08.png
│  │     │  │  ├─ clock_09.png
│  │     │  │  ├─ clock_10.png
│  │     │  │  ├─ clock_11.png
│  │     │  │  ├─ clock_12.png
│  │     │  │  ├─ clock_13.png
│  │     │  │  ├─ clock_14.png
│  │     │  │  ├─ clock_15.png
│  │     │  │  ├─ clock_16.png
│  │     │  │  ├─ clock_17.png
│  │     │  │  ├─ clock_18.png
│  │     │  │  ├─ clock_19.png
│  │     │  │  ├─ clock_20.png
│  │     │  │  ├─ clock_21.png
│  │     │  │  ├─ clock_22.png
│  │     │  │  ├─ clock_23.png
│  │     │  │  ├─ clock_24.png
│  │     │  │  ├─ clock_25.png
│  │     │  │  ├─ clock_26.png
│  │     │  │  ├─ clock_27.png
│  │     │  │  ├─ clock_28.png
│  │     │  │  ├─ clock_29.png
│  │     │  │  ├─ clock_30.png
│  │     │  │  ├─ clock_31.png
│  │     │  │  ├─ clock_32.png
│  │     │  │  ├─ clock_33.png
│  │     │  │  ├─ clock_34.png
│  │     │  │  ├─ clock_35.png
│  │     │  │  ├─ clock_36.png
│  │     │  │  ├─ clock_37.png
│  │     │  │  ├─ clock_38.png
│  │     │  │  ├─ clock_39.png
│  │     │  │  ├─ clock_40.png
│  │     │  │  ├─ clock_41.png
│  │     │  │  ├─ clock_42.png
│  │     │  │  ├─ clock_43.png
│  │     │  │  ├─ clock_44.png
│  │     │  │  ├─ clock_45.png
│  │     │  │  ├─ clock_46.png
│  │     │  │  ├─ clock_47.png
│  │     │  │  ├─ clock_48.png
│  │     │  │  ├─ clock_49.png
│  │     │  │  ├─ clock_50.png
│  │     │  │  ├─ clock_51.png
│  │     │  │  ├─ clock_52.png
│  │     │  │  ├─ clock_53.png
│  │     │  │  ├─ clock_54.png
│  │     │  │  ├─ clock_55.png
│  │     │  │  ├─ clock_56.png
│  │     │  │  ├─ clock_57.png
│  │     │  │  ├─ clock_58.png
│  │     │  │  ├─ clock_59.png
│  │     │  │  ├─ clock_60.png
│  │     │  │  ├─ clock_61.png
│  │     │  │  ├─ clock_62.png
│  │     │  │  ├─ clock_63.png
│  │     │  │  ├─ coal.png
│  │     │  │  ├─ coast_armor_trim_smithing_template.png
│  │     │  │  ├─ cocoa_beans.png
│  │     │  │  ├─ cod.png
│  │     │  │  ├─ cod_bucket.png
│  │     │  │  ├─ cod_spawn_egg.png
│  │     │  │  ├─ command_block_minecart.png
│  │     │  │  ├─ comparator.png
│  │     │  │  ├─ compass_00.png
│  │     │  │  ├─ compass_01.png
│  │     │  │  ├─ compass_02.png
│  │     │  │  ├─ compass_03.png
│  │     │  │  ├─ compass_04.png
│  │     │  │  ├─ compass_05.png
│  │     │  │  ├─ compass_06.png
│  │     │  │  ├─ compass_07.png
│  │     │  │  ├─ compass_08.png
│  │     │  │  ├─ compass_09.png
│  │     │  │  ├─ compass_10.png
│  │     │  │  ├─ compass_11.png
│  │     │  │  ├─ compass_12.png
│  │     │  │  ├─ compass_13.png
│  │     │  │  ├─ compass_14.png
│  │     │  │  ├─ compass_15.png
│  │     │  │  ├─ compass_16.png
│  │     │  │  ├─ compass_17.png
│  │     │  │  ├─ compass_18.png
│  │     │  │  ├─ compass_19.png
│  │     │  │  ├─ compass_20.png
│  │     │  │  ├─ compass_21.png
│  │     │  │  ├─ compass_22.png
│  │     │  │  ├─ compass_23.png
│  │     │  │  ├─ compass_24.png
│  │     │  │  ├─ compass_25.png
│  │     │  │  ├─ compass_26.png
│  │     │  │  ├─ compass_27.png
│  │     │  │  ├─ compass_28.png
│  │     │  │  ├─ compass_29.png
│  │     │  │  ├─ compass_30.png
│  │     │  │  ├─ compass_31.png
│  │     │  │  ├─ cooked_beef.png
│  │     │  │  ├─ cooked_chicken.png
│  │     │  │  ├─ cooked_cod.png
│  │     │  │  ├─ cooked_mutton.png
│  │     │  │  ├─ cooked_porkchop.png
│  │     │  │  ├─ cooked_rabbit.png
│  │     │  │  ├─ cooked_salmon.png
│  │     │  │  ├─ cookie.png
│  │     │  │  ├─ copper_axe.png
│  │     │  │  ├─ copper_boots.png
│  │     │  │  ├─ copper_chain.png
│  │     │  │  ├─ copper_chestplate.png
│  │     │  │  ├─ copper_door.png
│  │     │  │  ├─ copper_golem_spawn_egg.png
│  │     │  │  ├─ copper_helmet.png
│  │     │  │  ├─ copper_hoe.png
│  │     │  │  ├─ copper_horse_armor.png
│  │     │  │  ├─ copper_ingot.png
│  │     │  │  ├─ copper_lantern.png
│  │     │  │  ├─ copper_leggings.png
│  │     │  │  ├─ copper_nautilus_armor.png
│  │     │  │  ├─ copper_nugget.png
│  │     │  │  ├─ copper_pickaxe.png
│  │     │  │  ├─ copper_shovel.png
│  │     │  │  ├─ copper_spear.png
│  │     │  │  ├─ copper_spear_in_hand.png
│  │     │  │  ├─ copper_sword.png
│  │     │  │  ├─ cow_spawn_egg.png
│  │     │  │  ├─ creaking_spawn_egg.png
│  │     │  │  ├─ creeper_banner_pattern.png
│  │     │  │  ├─ creeper_spawn_egg.png
│  │     │  │  ├─ crimson_door.png
│  │     │  │  ├─ crimson_hanging_sign.png
│  │     │  │  ├─ crimson_sign.png
│  │     │  │  ├─ crossbow_arrow.png
│  │     │  │  ├─ crossbow_firework.png
│  │     │  │  ├─ crossbow_pulling_0.png
│  │     │  │  ├─ crossbow_pulling_1.png
│  │     │  │  ├─ crossbow_pulling_2.png
│  │     │  │  ├─ crossbow_standby.png
│  │     │  │  ├─ cyan_bundle.png
│  │     │  │  ├─ cyan_bundle_open_back.png
│  │     │  │  ├─ cyan_bundle_open_front.png
│  │     │  │  ├─ cyan_candle.png
│  │     │  │  ├─ cyan_dye.png
│  │     │  │  ├─ cyan_harness.png
│  │     │  │  ├─ danger_pottery_sherd.png
│  │     │  │  ├─ dark_oak_boat.png
│  │     │  │  ├─ dark_oak_chest_boat.png
│  │     │  │  ├─ dark_oak_door.png
│  │     │  │  ├─ dark_oak_hanging_sign.png
│  │     │  │  ├─ dark_oak_sign.png
│  │     │  │  ├─ diamond.png
│  │     │  │  ├─ diamond_axe.png
│  │     │  │  ├─ diamond_boots.png
│  │     │  │  ├─ diamond_chestplate.png
│  │     │  │  ├─ diamond_helmet.png
│  │     │  │  ├─ diamond_hoe.png
│  │     │  │  ├─ diamond_horse_armor.png
│  │     │  │  ├─ diamond_leggings.png
│  │     │  │  ├─ diamond_nautilus_armor.png
│  │     │  │  ├─ diamond_pickaxe.png
│  │     │  │  ├─ diamond_shovel.png
│  │     │  │  ├─ diamond_spear.png
│  │     │  │  ├─ diamond_spear_in_hand.png
│  │     │  │  ├─ diamond_sword.png
│  │     │  │  ├─ disc_fragment_5.png
│  │     │  │  ├─ dolphin_spawn_egg.png
│  │     │  │  ├─ donkey_spawn_egg.png
│  │     │  │  ├─ dragon_breath.png
│  │     │  │  ├─ dried_kelp.png
│  │     │  │  ├─ drowned_spawn_egg.png
│  │     │  │  ├─ dune_armor_trim_smithing_template.png
│  │     │  │  ├─ echo_shard.png
│  │     │  │  ├─ egg.png
│  │     │  │  ├─ elder_guardian_spawn_egg.png
│  │     │  │  ├─ elytra.png
│  │     │  │  ├─ elytra_broken.png
│  │     │  │  ├─ emerald.png
│  │     │  │  ├─ enchanted_book.png
│  │     │  │  ├─ enderman_spawn_egg.png
│  │     │  │  ├─ endermite_spawn_egg.png
│  │     │  │  ├─ ender_dragon_spawn_egg.png
│  │     │  │  ├─ ender_eye.png
│  │     │  │  ├─ ender_pearl.png
│  │     │  │  ├─ end_crystal.png
│  │     │  │  ├─ evoker_spawn_egg.png
│  │     │  │  ├─ experience_bottle.png
│  │     │  │  ├─ explorer_pottery_sherd.png
│  │     │  │  ├─ exposed_copper_chain.png
│  │     │  │  ├─ exposed_copper_door.png
│  │     │  │  ├─ exposed_copper_lantern.png
│  │     │  │  ├─ eye_armor_trim_smithing_template.png
│  │     │  │  ├─ feather.png
│  │     │  │  ├─ fermented_spider_eye.png
│  │     │  │  ├─ field_masoned_banner_pattern.png
│  │     │  │  ├─ filled_map.png
│  │     │  │  ├─ filled_map_markings.png
│  │     │  │  ├─ firefly_bush.png
│  │     │  │  ├─ firework_rocket.png
│  │     │  │  ├─ firework_star.png
│  │     │  │  ├─ firework_star_overlay.png
│  │     │  │  ├─ fire_charge.png
│  │     │  │  ├─ fishing_rod.png
│  │     │  │  ├─ fishing_rod_cast.png
│  │     │  │  ├─ flint.png
│  │     │  │  ├─ flint_and_steel.png
│  │     │  │  ├─ flower_banner_pattern.png
│  │     │  │  ├─ flower_pot.png
│  │     │  │  ├─ flow_armor_trim_smithing_template.png
│  │     │  │  ├─ flow_banner_pattern.png
│  │     │  │  ├─ flow_pottery_sherd.png
│  │     │  │  ├─ fox_spawn_egg.png
│  │     │  │  ├─ friend_pottery_sherd.png
│  │     │  │  ├─ frog_spawn_egg.png
│  │     │  │  ├─ furnace_minecart.png
│  │     │  │  ├─ ghast_spawn_egg.png
│  │     │  │  ├─ ghast_tear.png
│  │     │  │  ├─ glass_bottle.png
│  │     │  │  ├─ glistering_melon_slice.png
│  │     │  │  ├─ globe_banner_pattern.png
│  │     │  │  ├─ glowstone_dust.png
│  │     │  │  ├─ glow_berries.png
│  │     │  │  ├─ glow_ink_sac.png
│  │     │  │  ├─ glow_item_frame.png
│  │     │  │  ├─ glow_squid_spawn_egg.png
│  │     │  │  ├─ goat_horn.png
│  │     │  │  ├─ goat_spawn_egg.png
│  │     │  │  ├─ golden_apple.png
│  │     │  │  ├─ golden_axe.png
│  │     │  │  ├─ golden_boots.png
│  │     │  │  ├─ golden_carrot.png
│  │     │  │  ├─ golden_chestplate.png
│  │     │  │  ├─ golden_helmet.png
│  │     │  │  ├─ golden_hoe.png
│  │     │  │  ├─ golden_horse_armor.png
│  │     │  │  ├─ golden_leggings.png
│  │     │  │  ├─ golden_nautilus_armor.png
│  │     │  │  ├─ golden_pickaxe.png
│  │     │  │  ├─ golden_shovel.png
│  │     │  │  ├─ golden_spear.png
│  │     │  │  ├─ golden_spear_in_hand.png
│  │     │  │  ├─ golden_sword.png
│  │     │  │  ├─ gold_ingot.png
│  │     │  │  ├─ gold_nugget.png
│  │     │  │  ├─ gray_bundle.png
│  │     │  │  ├─ gray_bundle_open_back.png
│  │     │  │  ├─ gray_bundle_open_front.png
│  │     │  │  ├─ gray_candle.png
│  │     │  │  ├─ gray_dye.png
│  │     │  │  ├─ gray_harness.png
│  │     │  │  ├─ green_bundle.png
│  │     │  │  ├─ green_bundle_open_back.png
│  │     │  │  ├─ green_bundle_open_front.png
│  │     │  │  ├─ green_candle.png
│  │     │  │  ├─ green_dye.png
│  │     │  │  ├─ green_harness.png
│  │     │  │  ├─ guardian_spawn_egg.png
│  │     │  │  ├─ gunpowder.png
│  │     │  │  ├─ guster_banner_pattern.png
│  │     │  │  ├─ guster_pottery_sherd.png
│  │     │  │  ├─ happy_ghast_spawn_egg.png
│  │     │  │  ├─ heartbreak_pottery_sherd.png
│  │     │  │  ├─ heart_of_the_sea.png
│  │     │  │  ├─ heart_pottery_sherd.png
│  │     │  │  ├─ hoglin_spawn_egg.png
│  │     │  │  ├─ honeycomb.png
│  │     │  │  ├─ honey_bottle.png
│  │     │  │  ├─ hopper.png
│  │     │  │  ├─ hopper_minecart.png
│  │     │  │  ├─ horse_spawn_egg.png
│  │     │  │  ├─ host_armor_trim_smithing_template.png
│  │     │  │  ├─ howl_pottery_sherd.png
│  │     │  │  ├─ husk_spawn_egg.png
│  │     │  │  ├─ ink_sac.png
│  │     │  │  ├─ iron_axe.png
│  │     │  │  ├─ iron_boots.png
│  │     │  │  ├─ iron_chain.png
│  │     │  │  ├─ iron_chestplate.png
│  │     │  │  ├─ iron_door.png
│  │     │  │  ├─ iron_golem_spawn_egg.png
│  │     │  │  ├─ iron_helmet.png
│  │     │  │  ├─ iron_hoe.png
│  │     │  │  ├─ iron_horse_armor.png
│  │     │  │  ├─ iron_ingot.png
│  │     │  │  ├─ iron_leggings.png
│  │     │  │  ├─ iron_nautilus_armor.png
│  │     │  │  ├─ iron_nugget.png
│  │     │  │  ├─ iron_pickaxe.png
│  │     │  │  ├─ iron_shovel.png
│  │     │  │  ├─ iron_spear.png
│  │     │  │  ├─ iron_spear_in_hand.png
│  │     │  │  ├─ iron_sword.png
│  │     │  │  ├─ item_frame.png
│  │     │  │  ├─ jungle_boat.png
│  │     │  │  ├─ jungle_chest_boat.png
│  │     │  │  ├─ jungle_door.png
│  │     │  │  ├─ jungle_hanging_sign.png
│  │     │  │  ├─ jungle_sign.png
│  │     │  │  ├─ kelp.png
│  │     │  │  ├─ knowledge_book.png
│  │     │  │  ├─ lantern.png
│  │     │  │  ├─ lapis_lazuli.png
│  │     │  │  ├─ lava_bucket.png
│  │     │  │  ├─ lead.png
│  │     │  │  ├─ leaf_litter.png
│  │     │  │  ├─ leather.png
│  │     │  │  ├─ leather_boots.png
│  │     │  │  ├─ leather_boots_overlay.png
│  │     │  │  ├─ leather_chestplate.png
│  │     │  │  ├─ leather_chestplate_overlay.png
│  │     │  │  ├─ leather_helmet.png
│  │     │  │  ├─ leather_helmet_overlay.png
│  │     │  │  ├─ leather_horse_armor.png
│  │     │  │  ├─ leather_horse_armor_overlay.png
│  │     │  │  ├─ leather_leggings.png
│  │     │  │  ├─ leather_leggings_overlay.png
│  │     │  │  ├─ light.png
│  │     │  │  ├─ light_00.png
│  │     │  │  ├─ light_01.png
│  │     │  │  ├─ light_02.png
│  │     │  │  ├─ light_03.png
│  │     │  │  ├─ light_04.png
│  │     │  │  ├─ light_05.png
│  │     │  │  ├─ light_06.png
│  │     │  │  ├─ light_07.png
│  │     │  │  ├─ light_08.png
│  │     │  │  ├─ light_09.png
│  │     │  │  ├─ light_10.png
│  │     │  │  ├─ light_11.png
│  │     │  │  ├─ light_12.png
│  │     │  │  ├─ light_13.png
│  │     │  │  ├─ light_14.png
│  │     │  │  ├─ light_15.png
│  │     │  │  ├─ light_blue_bundle.png
│  │     │  │  ├─ light_blue_bundle_open_back.png
│  │     │  │  ├─ light_blue_bundle_open_front.png
│  │     │  │  ├─ light_blue_candle.png
│  │     │  │  ├─ light_blue_dye.png
│  │     │  │  ├─ light_blue_harness.png
│  │     │  │  ├─ light_gray_bundle.png
│  │     │  │  ├─ light_gray_bundle_open_back.png
│  │     │  │  ├─ light_gray_bundle_open_front.png
│  │     │  │  ├─ light_gray_candle.png
│  │     │  │  ├─ light_gray_dye.png
│  │     │  │  ├─ light_gray_harness.png
│  │     │  │  ├─ lime_bundle.png
│  │     │  │  ├─ lime_bundle_open_back.png
│  │     │  │  ├─ lime_bundle_open_front.png
│  │     │  │  ├─ lime_candle.png
│  │     │  │  ├─ lime_dye.png
│  │     │  │  ├─ lime_harness.png
│  │     │  │  ├─ lingering_potion.png
│  │     │  │  ├─ llama_spawn_egg.png
│  │     │  │  ├─ mace.png
│  │     │  │  ├─ magenta_bundle.png
│  │     │  │  ├─ magenta_bundle_open_back.png
│  │     │  │  ├─ magenta_bundle_open_front.png
│  │     │  │  ├─ magenta_candle.png
│  │     │  │  ├─ magenta_dye.png
│  │     │  │  ├─ magenta_harness.png
│  │     │  │  ├─ magma_cream.png
│  │     │  │  ├─ magma_cube_spawn_egg.png
│  │     │  │  ├─ mangrove_boat.png
│  │     │  │  ├─ mangrove_chest_boat.png
│  │     │  │  ├─ mangrove_door.png
│  │     │  │  ├─ mangrove_hanging_sign.png
│  │     │  │  ├─ mangrove_propagule.png
│  │     │  │  ├─ mangrove_sign.png
│  │     │  │  ├─ map.png
│  │     │  │  ├─ melon_seeds.png
│  │     │  │  ├─ melon_slice.png
│  │     │  │  ├─ milk_bucket.png
│  │     │  │  ├─ minecart.png
│  │     │  │  ├─ miner_pottery_sherd.png
│  │     │  │  ├─ mojang_banner_pattern.png
│  │     │  │  ├─ mooshroom_spawn_egg.png
│  │     │  │  ├─ mourner_pottery_sherd.png
│  │     │  │  ├─ mule_spawn_egg.png
│  │     │  │  ├─ mushroom_stew.png
│  │     │  │  ├─ music_disc_11.png
│  │     │  │  ├─ music_disc_13.png
│  │     │  │  ├─ music_disc_5.png
│  │     │  │  ├─ music_disc_blocks.png
│  │     │  │  ├─ music_disc_cat.png
│  │     │  │  ├─ music_disc_chirp.png
│  │     │  │  ├─ music_disc_creator.png
│  │     │  │  ├─ music_disc_creator_music_box.png
│  │     │  │  ├─ music_disc_far.png
│  │     │  │  ├─ music_disc_lava_chicken.png
│  │     │  │  ├─ music_disc_mall.png
│  │     │  │  ├─ music_disc_mellohi.png
│  │     │  │  ├─ music_disc_otherside.png
│  │     │  │  ├─ music_disc_pigstep.png
│  │     │  │  ├─ music_disc_precipice.png
│  │     │  │  ├─ music_disc_relic.png
│  │     │  │  ├─ music_disc_stal.png
│  │     │  │  ├─ music_disc_strad.png
│  │     │  │  ├─ music_disc_tears.png
│  │     │  │  ├─ music_disc_wait.png
│  │     │  │  ├─ music_disc_ward.png
│  │     │  │  ├─ mutton.png
│  │     │  │  ├─ name_tag.png
│  │     │  │  ├─ nautilus_shell.png
│  │     │  │  ├─ nautilus_spawn_egg.png
│  │     │  │  ├─ netherite_axe.png
│  │     │  │  ├─ netherite_boots.png
│  │     │  │  ├─ netherite_chestplate.png
│  │     │  │  ├─ netherite_helmet.png
│  │     │  │  ├─ netherite_hoe.png
│  │     │  │  ├─ netherite_horse_armor.png
│  │     │  │  ├─ netherite_ingot.png
│  │     │  │  ├─ netherite_leggings.png
│  │     │  │  ├─ netherite_nautilus_armor.png
│  │     │  │  ├─ netherite_pickaxe.png
│  │     │  │  ├─ netherite_scrap.png
│  │     │  │  ├─ netherite_shovel.png
│  │     │  │  ├─ netherite_spear.png
│  │     │  │  ├─ netherite_spear_in_hand.png
│  │     │  │  ├─ netherite_sword.png
│  │     │  │  ├─ netherite_upgrade_smithing_template.png
│  │     │  │  ├─ nether_brick.png
│  │     │  │  ├─ nether_sprouts.png
│  │     │  │  ├─ nether_star.png
│  │     │  │  ├─ nether_wart.png
│  │     │  │  ├─ oak_boat.png
│  │     │  │  ├─ oak_chest_boat.png
│  │     │  │  ├─ oak_door.png
│  │     │  │  ├─ oak_hanging_sign.png
│  │     │  │  ├─ oak_sign.png
│  │     │  │  ├─ ocelot_spawn_egg.png
│  │     │  │  ├─ ominous_bottle.png
│  │     │  │  ├─ ominous_trial_key.png
│  │     │  │  ├─ orange_bundle.png
│  │     │  │  ├─ orange_bundle_open_back.png
│  │     │  │  ├─ orange_bundle_open_front.png
│  │     │  │  ├─ orange_candle.png
│  │     │  │  ├─ orange_dye.png
│  │     │  │  ├─ orange_harness.png
│  │     │  │  ├─ oxidized_copper_chain.png
│  │     │  │  ├─ oxidized_copper_door.png
│  │     │  │  ├─ oxidized_copper_lantern.png
│  │     │  │  ├─ painting.png
│  │     │  │  ├─ pale_oak_boat.png
│  │     │  │  ├─ pale_oak_chest_boat.png
│  │     │  │  ├─ pale_oak_door.png
│  │     │  │  ├─ pale_oak_hanging_sign.png
│  │     │  │  ├─ pale_oak_sign.png
│  │     │  │  ├─ panda_spawn_egg.png
│  │     │  │  ├─ paper.png
│  │     │  │  ├─ parched_spawn_egg.png
│  │     │  │  ├─ parrot_spawn_egg.png
│  │     │  │  ├─ phantom_membrane.png
│  │     │  │  ├─ phantom_spawn_egg.png
│  │     │  │  ├─ piglin_banner_pattern.png
│  │     │  │  ├─ piglin_brute_spawn_egg.png
│  │     │  │  ├─ piglin_spawn_egg.png
│  │     │  │  ├─ pig_spawn_egg.png
│  │     │  │  ├─ pillager_spawn_egg.png
│  │     │  │  ├─ pink_bundle.png
│  │     │  │  ├─ pink_bundle_open_back.png
│  │     │  │  ├─ pink_bundle_open_front.png
│  │     │  │  ├─ pink_candle.png
│  │     │  │  ├─ pink_dye.png
│  │     │  │  ├─ pink_harness.png
│  │     │  │  ├─ pink_petals.png
│  │     │  │  ├─ pitcher_plant.png
│  │     │  │  ├─ pitcher_pod.png
│  │     │  │  ├─ plenty_pottery_sherd.png
│  │     │  │  ├─ pointed_dripstone.png
│  │     │  │  ├─ poisonous_potato.png
│  │     │  │  ├─ polar_bear_spawn_egg.png
│  │     │  │  ├─ popped_chorus_fruit.png
│  │     │  │  ├─ porkchop.png
│  │     │  │  ├─ potato.png
│  │     │  │  ├─ potion.png
│  │     │  │  ├─ potion_overlay.png
│  │     │  │  ├─ powder_snow_bucket.png
│  │     │  │  ├─ prismarine_crystals.png
│  │     │  │  ├─ prismarine_shard.png
│  │     │  │  ├─ prize_pottery_sherd.png
│  │     │  │  ├─ pufferfish.png
│  │     │  │  ├─ pufferfish_bucket.png
│  │     │  │  ├─ pufferfish_spawn_egg.png
│  │     │  │  ├─ pumpkin_pie.png
│  │     │  │  ├─ pumpkin_seeds.png
│  │     │  │  ├─ purple_bundle.png
│  │     │  │  ├─ purple_bundle_open_back.png
│  │     │  │  ├─ purple_bundle_open_front.png
│  │     │  │  ├─ purple_candle.png
│  │     │  │  ├─ purple_dye.png
│  │     │  │  ├─ purple_harness.png
│  │     │  │  ├─ quartz.png
│  │     │  │  ├─ rabbit.png
│  │     │  │  ├─ rabbit_foot.png
│  │     │  │  ├─ rabbit_hide.png
│  │     │  │  ├─ rabbit_spawn_egg.png
│  │     │  │  ├─ rabbit_stew.png
│  │     │  │  ├─ raiser_armor_trim_smithing_template.png
│  │     │  │  ├─ ravager_spawn_egg.png
│  │     │  │  ├─ raw_copper.png
│  │     │  │  ├─ raw_gold.png
│  │     │  │  ├─ raw_iron.png
│  │     │  │  ├─ recovery_compass_00.png
│  │     │  │  ├─ recovery_compass_01.png
│  │     │  │  ├─ recovery_compass_02.png
│  │     │  │  ├─ recovery_compass_03.png
│  │     │  │  ├─ recovery_compass_04.png
│  │     │  │  ├─ recovery_compass_05.png
│  │     │  │  ├─ recovery_compass_06.png
│  │     │  │  ├─ recovery_compass_07.png
│  │     │  │  ├─ recovery_compass_08.png
│  │     │  │  ├─ recovery_compass_09.png
│  │     │  │  ├─ recovery_compass_10.png
│  │     │  │  ├─ recovery_compass_11.png
│  │     │  │  ├─ recovery_compass_12.png
│  │     │  │  ├─ recovery_compass_13.png
│  │     │  │  ├─ recovery_compass_14.png
│  │     │  │  ├─ recovery_compass_15.png
│  │     │  │  ├─ recovery_compass_16.png
│  │     │  │  ├─ recovery_compass_17.png
│  │     │  │  ├─ recovery_compass_18.png
│  │     │  │  ├─ recovery_compass_19.png
│  │     │  │  ├─ recovery_compass_20.png
│  │     │  │  ├─ recovery_compass_21.png
│  │     │  │  ├─ recovery_compass_22.png
│  │     │  │  ├─ recovery_compass_23.png
│  │     │  │  ├─ recovery_compass_24.png
│  │     │  │  ├─ recovery_compass_25.png
│  │     │  │  ├─ recovery_compass_26.png
│  │     │  │  ├─ recovery_compass_27.png
│  │     │  │  ├─ recovery_compass_28.png
│  │     │  │  ├─ recovery_compass_29.png
│  │     │  │  ├─ recovery_compass_30.png
│  │     │  │  ├─ recovery_compass_31.png
│  │     │  │  ├─ redstone.png
│  │     │  │  ├─ red_bundle.png
│  │     │  │  ├─ red_bundle_open_back.png
│  │     │  │  ├─ red_bundle_open_front.png
│  │     │  │  ├─ red_candle.png
│  │     │  │  ├─ red_dye.png
│  │     │  │  ├─ red_harness.png
│  │     │  │  ├─ repeater.png
│  │     │  │  ├─ resin_brick.png
│  │     │  │  ├─ resin_clump.png
│  │     │  │  ├─ rib_armor_trim_smithing_template.png
│  │     │  │  ├─ rotten_flesh.png
│  │     │  │  ├─ saddle.png
│  │     │  │  ├─ salmon.png
│  │     │  │  ├─ salmon_bucket.png
│  │     │  │  ├─ salmon_spawn_egg.png
│  │     │  │  ├─ scrape_pottery_sherd.png
│  │     │  │  ├─ seagrass.png
│  │     │  │  ├─ sea_pickle.png
│  │     │  │  ├─ sentry_armor_trim_smithing_template.png
│  │     │  │  ├─ shaper_armor_trim_smithing_template.png
│  │     │  │  ├─ sheaf_pottery_sherd.png
│  │     │  │  ├─ shears.png
│  │     │  │  ├─ sheep_spawn_egg.png
│  │     │  │  ├─ shelter_pottery_sherd.png
│  │     │  │  ├─ shulker_shell.png
│  │     │  │  ├─ shulker_spawn_egg.png
│  │     │  │  ├─ silence_armor_trim_smithing_template.png
│  │     │  │  ├─ silverfish_spawn_egg.png
│  │     │  │  ├─ skeleton_horse_spawn_egg.png
│  │     │  │  ├─ skeleton_spawn_egg.png
│  │     │  │  ├─ skull_banner_pattern.png
│  │     │  │  ├─ skull_pottery_sherd.png
│  │     │  │  ├─ slime_ball.png
│  │     │  │  ├─ slime_spawn_egg.png
│  │     │  │  ├─ sniffer_egg.png
│  │     │  │  ├─ sniffer_spawn_egg.png
│  │     │  │  ├─ snort_pottery_sherd.png
│  │     │  │  ├─ snout_armor_trim_smithing_template.png
│  │     │  │  ├─ snowball.png
│  │     │  │  ├─ snow_golem_spawn_egg.png
│  │     │  │  ├─ soul_campfire.png
│  │     │  │  ├─ soul_lantern.png
│  │     │  │  ├─ spectral_arrow.png
│  │     │  │  ├─ spider_eye.png
│  │     │  │  ├─ spider_spawn_egg.png
│  │     │  │  ├─ spire_armor_trim_smithing_template.png
│  │     │  │  ├─ splash_potion.png
│  │     │  │  ├─ spruce_boat.png
│  │     │  │  ├─ spruce_chest_boat.png
│  │     │  │  ├─ spruce_door.png
│  │     │  │  ├─ spruce_hanging_sign.png
│  │     │  │  ├─ spruce_sign.png
│  │     │  │  ├─ spyglass.png
│  │     │  │  ├─ spyglass_model.png
│  │     │  │  ├─ squid_spawn_egg.png
│  │     │  │  ├─ stick.png
│  │     │  │  ├─ stone_axe.png
│  │     │  │  ├─ stone_hoe.png
│  │     │  │  ├─ stone_pickaxe.png
│  │     │  │  ├─ stone_shovel.png
│  │     │  │  ├─ stone_spear.png
│  │     │  │  ├─ stone_spear_in_hand.png
│  │     │  │  ├─ stone_sword.png
│  │     │  │  ├─ stray_spawn_egg.png
│  │     │  │  ├─ strider_spawn_egg.png
│  │     │  │  ├─ string.png
│  │     │  │  ├─ structure_void.png
│  │     │  │  ├─ sugar.png
│  │     │  │  ├─ sugar_cane.png
│  │     │  │  ├─ suspicious_stew.png
│  │     │  │  ├─ sweet_berries.png
│  │     │  │  ├─ tadpole_bucket.png
│  │     │  │  ├─ tadpole_spawn_egg.png
│  │     │  │  ├─ tide_armor_trim_smithing_template.png
│  │     │  │  ├─ tipped_arrow_base.png
│  │     │  │  ├─ tipped_arrow_head.png
│  │     │  │  ├─ tnt_minecart.png
│  │     │  │  ├─ torchflower_seeds.png
│  │     │  │  ├─ totem_of_undying.png
│  │     │  │  ├─ trader_llama_spawn_egg.png
│  │     │  │  ├─ trial_key.png
│  │     │  │  ├─ trident.png
│  │     │  │  ├─ tropical_fish.png
│  │     │  │  ├─ tropical_fish_bucket.png
│  │     │  │  ├─ tropical_fish_spawn_egg.png
│  │     │  │  ├─ turtle_egg.png
│  │     │  │  ├─ turtle_helmet.png
│  │     │  │  ├─ turtle_scute.png
│  │     │  │  ├─ turtle_spawn_egg.png
│  │     │  │  ├─ vex_armor_trim_smithing_template.png
│  │     │  │  ├─ vex_spawn_egg.png
│  │     │  │  ├─ villager_spawn_egg.png
│  │     │  │  ├─ vindicator_spawn_egg.png
│  │     │  │  ├─ wandering_trader_spawn_egg.png
│  │     │  │  ├─ warden_spawn_egg.png
│  │     │  │  ├─ ward_armor_trim_smithing_template.png
│  │     │  │  ├─ warped_door.png
│  │     │  │  ├─ warped_fungus_on_a_stick.png
│  │     │  │  ├─ warped_hanging_sign.png
│  │     │  │  ├─ warped_sign.png
│  │     │  │  ├─ water_bucket.png
│  │     │  │  ├─ wayfinder_armor_trim_smithing_template.png
│  │     │  │  ├─ weathered_copper_chain.png
│  │     │  │  ├─ weathered_copper_door.png
│  │     │  │  ├─ weathered_copper_lantern.png
│  │     │  │  ├─ wheat.png
│  │     │  │  ├─ wheat_seeds.png
│  │     │  │  ├─ white_bundle.png
│  │     │  │  ├─ white_bundle_open_back.png
│  │     │  │  ├─ white_bundle_open_front.png
│  │     │  │  ├─ white_candle.png
│  │     │  │  ├─ white_dye.png
│  │     │  │  ├─ white_harness.png
│  │     │  │  ├─ wildflowers.png
│  │     │  │  ├─ wild_armor_trim_smithing_template.png
│  │     │  │  ├─ wind_charge.png
│  │     │  │  ├─ witch_spawn_egg.png
│  │     │  │  ├─ wither_skeleton_spawn_egg.png
│  │     │  │  ├─ wither_spawn_egg.png
│  │     │  │  ├─ wolf_armor.png
│  │     │  │  ├─ wolf_armor_overlay.png
│  │     │  │  ├─ wolf_spawn_egg.png
│  │     │  │  ├─ wooden_axe.png
│  │     │  │  ├─ wooden_hoe.png
│  │     │  │  ├─ wooden_pickaxe.png
│  │     │  │  ├─ wooden_shovel.png
│  │     │  │  ├─ wooden_spear.png
│  │     │  │  ├─ wooden_spear_in_hand.png
│  │     │  │  ├─ wooden_sword.png
│  │     │  │  ├─ writable_book.png
│  │     │  │  ├─ written_book.png
│  │     │  │  ├─ yellow_bundle.png
│  │     │  │  ├─ yellow_bundle_open_back.png
│  │     │  │  ├─ yellow_bundle_open_front.png
│  │     │  │  ├─ yellow_candle.png
│  │     │  │  ├─ yellow_dye.png
│  │     │  │  ├─ yellow_harness.png
│  │     │  │  ├─ zoglin_spawn_egg.png
│  │     │  │  ├─ zombie_horse_spawn_egg.png
│  │     │  │  ├─ zombie_nautilus_spawn_egg.png
│  │     │  │  ├─ zombie_spawn_egg.png
│  │     │  │  ├─ zombie_villager_spawn_egg.png
│  │     │  │  └─ zombified_piglin_spawn_egg.png
│  │     │  ├─ map
│  │     │  │  ├─ decorations
│  │     │  │  │  ├─ black_banner.png
│  │     │  │  │  ├─ blue_banner.png
│  │     │  │  │  ├─ blue_marker.png
│  │     │  │  │  ├─ brown_banner.png
│  │     │  │  │  ├─ cyan_banner.png
│  │     │  │  │  ├─ desert_village.png
│  │     │  │  │  ├─ frame.png
│  │     │  │  │  ├─ gray_banner.png
│  │     │  │  │  ├─ green_banner.png
│  │     │  │  │  ├─ jungle_temple.png
│  │     │  │  │  ├─ light_blue_banner.png
│  │     │  │  │  ├─ light_gray_banner.png
│  │     │  │  │  ├─ lime_banner.png
│  │     │  │  │  ├─ magenta_banner.png
│  │     │  │  │  ├─ ocean_monument.png
│  │     │  │  │  ├─ orange_banner.png
│  │     │  │  │  ├─ pink_banner.png
│  │     │  │  │  ├─ plains_village.png
│  │     │  │  │  ├─ player.png
│  │     │  │  │  ├─ player_off_limits.png
│  │     │  │  │  ├─ player_off_map.png
│  │     │  │  │  ├─ purple_banner.png
│  │     │  │  │  ├─ red_banner.png
│  │     │  │  │  ├─ red_marker.png
│  │     │  │  │  ├─ red_x.png
│  │     │  │  │  ├─ savanna_village.png
│  │     │  │  │  ├─ snowy_village.png
│  │     │  │  │  ├─ swamp_hut.png
│  │     │  │  │  ├─ taiga_village.png
│  │     │  │  │  ├─ target_point.png
│  │     │  │  │  ├─ target_x.png
│  │     │  │  │  ├─ trial_chambers.png
│  │     │  │  │  ├─ white_banner.png
│  │     │  │  │  ├─ woodland_mansion.png
│  │     │  │  │  └─ yellow_banner.png
│  │     │  │  ├─ map_background.png
│  │     │  │  └─ map_background_checkerboard.png
│  │     │  ├─ misc
│  │     │  │  ├─ credits_vignette.png
│  │     │  │  ├─ credits_vignette.png.mcmeta
│  │     │  │  ├─ enchanted_glint_armor.png
│  │     │  │  ├─ enchanted_glint_armor.png.mcmeta
│  │     │  │  ├─ enchanted_glint_item.png
│  │     │  │  ├─ enchanted_glint_item.png.mcmeta
│  │     │  │  ├─ forcefield.png
│  │     │  │  ├─ nausea.png
│  │     │  │  ├─ nausea.png.mcmeta
│  │     │  │  ├─ powder_snow_outline.png
│  │     │  │  ├─ pumpkinblur.png
│  │     │  │  ├─ pumpkinblur.png.mcmeta
│  │     │  │  ├─ shadow.png
│  │     │  │  ├─ shadow.png.mcmeta
│  │     │  │  ├─ spyglass_scope.png
│  │     │  │  ├─ underwater.png
│  │     │  │  ├─ unknown_pack.png
│  │     │  │  ├─ unknown_server.png
│  │     │  │  ├─ vignette.png
│  │     │  │  └─ vignette.png.mcmeta
│  │     │  ├─ mob_effect
│  │     │  │  ├─ absorption.png
│  │     │  │  ├─ bad_omen.png
│  │     │  │  ├─ blindness.png
│  │     │  │  ├─ breath_of_the_nautilus.png
│  │     │  │  ├─ conduit_power.png
│  │     │  │  ├─ darkness.png
│  │     │  │  ├─ dolphins_grace.png
│  │     │  │  ├─ fire_resistance.png
│  │     │  │  ├─ glowing.png
│  │     │  │  ├─ haste.png
│  │     │  │  ├─ health_boost.png
│  │     │  │  ├─ hero_of_the_village.png
│  │     │  │  ├─ hunger.png
│  │     │  │  ├─ infested.png
│  │     │  │  ├─ instant_damage.png
│  │     │  │  ├─ instant_health.png
│  │     │  │  ├─ invisibility.png
│  │     │  │  ├─ jump_boost.png
│  │     │  │  ├─ levitation.png
│  │     │  │  ├─ luck.png
│  │     │  │  ├─ mining_fatigue.png
│  │     │  │  ├─ nausea.png
│  │     │  │  ├─ night_vision.png
│  │     │  │  ├─ oozing.png
│  │     │  │  ├─ poison.png
│  │     │  │  ├─ raid_omen.png
│  │     │  │  ├─ regeneration.png
│  │     │  │  ├─ resistance.png
│  │     │  │  ├─ saturation.png
│  │     │  │  ├─ slowness.png
│  │     │  │  ├─ slow_falling.png
│  │     │  │  ├─ speed.png
│  │     │  │  ├─ strength.png
│  │     │  │  ├─ trial_omen.png
│  │     │  │  ├─ unluck.png
│  │     │  │  ├─ water_breathing.png
│  │     │  │  ├─ weakness.png
│  │     │  │  ├─ weaving.png
│  │     │  │  ├─ wind_charged.png
│  │     │  │  └─ wither.png
│  │     │  ├─ painting
│  │     │  │  ├─ alban.png
│  │     │  │  ├─ aztec.png
│  │     │  │  ├─ aztec2.png
│  │     │  │  ├─ back.png
│  │     │  │  ├─ backyard.png
│  │     │  │  ├─ baroque.png
│  │     │  │  ├─ bomb.png
│  │     │  │  ├─ bouquet.png
│  │     │  │  ├─ burning_skull.png
│  │     │  │  ├─ bust.png
│  │     │  │  ├─ cavebird.png
│  │     │  │  ├─ changing.png
│  │     │  │  ├─ cotan.png
│  │     │  │  ├─ courbet.png
│  │     │  │  ├─ creebet.png
│  │     │  │  ├─ dennis.png
│  │     │  │  ├─ donkey_kong.png
│  │     │  │  ├─ earth.png
│  │     │  │  ├─ endboss.png
│  │     │  │  ├─ fern.png
│  │     │  │  ├─ fighters.png
│  │     │  │  ├─ finding.png
│  │     │  │  ├─ fire.png
│  │     │  │  ├─ graham.png
│  │     │  │  ├─ humble.png
│  │     │  │  ├─ kebab.png
│  │     │  │  ├─ lowmist.png
│  │     │  │  ├─ match.png
│  │     │  │  ├─ meditative.png
│  │     │  │  ├─ orb.png
│  │     │  │  ├─ owlemons.png
│  │     │  │  ├─ passage.png
│  │     │  │  ├─ pigscene.png
│  │     │  │  ├─ plant.png
│  │     │  │  ├─ pointer.png
│  │     │  │  ├─ pond.png
│  │     │  │  ├─ pool.png
│  │     │  │  ├─ prairie_ride.png
│  │     │  │  ├─ sea.png
│  │     │  │  ├─ skeleton.png
│  │     │  │  ├─ skull_and_roses.png
│  │     │  │  ├─ stage.png
│  │     │  │  ├─ sunflowers.png
│  │     │  │  ├─ sunset.png
│  │     │  │  ├─ tides.png
│  │     │  │  ├─ unpacked.png
│  │     │  │  ├─ void.png
│  │     │  │  ├─ wanderer.png
│  │     │  │  ├─ wasteland.png
│  │     │  │  ├─ water.png
│  │     │  │  ├─ wind.png
│  │     │  │  └─ wither.png
│  │     │  ├─ particle
│  │     │  │  ├─ angry.png
│  │     │  │  ├─ big_smoke_0.png
│  │     │  │  ├─ big_smoke_1.png
│  │     │  │  ├─ big_smoke_10.png
│  │     │  │  ├─ big_smoke_11.png
│  │     │  │  ├─ big_smoke_2.png
│  │     │  │  ├─ big_smoke_3.png
│  │     │  │  ├─ big_smoke_4.png
│  │     │  │  ├─ big_smoke_5.png
│  │     │  │  ├─ big_smoke_6.png
│  │     │  │  ├─ big_smoke_7.png
│  │     │  │  ├─ big_smoke_8.png
│  │     │  │  ├─ big_smoke_9.png
│  │     │  │  ├─ bubble.png
│  │     │  │  ├─ bubble_pop_0.png
│  │     │  │  ├─ bubble_pop_1.png
│  │     │  │  ├─ bubble_pop_2.png
│  │     │  │  ├─ bubble_pop_3.png
│  │     │  │  ├─ bubble_pop_4.png
│  │     │  │  ├─ cherry_0.png
│  │     │  │  ├─ cherry_1.png
│  │     │  │  ├─ cherry_10.png
│  │     │  │  ├─ cherry_11.png
│  │     │  │  ├─ cherry_2.png
│  │     │  │  ├─ cherry_3.png
│  │     │  │  ├─ cherry_4.png
│  │     │  │  ├─ cherry_5.png
│  │     │  │  ├─ cherry_6.png
│  │     │  │  ├─ cherry_7.png
│  │     │  │  ├─ cherry_8.png
│  │     │  │  ├─ cherry_9.png
│  │     │  │  ├─ copper_fire_flame.png
│  │     │  │  ├─ critical_hit.png
│  │     │  │  ├─ damage.png
│  │     │  │  ├─ drip_fall.png
│  │     │  │  ├─ drip_hang.png
│  │     │  │  ├─ drip_land.png
│  │     │  │  ├─ effect_0.png
│  │     │  │  ├─ effect_1.png
│  │     │  │  ├─ effect_2.png
│  │     │  │  ├─ effect_3.png
│  │     │  │  ├─ effect_4.png
│  │     │  │  ├─ effect_5.png
│  │     │  │  ├─ effect_6.png
│  │     │  │  ├─ effect_7.png
│  │     │  │  ├─ enchanted_hit.png
│  │     │  │  ├─ explosion_0.png
│  │     │  │  ├─ explosion_1.png
│  │     │  │  ├─ explosion_10.png
│  │     │  │  ├─ explosion_11.png
│  │     │  │  ├─ explosion_12.png
│  │     │  │  ├─ explosion_13.png
│  │     │  │  ├─ explosion_14.png
│  │     │  │  ├─ explosion_15.png
│  │     │  │  ├─ explosion_2.png
│  │     │  │  ├─ explosion_3.png
│  │     │  │  ├─ explosion_4.png
│  │     │  │  ├─ explosion_5.png
│  │     │  │  ├─ explosion_6.png
│  │     │  │  ├─ explosion_7.png
│  │     │  │  ├─ explosion_8.png
│  │     │  │  ├─ explosion_9.png
│  │     │  │  ├─ firefly.png
│  │     │  │  ├─ flame.png
│  │     │  │  ├─ flash.png
│  │     │  │  ├─ generic_0.png
│  │     │  │  ├─ generic_1.png
│  │     │  │  ├─ generic_2.png
│  │     │  │  ├─ generic_3.png
│  │     │  │  ├─ generic_4.png
│  │     │  │  ├─ generic_5.png
│  │     │  │  ├─ generic_6.png
│  │     │  │  ├─ generic_7.png
│  │     │  │  ├─ glint.png
│  │     │  │  ├─ glitter_0.png
│  │     │  │  ├─ glitter_1.png
│  │     │  │  ├─ glitter_2.png
│  │     │  │  ├─ glitter_3.png
│  │     │  │  ├─ glitter_4.png
│  │     │  │  ├─ glitter_5.png
│  │     │  │  ├─ glitter_6.png
│  │     │  │  ├─ glitter_7.png
│  │     │  │  ├─ glow.png
│  │     │  │  ├─ goldheart_0.png
│  │     │  │  ├─ goldheart_1.png
│  │     │  │  ├─ goldheart_2.png
│  │     │  │  ├─ gust_0.png
│  │     │  │  ├─ gust_1.png
│  │     │  │  ├─ gust_10.png
│  │     │  │  ├─ gust_11.png
│  │     │  │  ├─ gust_2.png
│  │     │  │  ├─ gust_3.png
│  │     │  │  ├─ gust_4.png
│  │     │  │  ├─ gust_5.png
│  │     │  │  ├─ gust_6.png
│  │     │  │  ├─ gust_7.png
│  │     │  │  ├─ gust_8.png
│  │     │  │  ├─ gust_9.png
│  │     │  │  ├─ heart.png
│  │     │  │  ├─ infested.png
│  │     │  │  ├─ lava.png
│  │     │  │  ├─ leaf_0.png
│  │     │  │  ├─ leaf_1.png
│  │     │  │  ├─ leaf_10.png
│  │     │  │  ├─ leaf_11.png
│  │     │  │  ├─ leaf_2.png
│  │     │  │  ├─ leaf_3.png
│  │     │  │  ├─ leaf_4.png
│  │     │  │  ├─ leaf_5.png
│  │     │  │  ├─ leaf_6.png
│  │     │  │  ├─ leaf_7.png
│  │     │  │  ├─ leaf_8.png
│  │     │  │  ├─ leaf_9.png
│  │     │  │  ├─ nautilus.png
│  │     │  │  ├─ note.png
│  │     │  │  ├─ ominous_spawning.png
│  │     │  │  ├─ pale_oak_0.png
│  │     │  │  ├─ pale_oak_1.png
│  │     │  │  ├─ pale_oak_10.png
│  │     │  │  ├─ pale_oak_11.png
│  │     │  │  ├─ pale_oak_2.png
│  │     │  │  ├─ pale_oak_3.png
│  │     │  │  ├─ pale_oak_4.png
│  │     │  │  ├─ pale_oak_5.png
│  │     │  │  ├─ pale_oak_6.png
│  │     │  │  ├─ pale_oak_7.png
│  │     │  │  ├─ pale_oak_8.png
│  │     │  │  ├─ pale_oak_9.png
│  │     │  │  ├─ raid_omen.png
│  │     │  │  ├─ sculk_charge_0.png
│  │     │  │  ├─ sculk_charge_1.png
│  │     │  │  ├─ sculk_charge_2.png
│  │     │  │  ├─ sculk_charge_3.png
│  │     │  │  ├─ sculk_charge_4.png
│  │     │  │  ├─ sculk_charge_5.png
│  │     │  │  ├─ sculk_charge_6.png
│  │     │  │  ├─ sculk_charge_pop_0.png
│  │     │  │  ├─ sculk_charge_pop_1.png
│  │     │  │  ├─ sculk_charge_pop_2.png
│  │     │  │  ├─ sculk_charge_pop_3.png
│  │     │  │  ├─ sculk_soul_0.png
│  │     │  │  ├─ sculk_soul_1.png
│  │     │  │  ├─ sculk_soul_10.png
│  │     │  │  ├─ sculk_soul_2.png
│  │     │  │  ├─ sculk_soul_3.png
│  │     │  │  ├─ sculk_soul_4.png
│  │     │  │  ├─ sculk_soul_5.png
│  │     │  │  ├─ sculk_soul_6.png
│  │     │  │  ├─ sculk_soul_7.png
│  │     │  │  ├─ sculk_soul_8.png
│  │     │  │  ├─ sculk_soul_9.png
│  │     │  │  ├─ sga_a.png
│  │     │  │  ├─ sga_b.png
│  │     │  │  ├─ sga_c.png
│  │     │  │  ├─ sga_d.png
│  │     │  │  ├─ sga_e.png
│  │     │  │  ├─ sga_f.png
│  │     │  │  ├─ sga_g.png
│  │     │  │  ├─ sga_h.png
│  │     │  │  ├─ sga_i.png
│  │     │  │  ├─ sga_j.png
│  │     │  │  ├─ sga_k.png
│  │     │  │  ├─ sga_l.png
│  │     │  │  ├─ sga_m.png
│  │     │  │  ├─ sga_n.png
│  │     │  │  ├─ sga_o.png
│  │     │  │  ├─ sga_p.png
│  │     │  │  ├─ sga_q.png
│  │     │  │  ├─ sga_r.png
│  │     │  │  ├─ sga_s.png
│  │     │  │  ├─ sga_t.png
│  │     │  │  ├─ sga_u.png
│  │     │  │  ├─ sga_v.png
│  │     │  │  ├─ sga_w.png
│  │     │  │  ├─ sga_x.png
│  │     │  │  ├─ sga_y.png
│  │     │  │  ├─ sga_z.png
│  │     │  │  ├─ shriek.png
│  │     │  │  ├─ small_gust_0.png
│  │     │  │  ├─ small_gust_1.png
│  │     │  │  ├─ small_gust_2.png
│  │     │  │  ├─ small_gust_3.png
│  │     │  │  ├─ small_gust_4.png
│  │     │  │  ├─ small_gust_5.png
│  │     │  │  ├─ small_gust_6.png
│  │     │  │  ├─ sonic_boom_0.png
│  │     │  │  ├─ sonic_boom_1.png
│  │     │  │  ├─ sonic_boom_10.png
│  │     │  │  ├─ sonic_boom_11.png
│  │     │  │  ├─ sonic_boom_12.png
│  │     │  │  ├─ sonic_boom_13.png
│  │     │  │  ├─ sonic_boom_14.png
│  │     │  │  ├─ sonic_boom_15.png
│  │     │  │  ├─ sonic_boom_2.png
│  │     │  │  ├─ sonic_boom_3.png
│  │     │  │  ├─ sonic_boom_4.png
│  │     │  │  ├─ sonic_boom_5.png
│  │     │  │  ├─ sonic_boom_6.png
│  │     │  │  ├─ sonic_boom_7.png
│  │     │  │  ├─ sonic_boom_8.png
│  │     │  │  ├─ sonic_boom_9.png
│  │     │  │  ├─ soul_0.png
│  │     │  │  ├─ soul_1.png
│  │     │  │  ├─ soul_10.png
│  │     │  │  ├─ soul_2.png
│  │     │  │  ├─ soul_3.png
│  │     │  │  ├─ soul_4.png
│  │     │  │  ├─ soul_5.png
│  │     │  │  ├─ soul_6.png
│  │     │  │  ├─ soul_7.png
│  │     │  │  ├─ soul_8.png
│  │     │  │  ├─ soul_9.png
│  │     │  │  ├─ soul_fire_flame.png
│  │     │  │  ├─ spark_0.png
│  │     │  │  ├─ spark_1.png
│  │     │  │  ├─ spark_2.png
│  │     │  │  ├─ spark_3.png
│  │     │  │  ├─ spark_4.png
│  │     │  │  ├─ spark_5.png
│  │     │  │  ├─ spark_6.png
│  │     │  │  ├─ spark_7.png
│  │     │  │  ├─ spell_0.png
│  │     │  │  ├─ spell_1.png
│  │     │  │  ├─ spell_2.png
│  │     │  │  ├─ spell_3.png
│  │     │  │  ├─ spell_4.png
│  │     │  │  ├─ spell_5.png
│  │     │  │  ├─ spell_6.png
│  │     │  │  ├─ spell_7.png
│  │     │  │  ├─ splash_0.png
│  │     │  │  ├─ splash_1.png
│  │     │  │  ├─ splash_2.png
│  │     │  │  ├─ splash_3.png
│  │     │  │  ├─ sweep_0.png
│  │     │  │  ├─ sweep_1.png
│  │     │  │  ├─ sweep_2.png
│  │     │  │  ├─ sweep_3.png
│  │     │  │  ├─ sweep_4.png
│  │     │  │  ├─ sweep_5.png
│  │     │  │  ├─ sweep_6.png
│  │     │  │  ├─ sweep_7.png
│  │     │  │  ├─ trial_omen.png
│  │     │  │  ├─ trial_spawner_detection_0.png
│  │     │  │  ├─ trial_spawner_detection_1.png
│  │     │  │  ├─ trial_spawner_detection_2.png
│  │     │  │  ├─ trial_spawner_detection_3.png
│  │     │  │  ├─ trial_spawner_detection_4.png
│  │     │  │  ├─ trial_spawner_detection_ominous_0.png
│  │     │  │  ├─ trial_spawner_detection_ominous_1.png
│  │     │  │  ├─ trial_spawner_detection_ominous_2.png
│  │     │  │  ├─ trial_spawner_detection_ominous_3.png
│  │     │  │  ├─ trial_spawner_detection_ominous_4.png
│  │     │  │  ├─ vault_connection.png
│  │     │  │  ├─ vibration.png
│  │     │  │  └─ vibration.png.mcmeta
│  │     │  └─ trims
│  │     │     ├─ color_palettes
│  │     │     │  ├─ amethyst.png
│  │     │     │  ├─ copper.png
│  │     │     │  ├─ copper_darker.png
│  │     │     │  ├─ diamond.png
│  │     │     │  ├─ diamond_darker.png
│  │     │     │  ├─ emerald.png
│  │     │     │  ├─ gold.png
│  │     │     │  ├─ gold_darker.png
│  │     │     │  ├─ iron.png
│  │     │     │  ├─ iron_darker.png
│  │     │     │  ├─ lapis.png
│  │     │     │  ├─ netherite.png
│  │     │     │  ├─ netherite_darker.png
│  │     │     │  ├─ quartz.png
│  │     │     │  ├─ redstone.png
│  │     │     │  ├─ resin.png
│  │     │     │  └─ trim_palette.png
│  │     │     ├─ entity
│  │     │     │  ├─ humanoid
│  │     │     │  │  ├─ bolt.png
│  │     │     │  │  ├─ coast.png
│  │     │     │  │  ├─ dune.png
│  │     │     │  │  ├─ eye.png
│  │     │     │  │  ├─ flow.png
│  │     │     │  │  ├─ host.png
│  │     │     │  │  ├─ raiser.png
│  │     │     │  │  ├─ rib.png
│  │     │     │  │  ├─ sentry.png
│  │     │     │  │  ├─ shaper.png
│  │     │     │  │  ├─ silence.png
│  │     │     │  │  ├─ snout.png
│  │     │     │  │  ├─ spire.png
│  │     │     │  │  ├─ tide.png
│  │     │     │  │  ├─ vex.png
│  │     │     │  │  ├─ ward.png
│  │     │     │  │  ├─ wayfinder.png
│  │     │     │  │  └─ wild.png
│  │     │     │  └─ humanoid_leggings
│  │     │     │     ├─ bolt.png
│  │     │     │     ├─ coast.png
│  │     │     │     ├─ dune.png
│  │     │     │     ├─ eye.png
│  │     │     │     ├─ flow.png
│  │     │     │     ├─ host.png
│  │     │     │     ├─ raiser.png
│  │     │     │     ├─ rib.png
│  │     │     │     ├─ sentry.png
│  │     │     │     ├─ shaper.png
│  │     │     │     ├─ silence.png
│  │     │     │     ├─ snout.png
│  │     │     │     ├─ spire.png
│  │     │     │     ├─ tide.png
│  │     │     │     ├─ vex.png
│  │     │     │     ├─ ward.png
│  │     │     │     ├─ wayfinder.png
│  │     │     │     └─ wild.png
│  │     │     └─ items
│  │     │        ├─ boots_trim.png
│  │     │        ├─ chestplate_trim.png
│  │     │        ├─ helmet_trim.png
│  │     │        └─ leggings_trim.png
│  │     └─ waypoint_style
│  │        ├─ bowtie.json
│  │        └─ default.json
│  └─ data
│     └─ minecraft
│        ├─ advancement
│        │  ├─ adventure
│        │  │  ├─ adventuring_time.json
│        │  │  ├─ arbalistic.json
│        │  │  ├─ avoid_vibration.json
│        │  │  ├─ blowback.json
│        │  │  ├─ brush_armadillo.json
│        │  │  ├─ bullseye.json
│        │  │  ├─ crafters_crafting_crafters.json
│        │  │  ├─ craft_decorated_pot_using_only_sherds.json
│        │  │  ├─ fall_from_world_height.json
│        │  │  ├─ heart_transplanter.json
│        │  │  ├─ hero_of_the_village.json
│        │  │  ├─ honey_block_slide.json
│        │  │  ├─ kill_all_mobs.json
│        │  │  ├─ kill_a_mob.json
│        │  │  ├─ kill_mob_near_sculk_catalyst.json
│        │  │  ├─ lighten_up.json
│        │  │  ├─ lightning_rod_with_villager_no_fire.json
│        │  │  ├─ minecraft_trials_edition.json
│        │  │  ├─ ol_betsy.json
│        │  │  ├─ overoverkill.json
│        │  │  ├─ play_jukebox_in_meadows.json
│        │  │  ├─ read_power_of_chiseled_bookshelf.json
│        │  │  ├─ revaulting.json
│        │  │  ├─ root.json
│        │  │  ├─ salvage_sherd.json
│        │  │  ├─ shoot_arrow.json
│        │  │  ├─ sleep_in_bed.json
│        │  │  ├─ sniper_duel.json
│        │  │  ├─ spear_many_mobs.json
│        │  │  ├─ spyglass_at_dragon.json
│        │  │  ├─ spyglass_at_ghast.json
│        │  │  ├─ spyglass_at_parrot.json
│        │  │  ├─ summon_iron_golem.json
│        │  │  ├─ throw_trident.json
│        │  │  ├─ totem_of_undying.json
│        │  │  ├─ trade.json
│        │  │  ├─ trade_at_world_height.json
│        │  │  ├─ trim_with_all_exclusive_armor_patterns.json
│        │  │  ├─ trim_with_any_armor_pattern.json
│        │  │  ├─ two_birds_one_arrow.json
│        │  │  ├─ under_lock_and_key.json
│        │  │  ├─ use_lodestone.json
│        │  │  ├─ very_very_frightening.json
│        │  │  ├─ voluntary_exile.json
│        │  │  ├─ walk_on_powder_snow_with_leather_boots.json
│        │  │  ├─ whos_the_pillager_now.json
│        │  │  └─ who_needs_rockets.json
│        │  ├─ end
│        │  │  ├─ dragon_breath.json
│        │  │  ├─ dragon_egg.json
│        │  │  ├─ elytra.json
│        │  │  ├─ enter_end_gateway.json
│        │  │  ├─ find_end_city.json
│        │  │  ├─ kill_dragon.json
│        │  │  ├─ levitate.json
│        │  │  ├─ respawn_dragon.json
│        │  │  └─ root.json
│        │  ├─ husbandry
│        │  │  ├─ allay_deliver_cake_to_note_block.json
│        │  │  ├─ allay_deliver_item_to_player.json
│        │  │  ├─ axolotl_in_a_bucket.json
│        │  │  ├─ balanced_diet.json
│        │  │  ├─ bred_all_animals.json
│        │  │  ├─ breed_an_animal.json
│        │  │  ├─ complete_catalogue.json
│        │  │  ├─ feed_snifflet.json
│        │  │  ├─ fishy_business.json
│        │  │  ├─ froglights.json
│        │  │  ├─ kill_axolotl_target.json
│        │  │  ├─ leash_all_frog_variants.json
│        │  │  ├─ make_a_sign_glow.json
│        │  │  ├─ obtain_netherite_hoe.json
│        │  │  ├─ obtain_sniffer_egg.json
│        │  │  ├─ place_dried_ghast_in_water.json
│        │  │  ├─ plant_any_sniffer_seed.json
│        │  │  ├─ plant_seed.json
│        │  │  ├─ remove_wolf_armor.json
│        │  │  ├─ repair_wolf_armor.json
│        │  │  ├─ ride_a_boat_with_a_goat.json
│        │  │  ├─ root.json
│        │  │  ├─ safely_harvest_honey.json
│        │  │  ├─ silk_touch_nest.json
│        │  │  ├─ tactical_fishing.json
│        │  │  ├─ tadpole_in_a_bucket.json
│        │  │  ├─ tame_an_animal.json
│        │  │  ├─ wax_off.json
│        │  │  ├─ wax_on.json
│        │  │  └─ whole_pack.json
│        │  ├─ nether
│        │  │  ├─ all_effects.json
│        │  │  ├─ all_potions.json
│        │  │  ├─ brew_potion.json
│        │  │  ├─ charge_respawn_anchor.json
│        │  │  ├─ create_beacon.json
│        │  │  ├─ create_full_beacon.json
│        │  │  ├─ distract_piglin.json
│        │  │  ├─ explore_nether.json
│        │  │  ├─ fast_travel.json
│        │  │  ├─ find_bastion.json
│        │  │  ├─ find_fortress.json
│        │  │  ├─ get_wither_skull.json
│        │  │  ├─ loot_bastion.json
│        │  │  ├─ netherite_armor.json
│        │  │  ├─ obtain_ancient_debris.json
│        │  │  ├─ obtain_blaze_rod.json
│        │  │  ├─ obtain_crying_obsidian.json
│        │  │  ├─ return_to_sender.json
│        │  │  ├─ ride_strider.json
│        │  │  ├─ ride_strider_in_overworld_lava.json
│        │  │  ├─ root.json
│        │  │  ├─ summon_wither.json
│        │  │  └─ uneasy_alliance.json
│        │  ├─ recipes
│        │  │  ├─ brewing
│        │  │  │  ├─ blaze_powder.json
│        │  │  │  ├─ brewing_stand.json
│        │  │  │  ├─ cauldron.json
│        │  │  │  ├─ fermented_spider_eye.json
│        │  │  │  ├─ glass_bottle.json
│        │  │  │  ├─ glistering_melon_slice.json
│        │  │  │  ├─ golden_carrot.json
│        │  │  │  └─ magma_cream.json
│        │  │  ├─ building_blocks
│        │  │  │  ├─ acacia_planks.json
│        │  │  │  ├─ acacia_slab.json
│        │  │  │  ├─ acacia_stairs.json
│        │  │  │  ├─ acacia_wood.json
│        │  │  │  ├─ amethyst_block.json
│        │  │  │  ├─ andesite.json
│        │  │  │  ├─ andesite_slab.json
│        │  │  │  ├─ andesite_slab_from_andesite_stonecutting.json
│        │  │  │  ├─ andesite_stairs.json
│        │  │  │  ├─ andesite_stairs_from_andesite_stonecutting.json
│        │  │  │  ├─ bamboo_block.json
│        │  │  │  ├─ bamboo_mosaic_slab.json
│        │  │  │  ├─ bamboo_mosaic_stairs.json
│        │  │  │  ├─ bamboo_planks.json
│        │  │  │  ├─ bamboo_slab.json
│        │  │  │  ├─ bamboo_stairs.json
│        │  │  │  ├─ birch_planks.json
│        │  │  │  ├─ birch_slab.json
│        │  │  │  ├─ birch_stairs.json
│        │  │  │  ├─ birch_wood.json
│        │  │  │  ├─ blackstone_slab.json
│        │  │  │  ├─ blackstone_slab_from_blackstone_stonecutting.json
│        │  │  │  ├─ blackstone_stairs.json
│        │  │  │  ├─ blackstone_stairs_from_blackstone_stonecutting.json
│        │  │  │  ├─ black_concrete_powder.json
│        │  │  │  ├─ black_stained_glass.json
│        │  │  │  ├─ black_terracotta.json
│        │  │  │  ├─ blue_concrete_powder.json
│        │  │  │  ├─ blue_ice.json
│        │  │  │  ├─ blue_stained_glass.json
│        │  │  │  ├─ blue_terracotta.json
│        │  │  │  ├─ bone_block.json
│        │  │  │  ├─ bookshelf.json
│        │  │  │  ├─ bricks.json
│        │  │  │  ├─ brick_slab.json
│        │  │  │  ├─ brick_slab_from_bricks_stonecutting.json
│        │  │  │  ├─ brick_stairs.json
│        │  │  │  ├─ brick_stairs_from_bricks_stonecutting.json
│        │  │  │  ├─ brown_concrete_powder.json
│        │  │  │  ├─ brown_stained_glass.json
│        │  │  │  ├─ brown_terracotta.json
│        │  │  │  ├─ cherry_planks.json
│        │  │  │  ├─ cherry_slab.json
│        │  │  │  ├─ cherry_stairs.json
│        │  │  │  ├─ cherry_wood.json
│        │  │  │  ├─ chiseled_bookshelf.json
│        │  │  │  ├─ chiseled_copper.json
│        │  │  │  ├─ chiseled_copper_from_copper_block_stonecutting.json
│        │  │  │  ├─ chiseled_copper_from_cut_copper_stonecutting.json
│        │  │  │  ├─ chiseled_deepslate.json
│        │  │  │  ├─ chiseled_deepslate_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ chiseled_nether_bricks.json
│        │  │  │  ├─ chiseled_nether_bricks_from_nether_bricks_stonecutting.json
│        │  │  │  ├─ chiseled_polished_blackstone.json
│        │  │  │  ├─ chiseled_polished_blackstone_from_blackstone_stonecutting.json
│        │  │  │  ├─ chiseled_polished_blackstone_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ chiseled_quartz_block.json
│        │  │  │  ├─ chiseled_quartz_block_from_quartz_block_stonecutting.json
│        │  │  │  ├─ chiseled_red_sandstone.json
│        │  │  │  ├─ chiseled_red_sandstone_from_red_sandstone_stonecutting.json
│        │  │  │  ├─ chiseled_resin_bricks.json
│        │  │  │  ├─ chiseled_resin_bricks_from_resin_bricks_stonecutting.json
│        │  │  │  ├─ chiseled_sandstone.json
│        │  │  │  ├─ chiseled_sandstone_from_sandstone_stonecutting.json
│        │  │  │  ├─ chiseled_stone_bricks.json
│        │  │  │  ├─ chiseled_stone_bricks_from_stone_bricks_stonecutting.json
│        │  │  │  ├─ chiseled_stone_bricks_stone_from_stonecutting.json
│        │  │  │  ├─ chiseled_tuff.json
│        │  │  │  ├─ chiseled_tuff_bricks.json
│        │  │  │  ├─ chiseled_tuff_bricks_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ chiseled_tuff_bricks_from_tuff_bricks_stonecutting.json
│        │  │  │  ├─ chiseled_tuff_bricks_from_tuff_stonecutting.json
│        │  │  │  ├─ chiseled_tuff_from_tuff_stonecutting.json
│        │  │  │  ├─ clay.json
│        │  │  │  ├─ coal_block.json
│        │  │  │  ├─ coarse_dirt.json
│        │  │  │  ├─ cobbled_deepslate_slab.json
│        │  │  │  ├─ cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ cobbled_deepslate_stairs.json
│        │  │  │  ├─ cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ cobblestone_slab.json
│        │  │  │  ├─ cobblestone_slab_from_cobblestone_stonecutting.json
│        │  │  │  ├─ cobblestone_stairs.json
│        │  │  │  ├─ cobblestone_stairs_from_cobblestone_stonecutting.json
│        │  │  │  ├─ copper_block.json
│        │  │  │  ├─ copper_grate.json
│        │  │  │  ├─ copper_grate_from_copper_block_stonecutting.json
│        │  │  │  ├─ cracked_deepslate_bricks.json
│        │  │  │  ├─ cracked_deepslate_tiles.json
│        │  │  │  ├─ cracked_nether_bricks.json
│        │  │  │  ├─ cracked_polished_blackstone_bricks.json
│        │  │  │  ├─ cracked_stone_bricks.json
│        │  │  │  ├─ crimson_hyphae.json
│        │  │  │  ├─ crimson_planks.json
│        │  │  │  ├─ crimson_slab.json
│        │  │  │  ├─ crimson_stairs.json
│        │  │  │  ├─ cut_copper.json
│        │  │  │  ├─ cut_copper_from_copper_block_stonecutting.json
│        │  │  │  ├─ cut_copper_slab.json
│        │  │  │  ├─ cut_copper_slab_from_copper_block_stonecutting.json
│        │  │  │  ├─ cut_copper_slab_from_cut_copper_stonecutting.json
│        │  │  │  ├─ cut_copper_stairs.json
│        │  │  │  ├─ cut_copper_stairs_from_copper_block_stonecutting.json
│        │  │  │  ├─ cut_copper_stairs_from_cut_copper_stonecutting.json
│        │  │  │  ├─ cut_red_sandstone.json
│        │  │  │  ├─ cut_red_sandstone_from_red_sandstone_stonecutting.json
│        │  │  │  ├─ cut_red_sandstone_slab.json
│        │  │  │  ├─ cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting.json
│        │  │  │  ├─ cut_red_sandstone_slab_from_red_sandstone_stonecutting.json
│        │  │  │  ├─ cut_sandstone.json
│        │  │  │  ├─ cut_sandstone_from_sandstone_stonecutting.json
│        │  │  │  ├─ cut_sandstone_slab.json
│        │  │  │  ├─ cut_sandstone_slab_from_cut_sandstone_stonecutting.json
│        │  │  │  ├─ cut_sandstone_slab_from_sandstone_stonecutting.json
│        │  │  │  ├─ cyan_concrete_powder.json
│        │  │  │  ├─ cyan_stained_glass.json
│        │  │  │  ├─ cyan_terracotta.json
│        │  │  │  ├─ dark_oak_planks.json
│        │  │  │  ├─ dark_oak_slab.json
│        │  │  │  ├─ dark_oak_stairs.json
│        │  │  │  ├─ dark_oak_wood.json
│        │  │  │  ├─ dark_prismarine.json
│        │  │  │  ├─ dark_prismarine_slab.json
│        │  │  │  ├─ dark_prismarine_slab_from_dark_prismarine_stonecutting.json
│        │  │  │  ├─ dark_prismarine_stairs.json
│        │  │  │  ├─ dark_prismarine_stairs_from_dark_prismarine_stonecutting.json
│        │  │  │  ├─ deepslate.json
│        │  │  │  ├─ deepslate_bricks.json
│        │  │  │  ├─ deepslate_bricks_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_bricks_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_brick_slab.json
│        │  │  │  ├─ deepslate_brick_slab_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_brick_slab_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_brick_slab_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_brick_stairs.json
│        │  │  │  ├─ deepslate_brick_stairs_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_brick_stairs_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_brick_stairs_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tiles.json
│        │  │  │  ├─ deepslate_tiles_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tiles_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_tiles_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tile_slab.json
│        │  │  │  ├─ deepslate_tile_slab_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tile_slab_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_tile_slab_from_deepslate_tiles_stonecutting.json
│        │  │  │  ├─ deepslate_tile_slab_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tile_stairs.json
│        │  │  │  ├─ deepslate_tile_stairs_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tile_stairs_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_tile_stairs_from_deepslate_tiles_stonecutting.json
│        │  │  │  ├─ deepslate_tile_stairs_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ diamond_block.json
│        │  │  │  ├─ diorite.json
│        │  │  │  ├─ diorite_slab.json
│        │  │  │  ├─ diorite_slab_from_diorite_stonecutting.json
│        │  │  │  ├─ diorite_stairs.json
│        │  │  │  ├─ diorite_stairs_from_diorite_stonecutting.json
│        │  │  │  ├─ dried_ghast.json
│        │  │  │  ├─ dried_kelp_block.json
│        │  │  │  ├─ dripstone_block.json
│        │  │  │  ├─ dye_black_wool.json
│        │  │  │  ├─ dye_blue_wool.json
│        │  │  │  ├─ dye_brown_wool.json
│        │  │  │  ├─ dye_cyan_wool.json
│        │  │  │  ├─ dye_gray_wool.json
│        │  │  │  ├─ dye_green_wool.json
│        │  │  │  ├─ dye_light_blue_wool.json
│        │  │  │  ├─ dye_light_gray_wool.json
│        │  │  │  ├─ dye_lime_wool.json
│        │  │  │  ├─ dye_magenta_wool.json
│        │  │  │  ├─ dye_orange_wool.json
│        │  │  │  ├─ dye_pink_wool.json
│        │  │  │  ├─ dye_purple_wool.json
│        │  │  │  ├─ dye_red_wool.json
│        │  │  │  ├─ dye_white_wool.json
│        │  │  │  ├─ dye_yellow_wool.json
│        │  │  │  ├─ emerald_block.json
│        │  │  │  ├─ end_stone_bricks.json
│        │  │  │  ├─ end_stone_bricks_from_end_stone_stonecutting.json
│        │  │  │  ├─ end_stone_brick_slab.json
│        │  │  │  ├─ end_stone_brick_slab_from_end_stone_brick_stonecutting.json
│        │  │  │  ├─ end_stone_brick_slab_from_end_stone_stonecutting.json
│        │  │  │  ├─ end_stone_brick_stairs.json
│        │  │  │  ├─ end_stone_brick_stairs_from_end_stone_brick_stonecutting.json
│        │  │  │  ├─ end_stone_brick_stairs_from_end_stone_stonecutting.json
│        │  │  │  ├─ exposed_chiseled_copper.json
│        │  │  │  ├─ exposed_chiseled_copper_from_exposed_copper_stonecutting.json
│        │  │  │  ├─ exposed_chiseled_copper_from_exposed_cut_copper_stonecutting.json
│        │  │  │  ├─ exposed_copper_grate.json
│        │  │  │  ├─ exposed_copper_grate_from_exposed_copper_stonecutting.json
│        │  │  │  ├─ exposed_cut_copper.json
│        │  │  │  ├─ exposed_cut_copper_from_exposed_copper_stonecutting.json
│        │  │  │  ├─ exposed_cut_copper_slab.json
│        │  │  │  ├─ exposed_cut_copper_slab_from_exposed_copper_stonecutting.json
│        │  │  │  ├─ exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting.json
│        │  │  │  ├─ exposed_cut_copper_stairs.json
│        │  │  │  ├─ exposed_cut_copper_stairs_from_exposed_copper_stonecutting.json
│        │  │  │  ├─ exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting.json
│        │  │  │  ├─ glass.json
│        │  │  │  ├─ glowstone.json
│        │  │  │  ├─ gold_block.json
│        │  │  │  ├─ granite.json
│        │  │  │  ├─ granite_slab.json
│        │  │  │  ├─ granite_slab_from_granite_stonecutting.json
│        │  │  │  ├─ granite_stairs.json
│        │  │  │  ├─ granite_stairs_from_granite_stonecutting.json
│        │  │  │  ├─ gray_concrete_powder.json
│        │  │  │  ├─ gray_stained_glass.json
│        │  │  │  ├─ gray_terracotta.json
│        │  │  │  ├─ green_concrete_powder.json
│        │  │  │  ├─ green_stained_glass.json
│        │  │  │  ├─ green_terracotta.json
│        │  │  │  ├─ hay_block.json
│        │  │  │  ├─ iron_block.json
│        │  │  │  ├─ jack_o_lantern.json
│        │  │  │  ├─ jungle_planks.json
│        │  │  │  ├─ jungle_slab.json
│        │  │  │  ├─ jungle_stairs.json
│        │  │  │  ├─ jungle_wood.json
│        │  │  │  ├─ lapis_block.json
│        │  │  │  ├─ light_blue_concrete_powder.json
│        │  │  │  ├─ light_blue_stained_glass.json
│        │  │  │  ├─ light_blue_terracotta.json
│        │  │  │  ├─ light_gray_concrete_powder.json
│        │  │  │  ├─ light_gray_stained_glass.json
│        │  │  │  ├─ light_gray_terracotta.json
│        │  │  │  ├─ lime_concrete_powder.json
│        │  │  │  ├─ lime_stained_glass.json
│        │  │  │  ├─ lime_terracotta.json
│        │  │  │  ├─ magenta_concrete_powder.json
│        │  │  │  ├─ magenta_stained_glass.json
│        │  │  │  ├─ magenta_terracotta.json
│        │  │  │  ├─ magma_block.json
│        │  │  │  ├─ mangrove_planks.json
│        │  │  │  ├─ mangrove_slab.json
│        │  │  │  ├─ mangrove_stairs.json
│        │  │  │  ├─ mangrove_wood.json
│        │  │  │  ├─ melon.json
│        │  │  │  ├─ mossy_cobblestone_from_moss_block.json
│        │  │  │  ├─ mossy_cobblestone_from_vine.json
│        │  │  │  ├─ mossy_cobblestone_slab.json
│        │  │  │  ├─ mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting.json
│        │  │  │  ├─ mossy_cobblestone_stairs.json
│        │  │  │  ├─ mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting.json
│        │  │  │  ├─ mossy_stone_bricks_from_moss_block.json
│        │  │  │  ├─ mossy_stone_bricks_from_vine.json
│        │  │  │  ├─ mossy_stone_brick_slab.json
│        │  │  │  ├─ mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting.json
│        │  │  │  ├─ mossy_stone_brick_stairs.json
│        │  │  │  ├─ mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting.json
│        │  │  │  ├─ muddy_mangrove_roots.json
│        │  │  │  ├─ mud_bricks.json
│        │  │  │  ├─ mud_brick_slab.json
│        │  │  │  ├─ mud_brick_slab_from_mud_bricks_stonecutting.json
│        │  │  │  ├─ mud_brick_stairs.json
│        │  │  │  ├─ mud_brick_stairs_from_mud_bricks_stonecutting.json
│        │  │  │  ├─ netherite_block.json
│        │  │  │  ├─ nether_bricks.json
│        │  │  │  ├─ nether_brick_slab.json
│        │  │  │  ├─ nether_brick_slab_from_nether_bricks_stonecutting.json
│        │  │  │  ├─ nether_brick_stairs.json
│        │  │  │  ├─ nether_brick_stairs_from_nether_bricks_stonecutting.json
│        │  │  │  ├─ nether_wart_block.json
│        │  │  │  ├─ oak_planks.json
│        │  │  │  ├─ oak_slab.json
│        │  │  │  ├─ oak_stairs.json
│        │  │  │  ├─ oak_wood.json
│        │  │  │  ├─ orange_concrete_powder.json
│        │  │  │  ├─ orange_stained_glass.json
│        │  │  │  ├─ orange_terracotta.json
│        │  │  │  ├─ oxidized_chiseled_copper.json
│        │  │  │  ├─ oxidized_chiseled_copper_from_oxidized_copper_stonecutting.json
│        │  │  │  ├─ oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting.json
│        │  │  │  ├─ oxidized_copper_grate.json
│        │  │  │  ├─ oxidized_copper_grate_from_oxidized_copper_stonecutting.json
│        │  │  │  ├─ oxidized_cut_copper.json
│        │  │  │  ├─ oxidized_cut_copper_from_oxidized_copper_stonecutting.json
│        │  │  │  ├─ oxidized_cut_copper_slab.json
│        │  │  │  ├─ oxidized_cut_copper_slab_from_oxidized_copper_stonecutting.json
│        │  │  │  ├─ oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting.json
│        │  │  │  ├─ oxidized_cut_copper_stairs.json
│        │  │  │  ├─ oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting.json
│        │  │  │  ├─ oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting.json
│        │  │  │  ├─ packed_ice.json
│        │  │  │  ├─ packed_mud.json
│        │  │  │  ├─ pale_oak_planks.json
│        │  │  │  ├─ pale_oak_slab.json
│        │  │  │  ├─ pale_oak_stairs.json
│        │  │  │  ├─ pale_oak_wood.json
│        │  │  │  ├─ pink_concrete_powder.json
│        │  │  │  ├─ pink_stained_glass.json
│        │  │  │  ├─ pink_terracotta.json
│        │  │  │  ├─ polished_andesite.json
│        │  │  │  ├─ polished_andesite_from_andesite_stonecutting.json
│        │  │  │  ├─ polished_andesite_slab.json
│        │  │  │  ├─ polished_andesite_slab_from_andesite_stonecutting.json
│        │  │  │  ├─ polished_andesite_slab_from_polished_andesite_stonecutting.json
│        │  │  │  ├─ polished_andesite_stairs.json
│        │  │  │  ├─ polished_andesite_stairs_from_andesite_stonecutting.json
│        │  │  │  ├─ polished_andesite_stairs_from_polished_andesite_stonecutting.json
│        │  │  │  ├─ polished_basalt.json
│        │  │  │  ├─ polished_basalt_from_basalt_stonecutting.json
│        │  │  │  ├─ polished_blackstone.json
│        │  │  │  ├─ polished_blackstone_bricks.json
│        │  │  │  ├─ polished_blackstone_bricks_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_bricks_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_slab.json
│        │  │  │  ├─ polished_blackstone_brick_slab_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_slab_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_stairs.json
│        │  │  │  ├─ polished_blackstone_brick_stairs_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_slab.json
│        │  │  │  ├─ polished_blackstone_slab_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_slab_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_stairs.json
│        │  │  │  ├─ polished_blackstone_stairs_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_stairs_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_deepslate.json
│        │  │  │  ├─ polished_deepslate_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ polished_deepslate_slab.json
│        │  │  │  ├─ polished_deepslate_slab_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ polished_deepslate_slab_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ polished_deepslate_stairs.json
│        │  │  │  ├─ polished_deepslate_stairs_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ polished_deepslate_stairs_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ polished_diorite.json
│        │  │  │  ├─ polished_diorite_from_diorite_stonecutting.json
│        │  │  │  ├─ polished_diorite_slab.json
│        │  │  │  ├─ polished_diorite_slab_from_diorite_stonecutting.json
│        │  │  │  ├─ polished_diorite_slab_from_polished_diorite_stonecutting.json
│        │  │  │  ├─ polished_diorite_stairs.json
│        │  │  │  ├─ polished_diorite_stairs_from_diorite_stonecutting.json
│        │  │  │  ├─ polished_diorite_stairs_from_polished_diorite_stonecutting.json
│        │  │  │  ├─ polished_granite.json
│        │  │  │  ├─ polished_granite_from_granite_stonecutting.json
│        │  │  │  ├─ polished_granite_slab.json
│        │  │  │  ├─ polished_granite_slab_from_granite_stonecutting.json
│        │  │  │  ├─ polished_granite_slab_from_polished_granite_stonecutting.json
│        │  │  │  ├─ polished_granite_stairs.json
│        │  │  │  ├─ polished_granite_stairs_from_granite_stonecutting.json
│        │  │  │  ├─ polished_granite_stairs_from_polished_granite_stonecutting.json
│        │  │  │  ├─ polished_tuff.json
│        │  │  │  ├─ polished_tuff_from_tuff_stonecutting.json
│        │  │  │  ├─ polished_tuff_slab.json
│        │  │  │  ├─ polished_tuff_slab_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ polished_tuff_slab_from_tuff_stonecutting.json
│        │  │  │  ├─ polished_tuff_stairs.json
│        │  │  │  ├─ polished_tuff_stairs_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ polished_tuff_stairs_from_tuff_stonecutting.json
│        │  │  │  ├─ prismarine.json
│        │  │  │  ├─ prismarine_bricks.json
│        │  │  │  ├─ prismarine_brick_slab.json
│        │  │  │  ├─ prismarine_brick_slab_from_prismarine_stonecutting.json
│        │  │  │  ├─ prismarine_brick_stairs.json
│        │  │  │  ├─ prismarine_brick_stairs_from_prismarine_stonecutting.json
│        │  │  │  ├─ prismarine_slab.json
│        │  │  │  ├─ prismarine_slab_from_prismarine_stonecutting.json
│        │  │  │  ├─ prismarine_stairs.json
│        │  │  │  ├─ prismarine_stairs_from_prismarine_stonecutting.json
│        │  │  │  ├─ purple_concrete_powder.json
│        │  │  │  ├─ purple_stained_glass.json
│        │  │  │  ├─ purple_terracotta.json
│        │  │  │  ├─ purpur_block.json
│        │  │  │  ├─ purpur_pillar.json
│        │  │  │  ├─ purpur_pillar_from_purpur_block_stonecutting.json
│        │  │  │  ├─ purpur_slab.json
│        │  │  │  ├─ purpur_slab_from_purpur_block_stonecutting.json
│        │  │  │  ├─ purpur_stairs.json
│        │  │  │  ├─ purpur_stairs_from_purpur_block_stonecutting.json
│        │  │  │  ├─ quartz_block.json
│        │  │  │  ├─ quartz_bricks.json
│        │  │  │  ├─ quartz_bricks_from_quartz_block_stonecutting.json
│        │  │  │  ├─ quartz_pillar.json
│        │  │  │  ├─ quartz_pillar_from_quartz_block_stonecutting.json
│        │  │  │  ├─ quartz_slab.json
│        │  │  │  ├─ quartz_slab_from_stonecutting.json
│        │  │  │  ├─ quartz_stairs.json
│        │  │  │  ├─ quartz_stairs_from_quartz_block_stonecutting.json
│        │  │  │  ├─ raw_copper_block.json
│        │  │  │  ├─ raw_gold_block.json
│        │  │  │  ├─ raw_iron_block.json
│        │  │  │  ├─ red_concrete_powder.json
│        │  │  │  ├─ red_nether_bricks.json
│        │  │  │  ├─ red_nether_brick_slab.json
│        │  │  │  ├─ red_nether_brick_slab_from_red_nether_bricks_stonecutting.json
│        │  │  │  ├─ red_nether_brick_stairs.json
│        │  │  │  ├─ red_nether_brick_stairs_from_red_nether_bricks_stonecutting.json
│        │  │  │  ├─ red_sandstone.json
│        │  │  │  ├─ red_sandstone_slab.json
│        │  │  │  ├─ red_sandstone_slab_from_red_sandstone_stonecutting.json
│        │  │  │  ├─ red_sandstone_stairs.json
│        │  │  │  ├─ red_sandstone_stairs_from_red_sandstone_stonecutting.json
│        │  │  │  ├─ red_stained_glass.json
│        │  │  │  ├─ red_terracotta.json
│        │  │  │  ├─ resin_block.json
│        │  │  │  ├─ resin_bricks.json
│        │  │  │  ├─ resin_brick_slab.json
│        │  │  │  ├─ resin_brick_slab_from_resin_bricks_stonecutting.json
│        │  │  │  ├─ resin_brick_stairs.json
│        │  │  │  ├─ resin_brick_stairs_from_resin_bricks_stonecutting.json
│        │  │  │  ├─ sandstone.json
│        │  │  │  ├─ sandstone_slab.json
│        │  │  │  ├─ sandstone_slab_from_sandstone_stonecutting.json
│        │  │  │  ├─ sandstone_stairs.json
│        │  │  │  ├─ sandstone_stairs_from_sandstone_stonecutting.json
│        │  │  │  ├─ sea_lantern.json
│        │  │  │  ├─ smooth_basalt.json
│        │  │  │  ├─ smooth_quartz.json
│        │  │  │  ├─ smooth_quartz_slab.json
│        │  │  │  ├─ smooth_quartz_slab_from_smooth_quartz_stonecutting.json
│        │  │  │  ├─ smooth_quartz_stairs.json
│        │  │  │  ├─ smooth_quartz_stairs_from_smooth_quartz_stonecutting.json
│        │  │  │  ├─ smooth_red_sandstone.json
│        │  │  │  ├─ smooth_red_sandstone_slab.json
│        │  │  │  ├─ smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting.json
│        │  │  │  ├─ smooth_red_sandstone_stairs.json
│        │  │  │  ├─ smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting.json
│        │  │  │  ├─ smooth_sandstone.json
│        │  │  │  ├─ smooth_sandstone_slab.json
│        │  │  │  ├─ smooth_sandstone_slab_from_smooth_sandstone_stonecutting.json
│        │  │  │  ├─ smooth_sandstone_stairs.json
│        │  │  │  ├─ smooth_sandstone_stairs_from_smooth_sandstone_stonecutting.json
│        │  │  │  ├─ smooth_stone.json
│        │  │  │  ├─ smooth_stone_slab.json
│        │  │  │  ├─ smooth_stone_slab_from_smooth_stone_stonecutting.json
│        │  │  │  ├─ snow_block.json
│        │  │  │  ├─ sponge.json
│        │  │  │  ├─ spruce_planks.json
│        │  │  │  ├─ spruce_slab.json
│        │  │  │  ├─ spruce_stairs.json
│        │  │  │  ├─ spruce_wood.json
│        │  │  │  ├─ stone.json
│        │  │  │  ├─ stone_bricks.json
│        │  │  │  ├─ stone_bricks_from_stone_stonecutting.json
│        │  │  │  ├─ stone_brick_slab.json
│        │  │  │  ├─ stone_brick_slab_from_stone_bricks_stonecutting.json
│        │  │  │  ├─ stone_brick_slab_from_stone_stonecutting.json
│        │  │  │  ├─ stone_brick_stairs.json
│        │  │  │  ├─ stone_brick_stairs_from_stone_bricks_stonecutting.json
│        │  │  │  ├─ stone_brick_stairs_from_stone_stonecutting.json
│        │  │  │  ├─ stone_slab.json
│        │  │  │  ├─ stone_slab_from_stone_stonecutting.json
│        │  │  │  ├─ stone_stairs.json
│        │  │  │  ├─ stone_stairs_from_stone_stonecutting.json
│        │  │  │  ├─ stripped_acacia_wood.json
│        │  │  │  ├─ stripped_birch_wood.json
│        │  │  │  ├─ stripped_cherry_wood.json
│        │  │  │  ├─ stripped_crimson_hyphae.json
│        │  │  │  ├─ stripped_dark_oak_wood.json
│        │  │  │  ├─ stripped_jungle_wood.json
│        │  │  │  ├─ stripped_mangrove_wood.json
│        │  │  │  ├─ stripped_oak_wood.json
│        │  │  │  ├─ stripped_pale_oak_wood.json
│        │  │  │  ├─ stripped_spruce_wood.json
│        │  │  │  ├─ stripped_warped_hyphae.json
│        │  │  │  ├─ terracotta.json
│        │  │  │  ├─ tinted_glass.json
│        │  │  │  ├─ tuff_bricks.json
│        │  │  │  ├─ tuff_bricks_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ tuff_bricks_from_tuff_stonecutting.json
│        │  │  │  ├─ tuff_brick_slab.json
│        │  │  │  ├─ tuff_brick_slab_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ tuff_brick_slab_from_tuff_bricks_stonecutting.json
│        │  │  │  ├─ tuff_brick_slab_from_tuff_stonecutting.json
│        │  │  │  ├─ tuff_brick_stairs.json
│        │  │  │  ├─ tuff_brick_stairs_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ tuff_brick_stairs_from_tuff_bricks_stonecutting.json
│        │  │  │  ├─ tuff_brick_stairs_from_tuff_stonecutting.json
│        │  │  │  ├─ tuff_slab.json
│        │  │  │  ├─ tuff_slab_from_tuff_stonecutting.json
│        │  │  │  ├─ tuff_stairs.json
│        │  │  │  ├─ tuff_stairs_from_tuff_stonecutting.json
│        │  │  │  ├─ warped_hyphae.json
│        │  │  │  ├─ warped_planks.json
│        │  │  │  ├─ warped_slab.json
│        │  │  │  ├─ warped_stairs.json
│        │  │  │  ├─ waxed_chiseled_copper.json
│        │  │  │  ├─ waxed_chiseled_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_chiseled_copper_from_waxed_copper_block_stonecutting.json
│        │  │  │  ├─ waxed_chiseled_copper_from_waxed_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_copper_bars_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_block_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_chain_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_chest_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_golem_statue_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_grate.json
│        │  │  │  ├─ waxed_copper_grate_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_grate_from_waxed_copper_block_stonecutting.json
│        │  │  │  ├─ waxed_copper_lantern_from_honeycomb.json
│        │  │  │  ├─ waxed_cut_copper.json
│        │  │  │  ├─ waxed_cut_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_cut_copper_from_waxed_copper_block_stonecutting.json
│        │  │  │  ├─ waxed_cut_copper_slab.json
│        │  │  │  ├─ waxed_cut_copper_slab_from_honeycomb.json
│        │  │  │  ├─ waxed_cut_copper_slab_from_waxed_copper_block_stonecutting.json
│        │  │  │  ├─ waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_cut_copper_stairs.json
│        │  │  │  ├─ waxed_cut_copper_stairs_from_honeycomb.json
│        │  │  │  ├─ waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting.json
│        │  │  │  ├─ waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_chiseled_copper.json
│        │  │  │  ├─ waxed_exposed_chiseled_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_copper_bars_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_chain_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_chest_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_golem_statue_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_grate.json
│        │  │  │  ├─ waxed_exposed_copper_grate_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_copper_lantern_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_cut_copper.json
│        │  │  │  ├─ waxed_exposed_cut_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_cut_copper_slab.json
│        │  │  │  ├─ waxed_exposed_cut_copper_slab_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_cut_copper_stairs.json
│        │  │  │  ├─ waxed_exposed_cut_copper_stairs_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_exposed_lightning_rod_from_honeycomb.json
│        │  │  │  ├─ waxed_lightning_rod_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_chiseled_copper.json
│        │  │  │  ├─ waxed_oxidized_chiseled_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_copper_bars_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_chain_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_chest_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_golem_statue_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_grate.json
│        │  │  │  ├─ waxed_oxidized_copper_grate_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_copper_lantern_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_cut_copper.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_slab.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_slab_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_stairs.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_stairs_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_oxidized_lightning_rod_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_chiseled_copper.json
│        │  │  │  ├─ waxed_weathered_chiseled_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_copper_bars_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_chain_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_chest_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_golem_statue_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_grate.json
│        │  │  │  ├─ waxed_weathered_copper_grate_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_copper_lantern_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_cut_copper.json
│        │  │  │  ├─ waxed_weathered_cut_copper_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_cut_copper_slab.json
│        │  │  │  ├─ waxed_weathered_cut_copper_slab_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_cut_copper_stairs.json
│        │  │  │  ├─ waxed_weathered_cut_copper_stairs_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting.json
│        │  │  │  ├─ waxed_weathered_lightning_rod_from_honeycomb.json
│        │  │  │  ├─ weathered_chiseled_copper.json
│        │  │  │  ├─ weathered_chiseled_copper_from_weathered_copper_stonecutting.json
│        │  │  │  ├─ weathered_chiseled_copper_from_weathered_cut_copper_stonecutting.json
│        │  │  │  ├─ weathered_copper_grate.json
│        │  │  │  ├─ weathered_copper_grate_from_weathered_copper_stonecutting.json
│        │  │  │  ├─ weathered_cut_copper.json
│        │  │  │  ├─ weathered_cut_copper_from_weathered_copper_stonecutting.json
│        │  │  │  ├─ weathered_cut_copper_slab.json
│        │  │  │  ├─ weathered_cut_copper_slab_from_weathered_copper_stonecutting.json
│        │  │  │  ├─ weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting.json
│        │  │  │  ├─ weathered_cut_copper_stairs.json
│        │  │  │  ├─ weathered_cut_copper_stairs_from_weathered_copper_stonecutting.json
│        │  │  │  ├─ weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting.json
│        │  │  │  ├─ white_concrete_powder.json
│        │  │  │  ├─ white_stained_glass.json
│        │  │  │  ├─ white_terracotta.json
│        │  │  │  ├─ white_wool_from_string.json
│        │  │  │  ├─ yellow_concrete_powder.json
│        │  │  │  ├─ yellow_stained_glass.json
│        │  │  │  └─ yellow_terracotta.json
│        │  │  ├─ combat
│        │  │  │  ├─ arrow.json
│        │  │  │  ├─ black_harness.json
│        │  │  │  ├─ blue_harness.json
│        │  │  │  ├─ bow.json
│        │  │  │  ├─ brown_harness.json
│        │  │  │  ├─ copper_boots.json
│        │  │  │  ├─ copper_chestplate.json
│        │  │  │  ├─ copper_helmet.json
│        │  │  │  ├─ copper_leggings.json
│        │  │  │  ├─ copper_spear.json
│        │  │  │  ├─ copper_sword.json
│        │  │  │  ├─ crossbow.json
│        │  │  │  ├─ cyan_harness.json
│        │  │  │  ├─ diamond_boots.json
│        │  │  │  ├─ diamond_chestplate.json
│        │  │  │  ├─ diamond_helmet.json
│        │  │  │  ├─ diamond_leggings.json
│        │  │  │  ├─ diamond_spear.json
│        │  │  │  ├─ diamond_sword.json
│        │  │  │  ├─ dye_black_harness.json
│        │  │  │  ├─ dye_blue_harness.json
│        │  │  │  ├─ dye_brown_harness.json
│        │  │  │  ├─ dye_cyan_harness.json
│        │  │  │  ├─ dye_gray_harness.json
│        │  │  │  ├─ dye_green_harness.json
│        │  │  │  ├─ dye_light_blue_harness.json
│        │  │  │  ├─ dye_light_gray_harness.json
│        │  │  │  ├─ dye_lime_harness.json
│        │  │  │  ├─ dye_magenta_harness.json
│        │  │  │  ├─ dye_orange_harness.json
│        │  │  │  ├─ dye_pink_harness.json
│        │  │  │  ├─ dye_purple_harness.json
│        │  │  │  ├─ dye_red_harness.json
│        │  │  │  ├─ dye_white_harness.json
│        │  │  │  ├─ dye_yellow_harness.json
│        │  │  │  ├─ golden_boots.json
│        │  │  │  ├─ golden_chestplate.json
│        │  │  │  ├─ golden_helmet.json
│        │  │  │  ├─ golden_leggings.json
│        │  │  │  ├─ golden_spear.json
│        │  │  │  ├─ golden_sword.json
│        │  │  │  ├─ gray_harness.json
│        │  │  │  ├─ green_harness.json
│        │  │  │  ├─ iron_boots.json
│        │  │  │  ├─ iron_chestplate.json
│        │  │  │  ├─ iron_helmet.json
│        │  │  │  ├─ iron_leggings.json
│        │  │  │  ├─ iron_spear.json
│        │  │  │  ├─ iron_sword.json
│        │  │  │  ├─ leather_boots.json
│        │  │  │  ├─ leather_chestplate.json
│        │  │  │  ├─ leather_helmet.json
│        │  │  │  ├─ leather_leggings.json
│        │  │  │  ├─ light_blue_harness.json
│        │  │  │  ├─ light_gray_harness.json
│        │  │  │  ├─ lime_harness.json
│        │  │  │  ├─ mace.json
│        │  │  │  ├─ magenta_harness.json
│        │  │  │  ├─ netherite_boots_smithing.json
│        │  │  │  ├─ netherite_chestplate_smithing.json
│        │  │  │  ├─ netherite_helmet_smithing.json
│        │  │  │  ├─ netherite_horse_armor_smithing.json
│        │  │  │  ├─ netherite_leggings_smithing.json
│        │  │  │  ├─ netherite_nautilus_armor_smithing.json
│        │  │  │  ├─ netherite_spear_smithing.json
│        │  │  │  ├─ netherite_sword_smithing.json
│        │  │  │  ├─ orange_harness.json
│        │  │  │  ├─ pink_harness.json
│        │  │  │  ├─ purple_harness.json
│        │  │  │  ├─ red_harness.json
│        │  │  │  ├─ saddle.json
│        │  │  │  ├─ shield.json
│        │  │  │  ├─ spectral_arrow.json
│        │  │  │  ├─ stone_spear.json
│        │  │  │  ├─ stone_sword.json
│        │  │  │  ├─ turtle_helmet.json
│        │  │  │  ├─ white_harness.json
│        │  │  │  ├─ wolf_armor.json
│        │  │  │  ├─ wooden_spear.json
│        │  │  │  ├─ wooden_sword.json
│        │  │  │  └─ yellow_harness.json
│        │  │  ├─ decorations
│        │  │  │  ├─ acacia_fence.json
│        │  │  │  ├─ acacia_hanging_sign.json
│        │  │  │  ├─ acacia_shelf.json
│        │  │  │  ├─ acacia_sign.json
│        │  │  │  ├─ andesite_wall.json
│        │  │  │  ├─ andesite_wall_from_andesite_stonecutting.json
│        │  │  │  ├─ anvil.json
│        │  │  │  ├─ armor_stand.json
│        │  │  │  ├─ bamboo_fence.json
│        │  │  │  ├─ bamboo_hanging_sign.json
│        │  │  │  ├─ bamboo_mosaic.json
│        │  │  │  ├─ bamboo_shelf.json
│        │  │  │  ├─ bamboo_sign.json
│        │  │  │  ├─ barrel.json
│        │  │  │  ├─ beehive.json
│        │  │  │  ├─ birch_fence.json
│        │  │  │  ├─ birch_hanging_sign.json
│        │  │  │  ├─ birch_shelf.json
│        │  │  │  ├─ birch_sign.json
│        │  │  │  ├─ blackstone_wall.json
│        │  │  │  ├─ blackstone_wall_from_blackstone_stonecutting.json
│        │  │  │  ├─ black_banner.json
│        │  │  │  ├─ black_bed.json
│        │  │  │  ├─ black_candle.json
│        │  │  │  ├─ black_carpet.json
│        │  │  │  ├─ black_glazed_terracotta.json
│        │  │  │  ├─ black_shulker_box.json
│        │  │  │  ├─ black_stained_glass_pane.json
│        │  │  │  ├─ black_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ blast_furnace.json
│        │  │  │  ├─ blue_banner.json
│        │  │  │  ├─ blue_bed.json
│        │  │  │  ├─ blue_candle.json
│        │  │  │  ├─ blue_carpet.json
│        │  │  │  ├─ blue_glazed_terracotta.json
│        │  │  │  ├─ blue_shulker_box.json
│        │  │  │  ├─ blue_stained_glass_pane.json
│        │  │  │  ├─ blue_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ brick_wall.json
│        │  │  │  ├─ brick_wall_from_bricks_stonecutting.json
│        │  │  │  ├─ brown_banner.json
│        │  │  │  ├─ brown_bed.json
│        │  │  │  ├─ brown_candle.json
│        │  │  │  ├─ brown_carpet.json
│        │  │  │  ├─ brown_glazed_terracotta.json
│        │  │  │  ├─ brown_shulker_box.json
│        │  │  │  ├─ brown_stained_glass_pane.json
│        │  │  │  ├─ brown_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ campfire.json
│        │  │  │  ├─ candle.json
│        │  │  │  ├─ cartography_table.json
│        │  │  │  ├─ cherry_fence.json
│        │  │  │  ├─ cherry_hanging_sign.json
│        │  │  │  ├─ cherry_shelf.json
│        │  │  │  ├─ cherry_sign.json
│        │  │  │  ├─ chest.json
│        │  │  │  ├─ cobbled_deepslate_wall.json
│        │  │  │  ├─ cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ cobblestone_wall.json
│        │  │  │  ├─ cobblestone_wall_from_cobblestone_stonecutting.json
│        │  │  │  ├─ composter.json
│        │  │  │  ├─ copper_bars.json
│        │  │  │  ├─ copper_chain.json
│        │  │  │  ├─ copper_chest.json
│        │  │  │  ├─ copper_lantern.json
│        │  │  │  ├─ copper_torch.json
│        │  │  │  ├─ crafting_table.json
│        │  │  │  ├─ crimson_fence.json
│        │  │  │  ├─ crimson_hanging_sign.json
│        │  │  │  ├─ crimson_shelf.json
│        │  │  │  ├─ crimson_sign.json
│        │  │  │  ├─ cyan_banner.json
│        │  │  │  ├─ cyan_bed.json
│        │  │  │  ├─ cyan_candle.json
│        │  │  │  ├─ cyan_carpet.json
│        │  │  │  ├─ cyan_glazed_terracotta.json
│        │  │  │  ├─ cyan_shulker_box.json
│        │  │  │  ├─ cyan_stained_glass_pane.json
│        │  │  │  ├─ cyan_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ dark_oak_fence.json
│        │  │  │  ├─ dark_oak_hanging_sign.json
│        │  │  │  ├─ dark_oak_shelf.json
│        │  │  │  ├─ dark_oak_sign.json
│        │  │  │  ├─ decorated_pot_simple.json
│        │  │  │  ├─ deepslate_brick_wall.json
│        │  │  │  ├─ deepslate_brick_wall_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_brick_wall_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_brick_wall_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tile_wall.json
│        │  │  │  ├─ deepslate_tile_wall_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ deepslate_tile_wall_from_deepslate_bricks_stonecutting.json
│        │  │  │  ├─ deepslate_tile_wall_from_deepslate_tiles_stonecutting.json
│        │  │  │  ├─ deepslate_tile_wall_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ diorite_wall.json
│        │  │  │  ├─ diorite_wall_from_diorite_stonecutting.json
│        │  │  │  ├─ dye_black_bed.json
│        │  │  │  ├─ dye_black_carpet.json
│        │  │  │  ├─ dye_blue_bed.json
│        │  │  │  ├─ dye_blue_carpet.json
│        │  │  │  ├─ dye_brown_bed.json
│        │  │  │  ├─ dye_brown_carpet.json
│        │  │  │  ├─ dye_cyan_bed.json
│        │  │  │  ├─ dye_cyan_carpet.json
│        │  │  │  ├─ dye_gray_bed.json
│        │  │  │  ├─ dye_gray_carpet.json
│        │  │  │  ├─ dye_green_bed.json
│        │  │  │  ├─ dye_green_carpet.json
│        │  │  │  ├─ dye_light_blue_bed.json
│        │  │  │  ├─ dye_light_blue_carpet.json
│        │  │  │  ├─ dye_light_gray_bed.json
│        │  │  │  ├─ dye_light_gray_carpet.json
│        │  │  │  ├─ dye_lime_bed.json
│        │  │  │  ├─ dye_lime_carpet.json
│        │  │  │  ├─ dye_magenta_bed.json
│        │  │  │  ├─ dye_magenta_carpet.json
│        │  │  │  ├─ dye_orange_bed.json
│        │  │  │  ├─ dye_orange_carpet.json
│        │  │  │  ├─ dye_pink_bed.json
│        │  │  │  ├─ dye_pink_carpet.json
│        │  │  │  ├─ dye_purple_bed.json
│        │  │  │  ├─ dye_purple_carpet.json
│        │  │  │  ├─ dye_red_bed.json
│        │  │  │  ├─ dye_red_carpet.json
│        │  │  │  ├─ dye_white_bed.json
│        │  │  │  ├─ dye_white_carpet.json
│        │  │  │  ├─ dye_yellow_bed.json
│        │  │  │  ├─ dye_yellow_carpet.json
│        │  │  │  ├─ enchanting_table.json
│        │  │  │  ├─ ender_chest.json
│        │  │  │  ├─ end_crystal.json
│        │  │  │  ├─ end_rod.json
│        │  │  │  ├─ end_stone_brick_wall.json
│        │  │  │  ├─ end_stone_brick_wall_from_end_stone_brick_stonecutting.json
│        │  │  │  ├─ end_stone_brick_wall_from_end_stone_stonecutting.json
│        │  │  │  ├─ fletching_table.json
│        │  │  │  ├─ flower_pot.json
│        │  │  │  ├─ furnace.json
│        │  │  │  ├─ glass_pane.json
│        │  │  │  ├─ glow_item_frame.json
│        │  │  │  ├─ granite_wall.json
│        │  │  │  ├─ granite_wall_from_granite_stonecutting.json
│        │  │  │  ├─ gray_banner.json
│        │  │  │  ├─ gray_bed.json
│        │  │  │  ├─ gray_candle.json
│        │  │  │  ├─ gray_carpet.json
│        │  │  │  ├─ gray_glazed_terracotta.json
│        │  │  │  ├─ gray_shulker_box.json
│        │  │  │  ├─ gray_stained_glass_pane.json
│        │  │  │  ├─ gray_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ green_banner.json
│        │  │  │  ├─ green_bed.json
│        │  │  │  ├─ green_candle.json
│        │  │  │  ├─ green_carpet.json
│        │  │  │  ├─ green_glazed_terracotta.json
│        │  │  │  ├─ green_shulker_box.json
│        │  │  │  ├─ green_stained_glass_pane.json
│        │  │  │  ├─ green_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ grindstone.json
│        │  │  │  ├─ honeycomb_block.json
│        │  │  │  ├─ iron_bars.json
│        │  │  │  ├─ iron_chain.json
│        │  │  │  ├─ item_frame.json
│        │  │  │  ├─ jukebox.json
│        │  │  │  ├─ jungle_fence.json
│        │  │  │  ├─ jungle_hanging_sign.json
│        │  │  │  ├─ jungle_shelf.json
│        │  │  │  ├─ jungle_sign.json
│        │  │  │  ├─ ladder.json
│        │  │  │  ├─ lantern.json
│        │  │  │  ├─ light_blue_banner.json
│        │  │  │  ├─ light_blue_bed.json
│        │  │  │  ├─ light_blue_candle.json
│        │  │  │  ├─ light_blue_carpet.json
│        │  │  │  ├─ light_blue_glazed_terracotta.json
│        │  │  │  ├─ light_blue_shulker_box.json
│        │  │  │  ├─ light_blue_stained_glass_pane.json
│        │  │  │  ├─ light_blue_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ light_gray_banner.json
│        │  │  │  ├─ light_gray_bed.json
│        │  │  │  ├─ light_gray_candle.json
│        │  │  │  ├─ light_gray_carpet.json
│        │  │  │  ├─ light_gray_glazed_terracotta.json
│        │  │  │  ├─ light_gray_shulker_box.json
│        │  │  │  ├─ light_gray_stained_glass_pane.json
│        │  │  │  ├─ light_gray_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ lime_banner.json
│        │  │  │  ├─ lime_bed.json
│        │  │  │  ├─ lime_candle.json
│        │  │  │  ├─ lime_carpet.json
│        │  │  │  ├─ lime_glazed_terracotta.json
│        │  │  │  ├─ lime_shulker_box.json
│        │  │  │  ├─ lime_stained_glass_pane.json
│        │  │  │  ├─ lime_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ lodestone.json
│        │  │  │  ├─ loom.json
│        │  │  │  ├─ magenta_banner.json
│        │  │  │  ├─ magenta_bed.json
│        │  │  │  ├─ magenta_candle.json
│        │  │  │  ├─ magenta_carpet.json
│        │  │  │  ├─ magenta_glazed_terracotta.json
│        │  │  │  ├─ magenta_shulker_box.json
│        │  │  │  ├─ magenta_stained_glass_pane.json
│        │  │  │  ├─ magenta_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ mangrove_fence.json
│        │  │  │  ├─ mangrove_hanging_sign.json
│        │  │  │  ├─ mangrove_shelf.json
│        │  │  │  ├─ mangrove_sign.json
│        │  │  │  ├─ mossy_cobblestone_wall.json
│        │  │  │  ├─ mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting.json
│        │  │  │  ├─ mossy_stone_brick_wall.json
│        │  │  │  ├─ mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting.json
│        │  │  │  ├─ moss_carpet.json
│        │  │  │  ├─ mud_brick_wall.json
│        │  │  │  ├─ mud_brick_wall_from_mud_bricks_stonecutting.json
│        │  │  │  ├─ nether_brick_fence.json
│        │  │  │  ├─ nether_brick_wall.json
│        │  │  │  ├─ nether_brick_wall_from_nether_bricks_stonecutting.json
│        │  │  │  ├─ oak_fence.json
│        │  │  │  ├─ oak_hanging_sign.json
│        │  │  │  ├─ oak_shelf.json
│        │  │  │  ├─ oak_sign.json
│        │  │  │  ├─ orange_banner.json
│        │  │  │  ├─ orange_bed.json
│        │  │  │  ├─ orange_candle.json
│        │  │  │  ├─ orange_carpet.json
│        │  │  │  ├─ orange_glazed_terracotta.json
│        │  │  │  ├─ orange_shulker_box.json
│        │  │  │  ├─ orange_stained_glass_pane.json
│        │  │  │  ├─ orange_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ painting.json
│        │  │  │  ├─ pale_moss_carpet.json
│        │  │  │  ├─ pale_oak_fence.json
│        │  │  │  ├─ pale_oak_hanging_sign.json
│        │  │  │  ├─ pale_oak_shelf.json
│        │  │  │  ├─ pale_oak_sign.json
│        │  │  │  ├─ pink_banner.json
│        │  │  │  ├─ pink_bed.json
│        │  │  │  ├─ pink_candle.json
│        │  │  │  ├─ pink_carpet.json
│        │  │  │  ├─ pink_glazed_terracotta.json
│        │  │  │  ├─ pink_shulker_box.json
│        │  │  │  ├─ pink_stained_glass_pane.json
│        │  │  │  ├─ pink_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ polished_blackstone_brick_wall.json
│        │  │  │  ├─ polished_blackstone_brick_wall_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting.json
│        │  │  │  ├─ polished_blackstone_brick_wall_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_wall.json
│        │  │  │  ├─ polished_blackstone_wall_from_blackstone_stonecutting.json
│        │  │  │  ├─ polished_blackstone_wall_from_polished_blackstone_stonecutting.json
│        │  │  │  ├─ polished_deepslate_wall.json
│        │  │  │  ├─ polished_deepslate_wall_from_cobbled_deepslate_stonecutting.json
│        │  │  │  ├─ polished_deepslate_wall_from_polished_deepslate_stonecutting.json
│        │  │  │  ├─ polished_tuff_wall.json
│        │  │  │  ├─ polished_tuff_wall_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ polished_tuff_wall_from_tuff_stonecutting.json
│        │  │  │  ├─ prismarine_wall.json
│        │  │  │  ├─ prismarine_wall_from_prismarine_stonecutting.json
│        │  │  │  ├─ purple_banner.json
│        │  │  │  ├─ purple_bed.json
│        │  │  │  ├─ purple_candle.json
│        │  │  │  ├─ purple_carpet.json
│        │  │  │  ├─ purple_glazed_terracotta.json
│        │  │  │  ├─ purple_shulker_box.json
│        │  │  │  ├─ purple_stained_glass_pane.json
│        │  │  │  ├─ purple_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ red_banner.json
│        │  │  │  ├─ red_bed.json
│        │  │  │  ├─ red_candle.json
│        │  │  │  ├─ red_carpet.json
│        │  │  │  ├─ red_glazed_terracotta.json
│        │  │  │  ├─ red_nether_brick_wall.json
│        │  │  │  ├─ red_nether_brick_wall_from_red_nether_bricks_stonecutting.json
│        │  │  │  ├─ red_sandstone_wall.json
│        │  │  │  ├─ red_sandstone_wall_from_red_sandstone_stonecutting.json
│        │  │  │  ├─ red_shulker_box.json
│        │  │  │  ├─ red_stained_glass_pane.json
│        │  │  │  ├─ red_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ resin_brick_wall.json
│        │  │  │  ├─ resin_brick_wall_from_resin_bricks_stonecutting.json
│        │  │  │  ├─ respawn_anchor.json
│        │  │  │  ├─ sandstone_wall.json
│        │  │  │  ├─ sandstone_wall_from_sandstone_stonecutting.json
│        │  │  │  ├─ scaffolding.json
│        │  │  │  ├─ shulker_box.json
│        │  │  │  ├─ smithing_table.json
│        │  │  │  ├─ smoker.json
│        │  │  │  ├─ snow.json
│        │  │  │  ├─ soul_campfire.json
│        │  │  │  ├─ soul_lantern.json
│        │  │  │  ├─ soul_torch.json
│        │  │  │  ├─ spruce_fence.json
│        │  │  │  ├─ spruce_hanging_sign.json
│        │  │  │  ├─ spruce_shelf.json
│        │  │  │  ├─ spruce_sign.json
│        │  │  │  ├─ stonecutter.json
│        │  │  │  ├─ stone_brick_wall.json
│        │  │  │  ├─ stone_brick_walls_from_stone_stonecutting.json
│        │  │  │  ├─ stone_brick_wall_from_stone_bricks_stonecutting.json
│        │  │  │  ├─ torch.json
│        │  │  │  ├─ tuff_brick_wall.json
│        │  │  │  ├─ tuff_brick_wall_from_polished_tuff_stonecutting.json
│        │  │  │  ├─ tuff_brick_wall_from_tuff_bricks_stonecutting.json
│        │  │  │  ├─ tuff_brick_wall_from_tuff_stonecutting.json
│        │  │  │  ├─ tuff_wall.json
│        │  │  │  ├─ tuff_wall_from_tuff_stonecutting.json
│        │  │  │  ├─ warped_fence.json
│        │  │  │  ├─ warped_hanging_sign.json
│        │  │  │  ├─ warped_shelf.json
│        │  │  │  ├─ warped_sign.json
│        │  │  │  ├─ white_banner.json
│        │  │  │  ├─ white_bed.json
│        │  │  │  ├─ white_candle.json
│        │  │  │  ├─ white_carpet.json
│        │  │  │  ├─ white_glazed_terracotta.json
│        │  │  │  ├─ white_shulker_box.json
│        │  │  │  ├─ white_stained_glass_pane.json
│        │  │  │  ├─ white_stained_glass_pane_from_glass_pane.json
│        │  │  │  ├─ yellow_banner.json
│        │  │  │  ├─ yellow_bed.json
│        │  │  │  ├─ yellow_candle.json
│        │  │  │  ├─ yellow_carpet.json
│        │  │  │  ├─ yellow_glazed_terracotta.json
│        │  │  │  ├─ yellow_shulker_box.json
│        │  │  │  ├─ yellow_stained_glass_pane.json
│        │  │  │  └─ yellow_stained_glass_pane_from_glass_pane.json
│        │  │  ├─ food
│        │  │  │  ├─ baked_potato.json
│        │  │  │  ├─ baked_potato_from_campfire_cooking.json
│        │  │  │  ├─ baked_potato_from_smoking.json
│        │  │  │  ├─ beetroot_soup.json
│        │  │  │  ├─ bread.json
│        │  │  │  ├─ cake.json
│        │  │  │  ├─ cooked_beef.json
│        │  │  │  ├─ cooked_beef_from_campfire_cooking.json
│        │  │  │  ├─ cooked_beef_from_smoking.json
│        │  │  │  ├─ cooked_chicken.json
│        │  │  │  ├─ cooked_chicken_from_campfire_cooking.json
│        │  │  │  ├─ cooked_chicken_from_smoking.json
│        │  │  │  ├─ cooked_cod.json
│        │  │  │  ├─ cooked_cod_from_campfire_cooking.json
│        │  │  │  ├─ cooked_cod_from_smoking.json
│        │  │  │  ├─ cooked_mutton.json
│        │  │  │  ├─ cooked_mutton_from_campfire_cooking.json
│        │  │  │  ├─ cooked_mutton_from_smoking.json
│        │  │  │  ├─ cooked_porkchop.json
│        │  │  │  ├─ cooked_porkchop_from_campfire_cooking.json
│        │  │  │  ├─ cooked_porkchop_from_smoking.json
│        │  │  │  ├─ cooked_rabbit.json
│        │  │  │  ├─ cooked_rabbit_from_campfire_cooking.json
│        │  │  │  ├─ cooked_rabbit_from_smoking.json
│        │  │  │  ├─ cooked_salmon.json
│        │  │  │  ├─ cooked_salmon_from_campfire_cooking.json
│        │  │  │  ├─ cooked_salmon_from_smoking.json
│        │  │  │  ├─ cookie.json
│        │  │  │  ├─ dried_kelp.json
│        │  │  │  ├─ dried_kelp_from_campfire_cooking.json
│        │  │  │  ├─ dried_kelp_from_smelting.json
│        │  │  │  ├─ dried_kelp_from_smoking.json
│        │  │  │  ├─ golden_apple.json
│        │  │  │  ├─ honey_bottle.json
│        │  │  │  ├─ mushroom_stew.json
│        │  │  │  ├─ pumpkin_pie.json
│        │  │  │  ├─ rabbit_stew_from_brown_mushroom.json
│        │  │  │  ├─ rabbit_stew_from_red_mushroom.json
│        │  │  │  ├─ suspicious_stew_from_allium.json
│        │  │  │  ├─ suspicious_stew_from_azure_bluet.json
│        │  │  │  ├─ suspicious_stew_from_blue_orchid.json
│        │  │  │  ├─ suspicious_stew_from_closed_eyeblossom.json
│        │  │  │  ├─ suspicious_stew_from_cornflower.json
│        │  │  │  ├─ suspicious_stew_from_dandelion.json
│        │  │  │  ├─ suspicious_stew_from_lily_of_the_valley.json
│        │  │  │  ├─ suspicious_stew_from_open_eyeblossom.json
│        │  │  │  ├─ suspicious_stew_from_orange_tulip.json
│        │  │  │  ├─ suspicious_stew_from_oxeye_daisy.json
│        │  │  │  ├─ suspicious_stew_from_pink_tulip.json
│        │  │  │  ├─ suspicious_stew_from_poppy.json
│        │  │  │  ├─ suspicious_stew_from_red_tulip.json
│        │  │  │  ├─ suspicious_stew_from_torchflower.json
│        │  │  │  ├─ suspicious_stew_from_white_tulip.json
│        │  │  │  └─ suspicious_stew_from_wither_rose.json
│        │  │  ├─ misc
│        │  │  │  ├─ beacon.json
│        │  │  │  ├─ black_dye.json
│        │  │  │  ├─ black_dye_from_wither_rose.json
│        │  │  │  ├─ blue_dye.json
│        │  │  │  ├─ blue_dye_from_cornflower.json
│        │  │  │  ├─ bolt_armor_trim_smithing_template.json
│        │  │  │  ├─ bolt_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ bone_meal.json
│        │  │  │  ├─ bone_meal_from_bone_block.json
│        │  │  │  ├─ book.json
│        │  │  │  ├─ bordure_indented_banner_pattern.json
│        │  │  │  ├─ bowl.json
│        │  │  │  ├─ brick.json
│        │  │  │  ├─ brown_dye.json
│        │  │  │  ├─ bucket.json
│        │  │  │  ├─ charcoal.json
│        │  │  │  ├─ coal.json
│        │  │  │  ├─ coal_from_blasting_coal_ore.json
│        │  │  │  ├─ coal_from_blasting_deepslate_coal_ore.json
│        │  │  │  ├─ coal_from_smelting_coal_ore.json
│        │  │  │  ├─ coal_from_smelting_deepslate_coal_ore.json
│        │  │  │  ├─ coast_armor_trim_smithing_template.json
│        │  │  │  ├─ coast_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ conduit.json
│        │  │  │  ├─ copper_ingot.json
│        │  │  │  ├─ copper_ingot_from_blasting_copper_ore.json
│        │  │  │  ├─ copper_ingot_from_blasting_deepslate_copper_ore.json
│        │  │  │  ├─ copper_ingot_from_blasting_raw_copper.json
│        │  │  │  ├─ copper_ingot_from_nuggets.json
│        │  │  │  ├─ copper_ingot_from_smelting_copper_ore.json
│        │  │  │  ├─ copper_ingot_from_smelting_deepslate_copper_ore.json
│        │  │  │  ├─ copper_ingot_from_smelting_raw_copper.json
│        │  │  │  ├─ copper_ingot_from_waxed_copper_block.json
│        │  │  │  ├─ copper_nugget.json
│        │  │  │  ├─ copper_nugget_from_blasting.json
│        │  │  │  ├─ copper_nugget_from_smelting.json
│        │  │  │  ├─ creaking_heart.json
│        │  │  │  ├─ creeper_banner_pattern.json
│        │  │  │  ├─ cyan_dye.json
│        │  │  │  ├─ cyan_dye_from_pitcher_plant.json
│        │  │  │  ├─ diamond.json
│        │  │  │  ├─ diamond_from_blasting_deepslate_diamond_ore.json
│        │  │  │  ├─ diamond_from_blasting_diamond_ore.json
│        │  │  │  ├─ diamond_from_smelting_deepslate_diamond_ore.json
│        │  │  │  ├─ diamond_from_smelting_diamond_ore.json
│        │  │  │  ├─ dune_armor_trim_smithing_template.json
│        │  │  │  ├─ dune_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ emerald.json
│        │  │  │  ├─ emerald_from_blasting_deepslate_emerald_ore.json
│        │  │  │  ├─ emerald_from_blasting_emerald_ore.json
│        │  │  │  ├─ emerald_from_smelting_deepslate_emerald_ore.json
│        │  │  │  ├─ emerald_from_smelting_emerald_ore.json
│        │  │  │  ├─ ender_eye.json
│        │  │  │  ├─ eye_armor_trim_smithing_template.json
│        │  │  │  ├─ eye_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ field_masoned_banner_pattern.json
│        │  │  │  ├─ firework_rocket_simple.json
│        │  │  │  ├─ fire_charge.json
│        │  │  │  ├─ flower_banner_pattern.json
│        │  │  │  ├─ flow_armor_trim_smithing_template.json
│        │  │  │  ├─ flow_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ gold_ingot_from_blasting_deepslate_gold_ore.json
│        │  │  │  ├─ gold_ingot_from_blasting_gold_ore.json
│        │  │  │  ├─ gold_ingot_from_blasting_nether_gold_ore.json
│        │  │  │  ├─ gold_ingot_from_blasting_raw_gold.json
│        │  │  │  ├─ gold_ingot_from_gold_block.json
│        │  │  │  ├─ gold_ingot_from_nuggets.json
│        │  │  │  ├─ gold_ingot_from_smelting_deepslate_gold_ore.json
│        │  │  │  ├─ gold_ingot_from_smelting_gold_ore.json
│        │  │  │  ├─ gold_ingot_from_smelting_nether_gold_ore.json
│        │  │  │  ├─ gold_ingot_from_smelting_raw_gold.json
│        │  │  │  ├─ gold_nugget.json
│        │  │  │  ├─ gold_nugget_from_blasting.json
│        │  │  │  ├─ gold_nugget_from_smelting.json
│        │  │  │  ├─ gray_dye.json
│        │  │  │  ├─ gray_dye_from_closed_eyeblossom.json
│        │  │  │  ├─ green_dye.json
│        │  │  │  ├─ host_armor_trim_smithing_template.json
│        │  │  │  ├─ host_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ iron_ingot_from_blasting_deepslate_iron_ore.json
│        │  │  │  ├─ iron_ingot_from_blasting_iron_ore.json
│        │  │  │  ├─ iron_ingot_from_blasting_raw_iron.json
│        │  │  │  ├─ iron_ingot_from_iron_block.json
│        │  │  │  ├─ iron_ingot_from_nuggets.json
│        │  │  │  ├─ iron_ingot_from_smelting_deepslate_iron_ore.json
│        │  │  │  ├─ iron_ingot_from_smelting_iron_ore.json
│        │  │  │  ├─ iron_ingot_from_smelting_raw_iron.json
│        │  │  │  ├─ iron_nugget.json
│        │  │  │  ├─ iron_nugget_from_blasting.json
│        │  │  │  ├─ iron_nugget_from_smelting.json
│        │  │  │  ├─ lapis_lazuli.json
│        │  │  │  ├─ lapis_lazuli_from_blasting_deepslate_lapis_ore.json
│        │  │  │  ├─ lapis_lazuli_from_blasting_lapis_ore.json
│        │  │  │  ├─ lapis_lazuli_from_smelting_deepslate_lapis_ore.json
│        │  │  │  ├─ lapis_lazuli_from_smelting_lapis_ore.json
│        │  │  │  ├─ leaf_litter.json
│        │  │  │  ├─ leather.json
│        │  │  │  ├─ leather_horse_armor.json
│        │  │  │  ├─ light_blue_dye_from_blue_orchid.json
│        │  │  │  ├─ light_blue_dye_from_blue_white_dye.json
│        │  │  │  ├─ light_gray_dye_from_azure_bluet.json
│        │  │  │  ├─ light_gray_dye_from_black_white_dye.json
│        │  │  │  ├─ light_gray_dye_from_gray_white_dye.json
│        │  │  │  ├─ light_gray_dye_from_oxeye_daisy.json
│        │  │  │  ├─ light_gray_dye_from_white_tulip.json
│        │  │  │  ├─ lime_dye.json
│        │  │  │  ├─ lime_dye_from_smelting.json
│        │  │  │  ├─ magenta_dye_from_allium.json
│        │  │  │  ├─ magenta_dye_from_blue_red_pink.json
│        │  │  │  ├─ magenta_dye_from_blue_red_white_dye.json
│        │  │  │  ├─ magenta_dye_from_lilac.json
│        │  │  │  ├─ magenta_dye_from_purple_and_pink.json
│        │  │  │  ├─ map.json
│        │  │  │  ├─ melon_seeds.json
│        │  │  │  ├─ mojang_banner_pattern.json
│        │  │  │  ├─ music_disc_5.json
│        │  │  │  ├─ netherite_ingot.json
│        │  │  │  ├─ netherite_ingot_from_netherite_block.json
│        │  │  │  ├─ netherite_scrap.json
│        │  │  │  ├─ netherite_scrap_from_blasting.json
│        │  │  │  ├─ netherite_upgrade_smithing_template.json
│        │  │  │  ├─ nether_brick.json
│        │  │  │  ├─ orange_dye_from_open_eyeblossom.json
│        │  │  │  ├─ orange_dye_from_orange_tulip.json
│        │  │  │  ├─ orange_dye_from_red_yellow.json
│        │  │  │  ├─ orange_dye_from_torchflower.json
│        │  │  │  ├─ paper.json
│        │  │  │  ├─ pink_dye_from_cactus_flower.json
│        │  │  │  ├─ pink_dye_from_peony.json
│        │  │  │  ├─ pink_dye_from_pink_petals.json
│        │  │  │  ├─ pink_dye_from_pink_tulip.json
│        │  │  │  ├─ pink_dye_from_red_white_dye.json
│        │  │  │  ├─ popped_chorus_fruit.json
│        │  │  │  ├─ pumpkin_seeds.json
│        │  │  │  ├─ purple_dye.json
│        │  │  │  ├─ quartz.json
│        │  │  │  ├─ quartz_from_blasting.json
│        │  │  │  ├─ raiser_armor_trim_smithing_template.json
│        │  │  │  ├─ raiser_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ raw_copper.json
│        │  │  │  ├─ raw_gold.json
│        │  │  │  ├─ raw_iron.json
│        │  │  │  ├─ red_dye_from_beetroot.json
│        │  │  │  ├─ red_dye_from_poppy.json
│        │  │  │  ├─ red_dye_from_rose_bush.json
│        │  │  │  ├─ red_dye_from_tulip.json
│        │  │  │  ├─ resin_brick.json
│        │  │  │  ├─ resin_clump.json
│        │  │  │  ├─ rib_armor_trim_smithing_template.json
│        │  │  │  ├─ rib_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ sentry_armor_trim_smithing_template.json
│        │  │  │  ├─ sentry_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ shaper_armor_trim_smithing_template.json
│        │  │  │  ├─ shaper_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ silence_armor_trim_smithing_template.json
│        │  │  │  ├─ silence_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ skull_banner_pattern.json
│        │  │  │  ├─ slime_ball.json
│        │  │  │  ├─ snout_armor_trim_smithing_template.json
│        │  │  │  ├─ snout_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ spire_armor_trim_smithing_template.json
│        │  │  │  ├─ spire_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ stick.json
│        │  │  │  ├─ stick_from_bamboo_item.json
│        │  │  │  ├─ sugar_from_honey_bottle.json
│        │  │  │  ├─ sugar_from_sugar_cane.json
│        │  │  │  ├─ tide_armor_trim_smithing_template.json
│        │  │  │  ├─ tide_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ vex_armor_trim_smithing_template.json
│        │  │  │  ├─ vex_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ ward_armor_trim_smithing_template.json
│        │  │  │  ├─ ward_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ wayfinder_armor_trim_smithing_template.json
│        │  │  │  ├─ wayfinder_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ wheat.json
│        │  │  │  ├─ white_dye.json
│        │  │  │  ├─ white_dye_from_lily_of_the_valley.json
│        │  │  │  ├─ wild_armor_trim_smithing_template.json
│        │  │  │  ├─ wild_armor_trim_smithing_template_smithing_trim.json
│        │  │  │  ├─ wind_charge.json
│        │  │  │  ├─ writable_book.json
│        │  │  │  ├─ yellow_dye_from_dandelion.json
│        │  │  │  ├─ yellow_dye_from_sunflower.json
│        │  │  │  └─ yellow_dye_from_wildflowers.json
│        │  │  ├─ redstone
│        │  │  │  ├─ acacia_button.json
│        │  │  │  ├─ acacia_door.json
│        │  │  │  ├─ acacia_fence_gate.json
│        │  │  │  ├─ acacia_pressure_plate.json
│        │  │  │  ├─ acacia_trapdoor.json
│        │  │  │  ├─ bamboo_button.json
│        │  │  │  ├─ bamboo_door.json
│        │  │  │  ├─ bamboo_fence_gate.json
│        │  │  │  ├─ bamboo_pressure_plate.json
│        │  │  │  ├─ bamboo_trapdoor.json
│        │  │  │  ├─ birch_button.json
│        │  │  │  ├─ birch_door.json
│        │  │  │  ├─ birch_fence_gate.json
│        │  │  │  ├─ birch_pressure_plate.json
│        │  │  │  ├─ birch_trapdoor.json
│        │  │  │  ├─ calibrated_sculk_sensor.json
│        │  │  │  ├─ cherry_button.json
│        │  │  │  ├─ cherry_door.json
│        │  │  │  ├─ cherry_fence_gate.json
│        │  │  │  ├─ cherry_pressure_plate.json
│        │  │  │  ├─ cherry_trapdoor.json
│        │  │  │  ├─ comparator.json
│        │  │  │  ├─ copper_bulb.json
│        │  │  │  ├─ copper_door.json
│        │  │  │  ├─ copper_trapdoor.json
│        │  │  │  ├─ crafter.json
│        │  │  │  ├─ crimson_button.json
│        │  │  │  ├─ crimson_door.json
│        │  │  │  ├─ crimson_fence_gate.json
│        │  │  │  ├─ crimson_pressure_plate.json
│        │  │  │  ├─ crimson_trapdoor.json
│        │  │  │  ├─ dark_oak_button.json
│        │  │  │  ├─ dark_oak_door.json
│        │  │  │  ├─ dark_oak_fence_gate.json
│        │  │  │  ├─ dark_oak_pressure_plate.json
│        │  │  │  ├─ dark_oak_trapdoor.json
│        │  │  │  ├─ daylight_detector.json
│        │  │  │  ├─ dispenser.json
│        │  │  │  ├─ dropper.json
│        │  │  │  ├─ exposed_copper_bulb.json
│        │  │  │  ├─ heavy_weighted_pressure_plate.json
│        │  │  │  ├─ honey_block.json
│        │  │  │  ├─ hopper.json
│        │  │  │  ├─ iron_door.json
│        │  │  │  ├─ iron_trapdoor.json
│        │  │  │  ├─ jungle_button.json
│        │  │  │  ├─ jungle_door.json
│        │  │  │  ├─ jungle_fence_gate.json
│        │  │  │  ├─ jungle_pressure_plate.json
│        │  │  │  ├─ jungle_trapdoor.json
│        │  │  │  ├─ lectern.json
│        │  │  │  ├─ lever.json
│        │  │  │  ├─ lightning_rod.json
│        │  │  │  ├─ light_weighted_pressure_plate.json
│        │  │  │  ├─ mangrove_button.json
│        │  │  │  ├─ mangrove_door.json
│        │  │  │  ├─ mangrove_fence_gate.json
│        │  │  │  ├─ mangrove_pressure_plate.json
│        │  │  │  ├─ mangrove_trapdoor.json
│        │  │  │  ├─ note_block.json
│        │  │  │  ├─ oak_button.json
│        │  │  │  ├─ oak_door.json
│        │  │  │  ├─ oak_fence_gate.json
│        │  │  │  ├─ oak_pressure_plate.json
│        │  │  │  ├─ oak_trapdoor.json
│        │  │  │  ├─ observer.json
│        │  │  │  ├─ oxidized_copper_bulb.json
│        │  │  │  ├─ pale_oak_button.json
│        │  │  │  ├─ pale_oak_door.json
│        │  │  │  ├─ pale_oak_fence_gate.json
│        │  │  │  ├─ pale_oak_pressure_plate.json
│        │  │  │  ├─ pale_oak_trapdoor.json
│        │  │  │  ├─ piston.json
│        │  │  │  ├─ polished_blackstone_button.json
│        │  │  │  ├─ polished_blackstone_pressure_plate.json
│        │  │  │  ├─ redstone.json
│        │  │  │  ├─ redstone_block.json
│        │  │  │  ├─ redstone_from_blasting_deepslate_redstone_ore.json
│        │  │  │  ├─ redstone_from_blasting_redstone_ore.json
│        │  │  │  ├─ redstone_from_smelting_deepslate_redstone_ore.json
│        │  │  │  ├─ redstone_from_smelting_redstone_ore.json
│        │  │  │  ├─ redstone_lamp.json
│        │  │  │  ├─ redstone_torch.json
│        │  │  │  ├─ repeater.json
│        │  │  │  ├─ slime_block.json
│        │  │  │  ├─ spruce_button.json
│        │  │  │  ├─ spruce_door.json
│        │  │  │  ├─ spruce_fence_gate.json
│        │  │  │  ├─ spruce_pressure_plate.json
│        │  │  │  ├─ spruce_trapdoor.json
│        │  │  │  ├─ sticky_piston.json
│        │  │  │  ├─ stone_button.json
│        │  │  │  ├─ stone_pressure_plate.json
│        │  │  │  ├─ target.json
│        │  │  │  ├─ tnt.json
│        │  │  │  ├─ trapped_chest.json
│        │  │  │  ├─ tripwire_hook.json
│        │  │  │  ├─ warped_button.json
│        │  │  │  ├─ warped_door.json
│        │  │  │  ├─ warped_fence_gate.json
│        │  │  │  ├─ warped_pressure_plate.json
│        │  │  │  ├─ warped_trapdoor.json
│        │  │  │  ├─ waxed_copper_bulb.json
│        │  │  │  ├─ waxed_copper_bulb_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_door_from_honeycomb.json
│        │  │  │  ├─ waxed_copper_trapdoor_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_bulb.json
│        │  │  │  ├─ waxed_exposed_copper_bulb_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_door_from_honeycomb.json
│        │  │  │  ├─ waxed_exposed_copper_trapdoor_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_bulb.json
│        │  │  │  ├─ waxed_oxidized_copper_bulb_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_door_from_honeycomb.json
│        │  │  │  ├─ waxed_oxidized_copper_trapdoor_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_bulb.json
│        │  │  │  ├─ waxed_weathered_copper_bulb_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_door_from_honeycomb.json
│        │  │  │  ├─ waxed_weathered_copper_trapdoor_from_honeycomb.json
│        │  │  │  └─ weathered_copper_bulb.json
│        │  │  ├─ root.json
│        │  │  ├─ tools
│        │  │  │  ├─ black_bundle.json
│        │  │  │  ├─ blue_bundle.json
│        │  │  │  ├─ brown_bundle.json
│        │  │  │  ├─ brush.json
│        │  │  │  ├─ bundle.json
│        │  │  │  ├─ clock.json
│        │  │  │  ├─ compass.json
│        │  │  │  ├─ copper_axe.json
│        │  │  │  ├─ copper_hoe.json
│        │  │  │  ├─ copper_pickaxe.json
│        │  │  │  ├─ copper_shovel.json
│        │  │  │  ├─ cyan_bundle.json
│        │  │  │  ├─ diamond_axe.json
│        │  │  │  ├─ diamond_hoe.json
│        │  │  │  ├─ diamond_pickaxe.json
│        │  │  │  ├─ diamond_shovel.json
│        │  │  │  ├─ fishing_rod.json
│        │  │  │  ├─ flint_and_steel.json
│        │  │  │  ├─ golden_axe.json
│        │  │  │  ├─ golden_hoe.json
│        │  │  │  ├─ golden_pickaxe.json
│        │  │  │  ├─ golden_shovel.json
│        │  │  │  ├─ gray_bundle.json
│        │  │  │  ├─ green_bundle.json
│        │  │  │  ├─ iron_axe.json
│        │  │  │  ├─ iron_hoe.json
│        │  │  │  ├─ iron_pickaxe.json
│        │  │  │  ├─ iron_shovel.json
│        │  │  │  ├─ lead.json
│        │  │  │  ├─ light_blue_bundle.json
│        │  │  │  ├─ light_gray_bundle.json
│        │  │  │  ├─ lime_bundle.json
│        │  │  │  ├─ magenta_bundle.json
│        │  │  │  ├─ netherite_axe_smithing.json
│        │  │  │  ├─ netherite_hoe_smithing.json
│        │  │  │  ├─ netherite_pickaxe_smithing.json
│        │  │  │  ├─ netherite_shovel_smithing.json
│        │  │  │  ├─ orange_bundle.json
│        │  │  │  ├─ pink_bundle.json
│        │  │  │  ├─ purple_bundle.json
│        │  │  │  ├─ recovery_compass.json
│        │  │  │  ├─ red_bundle.json
│        │  │  │  ├─ shears.json
│        │  │  │  ├─ spyglass.json
│        │  │  │  ├─ stone_axe.json
│        │  │  │  ├─ stone_hoe.json
│        │  │  │  ├─ stone_pickaxe.json
│        │  │  │  ├─ stone_shovel.json
│        │  │  │  ├─ white_bundle.json
│        │  │  │  ├─ wooden_axe.json
│        │  │  │  ├─ wooden_hoe.json
│        │  │  │  ├─ wooden_pickaxe.json
│        │  │  │  ├─ wooden_shovel.json
│        │  │  │  └─ yellow_bundle.json
│        │  │  └─ transportation
│        │  │     ├─ acacia_boat.json
│        │  │     ├─ acacia_chest_boat.json
│        │  │     ├─ activator_rail.json
│        │  │     ├─ bamboo_chest_raft.json
│        │  │     ├─ bamboo_raft.json
│        │  │     ├─ birch_boat.json
│        │  │     ├─ birch_chest_boat.json
│        │  │     ├─ carrot_on_a_stick.json
│        │  │     ├─ cherry_boat.json
│        │  │     ├─ cherry_chest_boat.json
│        │  │     ├─ chest_minecart.json
│        │  │     ├─ dark_oak_boat.json
│        │  │     ├─ dark_oak_chest_boat.json
│        │  │     ├─ detector_rail.json
│        │  │     ├─ furnace_minecart.json
│        │  │     ├─ hopper_minecart.json
│        │  │     ├─ jungle_boat.json
│        │  │     ├─ jungle_chest_boat.json
│        │  │     ├─ mangrove_boat.json
│        │  │     ├─ mangrove_chest_boat.json
│        │  │     ├─ minecart.json
│        │  │     ├─ oak_boat.json
│        │  │     ├─ oak_chest_boat.json
│        │  │     ├─ pale_oak_boat.json
│        │  │     ├─ pale_oak_chest_boat.json
│        │  │     ├─ powered_rail.json
│        │  │     ├─ rail.json
│        │  │     ├─ spruce_boat.json
│        │  │     ├─ spruce_chest_boat.json
│        │  │     ├─ tnt_minecart.json
│        │  │     └─ warped_fungus_on_a_stick.json
│        │  └─ story
│        │     ├─ cure_zombie_villager.json
│        │     ├─ deflect_arrow.json
│        │     ├─ enchant_item.json
│        │     ├─ enter_the_end.json
│        │     ├─ enter_the_nether.json
│        │     ├─ follow_ender_eye.json
│        │     ├─ form_obsidian.json
│        │     ├─ iron_tools.json
│        │     ├─ lava_bucket.json
│        │     ├─ mine_diamond.json
│        │     ├─ mine_stone.json
│        │     ├─ obtain_armor.json
│        │     ├─ root.json
│        │     ├─ shiny_gear.json
│        │     ├─ smelt_iron.json
│        │     └─ upgrade_tools.json
│        ├─ banner_pattern
│        │  ├─ base.json
│        │  ├─ border.json
│        │  ├─ bricks.json
│        │  ├─ circle.json
│        │  ├─ creeper.json
│        │  ├─ cross.json
│        │  ├─ curly_border.json
│        │  ├─ diagonal_left.json
│        │  ├─ diagonal_right.json
│        │  ├─ diagonal_up_left.json
│        │  ├─ diagonal_up_right.json
│        │  ├─ flow.json
│        │  ├─ flower.json
│        │  ├─ globe.json
│        │  ├─ gradient.json
│        │  ├─ gradient_up.json
│        │  ├─ guster.json
│        │  ├─ half_horizontal.json
│        │  ├─ half_horizontal_bottom.json
│        │  ├─ half_vertical.json
│        │  ├─ half_vertical_right.json
│        │  ├─ mojang.json
│        │  ├─ piglin.json
│        │  ├─ rhombus.json
│        │  ├─ skull.json
│        │  ├─ small_stripes.json
│        │  ├─ square_bottom_left.json
│        │  ├─ square_bottom_right.json
│        │  ├─ square_top_left.json
│        │  ├─ square_top_right.json
│        │  ├─ straight_cross.json
│        │  ├─ stripe_bottom.json
│        │  ├─ stripe_center.json
│        │  ├─ stripe_downleft.json
│        │  ├─ stripe_downright.json
│        │  ├─ stripe_left.json
│        │  ├─ stripe_middle.json
│        │  ├─ stripe_right.json
│        │  ├─ stripe_top.json
│        │  ├─ triangles_bottom.json
│        │  ├─ triangles_top.json
│        │  ├─ triangle_bottom.json
│        │  └─ triangle_top.json
│        ├─ cat_variant
│        │  ├─ all_black.json
│        │  ├─ black.json
│        │  ├─ british_shorthair.json
│        │  ├─ calico.json
│        │  ├─ jellie.json
│        │  ├─ persian.json
│        │  ├─ ragdoll.json
│        │  ├─ red.json
│        │  ├─ siamese.json
│        │  ├─ tabby.json
│        │  └─ white.json
│        ├─ chat_type
│        │  ├─ chat.json
│        │  ├─ emote_command.json
│        │  ├─ msg_command_incoming.json
│        │  ├─ msg_command_outgoing.json
│        │  ├─ say_command.json
│        │  ├─ team_msg_command_incoming.json
│        │  └─ team_msg_command_outgoing.json
│        ├─ chicken_variant
│        │  ├─ cold.json
│        │  ├─ temperate.json
│        │  └─ warm.json
│        ├─ cow_variant
│        │  ├─ cold.json
│        │  ├─ temperate.json
│        │  └─ warm.json
│        ├─ damage_type
│        │  ├─ arrow.json
│        │  ├─ bad_respawn_point.json
│        │  ├─ cactus.json
│        │  ├─ campfire.json
│        │  ├─ cramming.json
│        │  ├─ dragon_breath.json
│        │  ├─ drown.json
│        │  ├─ dry_out.json
│        │  ├─ ender_pearl.json
│        │  ├─ explosion.json
│        │  ├─ fall.json
│        │  ├─ falling_anvil.json
│        │  ├─ falling_block.json
│        │  ├─ falling_stalactite.json
│        │  ├─ fireball.json
│        │  ├─ fireworks.json
│        │  ├─ fly_into_wall.json
│        │  ├─ freeze.json
│        │  ├─ generic.json
│        │  ├─ generic_kill.json
│        │  ├─ hot_floor.json
│        │  ├─ indirect_magic.json
│        │  ├─ in_fire.json
│        │  ├─ in_wall.json
│        │  ├─ lava.json
│        │  ├─ lightning_bolt.json
│        │  ├─ mace_smash.json
│        │  ├─ magic.json
│        │  ├─ mob_attack.json
│        │  ├─ mob_attack_no_aggro.json
│        │  ├─ mob_projectile.json
│        │  ├─ on_fire.json
│        │  ├─ outside_border.json
│        │  ├─ out_of_world.json
│        │  ├─ player_attack.json
│        │  ├─ player_explosion.json
│        │  ├─ sonic_boom.json
│        │  ├─ spear.json
│        │  ├─ spit.json
│        │  ├─ stalagmite.json
│        │  ├─ starve.json
│        │  ├─ sting.json
│        │  ├─ sweet_berry_bush.json
│        │  ├─ thorns.json
│        │  ├─ thrown.json
│        │  ├─ trident.json
│        │  ├─ unattributed_fireball.json
│        │  ├─ wind_charge.json
│        │  ├─ wither.json
│        │  └─ wither_skull.json
│        ├─ datapacks
│        │  ├─ minecart_improvements
│        │  │  └─ pack.mcmeta
│        │  ├─ redstone_experiments
│        │  │  └─ pack.mcmeta
│        │  └─ trade_rebalance
│        │     ├─ data
│        │     │  └─ minecraft
│        │     │     ├─ enchantment_provider
│        │     │     │  └─ trades
│        │     │     │     ├─ desert_armorer_boots_4.json
│        │     │     │     ├─ desert_armorer_chestplate_4.json
│        │     │     │     ├─ desert_armorer_chestplate_5.json
│        │     │     │     ├─ desert_armorer_helmet_4.json
│        │     │     │     ├─ desert_armorer_leggings_4.json
│        │     │     │     ├─ desert_armorer_leggings_5.json
│        │     │     │     ├─ jungle_armorer_boots_4.json
│        │     │     │     ├─ jungle_armorer_boots_5.json
│        │     │     │     ├─ jungle_armorer_chestplate_4.json
│        │     │     │     ├─ jungle_armorer_helmet_4.json
│        │     │     │     ├─ jungle_armorer_helmet_5.json
│        │     │     │     ├─ jungle_armorer_leggings_4.json
│        │     │     │     ├─ plains_armorer_boots_4.json
│        │     │     │     ├─ plains_armorer_boots_5.json
│        │     │     │     ├─ plains_armorer_chestplate_4.json
│        │     │     │     ├─ plains_armorer_helmet_4.json
│        │     │     │     ├─ plains_armorer_leggings_4.json
│        │     │     │     ├─ plains_armorer_leggings_5.json
│        │     │     │     ├─ savanna_armorer_boots_4.json
│        │     │     │     ├─ savanna_armorer_chestplate_4.json
│        │     │     │     ├─ savanna_armorer_chestplate_5.json
│        │     │     │     ├─ savanna_armorer_helmet_4.json
│        │     │     │     ├─ savanna_armorer_helmet_5.json
│        │     │     │     ├─ savanna_armorer_leggings_4.json
│        │     │     │     ├─ snow_armorer_boots_4.json
│        │     │     │     ├─ snow_armorer_boots_5.json
│        │     │     │     ├─ snow_armorer_helmet_4.json
│        │     │     │     ├─ snow_armorer_helmet_5.json
│        │     │     │     ├─ swamp_armorer_boots_4.json
│        │     │     │     ├─ swamp_armorer_boots_5.json
│        │     │     │     ├─ swamp_armorer_chestplate_4.json
│        │     │     │     ├─ swamp_armorer_helmet_4.json
│        │     │     │     ├─ swamp_armorer_helmet_5.json
│        │     │     │     ├─ swamp_armorer_leggings_4.json
│        │     │     │     ├─ taiga_armorer_chestplate_5.json
│        │     │     │     └─ taiga_armorer_leggings_5.json
│        │     │     ├─ loot_table
│        │     │     │  └─ chests
│        │     │     │     ├─ abandoned_mineshaft.json
│        │     │     │     ├─ ancient_city.json
│        │     │     │     ├─ desert_pyramid.json
│        │     │     │     ├─ jungle_temple.json
│        │     │     │     └─ pillager_outpost.json
│        │     │     └─ tags
│        │     │        └─ enchantment
│        │     │           └─ trades
│        │     │              ├─ desert_common.json
│        │     │              ├─ desert_special.json
│        │     │              ├─ jungle_common.json
│        │     │              ├─ jungle_special.json
│        │     │              ├─ plains_common.json
│        │     │              ├─ plains_special.json
│        │     │              ├─ savanna_common.json
│        │     │              ├─ savanna_special.json
│        │     │              ├─ snow_common.json
│        │     │              ├─ snow_special.json
│        │     │              ├─ swamp_common.json
│        │     │              ├─ swamp_special.json
│        │     │              ├─ taiga_common.json
│        │     │              └─ taiga_special.json
│        │     └─ pack.mcmeta
│        ├─ dialog
│        │  ├─ custom_options.json
│        │  ├─ quick_actions.json
│        │  └─ server_links.json
│        ├─ dimension_type
│        │  ├─ overworld.json
│        │  ├─ overworld_caves.json
│        │  ├─ the_end.json
│        │  └─ the_nether.json
│        ├─ enchantment
│        │  ├─ aqua_affinity.json
│        │  ├─ bane_of_arthropods.json
│        │  ├─ binding_curse.json
│        │  ├─ blast_protection.json
│        │  ├─ breach.json
│        │  ├─ channeling.json
│        │  ├─ density.json
│        │  ├─ depth_strider.json
│        │  ├─ efficiency.json
│        │  ├─ feather_falling.json
│        │  ├─ fire_aspect.json
│        │  ├─ fire_protection.json
│        │  ├─ flame.json
│        │  ├─ fortune.json
│        │  ├─ frost_walker.json
│        │  ├─ impaling.json
│        │  ├─ infinity.json
│        │  ├─ knockback.json
│        │  ├─ looting.json
│        │  ├─ loyalty.json
│        │  ├─ luck_of_the_sea.json
│        │  ├─ lunge.json
│        │  ├─ lure.json
│        │  ├─ mending.json
│        │  ├─ multishot.json
│        │  ├─ piercing.json
│        │  ├─ power.json
│        │  ├─ projectile_protection.json
│        │  ├─ protection.json
│        │  ├─ punch.json
│        │  ├─ quick_charge.json
│        │  ├─ respiration.json
│        │  ├─ riptide.json
│        │  ├─ sharpness.json
│        │  ├─ silk_touch.json
│        │  ├─ smite.json
│        │  ├─ soul_speed.json
│        │  ├─ sweeping_edge.json
│        │  ├─ swift_sneak.json
│        │  ├─ thorns.json
│        │  ├─ unbreaking.json
│        │  ├─ vanishing_curse.json
│        │  └─ wind_burst.json
│        ├─ enchantment_provider
│        │  ├─ enderman_loot_drop.json
│        │  ├─ mob_spawn_equipment.json
│        │  ├─ pillager_spawn_crossbow.json
│        │  └─ raid
│        │     ├─ pillager_post_wave_3.json
│        │     ├─ pillager_post_wave_5.json
│        │     ├─ vindicator.json
│        │     └─ vindicator_post_wave_5.json
│        ├─ frog_variant
│        │  ├─ cold.json
│        │  ├─ temperate.json
│        │  └─ warm.json
│        ├─ instrument
│        │  ├─ admire_goat_horn.json
│        │  ├─ call_goat_horn.json
│        │  ├─ dream_goat_horn.json
│        │  ├─ feel_goat_horn.json
│        │  ├─ ponder_goat_horn.json
│        │  ├─ seek_goat_horn.json
│        │  ├─ sing_goat_horn.json
│        │  └─ yearn_goat_horn.json
│        ├─ jukebox_song
│        │  ├─ 11.json
│        │  ├─ 13.json
│        │  ├─ 5.json
│        │  ├─ blocks.json
│        │  ├─ cat.json
│        │  ├─ chirp.json
│        │  ├─ creator.json
│        │  ├─ creator_music_box.json
│        │  ├─ far.json
│        │  ├─ lava_chicken.json
│        │  ├─ mall.json
│        │  ├─ mellohi.json
│        │  ├─ otherside.json
│        │  ├─ pigstep.json
│        │  ├─ precipice.json
│        │  ├─ relic.json
│        │  ├─ stal.json
│        │  ├─ strad.json
│        │  ├─ tears.json
│        │  ├─ wait.json
│        │  └─ ward.json
│        ├─ loot_table
│        │  ├─ archaeology
│        │  │  ├─ desert_pyramid.json
│        │  │  ├─ desert_well.json
│        │  │  ├─ ocean_ruin_cold.json
│        │  │  ├─ ocean_ruin_warm.json
│        │  │  ├─ trail_ruins_common.json
│        │  │  └─ trail_ruins_rare.json
│        │  ├─ blocks
│        │  │  ├─ acacia_button.json
│        │  │  ├─ acacia_door.json
│        │  │  ├─ acacia_fence.json
│        │  │  ├─ acacia_fence_gate.json
│        │  │  ├─ acacia_hanging_sign.json
│        │  │  ├─ acacia_leaves.json
│        │  │  ├─ acacia_log.json
│        │  │  ├─ acacia_planks.json
│        │  │  ├─ acacia_pressure_plate.json
│        │  │  ├─ acacia_sapling.json
│        │  │  ├─ acacia_shelf.json
│        │  │  ├─ acacia_sign.json
│        │  │  ├─ acacia_slab.json
│        │  │  ├─ acacia_stairs.json
│        │  │  ├─ acacia_trapdoor.json
│        │  │  ├─ acacia_wood.json
│        │  │  ├─ activator_rail.json
│        │  │  ├─ allium.json
│        │  │  ├─ amethyst_block.json
│        │  │  ├─ amethyst_cluster.json
│        │  │  ├─ ancient_debris.json
│        │  │  ├─ andesite.json
│        │  │  ├─ andesite_slab.json
│        │  │  ├─ andesite_stairs.json
│        │  │  ├─ andesite_wall.json
│        │  │  ├─ anvil.json
│        │  │  ├─ attached_melon_stem.json
│        │  │  ├─ attached_pumpkin_stem.json
│        │  │  ├─ azalea.json
│        │  │  ├─ azalea_leaves.json
│        │  │  ├─ azure_bluet.json
│        │  │  ├─ bamboo.json
│        │  │  ├─ bamboo_block.json
│        │  │  ├─ bamboo_button.json
│        │  │  ├─ bamboo_door.json
│        │  │  ├─ bamboo_fence.json
│        │  │  ├─ bamboo_fence_gate.json
│        │  │  ├─ bamboo_hanging_sign.json
│        │  │  ├─ bamboo_mosaic.json
│        │  │  ├─ bamboo_mosaic_slab.json
│        │  │  ├─ bamboo_mosaic_stairs.json
│        │  │  ├─ bamboo_planks.json
│        │  │  ├─ bamboo_pressure_plate.json
│        │  │  ├─ bamboo_sapling.json
│        │  │  ├─ bamboo_shelf.json
│        │  │  ├─ bamboo_sign.json
│        │  │  ├─ bamboo_slab.json
│        │  │  ├─ bamboo_stairs.json
│        │  │  ├─ bamboo_trapdoor.json
│        │  │  ├─ barrel.json
│        │  │  ├─ basalt.json
│        │  │  ├─ beacon.json
│        │  │  ├─ beehive.json
│        │  │  ├─ beetroots.json
│        │  │  ├─ bee_nest.json
│        │  │  ├─ bell.json
│        │  │  ├─ big_dripleaf.json
│        │  │  ├─ big_dripleaf_stem.json
│        │  │  ├─ birch_button.json
│        │  │  ├─ birch_door.json
│        │  │  ├─ birch_fence.json
│        │  │  ├─ birch_fence_gate.json
│        │  │  ├─ birch_hanging_sign.json
│        │  │  ├─ birch_leaves.json
│        │  │  ├─ birch_log.json
│        │  │  ├─ birch_planks.json
│        │  │  ├─ birch_pressure_plate.json
│        │  │  ├─ birch_sapling.json
│        │  │  ├─ birch_shelf.json
│        │  │  ├─ birch_sign.json
│        │  │  ├─ birch_slab.json
│        │  │  ├─ birch_stairs.json
│        │  │  ├─ birch_trapdoor.json
│        │  │  ├─ birch_wood.json
│        │  │  ├─ blackstone.json
│        │  │  ├─ blackstone_slab.json
│        │  │  ├─ blackstone_stairs.json
│        │  │  ├─ blackstone_wall.json
│        │  │  ├─ black_banner.json
│        │  │  ├─ black_bed.json
│        │  │  ├─ black_candle.json
│        │  │  ├─ black_candle_cake.json
│        │  │  ├─ black_carpet.json
│        │  │  ├─ black_concrete.json
│        │  │  ├─ black_concrete_powder.json
│        │  │  ├─ black_glazed_terracotta.json
│        │  │  ├─ black_shulker_box.json
│        │  │  ├─ black_stained_glass.json
│        │  │  ├─ black_stained_glass_pane.json
│        │  │  ├─ black_terracotta.json
│        │  │  ├─ black_wool.json
│        │  │  ├─ blast_furnace.json
│        │  │  ├─ blue_banner.json
│        │  │  ├─ blue_bed.json
│        │  │  ├─ blue_candle.json
│        │  │  ├─ blue_candle_cake.json
│        │  │  ├─ blue_carpet.json
│        │  │  ├─ blue_concrete.json
│        │  │  ├─ blue_concrete_powder.json
│        │  │  ├─ blue_glazed_terracotta.json
│        │  │  ├─ blue_ice.json
│        │  │  ├─ blue_orchid.json
│        │  │  ├─ blue_shulker_box.json
│        │  │  ├─ blue_stained_glass.json
│        │  │  ├─ blue_stained_glass_pane.json
│        │  │  ├─ blue_terracotta.json
│        │  │  ├─ blue_wool.json
│        │  │  ├─ bone_block.json
│        │  │  ├─ bookshelf.json
│        │  │  ├─ brain_coral.json
│        │  │  ├─ brain_coral_block.json
│        │  │  ├─ brain_coral_fan.json
│        │  │  ├─ brewing_stand.json
│        │  │  ├─ bricks.json
│        │  │  ├─ brick_slab.json
│        │  │  ├─ brick_stairs.json
│        │  │  ├─ brick_wall.json
│        │  │  ├─ brown_banner.json
│        │  │  ├─ brown_bed.json
│        │  │  ├─ brown_candle.json
│        │  │  ├─ brown_candle_cake.json
│        │  │  ├─ brown_carpet.json
│        │  │  ├─ brown_concrete.json
│        │  │  ├─ brown_concrete_powder.json
│        │  │  ├─ brown_glazed_terracotta.json
│        │  │  ├─ brown_mushroom.json
│        │  │  ├─ brown_mushroom_block.json
│        │  │  ├─ brown_shulker_box.json
│        │  │  ├─ brown_stained_glass.json
│        │  │  ├─ brown_stained_glass_pane.json
│        │  │  ├─ brown_terracotta.json
│        │  │  ├─ brown_wool.json
│        │  │  ├─ bubble_coral.json
│        │  │  ├─ bubble_coral_block.json
│        │  │  ├─ bubble_coral_fan.json
│        │  │  ├─ budding_amethyst.json
│        │  │  ├─ bush.json
│        │  │  ├─ cactus.json
│        │  │  ├─ cactus_flower.json
│        │  │  ├─ cake.json
│        │  │  ├─ calcite.json
│        │  │  ├─ calibrated_sculk_sensor.json
│        │  │  ├─ campfire.json
│        │  │  ├─ candle.json
│        │  │  ├─ candle_cake.json
│        │  │  ├─ carrots.json
│        │  │  ├─ cartography_table.json
│        │  │  ├─ carved_pumpkin.json
│        │  │  ├─ cauldron.json
│        │  │  ├─ cave_vines.json
│        │  │  ├─ cave_vines_plant.json
│        │  │  ├─ cherry_button.json
│        │  │  ├─ cherry_door.json
│        │  │  ├─ cherry_fence.json
│        │  │  ├─ cherry_fence_gate.json
│        │  │  ├─ cherry_hanging_sign.json
│        │  │  ├─ cherry_leaves.json
│        │  │  ├─ cherry_log.json
│        │  │  ├─ cherry_planks.json
│        │  │  ├─ cherry_pressure_plate.json
│        │  │  ├─ cherry_sapling.json
│        │  │  ├─ cherry_shelf.json
│        │  │  ├─ cherry_sign.json
│        │  │  ├─ cherry_slab.json
│        │  │  ├─ cherry_stairs.json
│        │  │  ├─ cherry_trapdoor.json
│        │  │  ├─ cherry_wood.json
│        │  │  ├─ chest.json
│        │  │  ├─ chipped_anvil.json
│        │  │  ├─ chiseled_bookshelf.json
│        │  │  ├─ chiseled_copper.json
│        │  │  ├─ chiseled_deepslate.json
│        │  │  ├─ chiseled_nether_bricks.json
│        │  │  ├─ chiseled_polished_blackstone.json
│        │  │  ├─ chiseled_quartz_block.json
│        │  │  ├─ chiseled_red_sandstone.json
│        │  │  ├─ chiseled_resin_bricks.json
│        │  │  ├─ chiseled_sandstone.json
│        │  │  ├─ chiseled_stone_bricks.json
│        │  │  ├─ chiseled_tuff.json
│        │  │  ├─ chiseled_tuff_bricks.json
│        │  │  ├─ chorus_flower.json
│        │  │  ├─ chorus_plant.json
│        │  │  ├─ clay.json
│        │  │  ├─ closed_eyeblossom.json
│        │  │  ├─ coal_block.json
│        │  │  ├─ coal_ore.json
│        │  │  ├─ coarse_dirt.json
│        │  │  ├─ cobbled_deepslate.json
│        │  │  ├─ cobbled_deepslate_slab.json
│        │  │  ├─ cobbled_deepslate_stairs.json
│        │  │  ├─ cobbled_deepslate_wall.json
│        │  │  ├─ cobblestone.json
│        │  │  ├─ cobblestone_slab.json
│        │  │  ├─ cobblestone_stairs.json
│        │  │  ├─ cobblestone_wall.json
│        │  │  ├─ cobweb.json
│        │  │  ├─ cocoa.json
│        │  │  ├─ comparator.json
│        │  │  ├─ composter.json
│        │  │  ├─ conduit.json
│        │  │  ├─ copper_bars.json
│        │  │  ├─ copper_block.json
│        │  │  ├─ copper_bulb.json
│        │  │  ├─ copper_chain.json
│        │  │  ├─ copper_chest.json
│        │  │  ├─ copper_door.json
│        │  │  ├─ copper_golem_statue.json
│        │  │  ├─ copper_grate.json
│        │  │  ├─ copper_lantern.json
│        │  │  ├─ copper_ore.json
│        │  │  ├─ copper_torch.json
│        │  │  ├─ copper_trapdoor.json
│        │  │  ├─ cornflower.json
│        │  │  ├─ cracked_deepslate_bricks.json
│        │  │  ├─ cracked_deepslate_tiles.json
│        │  │  ├─ cracked_nether_bricks.json
│        │  │  ├─ cracked_polished_blackstone_bricks.json
│        │  │  ├─ cracked_stone_bricks.json
│        │  │  ├─ crafter.json
│        │  │  ├─ crafting_table.json
│        │  │  ├─ creaking_heart.json
│        │  │  ├─ creeper_head.json
│        │  │  ├─ crimson_button.json
│        │  │  ├─ crimson_door.json
│        │  │  ├─ crimson_fence.json
│        │  │  ├─ crimson_fence_gate.json
│        │  │  ├─ crimson_fungus.json
│        │  │  ├─ crimson_hanging_sign.json
│        │  │  ├─ crimson_hyphae.json
│        │  │  ├─ crimson_nylium.json
│        │  │  ├─ crimson_planks.json
│        │  │  ├─ crimson_pressure_plate.json
│        │  │  ├─ crimson_roots.json
│        │  │  ├─ crimson_shelf.json
│        │  │  ├─ crimson_sign.json
│        │  │  ├─ crimson_slab.json
│        │  │  ├─ crimson_stairs.json
│        │  │  ├─ crimson_stem.json
│        │  │  ├─ crimson_trapdoor.json
│        │  │  ├─ crying_obsidian.json
│        │  │  ├─ cut_copper.json
│        │  │  ├─ cut_copper_slab.json
│        │  │  ├─ cut_copper_stairs.json
│        │  │  ├─ cut_red_sandstone.json
│        │  │  ├─ cut_red_sandstone_slab.json
│        │  │  ├─ cut_sandstone.json
│        │  │  ├─ cut_sandstone_slab.json
│        │  │  ├─ cyan_banner.json
│        │  │  ├─ cyan_bed.json
│        │  │  ├─ cyan_candle.json
│        │  │  ├─ cyan_candle_cake.json
│        │  │  ├─ cyan_carpet.json
│        │  │  ├─ cyan_concrete.json
│        │  │  ├─ cyan_concrete_powder.json
│        │  │  ├─ cyan_glazed_terracotta.json
│        │  │  ├─ cyan_shulker_box.json
│        │  │  ├─ cyan_stained_glass.json
│        │  │  ├─ cyan_stained_glass_pane.json
│        │  │  ├─ cyan_terracotta.json
│        │  │  ├─ cyan_wool.json
│        │  │  ├─ damaged_anvil.json
│        │  │  ├─ dandelion.json
│        │  │  ├─ dark_oak_button.json
│        │  │  ├─ dark_oak_door.json
│        │  │  ├─ dark_oak_fence.json
│        │  │  ├─ dark_oak_fence_gate.json
│        │  │  ├─ dark_oak_hanging_sign.json
│        │  │  ├─ dark_oak_leaves.json
│        │  │  ├─ dark_oak_log.json
│        │  │  ├─ dark_oak_planks.json
│        │  │  ├─ dark_oak_pressure_plate.json
│        │  │  ├─ dark_oak_sapling.json
│        │  │  ├─ dark_oak_shelf.json
│        │  │  ├─ dark_oak_sign.json
│        │  │  ├─ dark_oak_slab.json
│        │  │  ├─ dark_oak_stairs.json
│        │  │  ├─ dark_oak_trapdoor.json
│        │  │  ├─ dark_oak_wood.json
│        │  │  ├─ dark_prismarine.json
│        │  │  ├─ dark_prismarine_slab.json
│        │  │  ├─ dark_prismarine_stairs.json
│        │  │  ├─ daylight_detector.json
│        │  │  ├─ dead_brain_coral.json
│        │  │  ├─ dead_brain_coral_block.json
│        │  │  ├─ dead_brain_coral_fan.json
│        │  │  ├─ dead_bubble_coral.json
│        │  │  ├─ dead_bubble_coral_block.json
│        │  │  ├─ dead_bubble_coral_fan.json
│        │  │  ├─ dead_bush.json
│        │  │  ├─ dead_fire_coral.json
│        │  │  ├─ dead_fire_coral_block.json
│        │  │  ├─ dead_fire_coral_fan.json
│        │  │  ├─ dead_horn_coral.json
│        │  │  ├─ dead_horn_coral_block.json
│        │  │  ├─ dead_horn_coral_fan.json
│        │  │  ├─ dead_tube_coral.json
│        │  │  ├─ dead_tube_coral_block.json
│        │  │  ├─ dead_tube_coral_fan.json
│        │  │  ├─ decorated_pot.json
│        │  │  ├─ deepslate.json
│        │  │  ├─ deepslate_bricks.json
│        │  │  ├─ deepslate_brick_slab.json
│        │  │  ├─ deepslate_brick_stairs.json
│        │  │  ├─ deepslate_brick_wall.json
│        │  │  ├─ deepslate_coal_ore.json
│        │  │  ├─ deepslate_copper_ore.json
│        │  │  ├─ deepslate_diamond_ore.json
│        │  │  ├─ deepslate_emerald_ore.json
│        │  │  ├─ deepslate_gold_ore.json
│        │  │  ├─ deepslate_iron_ore.json
│        │  │  ├─ deepslate_lapis_ore.json
│        │  │  ├─ deepslate_redstone_ore.json
│        │  │  ├─ deepslate_tiles.json
│        │  │  ├─ deepslate_tile_slab.json
│        │  │  ├─ deepslate_tile_stairs.json
│        │  │  ├─ deepslate_tile_wall.json
│        │  │  ├─ detector_rail.json
│        │  │  ├─ diamond_block.json
│        │  │  ├─ diamond_ore.json
│        │  │  ├─ diorite.json
│        │  │  ├─ diorite_slab.json
│        │  │  ├─ diorite_stairs.json
│        │  │  ├─ diorite_wall.json
│        │  │  ├─ dirt.json
│        │  │  ├─ dirt_path.json
│        │  │  ├─ dispenser.json
│        │  │  ├─ dragon_egg.json
│        │  │  ├─ dragon_head.json
│        │  │  ├─ dried_ghast.json
│        │  │  ├─ dried_kelp_block.json
│        │  │  ├─ dripstone_block.json
│        │  │  ├─ dropper.json
│        │  │  ├─ emerald_block.json
│        │  │  ├─ emerald_ore.json
│        │  │  ├─ enchanting_table.json
│        │  │  ├─ ender_chest.json
│        │  │  ├─ end_rod.json
│        │  │  ├─ end_stone.json
│        │  │  ├─ end_stone_bricks.json
│        │  │  ├─ end_stone_brick_slab.json
│        │  │  ├─ end_stone_brick_stairs.json
│        │  │  ├─ end_stone_brick_wall.json
│        │  │  ├─ exposed_chiseled_copper.json
│        │  │  ├─ exposed_copper.json
│        │  │  ├─ exposed_copper_bars.json
│        │  │  ├─ exposed_copper_bulb.json
│        │  │  ├─ exposed_copper_chain.json
│        │  │  ├─ exposed_copper_chest.json
│        │  │  ├─ exposed_copper_door.json
│        │  │  ├─ exposed_copper_golem_statue.json
│        │  │  ├─ exposed_copper_grate.json
│        │  │  ├─ exposed_copper_lantern.json
│        │  │  ├─ exposed_copper_trapdoor.json
│        │  │  ├─ exposed_cut_copper.json
│        │  │  ├─ exposed_cut_copper_slab.json
│        │  │  ├─ exposed_cut_copper_stairs.json
│        │  │  ├─ exposed_lightning_rod.json
│        │  │  ├─ farmland.json
│        │  │  ├─ fern.json
│        │  │  ├─ fire.json
│        │  │  ├─ firefly_bush.json
│        │  │  ├─ fire_coral.json
│        │  │  ├─ fire_coral_block.json
│        │  │  ├─ fire_coral_fan.json
│        │  │  ├─ fletching_table.json
│        │  │  ├─ flowering_azalea.json
│        │  │  ├─ flowering_azalea_leaves.json
│        │  │  ├─ flower_pot.json
│        │  │  ├─ frogspawn.json
│        │  │  ├─ frosted_ice.json
│        │  │  ├─ furnace.json
│        │  │  ├─ gilded_blackstone.json
│        │  │  ├─ glass.json
│        │  │  ├─ glass_pane.json
│        │  │  ├─ glowstone.json
│        │  │  ├─ glow_lichen.json
│        │  │  ├─ gold_block.json
│        │  │  ├─ gold_ore.json
│        │  │  ├─ granite.json
│        │  │  ├─ granite_slab.json
│        │  │  ├─ granite_stairs.json
│        │  │  ├─ granite_wall.json
│        │  │  ├─ grass_block.json
│        │  │  ├─ gravel.json
│        │  │  ├─ gray_banner.json
│        │  │  ├─ gray_bed.json
│        │  │  ├─ gray_candle.json
│        │  │  ├─ gray_candle_cake.json
│        │  │  ├─ gray_carpet.json
│        │  │  ├─ gray_concrete.json
│        │  │  ├─ gray_concrete_powder.json
│        │  │  ├─ gray_glazed_terracotta.json
│        │  │  ├─ gray_shulker_box.json
│        │  │  ├─ gray_stained_glass.json
│        │  │  ├─ gray_stained_glass_pane.json
│        │  │  ├─ gray_terracotta.json
│        │  │  ├─ gray_wool.json
│        │  │  ├─ green_banner.json
│        │  │  ├─ green_bed.json
│        │  │  ├─ green_candle.json
│        │  │  ├─ green_candle_cake.json
│        │  │  ├─ green_carpet.json
│        │  │  ├─ green_concrete.json
│        │  │  ├─ green_concrete_powder.json
│        │  │  ├─ green_glazed_terracotta.json
│        │  │  ├─ green_shulker_box.json
│        │  │  ├─ green_stained_glass.json
│        │  │  ├─ green_stained_glass_pane.json
│        │  │  ├─ green_terracotta.json
│        │  │  ├─ green_wool.json
│        │  │  ├─ grindstone.json
│        │  │  ├─ hanging_roots.json
│        │  │  ├─ hay_block.json
│        │  │  ├─ heavy_core.json
│        │  │  ├─ heavy_weighted_pressure_plate.json
│        │  │  ├─ honeycomb_block.json
│        │  │  ├─ honey_block.json
│        │  │  ├─ hopper.json
│        │  │  ├─ horn_coral.json
│        │  │  ├─ horn_coral_block.json
│        │  │  ├─ horn_coral_fan.json
│        │  │  ├─ ice.json
│        │  │  ├─ infested_chiseled_stone_bricks.json
│        │  │  ├─ infested_cobblestone.json
│        │  │  ├─ infested_cracked_stone_bricks.json
│        │  │  ├─ infested_deepslate.json
│        │  │  ├─ infested_mossy_stone_bricks.json
│        │  │  ├─ infested_stone.json
│        │  │  ├─ infested_stone_bricks.json
│        │  │  ├─ iron_bars.json
│        │  │  ├─ iron_block.json
│        │  │  ├─ iron_chain.json
│        │  │  ├─ iron_door.json
│        │  │  ├─ iron_ore.json
│        │  │  ├─ iron_trapdoor.json
│        │  │  ├─ jack_o_lantern.json
│        │  │  ├─ jukebox.json
│        │  │  ├─ jungle_button.json
│        │  │  ├─ jungle_door.json
│        │  │  ├─ jungle_fence.json
│        │  │  ├─ jungle_fence_gate.json
│        │  │  ├─ jungle_hanging_sign.json
│        │  │  ├─ jungle_leaves.json
│        │  │  ├─ jungle_log.json
│        │  │  ├─ jungle_planks.json
│        │  │  ├─ jungle_pressure_plate.json
│        │  │  ├─ jungle_sapling.json
│        │  │  ├─ jungle_shelf.json
│        │  │  ├─ jungle_sign.json
│        │  │  ├─ jungle_slab.json
│        │  │  ├─ jungle_stairs.json
│        │  │  ├─ jungle_trapdoor.json
│        │  │  ├─ jungle_wood.json
│        │  │  ├─ kelp.json
│        │  │  ├─ kelp_plant.json
│        │  │  ├─ ladder.json
│        │  │  ├─ lantern.json
│        │  │  ├─ lapis_block.json
│        │  │  ├─ lapis_ore.json
│        │  │  ├─ large_amethyst_bud.json
│        │  │  ├─ large_fern.json
│        │  │  ├─ lava_cauldron.json
│        │  │  ├─ leaf_litter.json
│        │  │  ├─ lectern.json
│        │  │  ├─ lever.json
│        │  │  ├─ lightning_rod.json
│        │  │  ├─ light_blue_banner.json
│        │  │  ├─ light_blue_bed.json
│        │  │  ├─ light_blue_candle.json
│        │  │  ├─ light_blue_candle_cake.json
│        │  │  ├─ light_blue_carpet.json
│        │  │  ├─ light_blue_concrete.json
│        │  │  ├─ light_blue_concrete_powder.json
│        │  │  ├─ light_blue_glazed_terracotta.json
│        │  │  ├─ light_blue_shulker_box.json
│        │  │  ├─ light_blue_stained_glass.json
│        │  │  ├─ light_blue_stained_glass_pane.json
│        │  │  ├─ light_blue_terracotta.json
│        │  │  ├─ light_blue_wool.json
│        │  │  ├─ light_gray_banner.json
│        │  │  ├─ light_gray_bed.json
│        │  │  ├─ light_gray_candle.json
│        │  │  ├─ light_gray_candle_cake.json
│        │  │  ├─ light_gray_carpet.json
│        │  │  ├─ light_gray_concrete.json
│        │  │  ├─ light_gray_concrete_powder.json
│        │  │  ├─ light_gray_glazed_terracotta.json
│        │  │  ├─ light_gray_shulker_box.json
│        │  │  ├─ light_gray_stained_glass.json
│        │  │  ├─ light_gray_stained_glass_pane.json
│        │  │  ├─ light_gray_terracotta.json
│        │  │  ├─ light_gray_wool.json
│        │  │  ├─ light_weighted_pressure_plate.json
│        │  │  ├─ lilac.json
│        │  │  ├─ lily_of_the_valley.json
│        │  │  ├─ lily_pad.json
│        │  │  ├─ lime_banner.json
│        │  │  ├─ lime_bed.json
│        │  │  ├─ lime_candle.json
│        │  │  ├─ lime_candle_cake.json
│        │  │  ├─ lime_carpet.json
│        │  │  ├─ lime_concrete.json
│        │  │  ├─ lime_concrete_powder.json
│        │  │  ├─ lime_glazed_terracotta.json
│        │  │  ├─ lime_shulker_box.json
│        │  │  ├─ lime_stained_glass.json
│        │  │  ├─ lime_stained_glass_pane.json
│        │  │  ├─ lime_terracotta.json
│        │  │  ├─ lime_wool.json
│        │  │  ├─ lodestone.json
│        │  │  ├─ loom.json
│        │  │  ├─ magenta_banner.json
│        │  │  ├─ magenta_bed.json
│        │  │  ├─ magenta_candle.json
│        │  │  ├─ magenta_candle_cake.json
│        │  │  ├─ magenta_carpet.json
│        │  │  ├─ magenta_concrete.json
│        │  │  ├─ magenta_concrete_powder.json
│        │  │  ├─ magenta_glazed_terracotta.json
│        │  │  ├─ magenta_shulker_box.json
│        │  │  ├─ magenta_stained_glass.json
│        │  │  ├─ magenta_stained_glass_pane.json
│        │  │  ├─ magenta_terracotta.json
│        │  │  ├─ magenta_wool.json
│        │  │  ├─ magma_block.json
│        │  │  ├─ mangrove_button.json
│        │  │  ├─ mangrove_door.json
│        │  │  ├─ mangrove_fence.json
│        │  │  ├─ mangrove_fence_gate.json
│        │  │  ├─ mangrove_hanging_sign.json
│        │  │  ├─ mangrove_leaves.json
│        │  │  ├─ mangrove_log.json
│        │  │  ├─ mangrove_planks.json
│        │  │  ├─ mangrove_pressure_plate.json
│        │  │  ├─ mangrove_propagule.json
│        │  │  ├─ mangrove_roots.json
│        │  │  ├─ mangrove_shelf.json
│        │  │  ├─ mangrove_sign.json
│        │  │  ├─ mangrove_slab.json
│        │  │  ├─ mangrove_stairs.json
│        │  │  ├─ mangrove_trapdoor.json
│        │  │  ├─ mangrove_wood.json
│        │  │  ├─ medium_amethyst_bud.json
│        │  │  ├─ melon.json
│        │  │  ├─ melon_stem.json
│        │  │  ├─ mossy_cobblestone.json
│        │  │  ├─ mossy_cobblestone_slab.json
│        │  │  ├─ mossy_cobblestone_stairs.json
│        │  │  ├─ mossy_cobblestone_wall.json
│        │  │  ├─ mossy_stone_bricks.json
│        │  │  ├─ mossy_stone_brick_slab.json
│        │  │  ├─ mossy_stone_brick_stairs.json
│        │  │  ├─ mossy_stone_brick_wall.json
│        │  │  ├─ moss_block.json
│        │  │  ├─ moss_carpet.json
│        │  │  ├─ mud.json
│        │  │  ├─ muddy_mangrove_roots.json
│        │  │  ├─ mud_bricks.json
│        │  │  ├─ mud_brick_slab.json
│        │  │  ├─ mud_brick_stairs.json
│        │  │  ├─ mud_brick_wall.json
│        │  │  ├─ mushroom_stem.json
│        │  │  ├─ mycelium.json
│        │  │  ├─ netherite_block.json
│        │  │  ├─ netherrack.json
│        │  │  ├─ nether_bricks.json
│        │  │  ├─ nether_brick_fence.json
│        │  │  ├─ nether_brick_slab.json
│        │  │  ├─ nether_brick_stairs.json
│        │  │  ├─ nether_brick_wall.json
│        │  │  ├─ nether_gold_ore.json
│        │  │  ├─ nether_portal.json
│        │  │  ├─ nether_quartz_ore.json
│        │  │  ├─ nether_sprouts.json
│        │  │  ├─ nether_wart.json
│        │  │  ├─ nether_wart_block.json
│        │  │  ├─ note_block.json
│        │  │  ├─ oak_button.json
│        │  │  ├─ oak_door.json
│        │  │  ├─ oak_fence.json
│        │  │  ├─ oak_fence_gate.json
│        │  │  ├─ oak_hanging_sign.json
│        │  │  ├─ oak_leaves.json
│        │  │  ├─ oak_log.json
│        │  │  ├─ oak_planks.json
│        │  │  ├─ oak_pressure_plate.json
│        │  │  ├─ oak_sapling.json
│        │  │  ├─ oak_shelf.json
│        │  │  ├─ oak_sign.json
│        │  │  ├─ oak_slab.json
│        │  │  ├─ oak_stairs.json
│        │  │  ├─ oak_trapdoor.json
│        │  │  ├─ oak_wood.json
│        │  │  ├─ observer.json
│        │  │  ├─ obsidian.json
│        │  │  ├─ ochre_froglight.json
│        │  │  ├─ open_eyeblossom.json
│        │  │  ├─ orange_banner.json
│        │  │  ├─ orange_bed.json
│        │  │  ├─ orange_candle.json
│        │  │  ├─ orange_candle_cake.json
│        │  │  ├─ orange_carpet.json
│        │  │  ├─ orange_concrete.json
│        │  │  ├─ orange_concrete_powder.json
│        │  │  ├─ orange_glazed_terracotta.json
│        │  │  ├─ orange_shulker_box.json
│        │  │  ├─ orange_stained_glass.json
│        │  │  ├─ orange_stained_glass_pane.json
│        │  │  ├─ orange_terracotta.json
│        │  │  ├─ orange_tulip.json
│        │  │  ├─ orange_wool.json
│        │  │  ├─ oxeye_daisy.json
│        │  │  ├─ oxidized_chiseled_copper.json
│        │  │  ├─ oxidized_copper.json
│        │  │  ├─ oxidized_copper_bars.json
│        │  │  ├─ oxidized_copper_bulb.json
│        │  │  ├─ oxidized_copper_chain.json
│        │  │  ├─ oxidized_copper_chest.json
│        │  │  ├─ oxidized_copper_door.json
│        │  │  ├─ oxidized_copper_golem_statue.json
│        │  │  ├─ oxidized_copper_grate.json
│        │  │  ├─ oxidized_copper_lantern.json
│        │  │  ├─ oxidized_copper_trapdoor.json
│        │  │  ├─ oxidized_cut_copper.json
│        │  │  ├─ oxidized_cut_copper_slab.json
│        │  │  ├─ oxidized_cut_copper_stairs.json
│        │  │  ├─ oxidized_lightning_rod.json
│        │  │  ├─ packed_ice.json
│        │  │  ├─ packed_mud.json
│        │  │  ├─ pale_hanging_moss.json
│        │  │  ├─ pale_moss_block.json
│        │  │  ├─ pale_moss_carpet.json
│        │  │  ├─ pale_oak_button.json
│        │  │  ├─ pale_oak_door.json
│        │  │  ├─ pale_oak_fence.json
│        │  │  ├─ pale_oak_fence_gate.json
│        │  │  ├─ pale_oak_hanging_sign.json
│        │  │  ├─ pale_oak_leaves.json
│        │  │  ├─ pale_oak_log.json
│        │  │  ├─ pale_oak_planks.json
│        │  │  ├─ pale_oak_pressure_plate.json
│        │  │  ├─ pale_oak_sapling.json
│        │  │  ├─ pale_oak_shelf.json
│        │  │  ├─ pale_oak_sign.json
│        │  │  ├─ pale_oak_slab.json
│        │  │  ├─ pale_oak_stairs.json
│        │  │  ├─ pale_oak_trapdoor.json
│        │  │  ├─ pale_oak_wood.json
│        │  │  ├─ pearlescent_froglight.json
│        │  │  ├─ peony.json
│        │  │  ├─ petrified_oak_slab.json
│        │  │  ├─ piglin_head.json
│        │  │  ├─ pink_banner.json
│        │  │  ├─ pink_bed.json
│        │  │  ├─ pink_candle.json
│        │  │  ├─ pink_candle_cake.json
│        │  │  ├─ pink_carpet.json
│        │  │  ├─ pink_concrete.json
│        │  │  ├─ pink_concrete_powder.json
│        │  │  ├─ pink_glazed_terracotta.json
│        │  │  ├─ pink_petals.json
│        │  │  ├─ pink_shulker_box.json
│        │  │  ├─ pink_stained_glass.json
│        │  │  ├─ pink_stained_glass_pane.json
│        │  │  ├─ pink_terracotta.json
│        │  │  ├─ pink_tulip.json
│        │  │  ├─ pink_wool.json
│        │  │  ├─ piston.json
│        │  │  ├─ pitcher_crop.json
│        │  │  ├─ pitcher_plant.json
│        │  │  ├─ player_head.json
│        │  │  ├─ podzol.json
│        │  │  ├─ pointed_dripstone.json
│        │  │  ├─ polished_andesite.json
│        │  │  ├─ polished_andesite_slab.json
│        │  │  ├─ polished_andesite_stairs.json
│        │  │  ├─ polished_basalt.json
│        │  │  ├─ polished_blackstone.json
│        │  │  ├─ polished_blackstone_bricks.json
│        │  │  ├─ polished_blackstone_brick_slab.json
│        │  │  ├─ polished_blackstone_brick_stairs.json
│        │  │  ├─ polished_blackstone_brick_wall.json
│        │  │  ├─ polished_blackstone_button.json
│        │  │  ├─ polished_blackstone_pressure_plate.json
│        │  │  ├─ polished_blackstone_slab.json
│        │  │  ├─ polished_blackstone_stairs.json
│        │  │  ├─ polished_blackstone_wall.json
│        │  │  ├─ polished_deepslate.json
│        │  │  ├─ polished_deepslate_slab.json
│        │  │  ├─ polished_deepslate_stairs.json
│        │  │  ├─ polished_deepslate_wall.json
│        │  │  ├─ polished_diorite.json
│        │  │  ├─ polished_diorite_slab.json
│        │  │  ├─ polished_diorite_stairs.json
│        │  │  ├─ polished_granite.json
│        │  │  ├─ polished_granite_slab.json
│        │  │  ├─ polished_granite_stairs.json
│        │  │  ├─ polished_tuff.json
│        │  │  ├─ polished_tuff_slab.json
│        │  │  ├─ polished_tuff_stairs.json
│        │  │  ├─ polished_tuff_wall.json
│        │  │  ├─ poppy.json
│        │  │  ├─ potatoes.json
│        │  │  ├─ potted_acacia_sapling.json
│        │  │  ├─ potted_allium.json
│        │  │  ├─ potted_azalea_bush.json
│        │  │  ├─ potted_azure_bluet.json
│        │  │  ├─ potted_bamboo.json
│        │  │  ├─ potted_birch_sapling.json
│        │  │  ├─ potted_blue_orchid.json
│        │  │  ├─ potted_brown_mushroom.json
│        │  │  ├─ potted_cactus.json
│        │  │  ├─ potted_cherry_sapling.json
│        │  │  ├─ potted_closed_eyeblossom.json
│        │  │  ├─ potted_cornflower.json
│        │  │  ├─ potted_crimson_fungus.json
│        │  │  ├─ potted_crimson_roots.json
│        │  │  ├─ potted_dandelion.json
│        │  │  ├─ potted_dark_oak_sapling.json
│        │  │  ├─ potted_dead_bush.json
│        │  │  ├─ potted_fern.json
│        │  │  ├─ potted_flowering_azalea_bush.json
│        │  │  ├─ potted_jungle_sapling.json
│        │  │  ├─ potted_lily_of_the_valley.json
│        │  │  ├─ potted_mangrove_propagule.json
│        │  │  ├─ potted_oak_sapling.json
│        │  │  ├─ potted_open_eyeblossom.json
│        │  │  ├─ potted_orange_tulip.json
│        │  │  ├─ potted_oxeye_daisy.json
│        │  │  ├─ potted_pale_oak_sapling.json
│        │  │  ├─ potted_pink_tulip.json
│        │  │  ├─ potted_poppy.json
│        │  │  ├─ potted_red_mushroom.json
│        │  │  ├─ potted_red_tulip.json
│        │  │  ├─ potted_spruce_sapling.json
│        │  │  ├─ potted_torchflower.json
│        │  │  ├─ potted_warped_fungus.json
│        │  │  ├─ potted_warped_roots.json
│        │  │  ├─ potted_white_tulip.json
│        │  │  ├─ potted_wither_rose.json
│        │  │  ├─ powder_snow.json
│        │  │  ├─ powder_snow_cauldron.json
│        │  │  ├─ powered_rail.json
│        │  │  ├─ prismarine.json
│        │  │  ├─ prismarine_bricks.json
│        │  │  ├─ prismarine_brick_slab.json
│        │  │  ├─ prismarine_brick_stairs.json
│        │  │  ├─ prismarine_slab.json
│        │  │  ├─ prismarine_stairs.json
│        │  │  ├─ prismarine_wall.json
│        │  │  ├─ pumpkin.json
│        │  │  ├─ pumpkin_stem.json
│        │  │  ├─ purple_banner.json
│        │  │  ├─ purple_bed.json
│        │  │  ├─ purple_candle.json
│        │  │  ├─ purple_candle_cake.json
│        │  │  ├─ purple_carpet.json
│        │  │  ├─ purple_concrete.json
│        │  │  ├─ purple_concrete_powder.json
│        │  │  ├─ purple_glazed_terracotta.json
│        │  │  ├─ purple_shulker_box.json
│        │  │  ├─ purple_stained_glass.json
│        │  │  ├─ purple_stained_glass_pane.json
│        │  │  ├─ purple_terracotta.json
│        │  │  ├─ purple_wool.json
│        │  │  ├─ purpur_block.json
│        │  │  ├─ purpur_pillar.json
│        │  │  ├─ purpur_slab.json
│        │  │  ├─ purpur_stairs.json
│        │  │  ├─ quartz_block.json
│        │  │  ├─ quartz_bricks.json
│        │  │  ├─ quartz_pillar.json
│        │  │  ├─ quartz_slab.json
│        │  │  ├─ quartz_stairs.json
│        │  │  ├─ rail.json
│        │  │  ├─ raw_copper_block.json
│        │  │  ├─ raw_gold_block.json
│        │  │  ├─ raw_iron_block.json
│        │  │  ├─ redstone_block.json
│        │  │  ├─ redstone_lamp.json
│        │  │  ├─ redstone_ore.json
│        │  │  ├─ redstone_torch.json
│        │  │  ├─ redstone_wire.json
│        │  │  ├─ red_banner.json
│        │  │  ├─ red_bed.json
│        │  │  ├─ red_candle.json
│        │  │  ├─ red_candle_cake.json
│        │  │  ├─ red_carpet.json
│        │  │  ├─ red_concrete.json
│        │  │  ├─ red_concrete_powder.json
│        │  │  ├─ red_glazed_terracotta.json
│        │  │  ├─ red_mushroom.json
│        │  │  ├─ red_mushroom_block.json
│        │  │  ├─ red_nether_bricks.json
│        │  │  ├─ red_nether_brick_slab.json
│        │  │  ├─ red_nether_brick_stairs.json
│        │  │  ├─ red_nether_brick_wall.json
│        │  │  ├─ red_sand.json
│        │  │  ├─ red_sandstone.json
│        │  │  ├─ red_sandstone_slab.json
│        │  │  ├─ red_sandstone_stairs.json
│        │  │  ├─ red_sandstone_wall.json
│        │  │  ├─ red_shulker_box.json
│        │  │  ├─ red_stained_glass.json
│        │  │  ├─ red_stained_glass_pane.json
│        │  │  ├─ red_terracotta.json
│        │  │  ├─ red_tulip.json
│        │  │  ├─ red_wool.json
│        │  │  ├─ reinforced_deepslate.json
│        │  │  ├─ repeater.json
│        │  │  ├─ resin_block.json
│        │  │  ├─ resin_bricks.json
│        │  │  ├─ resin_brick_slab.json
│        │  │  ├─ resin_brick_stairs.json
│        │  │  ├─ resin_brick_wall.json
│        │  │  ├─ resin_clump.json
│        │  │  ├─ respawn_anchor.json
│        │  │  ├─ rooted_dirt.json
│        │  │  ├─ rose_bush.json
│        │  │  ├─ sand.json
│        │  │  ├─ sandstone.json
│        │  │  ├─ sandstone_slab.json
│        │  │  ├─ sandstone_stairs.json
│        │  │  ├─ sandstone_wall.json
│        │  │  ├─ scaffolding.json
│        │  │  ├─ sculk.json
│        │  │  ├─ sculk_catalyst.json
│        │  │  ├─ sculk_sensor.json
│        │  │  ├─ sculk_shrieker.json
│        │  │  ├─ sculk_vein.json
│        │  │  ├─ seagrass.json
│        │  │  ├─ sea_lantern.json
│        │  │  ├─ sea_pickle.json
│        │  │  ├─ short_dry_grass.json
│        │  │  ├─ short_grass.json
│        │  │  ├─ shroomlight.json
│        │  │  ├─ shulker_box.json
│        │  │  ├─ skeleton_skull.json
│        │  │  ├─ slime_block.json
│        │  │  ├─ small_amethyst_bud.json
│        │  │  ├─ small_dripleaf.json
│        │  │  ├─ smithing_table.json
│        │  │  ├─ smoker.json
│        │  │  ├─ smooth_basalt.json
│        │  │  ├─ smooth_quartz.json
│        │  │  ├─ smooth_quartz_slab.json
│        │  │  ├─ smooth_quartz_stairs.json
│        │  │  ├─ smooth_red_sandstone.json
│        │  │  ├─ smooth_red_sandstone_slab.json
│        │  │  ├─ smooth_red_sandstone_stairs.json
│        │  │  ├─ smooth_sandstone.json
│        │  │  ├─ smooth_sandstone_slab.json
│        │  │  ├─ smooth_sandstone_stairs.json
│        │  │  ├─ smooth_stone.json
│        │  │  ├─ smooth_stone_slab.json
│        │  │  ├─ sniffer_egg.json
│        │  │  ├─ snow.json
│        │  │  ├─ snow_block.json
│        │  │  ├─ soul_campfire.json
│        │  │  ├─ soul_fire.json
│        │  │  ├─ soul_lantern.json
│        │  │  ├─ soul_sand.json
│        │  │  ├─ soul_soil.json
│        │  │  ├─ soul_torch.json
│        │  │  ├─ spawner.json
│        │  │  ├─ sponge.json
│        │  │  ├─ spore_blossom.json
│        │  │  ├─ spruce_button.json
│        │  │  ├─ spruce_door.json
│        │  │  ├─ spruce_fence.json
│        │  │  ├─ spruce_fence_gate.json
│        │  │  ├─ spruce_hanging_sign.json
│        │  │  ├─ spruce_leaves.json
│        │  │  ├─ spruce_log.json
│        │  │  ├─ spruce_planks.json
│        │  │  ├─ spruce_pressure_plate.json
│        │  │  ├─ spruce_sapling.json
│        │  │  ├─ spruce_shelf.json
│        │  │  ├─ spruce_sign.json
│        │  │  ├─ spruce_slab.json
│        │  │  ├─ spruce_stairs.json
│        │  │  ├─ spruce_trapdoor.json
│        │  │  ├─ spruce_wood.json
│        │  │  ├─ sticky_piston.json
│        │  │  ├─ stone.json
│        │  │  ├─ stonecutter.json
│        │  │  ├─ stone_bricks.json
│        │  │  ├─ stone_brick_slab.json
│        │  │  ├─ stone_brick_stairs.json
│        │  │  ├─ stone_brick_wall.json
│        │  │  ├─ stone_button.json
│        │  │  ├─ stone_pressure_plate.json
│        │  │  ├─ stone_slab.json
│        │  │  ├─ stone_stairs.json
│        │  │  ├─ stripped_acacia_log.json
│        │  │  ├─ stripped_acacia_wood.json
│        │  │  ├─ stripped_bamboo_block.json
│        │  │  ├─ stripped_birch_log.json
│        │  │  ├─ stripped_birch_wood.json
│        │  │  ├─ stripped_cherry_log.json
│        │  │  ├─ stripped_cherry_wood.json
│        │  │  ├─ stripped_crimson_hyphae.json
│        │  │  ├─ stripped_crimson_stem.json
│        │  │  ├─ stripped_dark_oak_log.json
│        │  │  ├─ stripped_dark_oak_wood.json
│        │  │  ├─ stripped_jungle_log.json
│        │  │  ├─ stripped_jungle_wood.json
│        │  │  ├─ stripped_mangrove_log.json
│        │  │  ├─ stripped_mangrove_wood.json
│        │  │  ├─ stripped_oak_log.json
│        │  │  ├─ stripped_oak_wood.json
│        │  │  ├─ stripped_pale_oak_log.json
│        │  │  ├─ stripped_pale_oak_wood.json
│        │  │  ├─ stripped_spruce_log.json
│        │  │  ├─ stripped_spruce_wood.json
│        │  │  ├─ stripped_warped_hyphae.json
│        │  │  ├─ stripped_warped_stem.json
│        │  │  ├─ sugar_cane.json
│        │  │  ├─ sunflower.json
│        │  │  ├─ suspicious_gravel.json
│        │  │  ├─ suspicious_sand.json
│        │  │  ├─ sweet_berry_bush.json
│        │  │  ├─ tall_dry_grass.json
│        │  │  ├─ tall_grass.json
│        │  │  ├─ tall_seagrass.json
│        │  │  ├─ target.json
│        │  │  ├─ terracotta.json
│        │  │  ├─ tinted_glass.json
│        │  │  ├─ tnt.json
│        │  │  ├─ torch.json
│        │  │  ├─ torchflower.json
│        │  │  ├─ torchflower_crop.json
│        │  │  ├─ trapped_chest.json
│        │  │  ├─ trial_spawner.json
│        │  │  ├─ tripwire.json
│        │  │  ├─ tripwire_hook.json
│        │  │  ├─ tube_coral.json
│        │  │  ├─ tube_coral_block.json
│        │  │  ├─ tube_coral_fan.json
│        │  │  ├─ tuff.json
│        │  │  ├─ tuff_bricks.json
│        │  │  ├─ tuff_brick_slab.json
│        │  │  ├─ tuff_brick_stairs.json
│        │  │  ├─ tuff_brick_wall.json
│        │  │  ├─ tuff_slab.json
│        │  │  ├─ tuff_stairs.json
│        │  │  ├─ tuff_wall.json
│        │  │  ├─ turtle_egg.json
│        │  │  ├─ twisting_vines.json
│        │  │  ├─ twisting_vines_plant.json
│        │  │  ├─ vault.json
│        │  │  ├─ verdant_froglight.json
│        │  │  ├─ vine.json
│        │  │  ├─ warped_button.json
│        │  │  ├─ warped_door.json
│        │  │  ├─ warped_fence.json
│        │  │  ├─ warped_fence_gate.json
│        │  │  ├─ warped_fungus.json
│        │  │  ├─ warped_hanging_sign.json
│        │  │  ├─ warped_hyphae.json
│        │  │  ├─ warped_nylium.json
│        │  │  ├─ warped_planks.json
│        │  │  ├─ warped_pressure_plate.json
│        │  │  ├─ warped_roots.json
│        │  │  ├─ warped_shelf.json
│        │  │  ├─ warped_sign.json
│        │  │  ├─ warped_slab.json
│        │  │  ├─ warped_stairs.json
│        │  │  ├─ warped_stem.json
│        │  │  ├─ warped_trapdoor.json
│        │  │  ├─ warped_wart_block.json
│        │  │  ├─ water_cauldron.json
│        │  │  ├─ waxed_chiseled_copper.json
│        │  │  ├─ waxed_copper_bars.json
│        │  │  ├─ waxed_copper_block.json
│        │  │  ├─ waxed_copper_bulb.json
│        │  │  ├─ waxed_copper_chain.json
│        │  │  ├─ waxed_copper_chest.json
│        │  │  ├─ waxed_copper_door.json
│        │  │  ├─ waxed_copper_golem_statue.json
│        │  │  ├─ waxed_copper_grate.json
│        │  │  ├─ waxed_copper_lantern.json
│        │  │  ├─ waxed_copper_trapdoor.json
│        │  │  ├─ waxed_cut_copper.json
│        │  │  ├─ waxed_cut_copper_slab.json
│        │  │  ├─ waxed_cut_copper_stairs.json
│        │  │  ├─ waxed_exposed_chiseled_copper.json
│        │  │  ├─ waxed_exposed_copper.json
│        │  │  ├─ waxed_exposed_copper_bars.json
│        │  │  ├─ waxed_exposed_copper_bulb.json
│        │  │  ├─ waxed_exposed_copper_chain.json
│        │  │  ├─ waxed_exposed_copper_chest.json
│        │  │  ├─ waxed_exposed_copper_door.json
│        │  │  ├─ waxed_exposed_copper_golem_statue.json
│        │  │  ├─ waxed_exposed_copper_grate.json
│        │  │  ├─ waxed_exposed_copper_lantern.json
│        │  │  ├─ waxed_exposed_copper_trapdoor.json
│        │  │  ├─ waxed_exposed_cut_copper.json
│        │  │  ├─ waxed_exposed_cut_copper_slab.json
│        │  │  ├─ waxed_exposed_cut_copper_stairs.json
│        │  │  ├─ waxed_exposed_lightning_rod.json
│        │  │  ├─ waxed_lightning_rod.json
│        │  │  ├─ waxed_oxidized_chiseled_copper.json
│        │  │  ├─ waxed_oxidized_copper.json
│        │  │  ├─ waxed_oxidized_copper_bars.json
│        │  │  ├─ waxed_oxidized_copper_bulb.json
│        │  │  ├─ waxed_oxidized_copper_chain.json
│        │  │  ├─ waxed_oxidized_copper_chest.json
│        │  │  ├─ waxed_oxidized_copper_door.json
│        │  │  ├─ waxed_oxidized_copper_golem_statue.json
│        │  │  ├─ waxed_oxidized_copper_grate.json
│        │  │  ├─ waxed_oxidized_copper_lantern.json
│        │  │  ├─ waxed_oxidized_copper_trapdoor.json
│        │  │  ├─ waxed_oxidized_cut_copper.json
│        │  │  ├─ waxed_oxidized_cut_copper_slab.json
│        │  │  ├─ waxed_oxidized_cut_copper_stairs.json
│        │  │  ├─ waxed_oxidized_lightning_rod.json
│        │  │  ├─ waxed_weathered_chiseled_copper.json
│        │  │  ├─ waxed_weathered_copper.json
│        │  │  ├─ waxed_weathered_copper_bars.json
│        │  │  ├─ waxed_weathered_copper_bulb.json
│        │  │  ├─ waxed_weathered_copper_chain.json
│        │  │  ├─ waxed_weathered_copper_chest.json
│        │  │  ├─ waxed_weathered_copper_door.json
│        │  │  ├─ waxed_weathered_copper_golem_statue.json
│        │  │  ├─ waxed_weathered_copper_grate.json
│        │  │  ├─ waxed_weathered_copper_lantern.json
│        │  │  ├─ waxed_weathered_copper_trapdoor.json
│        │  │  ├─ waxed_weathered_cut_copper.json
│        │  │  ├─ waxed_weathered_cut_copper_slab.json
│        │  │  ├─ waxed_weathered_cut_copper_stairs.json
│        │  │  ├─ waxed_weathered_lightning_rod.json
│        │  │  ├─ weathered_chiseled_copper.json
│        │  │  ├─ weathered_copper.json
│        │  │  ├─ weathered_copper_bars.json
│        │  │  ├─ weathered_copper_bulb.json
│        │  │  ├─ weathered_copper_chain.json
│        │  │  ├─ weathered_copper_chest.json
│        │  │  ├─ weathered_copper_door.json
│        │  │  ├─ weathered_copper_golem_statue.json
│        │  │  ├─ weathered_copper_grate.json
│        │  │  ├─ weathered_copper_lantern.json
│        │  │  ├─ weathered_copper_trapdoor.json
│        │  │  ├─ weathered_cut_copper.json
│        │  │  ├─ weathered_cut_copper_slab.json
│        │  │  ├─ weathered_cut_copper_stairs.json
│        │  │  ├─ weathered_lightning_rod.json
│        │  │  ├─ weeping_vines.json
│        │  │  ├─ weeping_vines_plant.json
│        │  │  ├─ wet_sponge.json
│        │  │  ├─ wheat.json
│        │  │  ├─ white_banner.json
│        │  │  ├─ white_bed.json
│        │  │  ├─ white_candle.json
│        │  │  ├─ white_candle_cake.json
│        │  │  ├─ white_carpet.json
│        │  │  ├─ white_concrete.json
│        │  │  ├─ white_concrete_powder.json
│        │  │  ├─ white_glazed_terracotta.json
│        │  │  ├─ white_shulker_box.json
│        │  │  ├─ white_stained_glass.json
│        │  │  ├─ white_stained_glass_pane.json
│        │  │  ├─ white_terracotta.json
│        │  │  ├─ white_tulip.json
│        │  │  ├─ white_wool.json
│        │  │  ├─ wildflowers.json
│        │  │  ├─ wither_rose.json
│        │  │  ├─ wither_skeleton_skull.json
│        │  │  ├─ yellow_banner.json
│        │  │  ├─ yellow_bed.json
│        │  │  ├─ yellow_candle.json
│        │  │  ├─ yellow_candle_cake.json
│        │  │  ├─ yellow_carpet.json
│        │  │  ├─ yellow_concrete.json
│        │  │  ├─ yellow_concrete_powder.json
│        │  │  ├─ yellow_glazed_terracotta.json
│        │  │  ├─ yellow_shulker_box.json
│        │  │  ├─ yellow_stained_glass.json
│        │  │  ├─ yellow_stained_glass_pane.json
│        │  │  ├─ yellow_terracotta.json
│        │  │  ├─ yellow_wool.json
│        │  │  └─ zombie_head.json
│        │  ├─ brush
│        │  │  └─ armadillo.json
│        │  ├─ carve
│        │  │  └─ pumpkin.json
│        │  ├─ charged_creeper
│        │  │  ├─ creeper.json
│        │  │  ├─ piglin.json
│        │  │  ├─ root.json
│        │  │  ├─ skeleton.json
│        │  │  ├─ wither_skeleton.json
│        │  │  └─ zombie.json
│        │  ├─ chests
│        │  │  ├─ abandoned_mineshaft.json
│        │  │  ├─ ancient_city.json
│        │  │  ├─ ancient_city_ice_box.json
│        │  │  ├─ bastion_bridge.json
│        │  │  ├─ bastion_hoglin_stable.json
│        │  │  ├─ bastion_other.json
│        │  │  ├─ bastion_treasure.json
│        │  │  ├─ buried_treasure.json
│        │  │  ├─ desert_pyramid.json
│        │  │  ├─ end_city_treasure.json
│        │  │  ├─ igloo_chest.json
│        │  │  ├─ jungle_temple.json
│        │  │  ├─ jungle_temple_dispenser.json
│        │  │  ├─ nether_bridge.json
│        │  │  ├─ pillager_outpost.json
│        │  │  ├─ ruined_portal.json
│        │  │  ├─ shipwreck_map.json
│        │  │  ├─ shipwreck_supply.json
│        │  │  ├─ shipwreck_treasure.json
│        │  │  ├─ simple_dungeon.json
│        │  │  ├─ spawn_bonus_chest.json
│        │  │  ├─ stronghold_corridor.json
│        │  │  ├─ stronghold_crossing.json
│        │  │  ├─ stronghold_library.json
│        │  │  ├─ trial_chambers
│        │  │  │  ├─ corridor.json
│        │  │  │  ├─ entrance.json
│        │  │  │  ├─ intersection.json
│        │  │  │  ├─ intersection_barrel.json
│        │  │  │  ├─ reward.json
│        │  │  │  ├─ reward_common.json
│        │  │  │  ├─ reward_ominous.json
│        │  │  │  ├─ reward_ominous_common.json
│        │  │  │  ├─ reward_ominous_rare.json
│        │  │  │  ├─ reward_ominous_unique.json
│        │  │  │  ├─ reward_rare.json
│        │  │  │  ├─ reward_unique.json
│        │  │  │  └─ supply.json
│        │  │  ├─ underwater_ruin_big.json
│        │  │  ├─ underwater_ruin_small.json
│        │  │  ├─ village
│        │  │  │  ├─ village_armorer.json
│        │  │  │  ├─ village_butcher.json
│        │  │  │  ├─ village_cartographer.json
│        │  │  │  ├─ village_desert_house.json
│        │  │  │  ├─ village_fisher.json
│        │  │  │  ├─ village_fletcher.json
│        │  │  │  ├─ village_mason.json
│        │  │  │  ├─ village_plains_house.json
│        │  │  │  ├─ village_savanna_house.json
│        │  │  │  ├─ village_shepherd.json
│        │  │  │  ├─ village_snowy_house.json
│        │  │  │  ├─ village_taiga_house.json
│        │  │  │  ├─ village_tannery.json
│        │  │  │  ├─ village_temple.json
│        │  │  │  ├─ village_toolsmith.json
│        │  │  │  └─ village_weaponsmith.json
│        │  │  └─ woodland_mansion.json
│        │  ├─ dispensers
│        │  │  └─ trial_chambers
│        │  │     ├─ chamber.json
│        │  │     ├─ corridor.json
│        │  │     └─ water.json
│        │  ├─ entities
│        │  │  ├─ allay.json
│        │  │  ├─ armadillo.json
│        │  │  ├─ armor_stand.json
│        │  │  ├─ axolotl.json
│        │  │  ├─ bat.json
│        │  │  ├─ bee.json
│        │  │  ├─ blaze.json
│        │  │  ├─ bogged.json
│        │  │  ├─ breeze.json
│        │  │  ├─ camel.json
│        │  │  ├─ camel_husk.json
│        │  │  ├─ cat.json
│        │  │  ├─ cave_spider.json
│        │  │  ├─ chicken.json
│        │  │  ├─ cod.json
│        │  │  ├─ copper_golem.json
│        │  │  ├─ cow.json
│        │  │  ├─ creaking.json
│        │  │  ├─ creeper.json
│        │  │  ├─ dolphin.json
│        │  │  ├─ donkey.json
│        │  │  ├─ drowned.json
│        │  │  ├─ elder_guardian.json
│        │  │  ├─ enderman.json
│        │  │  ├─ endermite.json
│        │  │  ├─ ender_dragon.json
│        │  │  ├─ evoker.json
│        │  │  ├─ fox.json
│        │  │  ├─ frog.json
│        │  │  ├─ ghast.json
│        │  │  ├─ giant.json
│        │  │  ├─ glow_squid.json
│        │  │  ├─ goat.json
│        │  │  ├─ guardian.json
│        │  │  ├─ happy_ghast.json
│        │  │  ├─ hoglin.json
│        │  │  ├─ horse.json
│        │  │  ├─ husk.json
│        │  │  ├─ illusioner.json
│        │  │  ├─ iron_golem.json
│        │  │  ├─ llama.json
│        │  │  ├─ magma_cube.json
│        │  │  ├─ mannequin.json
│        │  │  ├─ mooshroom.json
│        │  │  ├─ mule.json
│        │  │  ├─ nautilus.json
│        │  │  ├─ ocelot.json
│        │  │  ├─ panda.json
│        │  │  ├─ parched.json
│        │  │  ├─ parrot.json
│        │  │  ├─ phantom.json
│        │  │  ├─ pig.json
│        │  │  ├─ piglin.json
│        │  │  ├─ piglin_brute.json
│        │  │  ├─ pillager.json
│        │  │  ├─ player.json
│        │  │  ├─ polar_bear.json
│        │  │  ├─ pufferfish.json
│        │  │  ├─ rabbit.json
│        │  │  ├─ ravager.json
│        │  │  ├─ salmon.json
│        │  │  ├─ sheep
│        │  │  │  ├─ black.json
│        │  │  │  ├─ blue.json
│        │  │  │  ├─ brown.json
│        │  │  │  ├─ cyan.json
│        │  │  │  ├─ gray.json
│        │  │  │  ├─ green.json
│        │  │  │  ├─ light_blue.json
│        │  │  │  ├─ light_gray.json
│        │  │  │  ├─ lime.json
│        │  │  │  ├─ magenta.json
│        │  │  │  ├─ orange.json
│        │  │  │  ├─ pink.json
│        │  │  │  ├─ purple.json
│        │  │  │  ├─ red.json
│        │  │  │  ├─ white.json
│        │  │  │  └─ yellow.json
│        │  │  ├─ sheep.json
│        │  │  ├─ shulker.json
│        │  │  ├─ silverfish.json
│        │  │  ├─ skeleton.json
│        │  │  ├─ skeleton_horse.json
│        │  │  ├─ slime.json
│        │  │  ├─ sniffer.json
│        │  │  ├─ snow_golem.json
│        │  │  ├─ spider.json
│        │  │  ├─ squid.json
│        │  │  ├─ stray.json
│        │  │  ├─ strider.json
│        │  │  ├─ tadpole.json
│        │  │  ├─ trader_llama.json
│        │  │  ├─ tropical_fish.json
│        │  │  ├─ turtle.json
│        │  │  ├─ vex.json
│        │  │  ├─ villager.json
│        │  │  ├─ vindicator.json
│        │  │  ├─ wandering_trader.json
│        │  │  ├─ warden.json
│        │  │  ├─ witch.json
│        │  │  ├─ wither.json
│        │  │  ├─ wither_skeleton.json
│        │  │  ├─ wolf.json
│        │  │  ├─ zoglin.json
│        │  │  ├─ zombie.json
│        │  │  ├─ zombie_horse.json
│        │  │  ├─ zombie_nautilus.json
│        │  │  ├─ zombie_villager.json
│        │  │  └─ zombified_piglin.json
│        │  ├─ equipment
│        │  │  ├─ trial_chamber.json
│        │  │  ├─ trial_chamber_melee.json
│        │  │  └─ trial_chamber_ranged.json
│        │  ├─ gameplay
│        │  │  ├─ armadillo_shed.json
│        │  │  ├─ cat_morning_gift.json
│        │  │  ├─ chicken_lay.json
│        │  │  ├─ fishing
│        │  │  │  ├─ fish.json
│        │  │  │  ├─ junk.json
│        │  │  │  └─ treasure.json
│        │  │  ├─ fishing.json
│        │  │  ├─ hero_of_the_village
│        │  │  │  ├─ armorer_gift.json
│        │  │  │  ├─ baby_gift.json
│        │  │  │  ├─ butcher_gift.json
│        │  │  │  ├─ cartographer_gift.json
│        │  │  │  ├─ cleric_gift.json
│        │  │  │  ├─ farmer_gift.json
│        │  │  │  ├─ fisherman_gift.json
│        │  │  │  ├─ fletcher_gift.json
│        │  │  │  ├─ leatherworker_gift.json
│        │  │  │  ├─ librarian_gift.json
│        │  │  │  ├─ mason_gift.json
│        │  │  │  ├─ shepherd_gift.json
│        │  │  │  ├─ toolsmith_gift.json
│        │  │  │  ├─ unemployed_gift.json
│        │  │  │  └─ weaponsmith_gift.json
│        │  │  ├─ panda_sneeze.json
│        │  │  ├─ piglin_bartering.json
│        │  │  ├─ sniffer_digging.json
│        │  │  └─ turtle_grow.json
│        │  ├─ harvest
│        │  │  ├─ beehive.json
│        │  │  ├─ cave_vine.json
│        │  │  └─ sweet_berry_bush.json
│        │  ├─ pots
│        │  │  └─ trial_chambers
│        │  │     └─ corridor.json
│        │  ├─ shearing
│        │  │  ├─ bogged.json
│        │  │  ├─ mooshroom
│        │  │  │  ├─ brown.json
│        │  │  │  └─ red.json
│        │  │  ├─ mooshroom.json
│        │  │  ├─ sheep
│        │  │  │  ├─ black.json
│        │  │  │  ├─ blue.json
│        │  │  │  ├─ brown.json
│        │  │  │  ├─ cyan.json
│        │  │  │  ├─ gray.json
│        │  │  │  ├─ green.json
│        │  │  │  ├─ light_blue.json
│        │  │  │  ├─ light_gray.json
│        │  │  │  ├─ lime.json
│        │  │  │  ├─ magenta.json
│        │  │  │  ├─ orange.json
│        │  │  │  ├─ pink.json
│        │  │  │  ├─ purple.json
│        │  │  │  ├─ red.json
│        │  │  │  ├─ white.json
│        │  │  │  └─ yellow.json
│        │  │  ├─ sheep.json
│        │  │  └─ snow_golem.json
│        │  └─ spawners
│        │     ├─ ominous
│        │     │  └─ trial_chamber
│        │     │     ├─ consumables.json
│        │     │     └─ key.json
│        │     └─ trial_chamber
│        │        ├─ consumables.json
│        │        ├─ items_to_drop_when_ominous.json
│        │        └─ key.json
│        ├─ painting_variant
│        │  ├─ alban.json
│        │  ├─ aztec.json
│        │  ├─ aztec2.json
│        │  ├─ backyard.json
│        │  ├─ baroque.json
│        │  ├─ bomb.json
│        │  ├─ bouquet.json
│        │  ├─ burning_skull.json
│        │  ├─ bust.json
│        │  ├─ cavebird.json
│        │  ├─ changing.json
│        │  ├─ cotan.json
│        │  ├─ courbet.json
│        │  ├─ creebet.json
│        │  ├─ dennis.json
│        │  ├─ donkey_kong.json
│        │  ├─ earth.json
│        │  ├─ endboss.json
│        │  ├─ fern.json
│        │  ├─ fighters.json
│        │  ├─ finding.json
│        │  ├─ fire.json
│        │  ├─ graham.json
│        │  ├─ humble.json
│        │  ├─ kebab.json
│        │  ├─ lowmist.json
│        │  ├─ match.json
│        │  ├─ meditative.json
│        │  ├─ orb.json
│        │  ├─ owlemons.json
│        │  ├─ passage.json
│        │  ├─ pigscene.json
│        │  ├─ plant.json
│        │  ├─ pointer.json
│        │  ├─ pond.json
│        │  ├─ pool.json
│        │  ├─ prairie_ride.json
│        │  ├─ sea.json
│        │  ├─ skeleton.json
│        │  ├─ skull_and_roses.json
│        │  ├─ stage.json
│        │  ├─ sunflowers.json
│        │  ├─ sunset.json
│        │  ├─ tides.json
│        │  ├─ unpacked.json
│        │  ├─ void.json
│        │  ├─ wanderer.json
│        │  ├─ wasteland.json
│        │  ├─ water.json
│        │  ├─ wind.json
│        │  └─ wither.json
│        ├─ pig_variant
│        │  ├─ cold.json
│        │  ├─ temperate.json
│        │  └─ warm.json
│        ├─ recipe
│        │  ├─ acacia_boat.json
│        │  ├─ acacia_button.json
│        │  ├─ acacia_chest_boat.json
│        │  ├─ acacia_door.json
│        │  ├─ acacia_fence.json
│        │  ├─ acacia_fence_gate.json
│        │  ├─ acacia_hanging_sign.json
│        │  ├─ acacia_planks.json
│        │  ├─ acacia_pressure_plate.json
│        │  ├─ acacia_shelf.json
│        │  ├─ acacia_sign.json
│        │  ├─ acacia_slab.json
│        │  ├─ acacia_stairs.json
│        │  ├─ acacia_trapdoor.json
│        │  ├─ acacia_wood.json
│        │  ├─ activator_rail.json
│        │  ├─ amethyst_block.json
│        │  ├─ andesite.json
│        │  ├─ andesite_slab.json
│        │  ├─ andesite_slab_from_andesite_stonecutting.json
│        │  ├─ andesite_stairs.json
│        │  ├─ andesite_stairs_from_andesite_stonecutting.json
│        │  ├─ andesite_wall.json
│        │  ├─ andesite_wall_from_andesite_stonecutting.json
│        │  ├─ anvil.json
│        │  ├─ armor_dye.json
│        │  ├─ armor_stand.json
│        │  ├─ arrow.json
│        │  ├─ baked_potato.json
│        │  ├─ baked_potato_from_campfire_cooking.json
│        │  ├─ baked_potato_from_smoking.json
│        │  ├─ bamboo_block.json
│        │  ├─ bamboo_button.json
│        │  ├─ bamboo_chest_raft.json
│        │  ├─ bamboo_door.json
│        │  ├─ bamboo_fence.json
│        │  ├─ bamboo_fence_gate.json
│        │  ├─ bamboo_hanging_sign.json
│        │  ├─ bamboo_mosaic.json
│        │  ├─ bamboo_mosaic_slab.json
│        │  ├─ bamboo_mosaic_stairs.json
│        │  ├─ bamboo_planks.json
│        │  ├─ bamboo_pressure_plate.json
│        │  ├─ bamboo_raft.json
│        │  ├─ bamboo_shelf.json
│        │  ├─ bamboo_sign.json
│        │  ├─ bamboo_slab.json
│        │  ├─ bamboo_stairs.json
│        │  ├─ bamboo_trapdoor.json
│        │  ├─ banner_duplicate.json
│        │  ├─ barrel.json
│        │  ├─ beacon.json
│        │  ├─ beehive.json
│        │  ├─ beetroot_soup.json
│        │  ├─ birch_boat.json
│        │  ├─ birch_button.json
│        │  ├─ birch_chest_boat.json
│        │  ├─ birch_door.json
│        │  ├─ birch_fence.json
│        │  ├─ birch_fence_gate.json
│        │  ├─ birch_hanging_sign.json
│        │  ├─ birch_planks.json
│        │  ├─ birch_pressure_plate.json
│        │  ├─ birch_shelf.json
│        │  ├─ birch_sign.json
│        │  ├─ birch_slab.json
│        │  ├─ birch_stairs.json
│        │  ├─ birch_trapdoor.json
│        │  ├─ birch_wood.json
│        │  ├─ blackstone_slab.json
│        │  ├─ blackstone_slab_from_blackstone_stonecutting.json
│        │  ├─ blackstone_stairs.json
│        │  ├─ blackstone_stairs_from_blackstone_stonecutting.json
│        │  ├─ blackstone_wall.json
│        │  ├─ blackstone_wall_from_blackstone_stonecutting.json
│        │  ├─ black_banner.json
│        │  ├─ black_bed.json
│        │  ├─ black_bundle.json
│        │  ├─ black_candle.json
│        │  ├─ black_carpet.json
│        │  ├─ black_concrete_powder.json
│        │  ├─ black_dye.json
│        │  ├─ black_dye_from_wither_rose.json
│        │  ├─ black_glazed_terracotta.json
│        │  ├─ black_harness.json
│        │  ├─ black_shulker_box.json
│        │  ├─ black_stained_glass.json
│        │  ├─ black_stained_glass_pane.json
│        │  ├─ black_stained_glass_pane_from_glass_pane.json
│        │  ├─ black_terracotta.json
│        │  ├─ blast_furnace.json
│        │  ├─ blaze_powder.json
│        │  ├─ blue_banner.json
│        │  ├─ blue_bed.json
│        │  ├─ blue_bundle.json
│        │  ├─ blue_candle.json
│        │  ├─ blue_carpet.json
│        │  ├─ blue_concrete_powder.json
│        │  ├─ blue_dye.json
│        │  ├─ blue_dye_from_cornflower.json
│        │  ├─ blue_glazed_terracotta.json
│        │  ├─ blue_harness.json
│        │  ├─ blue_ice.json
│        │  ├─ blue_shulker_box.json
│        │  ├─ blue_stained_glass.json
│        │  ├─ blue_stained_glass_pane.json
│        │  ├─ blue_stained_glass_pane_from_glass_pane.json
│        │  ├─ blue_terracotta.json
│        │  ├─ bolt_armor_trim_smithing_template.json
│        │  ├─ bolt_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ bone_block.json
│        │  ├─ bone_meal.json
│        │  ├─ bone_meal_from_bone_block.json
│        │  ├─ book.json
│        │  ├─ bookshelf.json
│        │  ├─ book_cloning.json
│        │  ├─ bordure_indented_banner_pattern.json
│        │  ├─ bow.json
│        │  ├─ bowl.json
│        │  ├─ bread.json
│        │  ├─ brewing_stand.json
│        │  ├─ brick.json
│        │  ├─ bricks.json
│        │  ├─ brick_slab.json
│        │  ├─ brick_slab_from_bricks_stonecutting.json
│        │  ├─ brick_stairs.json
│        │  ├─ brick_stairs_from_bricks_stonecutting.json
│        │  ├─ brick_wall.json
│        │  ├─ brick_wall_from_bricks_stonecutting.json
│        │  ├─ brown_banner.json
│        │  ├─ brown_bed.json
│        │  ├─ brown_bundle.json
│        │  ├─ brown_candle.json
│        │  ├─ brown_carpet.json
│        │  ├─ brown_concrete_powder.json
│        │  ├─ brown_dye.json
│        │  ├─ brown_glazed_terracotta.json
│        │  ├─ brown_harness.json
│        │  ├─ brown_shulker_box.json
│        │  ├─ brown_stained_glass.json
│        │  ├─ brown_stained_glass_pane.json
│        │  ├─ brown_stained_glass_pane_from_glass_pane.json
│        │  ├─ brown_terracotta.json
│        │  ├─ brush.json
│        │  ├─ bucket.json
│        │  ├─ bundle.json
│        │  ├─ cake.json
│        │  ├─ calibrated_sculk_sensor.json
│        │  ├─ campfire.json
│        │  ├─ candle.json
│        │  ├─ carrot_on_a_stick.json
│        │  ├─ cartography_table.json
│        │  ├─ cauldron.json
│        │  ├─ charcoal.json
│        │  ├─ cherry_boat.json
│        │  ├─ cherry_button.json
│        │  ├─ cherry_chest_boat.json
│        │  ├─ cherry_door.json
│        │  ├─ cherry_fence.json
│        │  ├─ cherry_fence_gate.json
│        │  ├─ cherry_hanging_sign.json
│        │  ├─ cherry_planks.json
│        │  ├─ cherry_pressure_plate.json
│        │  ├─ cherry_shelf.json
│        │  ├─ cherry_sign.json
│        │  ├─ cherry_slab.json
│        │  ├─ cherry_stairs.json
│        │  ├─ cherry_trapdoor.json
│        │  ├─ cherry_wood.json
│        │  ├─ chest.json
│        │  ├─ chest_minecart.json
│        │  ├─ chiseled_bookshelf.json
│        │  ├─ chiseled_copper.json
│        │  ├─ chiseled_copper_from_copper_block_stonecutting.json
│        │  ├─ chiseled_copper_from_cut_copper_stonecutting.json
│        │  ├─ chiseled_deepslate.json
│        │  ├─ chiseled_deepslate_from_cobbled_deepslate_stonecutting.json
│        │  ├─ chiseled_nether_bricks.json
│        │  ├─ chiseled_nether_bricks_from_nether_bricks_stonecutting.json
│        │  ├─ chiseled_polished_blackstone.json
│        │  ├─ chiseled_polished_blackstone_from_blackstone_stonecutting.json
│        │  ├─ chiseled_polished_blackstone_from_polished_blackstone_stonecutting.json
│        │  ├─ chiseled_quartz_block.json
│        │  ├─ chiseled_quartz_block_from_quartz_block_stonecutting.json
│        │  ├─ chiseled_red_sandstone.json
│        │  ├─ chiseled_red_sandstone_from_red_sandstone_stonecutting.json
│        │  ├─ chiseled_resin_bricks.json
│        │  ├─ chiseled_resin_bricks_from_resin_bricks_stonecutting.json
│        │  ├─ chiseled_sandstone.json
│        │  ├─ chiseled_sandstone_from_sandstone_stonecutting.json
│        │  ├─ chiseled_stone_bricks.json
│        │  ├─ chiseled_stone_bricks_from_stone_bricks_stonecutting.json
│        │  ├─ chiseled_stone_bricks_stone_from_stonecutting.json
│        │  ├─ chiseled_tuff.json
│        │  ├─ chiseled_tuff_bricks.json
│        │  ├─ chiseled_tuff_bricks_from_polished_tuff_stonecutting.json
│        │  ├─ chiseled_tuff_bricks_from_tuff_bricks_stonecutting.json
│        │  ├─ chiseled_tuff_bricks_from_tuff_stonecutting.json
│        │  ├─ chiseled_tuff_from_tuff_stonecutting.json
│        │  ├─ clay.json
│        │  ├─ clock.json
│        │  ├─ coal.json
│        │  ├─ coal_block.json
│        │  ├─ coal_from_blasting_coal_ore.json
│        │  ├─ coal_from_blasting_deepslate_coal_ore.json
│        │  ├─ coal_from_smelting_coal_ore.json
│        │  ├─ coal_from_smelting_deepslate_coal_ore.json
│        │  ├─ coarse_dirt.json
│        │  ├─ coast_armor_trim_smithing_template.json
│        │  ├─ coast_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ cobbled_deepslate_slab.json
│        │  ├─ cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting.json
│        │  ├─ cobbled_deepslate_stairs.json
│        │  ├─ cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting.json
│        │  ├─ cobbled_deepslate_wall.json
│        │  ├─ cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting.json
│        │  ├─ cobblestone_slab.json
│        │  ├─ cobblestone_slab_from_cobblestone_stonecutting.json
│        │  ├─ cobblestone_stairs.json
│        │  ├─ cobblestone_stairs_from_cobblestone_stonecutting.json
│        │  ├─ cobblestone_wall.json
│        │  ├─ cobblestone_wall_from_cobblestone_stonecutting.json
│        │  ├─ comparator.json
│        │  ├─ compass.json
│        │  ├─ composter.json
│        │  ├─ conduit.json
│        │  ├─ cooked_beef.json
│        │  ├─ cooked_beef_from_campfire_cooking.json
│        │  ├─ cooked_beef_from_smoking.json
│        │  ├─ cooked_chicken.json
│        │  ├─ cooked_chicken_from_campfire_cooking.json
│        │  ├─ cooked_chicken_from_smoking.json
│        │  ├─ cooked_cod.json
│        │  ├─ cooked_cod_from_campfire_cooking.json
│        │  ├─ cooked_cod_from_smoking.json
│        │  ├─ cooked_mutton.json
│        │  ├─ cooked_mutton_from_campfire_cooking.json
│        │  ├─ cooked_mutton_from_smoking.json
│        │  ├─ cooked_porkchop.json
│        │  ├─ cooked_porkchop_from_campfire_cooking.json
│        │  ├─ cooked_porkchop_from_smoking.json
│        │  ├─ cooked_rabbit.json
│        │  ├─ cooked_rabbit_from_campfire_cooking.json
│        │  ├─ cooked_rabbit_from_smoking.json
│        │  ├─ cooked_salmon.json
│        │  ├─ cooked_salmon_from_campfire_cooking.json
│        │  ├─ cooked_salmon_from_smoking.json
│        │  ├─ cookie.json
│        │  ├─ copper_axe.json
│        │  ├─ copper_bars.json
│        │  ├─ copper_block.json
│        │  ├─ copper_boots.json
│        │  ├─ copper_bulb.json
│        │  ├─ copper_chain.json
│        │  ├─ copper_chest.json
│        │  ├─ copper_chestplate.json
│        │  ├─ copper_door.json
│        │  ├─ copper_grate.json
│        │  ├─ copper_grate_from_copper_block_stonecutting.json
│        │  ├─ copper_helmet.json
│        │  ├─ copper_hoe.json
│        │  ├─ copper_ingot.json
│        │  ├─ copper_ingot_from_blasting_copper_ore.json
│        │  ├─ copper_ingot_from_blasting_deepslate_copper_ore.json
│        │  ├─ copper_ingot_from_blasting_raw_copper.json
│        │  ├─ copper_ingot_from_nuggets.json
│        │  ├─ copper_ingot_from_smelting_copper_ore.json
│        │  ├─ copper_ingot_from_smelting_deepslate_copper_ore.json
│        │  ├─ copper_ingot_from_smelting_raw_copper.json
│        │  ├─ copper_ingot_from_waxed_copper_block.json
│        │  ├─ copper_lantern.json
│        │  ├─ copper_leggings.json
│        │  ├─ copper_nugget.json
│        │  ├─ copper_nugget_from_blasting.json
│        │  ├─ copper_nugget_from_smelting.json
│        │  ├─ copper_pickaxe.json
│        │  ├─ copper_shovel.json
│        │  ├─ copper_spear.json
│        │  ├─ copper_sword.json
│        │  ├─ copper_torch.json
│        │  ├─ copper_trapdoor.json
│        │  ├─ cracked_deepslate_bricks.json
│        │  ├─ cracked_deepslate_tiles.json
│        │  ├─ cracked_nether_bricks.json
│        │  ├─ cracked_polished_blackstone_bricks.json
│        │  ├─ cracked_stone_bricks.json
│        │  ├─ crafter.json
│        │  ├─ crafting_table.json
│        │  ├─ creaking_heart.json
│        │  ├─ creeper_banner_pattern.json
│        │  ├─ crimson_button.json
│        │  ├─ crimson_door.json
│        │  ├─ crimson_fence.json
│        │  ├─ crimson_fence_gate.json
│        │  ├─ crimson_hanging_sign.json
│        │  ├─ crimson_hyphae.json
│        │  ├─ crimson_planks.json
│        │  ├─ crimson_pressure_plate.json
│        │  ├─ crimson_shelf.json
│        │  ├─ crimson_sign.json
│        │  ├─ crimson_slab.json
│        │  ├─ crimson_stairs.json
│        │  ├─ crimson_trapdoor.json
│        │  ├─ crossbow.json
│        │  ├─ cut_copper.json
│        │  ├─ cut_copper_from_copper_block_stonecutting.json
│        │  ├─ cut_copper_slab.json
│        │  ├─ cut_copper_slab_from_copper_block_stonecutting.json
│        │  ├─ cut_copper_slab_from_cut_copper_stonecutting.json
│        │  ├─ cut_copper_stairs.json
│        │  ├─ cut_copper_stairs_from_copper_block_stonecutting.json
│        │  ├─ cut_copper_stairs_from_cut_copper_stonecutting.json
│        │  ├─ cut_red_sandstone.json
│        │  ├─ cut_red_sandstone_from_red_sandstone_stonecutting.json
│        │  ├─ cut_red_sandstone_slab.json
│        │  ├─ cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting.json
│        │  ├─ cut_red_sandstone_slab_from_red_sandstone_stonecutting.json
│        │  ├─ cut_sandstone.json
│        │  ├─ cut_sandstone_from_sandstone_stonecutting.json
│        │  ├─ cut_sandstone_slab.json
│        │  ├─ cut_sandstone_slab_from_cut_sandstone_stonecutting.json
│        │  ├─ cut_sandstone_slab_from_sandstone_stonecutting.json
│        │  ├─ cyan_banner.json
│        │  ├─ cyan_bed.json
│        │  ├─ cyan_bundle.json
│        │  ├─ cyan_candle.json
│        │  ├─ cyan_carpet.json
│        │  ├─ cyan_concrete_powder.json
│        │  ├─ cyan_dye.json
│        │  ├─ cyan_dye_from_pitcher_plant.json
│        │  ├─ cyan_glazed_terracotta.json
│        │  ├─ cyan_harness.json
│        │  ├─ cyan_shulker_box.json
│        │  ├─ cyan_stained_glass.json
│        │  ├─ cyan_stained_glass_pane.json
│        │  ├─ cyan_stained_glass_pane_from_glass_pane.json
│        │  ├─ cyan_terracotta.json
│        │  ├─ dark_oak_boat.json
│        │  ├─ dark_oak_button.json
│        │  ├─ dark_oak_chest_boat.json
│        │  ├─ dark_oak_door.json
│        │  ├─ dark_oak_fence.json
│        │  ├─ dark_oak_fence_gate.json
│        │  ├─ dark_oak_hanging_sign.json
│        │  ├─ dark_oak_planks.json
│        │  ├─ dark_oak_pressure_plate.json
│        │  ├─ dark_oak_shelf.json
│        │  ├─ dark_oak_sign.json
│        │  ├─ dark_oak_slab.json
│        │  ├─ dark_oak_stairs.json
│        │  ├─ dark_oak_trapdoor.json
│        │  ├─ dark_oak_wood.json
│        │  ├─ dark_prismarine.json
│        │  ├─ dark_prismarine_slab.json
│        │  ├─ dark_prismarine_slab_from_dark_prismarine_stonecutting.json
│        │  ├─ dark_prismarine_stairs.json
│        │  ├─ dark_prismarine_stairs_from_dark_prismarine_stonecutting.json
│        │  ├─ daylight_detector.json
│        │  ├─ decorated_pot.json
│        │  ├─ decorated_pot_simple.json
│        │  ├─ deepslate.json
│        │  ├─ deepslate_bricks.json
│        │  ├─ deepslate_bricks_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_bricks_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_brick_slab.json
│        │  ├─ deepslate_brick_slab_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_brick_slab_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_brick_slab_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_brick_stairs.json
│        │  ├─ deepslate_brick_stairs_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_brick_stairs_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_brick_stairs_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_brick_wall.json
│        │  ├─ deepslate_brick_wall_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_brick_wall_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_brick_wall_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_tiles.json
│        │  ├─ deepslate_tiles_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_tiles_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_tiles_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_tile_slab.json
│        │  ├─ deepslate_tile_slab_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_tile_slab_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_tile_slab_from_deepslate_tiles_stonecutting.json
│        │  ├─ deepslate_tile_slab_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_tile_stairs.json
│        │  ├─ deepslate_tile_stairs_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_tile_stairs_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_tile_stairs_from_deepslate_tiles_stonecutting.json
│        │  ├─ deepslate_tile_stairs_from_polished_deepslate_stonecutting.json
│        │  ├─ deepslate_tile_wall.json
│        │  ├─ deepslate_tile_wall_from_cobbled_deepslate_stonecutting.json
│        │  ├─ deepslate_tile_wall_from_deepslate_bricks_stonecutting.json
│        │  ├─ deepslate_tile_wall_from_deepslate_tiles_stonecutting.json
│        │  ├─ deepslate_tile_wall_from_polished_deepslate_stonecutting.json
│        │  ├─ detector_rail.json
│        │  ├─ diamond.json
│        │  ├─ diamond_axe.json
│        │  ├─ diamond_block.json
│        │  ├─ diamond_boots.json
│        │  ├─ diamond_chestplate.json
│        │  ├─ diamond_from_blasting_deepslate_diamond_ore.json
│        │  ├─ diamond_from_blasting_diamond_ore.json
│        │  ├─ diamond_from_smelting_deepslate_diamond_ore.json
│        │  ├─ diamond_from_smelting_diamond_ore.json
│        │  ├─ diamond_helmet.json
│        │  ├─ diamond_hoe.json
│        │  ├─ diamond_leggings.json
│        │  ├─ diamond_pickaxe.json
│        │  ├─ diamond_shovel.json
│        │  ├─ diamond_spear.json
│        │  ├─ diamond_sword.json
│        │  ├─ diorite.json
│        │  ├─ diorite_slab.json
│        │  ├─ diorite_slab_from_diorite_stonecutting.json
│        │  ├─ diorite_stairs.json
│        │  ├─ diorite_stairs_from_diorite_stonecutting.json
│        │  ├─ diorite_wall.json
│        │  ├─ diorite_wall_from_diorite_stonecutting.json
│        │  ├─ dispenser.json
│        │  ├─ dried_ghast.json
│        │  ├─ dried_kelp.json
│        │  ├─ dried_kelp_block.json
│        │  ├─ dried_kelp_from_campfire_cooking.json
│        │  ├─ dried_kelp_from_smelting.json
│        │  ├─ dried_kelp_from_smoking.json
│        │  ├─ dripstone_block.json
│        │  ├─ dropper.json
│        │  ├─ dune_armor_trim_smithing_template.json
│        │  ├─ dune_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ dye_black_bed.json
│        │  ├─ dye_black_carpet.json
│        │  ├─ dye_black_harness.json
│        │  ├─ dye_black_wool.json
│        │  ├─ dye_blue_bed.json
│        │  ├─ dye_blue_carpet.json
│        │  ├─ dye_blue_harness.json
│        │  ├─ dye_blue_wool.json
│        │  ├─ dye_brown_bed.json
│        │  ├─ dye_brown_carpet.json
│        │  ├─ dye_brown_harness.json
│        │  ├─ dye_brown_wool.json
│        │  ├─ dye_cyan_bed.json
│        │  ├─ dye_cyan_carpet.json
│        │  ├─ dye_cyan_harness.json
│        │  ├─ dye_cyan_wool.json
│        │  ├─ dye_gray_bed.json
│        │  ├─ dye_gray_carpet.json
│        │  ├─ dye_gray_harness.json
│        │  ├─ dye_gray_wool.json
│        │  ├─ dye_green_bed.json
│        │  ├─ dye_green_carpet.json
│        │  ├─ dye_green_harness.json
│        │  ├─ dye_green_wool.json
│        │  ├─ dye_light_blue_bed.json
│        │  ├─ dye_light_blue_carpet.json
│        │  ├─ dye_light_blue_harness.json
│        │  ├─ dye_light_blue_wool.json
│        │  ├─ dye_light_gray_bed.json
│        │  ├─ dye_light_gray_carpet.json
│        │  ├─ dye_light_gray_harness.json
│        │  ├─ dye_light_gray_wool.json
│        │  ├─ dye_lime_bed.json
│        │  ├─ dye_lime_carpet.json
│        │  ├─ dye_lime_harness.json
│        │  ├─ dye_lime_wool.json
│        │  ├─ dye_magenta_bed.json
│        │  ├─ dye_magenta_carpet.json
│        │  ├─ dye_magenta_harness.json
│        │  ├─ dye_magenta_wool.json
│        │  ├─ dye_orange_bed.json
│        │  ├─ dye_orange_carpet.json
│        │  ├─ dye_orange_harness.json
│        │  ├─ dye_orange_wool.json
│        │  ├─ dye_pink_bed.json
│        │  ├─ dye_pink_carpet.json
│        │  ├─ dye_pink_harness.json
│        │  ├─ dye_pink_wool.json
│        │  ├─ dye_purple_bed.json
│        │  ├─ dye_purple_carpet.json
│        │  ├─ dye_purple_harness.json
│        │  ├─ dye_purple_wool.json
│        │  ├─ dye_red_bed.json
│        │  ├─ dye_red_carpet.json
│        │  ├─ dye_red_harness.json
│        │  ├─ dye_red_wool.json
│        │  ├─ dye_white_bed.json
│        │  ├─ dye_white_carpet.json
│        │  ├─ dye_white_harness.json
│        │  ├─ dye_white_wool.json
│        │  ├─ dye_yellow_bed.json
│        │  ├─ dye_yellow_carpet.json
│        │  ├─ dye_yellow_harness.json
│        │  ├─ dye_yellow_wool.json
│        │  ├─ emerald.json
│        │  ├─ emerald_block.json
│        │  ├─ emerald_from_blasting_deepslate_emerald_ore.json
│        │  ├─ emerald_from_blasting_emerald_ore.json
│        │  ├─ emerald_from_smelting_deepslate_emerald_ore.json
│        │  ├─ emerald_from_smelting_emerald_ore.json
│        │  ├─ enchanting_table.json
│        │  ├─ ender_chest.json
│        │  ├─ ender_eye.json
│        │  ├─ end_crystal.json
│        │  ├─ end_rod.json
│        │  ├─ end_stone_bricks.json
│        │  ├─ end_stone_bricks_from_end_stone_stonecutting.json
│        │  ├─ end_stone_brick_slab.json
│        │  ├─ end_stone_brick_slab_from_end_stone_brick_stonecutting.json
│        │  ├─ end_stone_brick_slab_from_end_stone_stonecutting.json
│        │  ├─ end_stone_brick_stairs.json
│        │  ├─ end_stone_brick_stairs_from_end_stone_brick_stonecutting.json
│        │  ├─ end_stone_brick_stairs_from_end_stone_stonecutting.json
│        │  ├─ end_stone_brick_wall.json
│        │  ├─ end_stone_brick_wall_from_end_stone_brick_stonecutting.json
│        │  ├─ end_stone_brick_wall_from_end_stone_stonecutting.json
│        │  ├─ exposed_chiseled_copper.json
│        │  ├─ exposed_chiseled_copper_from_exposed_copper_stonecutting.json
│        │  ├─ exposed_chiseled_copper_from_exposed_cut_copper_stonecutting.json
│        │  ├─ exposed_copper_bulb.json
│        │  ├─ exposed_copper_grate.json
│        │  ├─ exposed_copper_grate_from_exposed_copper_stonecutting.json
│        │  ├─ exposed_cut_copper.json
│        │  ├─ exposed_cut_copper_from_exposed_copper_stonecutting.json
│        │  ├─ exposed_cut_copper_slab.json
│        │  ├─ exposed_cut_copper_slab_from_exposed_copper_stonecutting.json
│        │  ├─ exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting.json
│        │  ├─ exposed_cut_copper_stairs.json
│        │  ├─ exposed_cut_copper_stairs_from_exposed_copper_stonecutting.json
│        │  ├─ exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting.json
│        │  ├─ eye_armor_trim_smithing_template.json
│        │  ├─ eye_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ fermented_spider_eye.json
│        │  ├─ field_masoned_banner_pattern.json
│        │  ├─ firework_rocket.json
│        │  ├─ firework_rocket_simple.json
│        │  ├─ firework_star.json
│        │  ├─ firework_star_fade.json
│        │  ├─ fire_charge.json
│        │  ├─ fishing_rod.json
│        │  ├─ fletching_table.json
│        │  ├─ flint_and_steel.json
│        │  ├─ flower_banner_pattern.json
│        │  ├─ flower_pot.json
│        │  ├─ flow_armor_trim_smithing_template.json
│        │  ├─ flow_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ furnace.json
│        │  ├─ furnace_minecart.json
│        │  ├─ glass.json
│        │  ├─ glass_bottle.json
│        │  ├─ glass_pane.json
│        │  ├─ glistering_melon_slice.json
│        │  ├─ glowstone.json
│        │  ├─ glow_item_frame.json
│        │  ├─ golden_apple.json
│        │  ├─ golden_axe.json
│        │  ├─ golden_boots.json
│        │  ├─ golden_carrot.json
│        │  ├─ golden_chestplate.json
│        │  ├─ golden_helmet.json
│        │  ├─ golden_hoe.json
│        │  ├─ golden_leggings.json
│        │  ├─ golden_pickaxe.json
│        │  ├─ golden_shovel.json
│        │  ├─ golden_spear.json
│        │  ├─ golden_sword.json
│        │  ├─ gold_block.json
│        │  ├─ gold_ingot_from_blasting_deepslate_gold_ore.json
│        │  ├─ gold_ingot_from_blasting_gold_ore.json
│        │  ├─ gold_ingot_from_blasting_nether_gold_ore.json
│        │  ├─ gold_ingot_from_blasting_raw_gold.json
│        │  ├─ gold_ingot_from_gold_block.json
│        │  ├─ gold_ingot_from_nuggets.json
│        │  ├─ gold_ingot_from_smelting_deepslate_gold_ore.json
│        │  ├─ gold_ingot_from_smelting_gold_ore.json
│        │  ├─ gold_ingot_from_smelting_nether_gold_ore.json
│        │  ├─ gold_ingot_from_smelting_raw_gold.json
│        │  ├─ gold_nugget.json
│        │  ├─ gold_nugget_from_blasting.json
│        │  ├─ gold_nugget_from_smelting.json
│        │  ├─ granite.json
│        │  ├─ granite_slab.json
│        │  ├─ granite_slab_from_granite_stonecutting.json
│        │  ├─ granite_stairs.json
│        │  ├─ granite_stairs_from_granite_stonecutting.json
│        │  ├─ granite_wall.json
│        │  ├─ granite_wall_from_granite_stonecutting.json
│        │  ├─ gray_banner.json
│        │  ├─ gray_bed.json
│        │  ├─ gray_bundle.json
│        │  ├─ gray_candle.json
│        │  ├─ gray_carpet.json
│        │  ├─ gray_concrete_powder.json
│        │  ├─ gray_dye.json
│        │  ├─ gray_dye_from_closed_eyeblossom.json
│        │  ├─ gray_glazed_terracotta.json
│        │  ├─ gray_harness.json
│        │  ├─ gray_shulker_box.json
│        │  ├─ gray_stained_glass.json
│        │  ├─ gray_stained_glass_pane.json
│        │  ├─ gray_stained_glass_pane_from_glass_pane.json
│        │  ├─ gray_terracotta.json
│        │  ├─ green_banner.json
│        │  ├─ green_bed.json
│        │  ├─ green_bundle.json
│        │  ├─ green_candle.json
│        │  ├─ green_carpet.json
│        │  ├─ green_concrete_powder.json
│        │  ├─ green_dye.json
│        │  ├─ green_glazed_terracotta.json
│        │  ├─ green_harness.json
│        │  ├─ green_shulker_box.json
│        │  ├─ green_stained_glass.json
│        │  ├─ green_stained_glass_pane.json
│        │  ├─ green_stained_glass_pane_from_glass_pane.json
│        │  ├─ green_terracotta.json
│        │  ├─ grindstone.json
│        │  ├─ hay_block.json
│        │  ├─ heavy_weighted_pressure_plate.json
│        │  ├─ honeycomb_block.json
│        │  ├─ honey_block.json
│        │  ├─ honey_bottle.json
│        │  ├─ hopper.json
│        │  ├─ hopper_minecart.json
│        │  ├─ host_armor_trim_smithing_template.json
│        │  ├─ host_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ iron_axe.json
│        │  ├─ iron_bars.json
│        │  ├─ iron_block.json
│        │  ├─ iron_boots.json
│        │  ├─ iron_chain.json
│        │  ├─ iron_chestplate.json
│        │  ├─ iron_door.json
│        │  ├─ iron_helmet.json
│        │  ├─ iron_hoe.json
│        │  ├─ iron_ingot_from_blasting_deepslate_iron_ore.json
│        │  ├─ iron_ingot_from_blasting_iron_ore.json
│        │  ├─ iron_ingot_from_blasting_raw_iron.json
│        │  ├─ iron_ingot_from_iron_block.json
│        │  ├─ iron_ingot_from_nuggets.json
│        │  ├─ iron_ingot_from_smelting_deepslate_iron_ore.json
│        │  ├─ iron_ingot_from_smelting_iron_ore.json
│        │  ├─ iron_ingot_from_smelting_raw_iron.json
│        │  ├─ iron_leggings.json
│        │  ├─ iron_nugget.json
│        │  ├─ iron_nugget_from_blasting.json
│        │  ├─ iron_nugget_from_smelting.json
│        │  ├─ iron_pickaxe.json
│        │  ├─ iron_shovel.json
│        │  ├─ iron_spear.json
│        │  ├─ iron_sword.json
│        │  ├─ iron_trapdoor.json
│        │  ├─ item_frame.json
│        │  ├─ jack_o_lantern.json
│        │  ├─ jukebox.json
│        │  ├─ jungle_boat.json
│        │  ├─ jungle_button.json
│        │  ├─ jungle_chest_boat.json
│        │  ├─ jungle_door.json
│        │  ├─ jungle_fence.json
│        │  ├─ jungle_fence_gate.json
│        │  ├─ jungle_hanging_sign.json
│        │  ├─ jungle_planks.json
│        │  ├─ jungle_pressure_plate.json
│        │  ├─ jungle_shelf.json
│        │  ├─ jungle_sign.json
│        │  ├─ jungle_slab.json
│        │  ├─ jungle_stairs.json
│        │  ├─ jungle_trapdoor.json
│        │  ├─ jungle_wood.json
│        │  ├─ ladder.json
│        │  ├─ lantern.json
│        │  ├─ lapis_block.json
│        │  ├─ lapis_lazuli.json
│        │  ├─ lapis_lazuli_from_blasting_deepslate_lapis_ore.json
│        │  ├─ lapis_lazuli_from_blasting_lapis_ore.json
│        │  ├─ lapis_lazuli_from_smelting_deepslate_lapis_ore.json
│        │  ├─ lapis_lazuli_from_smelting_lapis_ore.json
│        │  ├─ lead.json
│        │  ├─ leaf_litter.json
│        │  ├─ leather.json
│        │  ├─ leather_boots.json
│        │  ├─ leather_chestplate.json
│        │  ├─ leather_helmet.json
│        │  ├─ leather_horse_armor.json
│        │  ├─ leather_leggings.json
│        │  ├─ lectern.json
│        │  ├─ lever.json
│        │  ├─ lightning_rod.json
│        │  ├─ light_blue_banner.json
│        │  ├─ light_blue_bed.json
│        │  ├─ light_blue_bundle.json
│        │  ├─ light_blue_candle.json
│        │  ├─ light_blue_carpet.json
│        │  ├─ light_blue_concrete_powder.json
│        │  ├─ light_blue_dye_from_blue_orchid.json
│        │  ├─ light_blue_dye_from_blue_white_dye.json
│        │  ├─ light_blue_glazed_terracotta.json
│        │  ├─ light_blue_harness.json
│        │  ├─ light_blue_shulker_box.json
│        │  ├─ light_blue_stained_glass.json
│        │  ├─ light_blue_stained_glass_pane.json
│        │  ├─ light_blue_stained_glass_pane_from_glass_pane.json
│        │  ├─ light_blue_terracotta.json
│        │  ├─ light_gray_banner.json
│        │  ├─ light_gray_bed.json
│        │  ├─ light_gray_bundle.json
│        │  ├─ light_gray_candle.json
│        │  ├─ light_gray_carpet.json
│        │  ├─ light_gray_concrete_powder.json
│        │  ├─ light_gray_dye_from_azure_bluet.json
│        │  ├─ light_gray_dye_from_black_white_dye.json
│        │  ├─ light_gray_dye_from_gray_white_dye.json
│        │  ├─ light_gray_dye_from_oxeye_daisy.json
│        │  ├─ light_gray_dye_from_white_tulip.json
│        │  ├─ light_gray_glazed_terracotta.json
│        │  ├─ light_gray_harness.json
│        │  ├─ light_gray_shulker_box.json
│        │  ├─ light_gray_stained_glass.json
│        │  ├─ light_gray_stained_glass_pane.json
│        │  ├─ light_gray_stained_glass_pane_from_glass_pane.json
│        │  ├─ light_gray_terracotta.json
│        │  ├─ light_weighted_pressure_plate.json
│        │  ├─ lime_banner.json
│        │  ├─ lime_bed.json
│        │  ├─ lime_bundle.json
│        │  ├─ lime_candle.json
│        │  ├─ lime_carpet.json
│        │  ├─ lime_concrete_powder.json
│        │  ├─ lime_dye.json
│        │  ├─ lime_dye_from_smelting.json
│        │  ├─ lime_glazed_terracotta.json
│        │  ├─ lime_harness.json
│        │  ├─ lime_shulker_box.json
│        │  ├─ lime_stained_glass.json
│        │  ├─ lime_stained_glass_pane.json
│        │  ├─ lime_stained_glass_pane_from_glass_pane.json
│        │  ├─ lime_terracotta.json
│        │  ├─ lodestone.json
│        │  ├─ loom.json
│        │  ├─ mace.json
│        │  ├─ magenta_banner.json
│        │  ├─ magenta_bed.json
│        │  ├─ magenta_bundle.json
│        │  ├─ magenta_candle.json
│        │  ├─ magenta_carpet.json
│        │  ├─ magenta_concrete_powder.json
│        │  ├─ magenta_dye_from_allium.json
│        │  ├─ magenta_dye_from_blue_red_pink.json
│        │  ├─ magenta_dye_from_blue_red_white_dye.json
│        │  ├─ magenta_dye_from_lilac.json
│        │  ├─ magenta_dye_from_purple_and_pink.json
│        │  ├─ magenta_glazed_terracotta.json
│        │  ├─ magenta_harness.json
│        │  ├─ magenta_shulker_box.json
│        │  ├─ magenta_stained_glass.json
│        │  ├─ magenta_stained_glass_pane.json
│        │  ├─ magenta_stained_glass_pane_from_glass_pane.json
│        │  ├─ magenta_terracotta.json
│        │  ├─ magma_block.json
│        │  ├─ magma_cream.json
│        │  ├─ mangrove_boat.json
│        │  ├─ mangrove_button.json
│        │  ├─ mangrove_chest_boat.json
│        │  ├─ mangrove_door.json
│        │  ├─ mangrove_fence.json
│        │  ├─ mangrove_fence_gate.json
│        │  ├─ mangrove_hanging_sign.json
│        │  ├─ mangrove_planks.json
│        │  ├─ mangrove_pressure_plate.json
│        │  ├─ mangrove_shelf.json
│        │  ├─ mangrove_sign.json
│        │  ├─ mangrove_slab.json
│        │  ├─ mangrove_stairs.json
│        │  ├─ mangrove_trapdoor.json
│        │  ├─ mangrove_wood.json
│        │  ├─ map.json
│        │  ├─ map_cloning.json
│        │  ├─ map_extending.json
│        │  ├─ melon.json
│        │  ├─ melon_seeds.json
│        │  ├─ minecart.json
│        │  ├─ mojang_banner_pattern.json
│        │  ├─ mossy_cobblestone_from_moss_block.json
│        │  ├─ mossy_cobblestone_from_vine.json
│        │  ├─ mossy_cobblestone_slab.json
│        │  ├─ mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting.json
│        │  ├─ mossy_cobblestone_stairs.json
│        │  ├─ mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting.json
│        │  ├─ mossy_cobblestone_wall.json
│        │  ├─ mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting.json
│        │  ├─ mossy_stone_bricks_from_moss_block.json
│        │  ├─ mossy_stone_bricks_from_vine.json
│        │  ├─ mossy_stone_brick_slab.json
│        │  ├─ mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting.json
│        │  ├─ mossy_stone_brick_stairs.json
│        │  ├─ mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting.json
│        │  ├─ mossy_stone_brick_wall.json
│        │  ├─ mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting.json
│        │  ├─ moss_carpet.json
│        │  ├─ muddy_mangrove_roots.json
│        │  ├─ mud_bricks.json
│        │  ├─ mud_brick_slab.json
│        │  ├─ mud_brick_slab_from_mud_bricks_stonecutting.json
│        │  ├─ mud_brick_stairs.json
│        │  ├─ mud_brick_stairs_from_mud_bricks_stonecutting.json
│        │  ├─ mud_brick_wall.json
│        │  ├─ mud_brick_wall_from_mud_bricks_stonecutting.json
│        │  ├─ mushroom_stew.json
│        │  ├─ music_disc_5.json
│        │  ├─ netherite_axe_smithing.json
│        │  ├─ netherite_block.json
│        │  ├─ netherite_boots_smithing.json
│        │  ├─ netherite_chestplate_smithing.json
│        │  ├─ netherite_helmet_smithing.json
│        │  ├─ netherite_hoe_smithing.json
│        │  ├─ netherite_horse_armor_smithing.json
│        │  ├─ netherite_ingot.json
│        │  ├─ netherite_ingot_from_netherite_block.json
│        │  ├─ netherite_leggings_smithing.json
│        │  ├─ netherite_nautilus_armor_smithing.json
│        │  ├─ netherite_pickaxe_smithing.json
│        │  ├─ netherite_scrap.json
│        │  ├─ netherite_scrap_from_blasting.json
│        │  ├─ netherite_shovel_smithing.json
│        │  ├─ netherite_spear_smithing.json
│        │  ├─ netherite_sword_smithing.json
│        │  ├─ netherite_upgrade_smithing_template.json
│        │  ├─ nether_brick.json
│        │  ├─ nether_bricks.json
│        │  ├─ nether_brick_fence.json
│        │  ├─ nether_brick_slab.json
│        │  ├─ nether_brick_slab_from_nether_bricks_stonecutting.json
│        │  ├─ nether_brick_stairs.json
│        │  ├─ nether_brick_stairs_from_nether_bricks_stonecutting.json
│        │  ├─ nether_brick_wall.json
│        │  ├─ nether_brick_wall_from_nether_bricks_stonecutting.json
│        │  ├─ nether_wart_block.json
│        │  ├─ note_block.json
│        │  ├─ oak_boat.json
│        │  ├─ oak_button.json
│        │  ├─ oak_chest_boat.json
│        │  ├─ oak_door.json
│        │  ├─ oak_fence.json
│        │  ├─ oak_fence_gate.json
│        │  ├─ oak_hanging_sign.json
│        │  ├─ oak_planks.json
│        │  ├─ oak_pressure_plate.json
│        │  ├─ oak_shelf.json
│        │  ├─ oak_sign.json
│        │  ├─ oak_slab.json
│        │  ├─ oak_stairs.json
│        │  ├─ oak_trapdoor.json
│        │  ├─ oak_wood.json
│        │  ├─ observer.json
│        │  ├─ orange_banner.json
│        │  ├─ orange_bed.json
│        │  ├─ orange_bundle.json
│        │  ├─ orange_candle.json
│        │  ├─ orange_carpet.json
│        │  ├─ orange_concrete_powder.json
│        │  ├─ orange_dye_from_open_eyeblossom.json
│        │  ├─ orange_dye_from_orange_tulip.json
│        │  ├─ orange_dye_from_red_yellow.json
│        │  ├─ orange_dye_from_torchflower.json
│        │  ├─ orange_glazed_terracotta.json
│        │  ├─ orange_harness.json
│        │  ├─ orange_shulker_box.json
│        │  ├─ orange_stained_glass.json
│        │  ├─ orange_stained_glass_pane.json
│        │  ├─ orange_stained_glass_pane_from_glass_pane.json
│        │  ├─ orange_terracotta.json
│        │  ├─ oxidized_chiseled_copper.json
│        │  ├─ oxidized_chiseled_copper_from_oxidized_copper_stonecutting.json
│        │  ├─ oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting.json
│        │  ├─ oxidized_copper_bulb.json
│        │  ├─ oxidized_copper_grate.json
│        │  ├─ oxidized_copper_grate_from_oxidized_copper_stonecutting.json
│        │  ├─ oxidized_cut_copper.json
│        │  ├─ oxidized_cut_copper_from_oxidized_copper_stonecutting.json
│        │  ├─ oxidized_cut_copper_slab.json
│        │  ├─ oxidized_cut_copper_slab_from_oxidized_copper_stonecutting.json
│        │  ├─ oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting.json
│        │  ├─ oxidized_cut_copper_stairs.json
│        │  ├─ oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting.json
│        │  ├─ oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting.json
│        │  ├─ packed_ice.json
│        │  ├─ packed_mud.json
│        │  ├─ painting.json
│        │  ├─ pale_moss_carpet.json
│        │  ├─ pale_oak_boat.json
│        │  ├─ pale_oak_button.json
│        │  ├─ pale_oak_chest_boat.json
│        │  ├─ pale_oak_door.json
│        │  ├─ pale_oak_fence.json
│        │  ├─ pale_oak_fence_gate.json
│        │  ├─ pale_oak_hanging_sign.json
│        │  ├─ pale_oak_planks.json
│        │  ├─ pale_oak_pressure_plate.json
│        │  ├─ pale_oak_shelf.json
│        │  ├─ pale_oak_sign.json
│        │  ├─ pale_oak_slab.json
│        │  ├─ pale_oak_stairs.json
│        │  ├─ pale_oak_trapdoor.json
│        │  ├─ pale_oak_wood.json
│        │  ├─ paper.json
│        │  ├─ pink_banner.json
│        │  ├─ pink_bed.json
│        │  ├─ pink_bundle.json
│        │  ├─ pink_candle.json
│        │  ├─ pink_carpet.json
│        │  ├─ pink_concrete_powder.json
│        │  ├─ pink_dye_from_cactus_flower.json
│        │  ├─ pink_dye_from_peony.json
│        │  ├─ pink_dye_from_pink_petals.json
│        │  ├─ pink_dye_from_pink_tulip.json
│        │  ├─ pink_dye_from_red_white_dye.json
│        │  ├─ pink_glazed_terracotta.json
│        │  ├─ pink_harness.json
│        │  ├─ pink_shulker_box.json
│        │  ├─ pink_stained_glass.json
│        │  ├─ pink_stained_glass_pane.json
│        │  ├─ pink_stained_glass_pane_from_glass_pane.json
│        │  ├─ pink_terracotta.json
│        │  ├─ piston.json
│        │  ├─ polished_andesite.json
│        │  ├─ polished_andesite_from_andesite_stonecutting.json
│        │  ├─ polished_andesite_slab.json
│        │  ├─ polished_andesite_slab_from_andesite_stonecutting.json
│        │  ├─ polished_andesite_slab_from_polished_andesite_stonecutting.json
│        │  ├─ polished_andesite_stairs.json
│        │  ├─ polished_andesite_stairs_from_andesite_stonecutting.json
│        │  ├─ polished_andesite_stairs_from_polished_andesite_stonecutting.json
│        │  ├─ polished_basalt.json
│        │  ├─ polished_basalt_from_basalt_stonecutting.json
│        │  ├─ polished_blackstone.json
│        │  ├─ polished_blackstone_bricks.json
│        │  ├─ polished_blackstone_bricks_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_bricks_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_brick_slab.json
│        │  ├─ polished_blackstone_brick_slab_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting.json
│        │  ├─ polished_blackstone_brick_slab_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_brick_stairs.json
│        │  ├─ polished_blackstone_brick_stairs_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting.json
│        │  ├─ polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_brick_wall.json
│        │  ├─ polished_blackstone_brick_wall_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting.json
│        │  ├─ polished_blackstone_brick_wall_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_button.json
│        │  ├─ polished_blackstone_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_pressure_plate.json
│        │  ├─ polished_blackstone_slab.json
│        │  ├─ polished_blackstone_slab_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_slab_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_stairs.json
│        │  ├─ polished_blackstone_stairs_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_stairs_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_wall.json
│        │  ├─ polished_blackstone_wall_from_blackstone_stonecutting.json
│        │  ├─ polished_blackstone_wall_from_polished_blackstone_stonecutting.json
│        │  ├─ polished_deepslate.json
│        │  ├─ polished_deepslate_from_cobbled_deepslate_stonecutting.json
│        │  ├─ polished_deepslate_slab.json
│        │  ├─ polished_deepslate_slab_from_cobbled_deepslate_stonecutting.json
│        │  ├─ polished_deepslate_slab_from_polished_deepslate_stonecutting.json
│        │  ├─ polished_deepslate_stairs.json
│        │  ├─ polished_deepslate_stairs_from_cobbled_deepslate_stonecutting.json
│        │  ├─ polished_deepslate_stairs_from_polished_deepslate_stonecutting.json
│        │  ├─ polished_deepslate_wall.json
│        │  ├─ polished_deepslate_wall_from_cobbled_deepslate_stonecutting.json
│        │  ├─ polished_deepslate_wall_from_polished_deepslate_stonecutting.json
│        │  ├─ polished_diorite.json
│        │  ├─ polished_diorite_from_diorite_stonecutting.json
│        │  ├─ polished_diorite_slab.json
│        │  ├─ polished_diorite_slab_from_diorite_stonecutting.json
│        │  ├─ polished_diorite_slab_from_polished_diorite_stonecutting.json
│        │  ├─ polished_diorite_stairs.json
│        │  ├─ polished_diorite_stairs_from_diorite_stonecutting.json
│        │  ├─ polished_diorite_stairs_from_polished_diorite_stonecutting.json
│        │  ├─ polished_granite.json
│        │  ├─ polished_granite_from_granite_stonecutting.json
│        │  ├─ polished_granite_slab.json
│        │  ├─ polished_granite_slab_from_granite_stonecutting.json
│        │  ├─ polished_granite_slab_from_polished_granite_stonecutting.json
│        │  ├─ polished_granite_stairs.json
│        │  ├─ polished_granite_stairs_from_granite_stonecutting.json
│        │  ├─ polished_granite_stairs_from_polished_granite_stonecutting.json
│        │  ├─ polished_tuff.json
│        │  ├─ polished_tuff_from_tuff_stonecutting.json
│        │  ├─ polished_tuff_slab.json
│        │  ├─ polished_tuff_slab_from_polished_tuff_stonecutting.json
│        │  ├─ polished_tuff_slab_from_tuff_stonecutting.json
│        │  ├─ polished_tuff_stairs.json
│        │  ├─ polished_tuff_stairs_from_polished_tuff_stonecutting.json
│        │  ├─ polished_tuff_stairs_from_tuff_stonecutting.json
│        │  ├─ polished_tuff_wall.json
│        │  ├─ polished_tuff_wall_from_polished_tuff_stonecutting.json
│        │  ├─ polished_tuff_wall_from_tuff_stonecutting.json
│        │  ├─ popped_chorus_fruit.json
│        │  ├─ powered_rail.json
│        │  ├─ prismarine.json
│        │  ├─ prismarine_bricks.json
│        │  ├─ prismarine_brick_slab.json
│        │  ├─ prismarine_brick_slab_from_prismarine_stonecutting.json
│        │  ├─ prismarine_brick_stairs.json
│        │  ├─ prismarine_brick_stairs_from_prismarine_stonecutting.json
│        │  ├─ prismarine_slab.json
│        │  ├─ prismarine_slab_from_prismarine_stonecutting.json
│        │  ├─ prismarine_stairs.json
│        │  ├─ prismarine_stairs_from_prismarine_stonecutting.json
│        │  ├─ prismarine_wall.json
│        │  ├─ prismarine_wall_from_prismarine_stonecutting.json
│        │  ├─ pumpkin_pie.json
│        │  ├─ pumpkin_seeds.json
│        │  ├─ purple_banner.json
│        │  ├─ purple_bed.json
│        │  ├─ purple_bundle.json
│        │  ├─ purple_candle.json
│        │  ├─ purple_carpet.json
│        │  ├─ purple_concrete_powder.json
│        │  ├─ purple_dye.json
│        │  ├─ purple_glazed_terracotta.json
│        │  ├─ purple_harness.json
│        │  ├─ purple_shulker_box.json
│        │  ├─ purple_stained_glass.json
│        │  ├─ purple_stained_glass_pane.json
│        │  ├─ purple_stained_glass_pane_from_glass_pane.json
│        │  ├─ purple_terracotta.json
│        │  ├─ purpur_block.json
│        │  ├─ purpur_pillar.json
│        │  ├─ purpur_pillar_from_purpur_block_stonecutting.json
│        │  ├─ purpur_slab.json
│        │  ├─ purpur_slab_from_purpur_block_stonecutting.json
│        │  ├─ purpur_stairs.json
│        │  ├─ purpur_stairs_from_purpur_block_stonecutting.json
│        │  ├─ quartz.json
│        │  ├─ quartz_block.json
│        │  ├─ quartz_bricks.json
│        │  ├─ quartz_bricks_from_quartz_block_stonecutting.json
│        │  ├─ quartz_from_blasting.json
│        │  ├─ quartz_pillar.json
│        │  ├─ quartz_pillar_from_quartz_block_stonecutting.json
│        │  ├─ quartz_slab.json
│        │  ├─ quartz_slab_from_stonecutting.json
│        │  ├─ quartz_stairs.json
│        │  ├─ quartz_stairs_from_quartz_block_stonecutting.json
│        │  ├─ rabbit_stew_from_brown_mushroom.json
│        │  ├─ rabbit_stew_from_red_mushroom.json
│        │  ├─ rail.json
│        │  ├─ raiser_armor_trim_smithing_template.json
│        │  ├─ raiser_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ raw_copper.json
│        │  ├─ raw_copper_block.json
│        │  ├─ raw_gold.json
│        │  ├─ raw_gold_block.json
│        │  ├─ raw_iron.json
│        │  ├─ raw_iron_block.json
│        │  ├─ recovery_compass.json
│        │  ├─ redstone.json
│        │  ├─ redstone_block.json
│        │  ├─ redstone_from_blasting_deepslate_redstone_ore.json
│        │  ├─ redstone_from_blasting_redstone_ore.json
│        │  ├─ redstone_from_smelting_deepslate_redstone_ore.json
│        │  ├─ redstone_from_smelting_redstone_ore.json
│        │  ├─ redstone_lamp.json
│        │  ├─ redstone_torch.json
│        │  ├─ red_banner.json
│        │  ├─ red_bed.json
│        │  ├─ red_bundle.json
│        │  ├─ red_candle.json
│        │  ├─ red_carpet.json
│        │  ├─ red_concrete_powder.json
│        │  ├─ red_dye_from_beetroot.json
│        │  ├─ red_dye_from_poppy.json
│        │  ├─ red_dye_from_rose_bush.json
│        │  ├─ red_dye_from_tulip.json
│        │  ├─ red_glazed_terracotta.json
│        │  ├─ red_harness.json
│        │  ├─ red_nether_bricks.json
│        │  ├─ red_nether_brick_slab.json
│        │  ├─ red_nether_brick_slab_from_red_nether_bricks_stonecutting.json
│        │  ├─ red_nether_brick_stairs.json
│        │  ├─ red_nether_brick_stairs_from_red_nether_bricks_stonecutting.json
│        │  ├─ red_nether_brick_wall.json
│        │  ├─ red_nether_brick_wall_from_red_nether_bricks_stonecutting.json
│        │  ├─ red_sandstone.json
│        │  ├─ red_sandstone_slab.json
│        │  ├─ red_sandstone_slab_from_red_sandstone_stonecutting.json
│        │  ├─ red_sandstone_stairs.json
│        │  ├─ red_sandstone_stairs_from_red_sandstone_stonecutting.json
│        │  ├─ red_sandstone_wall.json
│        │  ├─ red_sandstone_wall_from_red_sandstone_stonecutting.json
│        │  ├─ red_shulker_box.json
│        │  ├─ red_stained_glass.json
│        │  ├─ red_stained_glass_pane.json
│        │  ├─ red_stained_glass_pane_from_glass_pane.json
│        │  ├─ red_terracotta.json
│        │  ├─ repair_item.json
│        │  ├─ repeater.json
│        │  ├─ resin_block.json
│        │  ├─ resin_brick.json
│        │  ├─ resin_bricks.json
│        │  ├─ resin_brick_slab.json
│        │  ├─ resin_brick_slab_from_resin_bricks_stonecutting.json
│        │  ├─ resin_brick_stairs.json
│        │  ├─ resin_brick_stairs_from_resin_bricks_stonecutting.json
│        │  ├─ resin_brick_wall.json
│        │  ├─ resin_brick_wall_from_resin_bricks_stonecutting.json
│        │  ├─ resin_clump.json
│        │  ├─ respawn_anchor.json
│        │  ├─ rib_armor_trim_smithing_template.json
│        │  ├─ rib_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ saddle.json
│        │  ├─ sandstone.json
│        │  ├─ sandstone_slab.json
│        │  ├─ sandstone_slab_from_sandstone_stonecutting.json
│        │  ├─ sandstone_stairs.json
│        │  ├─ sandstone_stairs_from_sandstone_stonecutting.json
│        │  ├─ sandstone_wall.json
│        │  ├─ sandstone_wall_from_sandstone_stonecutting.json
│        │  ├─ scaffolding.json
│        │  ├─ sea_lantern.json
│        │  ├─ sentry_armor_trim_smithing_template.json
│        │  ├─ sentry_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ shaper_armor_trim_smithing_template.json
│        │  ├─ shaper_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ shears.json
│        │  ├─ shield.json
│        │  ├─ shield_decoration.json
│        │  ├─ shulker_box.json
│        │  ├─ silence_armor_trim_smithing_template.json
│        │  ├─ silence_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ skull_banner_pattern.json
│        │  ├─ slime_ball.json
│        │  ├─ slime_block.json
│        │  ├─ smithing_table.json
│        │  ├─ smoker.json
│        │  ├─ smooth_basalt.json
│        │  ├─ smooth_quartz.json
│        │  ├─ smooth_quartz_slab.json
│        │  ├─ smooth_quartz_slab_from_smooth_quartz_stonecutting.json
│        │  ├─ smooth_quartz_stairs.json
│        │  ├─ smooth_quartz_stairs_from_smooth_quartz_stonecutting.json
│        │  ├─ smooth_red_sandstone.json
│        │  ├─ smooth_red_sandstone_slab.json
│        │  ├─ smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting.json
│        │  ├─ smooth_red_sandstone_stairs.json
│        │  ├─ smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting.json
│        │  ├─ smooth_sandstone.json
│        │  ├─ smooth_sandstone_slab.json
│        │  ├─ smooth_sandstone_slab_from_smooth_sandstone_stonecutting.json
│        │  ├─ smooth_sandstone_stairs.json
│        │  ├─ smooth_sandstone_stairs_from_smooth_sandstone_stonecutting.json
│        │  ├─ smooth_stone.json
│        │  ├─ smooth_stone_slab.json
│        │  ├─ smooth_stone_slab_from_smooth_stone_stonecutting.json
│        │  ├─ snout_armor_trim_smithing_template.json
│        │  ├─ snout_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ snow.json
│        │  ├─ snow_block.json
│        │  ├─ soul_campfire.json
│        │  ├─ soul_lantern.json
│        │  ├─ soul_torch.json
│        │  ├─ spectral_arrow.json
│        │  ├─ spire_armor_trim_smithing_template.json
│        │  ├─ spire_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ sponge.json
│        │  ├─ spruce_boat.json
│        │  ├─ spruce_button.json
│        │  ├─ spruce_chest_boat.json
│        │  ├─ spruce_door.json
│        │  ├─ spruce_fence.json
│        │  ├─ spruce_fence_gate.json
│        │  ├─ spruce_hanging_sign.json
│        │  ├─ spruce_planks.json
│        │  ├─ spruce_pressure_plate.json
│        │  ├─ spruce_shelf.json
│        │  ├─ spruce_sign.json
│        │  ├─ spruce_slab.json
│        │  ├─ spruce_stairs.json
│        │  ├─ spruce_trapdoor.json
│        │  ├─ spruce_wood.json
│        │  ├─ spyglass.json
│        │  ├─ stick.json
│        │  ├─ sticky_piston.json
│        │  ├─ stick_from_bamboo_item.json
│        │  ├─ stone.json
│        │  ├─ stonecutter.json
│        │  ├─ stone_axe.json
│        │  ├─ stone_bricks.json
│        │  ├─ stone_bricks_from_stone_stonecutting.json
│        │  ├─ stone_brick_slab.json
│        │  ├─ stone_brick_slab_from_stone_bricks_stonecutting.json
│        │  ├─ stone_brick_slab_from_stone_stonecutting.json
│        │  ├─ stone_brick_stairs.json
│        │  ├─ stone_brick_stairs_from_stone_bricks_stonecutting.json
│        │  ├─ stone_brick_stairs_from_stone_stonecutting.json
│        │  ├─ stone_brick_wall.json
│        │  ├─ stone_brick_walls_from_stone_stonecutting.json
│        │  ├─ stone_brick_wall_from_stone_bricks_stonecutting.json
│        │  ├─ stone_button.json
│        │  ├─ stone_hoe.json
│        │  ├─ stone_pickaxe.json
│        │  ├─ stone_pressure_plate.json
│        │  ├─ stone_shovel.json
│        │  ├─ stone_slab.json
│        │  ├─ stone_slab_from_stone_stonecutting.json
│        │  ├─ stone_spear.json
│        │  ├─ stone_stairs.json
│        │  ├─ stone_stairs_from_stone_stonecutting.json
│        │  ├─ stone_sword.json
│        │  ├─ stripped_acacia_wood.json
│        │  ├─ stripped_birch_wood.json
│        │  ├─ stripped_cherry_wood.json
│        │  ├─ stripped_crimson_hyphae.json
│        │  ├─ stripped_dark_oak_wood.json
│        │  ├─ stripped_jungle_wood.json
│        │  ├─ stripped_mangrove_wood.json
│        │  ├─ stripped_oak_wood.json
│        │  ├─ stripped_pale_oak_wood.json
│        │  ├─ stripped_spruce_wood.json
│        │  ├─ stripped_warped_hyphae.json
│        │  ├─ sugar_from_honey_bottle.json
│        │  ├─ sugar_from_sugar_cane.json
│        │  ├─ suspicious_stew_from_allium.json
│        │  ├─ suspicious_stew_from_azure_bluet.json
│        │  ├─ suspicious_stew_from_blue_orchid.json
│        │  ├─ suspicious_stew_from_closed_eyeblossom.json
│        │  ├─ suspicious_stew_from_cornflower.json
│        │  ├─ suspicious_stew_from_dandelion.json
│        │  ├─ suspicious_stew_from_lily_of_the_valley.json
│        │  ├─ suspicious_stew_from_open_eyeblossom.json
│        │  ├─ suspicious_stew_from_orange_tulip.json
│        │  ├─ suspicious_stew_from_oxeye_daisy.json
│        │  ├─ suspicious_stew_from_pink_tulip.json
│        │  ├─ suspicious_stew_from_poppy.json
│        │  ├─ suspicious_stew_from_red_tulip.json
│        │  ├─ suspicious_stew_from_torchflower.json
│        │  ├─ suspicious_stew_from_white_tulip.json
│        │  ├─ suspicious_stew_from_wither_rose.json
│        │  ├─ target.json
│        │  ├─ terracotta.json
│        │  ├─ tide_armor_trim_smithing_template.json
│        │  ├─ tide_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ tinted_glass.json
│        │  ├─ tipped_arrow.json
│        │  ├─ tnt.json
│        │  ├─ tnt_minecart.json
│        │  ├─ torch.json
│        │  ├─ trapped_chest.json
│        │  ├─ tripwire_hook.json
│        │  ├─ tuff_bricks.json
│        │  ├─ tuff_bricks_from_polished_tuff_stonecutting.json
│        │  ├─ tuff_bricks_from_tuff_stonecutting.json
│        │  ├─ tuff_brick_slab.json
│        │  ├─ tuff_brick_slab_from_polished_tuff_stonecutting.json
│        │  ├─ tuff_brick_slab_from_tuff_bricks_stonecutting.json
│        │  ├─ tuff_brick_slab_from_tuff_stonecutting.json
│        │  ├─ tuff_brick_stairs.json
│        │  ├─ tuff_brick_stairs_from_polished_tuff_stonecutting.json
│        │  ├─ tuff_brick_stairs_from_tuff_bricks_stonecutting.json
│        │  ├─ tuff_brick_stairs_from_tuff_stonecutting.json
│        │  ├─ tuff_brick_wall.json
│        │  ├─ tuff_brick_wall_from_polished_tuff_stonecutting.json
│        │  ├─ tuff_brick_wall_from_tuff_bricks_stonecutting.json
│        │  ├─ tuff_brick_wall_from_tuff_stonecutting.json
│        │  ├─ tuff_slab.json
│        │  ├─ tuff_slab_from_tuff_stonecutting.json
│        │  ├─ tuff_stairs.json
│        │  ├─ tuff_stairs_from_tuff_stonecutting.json
│        │  ├─ tuff_wall.json
│        │  ├─ tuff_wall_from_tuff_stonecutting.json
│        │  ├─ turtle_helmet.json
│        │  ├─ vex_armor_trim_smithing_template.json
│        │  ├─ vex_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ ward_armor_trim_smithing_template.json
│        │  ├─ ward_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ warped_button.json
│        │  ├─ warped_door.json
│        │  ├─ warped_fence.json
│        │  ├─ warped_fence_gate.json
│        │  ├─ warped_fungus_on_a_stick.json
│        │  ├─ warped_hanging_sign.json
│        │  ├─ warped_hyphae.json
│        │  ├─ warped_planks.json
│        │  ├─ warped_pressure_plate.json
│        │  ├─ warped_shelf.json
│        │  ├─ warped_sign.json
│        │  ├─ warped_slab.json
│        │  ├─ warped_stairs.json
│        │  ├─ warped_trapdoor.json
│        │  ├─ waxed_chiseled_copper.json
│        │  ├─ waxed_chiseled_copper_from_honeycomb.json
│        │  ├─ waxed_chiseled_copper_from_waxed_copper_block_stonecutting.json
│        │  ├─ waxed_chiseled_copper_from_waxed_cut_copper_stonecutting.json
│        │  ├─ waxed_copper_bars_from_honeycomb.json
│        │  ├─ waxed_copper_block_from_honeycomb.json
│        │  ├─ waxed_copper_bulb.json
│        │  ├─ waxed_copper_bulb_from_honeycomb.json
│        │  ├─ waxed_copper_chain_from_honeycomb.json
│        │  ├─ waxed_copper_chest_from_honeycomb.json
│        │  ├─ waxed_copper_door_from_honeycomb.json
│        │  ├─ waxed_copper_golem_statue_from_honeycomb.json
│        │  ├─ waxed_copper_grate.json
│        │  ├─ waxed_copper_grate_from_honeycomb.json
│        │  ├─ waxed_copper_grate_from_waxed_copper_block_stonecutting.json
│        │  ├─ waxed_copper_lantern_from_honeycomb.json
│        │  ├─ waxed_copper_trapdoor_from_honeycomb.json
│        │  ├─ waxed_cut_copper.json
│        │  ├─ waxed_cut_copper_from_honeycomb.json
│        │  ├─ waxed_cut_copper_from_waxed_copper_block_stonecutting.json
│        │  ├─ waxed_cut_copper_slab.json
│        │  ├─ waxed_cut_copper_slab_from_honeycomb.json
│        │  ├─ waxed_cut_copper_slab_from_waxed_copper_block_stonecutting.json
│        │  ├─ waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting.json
│        │  ├─ waxed_cut_copper_stairs.json
│        │  ├─ waxed_cut_copper_stairs_from_honeycomb.json
│        │  ├─ waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting.json
│        │  ├─ waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting.json
│        │  ├─ waxed_exposed_chiseled_copper.json
│        │  ├─ waxed_exposed_chiseled_copper_from_honeycomb.json
│        │  ├─ waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting.json
│        │  ├─ waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting.json
│        │  ├─ waxed_exposed_copper_bars_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_bulb.json
│        │  ├─ waxed_exposed_copper_bulb_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_chain_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_chest_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_door_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_golem_statue_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_grate.json
│        │  ├─ waxed_exposed_copper_grate_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting.json
│        │  ├─ waxed_exposed_copper_lantern_from_honeycomb.json
│        │  ├─ waxed_exposed_copper_trapdoor_from_honeycomb.json
│        │  ├─ waxed_exposed_cut_copper.json
│        │  ├─ waxed_exposed_cut_copper_from_honeycomb.json
│        │  ├─ waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting.json
│        │  ├─ waxed_exposed_cut_copper_slab.json
│        │  ├─ waxed_exposed_cut_copper_slab_from_honeycomb.json
│        │  ├─ waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting.json
│        │  ├─ waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting.json
│        │  ├─ waxed_exposed_cut_copper_stairs.json
│        │  ├─ waxed_exposed_cut_copper_stairs_from_honeycomb.json
│        │  ├─ waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting.json
│        │  ├─ waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting.json
│        │  ├─ waxed_exposed_lightning_rod_from_honeycomb.json
│        │  ├─ waxed_lightning_rod_from_honeycomb.json
│        │  ├─ waxed_oxidized_chiseled_copper.json
│        │  ├─ waxed_oxidized_chiseled_copper_from_honeycomb.json
│        │  ├─ waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting.json
│        │  ├─ waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting.json
│        │  ├─ waxed_oxidized_copper_bars_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_bulb.json
│        │  ├─ waxed_oxidized_copper_bulb_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_chain_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_chest_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_door_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_golem_statue_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_grate.json
│        │  ├─ waxed_oxidized_copper_grate_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting.json
│        │  ├─ waxed_oxidized_copper_lantern_from_honeycomb.json
│        │  ├─ waxed_oxidized_copper_trapdoor_from_honeycomb.json
│        │  ├─ waxed_oxidized_cut_copper.json
│        │  ├─ waxed_oxidized_cut_copper_from_honeycomb.json
│        │  ├─ waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting.json
│        │  ├─ waxed_oxidized_cut_copper_slab.json
│        │  ├─ waxed_oxidized_cut_copper_slab_from_honeycomb.json
│        │  ├─ waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting.json
│        │  ├─ waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting.json
│        │  ├─ waxed_oxidized_cut_copper_stairs.json
│        │  ├─ waxed_oxidized_cut_copper_stairs_from_honeycomb.json
│        │  ├─ waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting.json
│        │  ├─ waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting.json
│        │  ├─ waxed_oxidized_lightning_rod_from_honeycomb.json
│        │  ├─ waxed_weathered_chiseled_copper.json
│        │  ├─ waxed_weathered_chiseled_copper_from_honeycomb.json
│        │  ├─ waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting.json
│        │  ├─ waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting.json
│        │  ├─ waxed_weathered_copper_bars_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_bulb.json
│        │  ├─ waxed_weathered_copper_bulb_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_chain_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_chest_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_door_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_golem_statue_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_grate.json
│        │  ├─ waxed_weathered_copper_grate_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting.json
│        │  ├─ waxed_weathered_copper_lantern_from_honeycomb.json
│        │  ├─ waxed_weathered_copper_trapdoor_from_honeycomb.json
│        │  ├─ waxed_weathered_cut_copper.json
│        │  ├─ waxed_weathered_cut_copper_from_honeycomb.json
│        │  ├─ waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting.json
│        │  ├─ waxed_weathered_cut_copper_slab.json
│        │  ├─ waxed_weathered_cut_copper_slab_from_honeycomb.json
│        │  ├─ waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting.json
│        │  ├─ waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting.json
│        │  ├─ waxed_weathered_cut_copper_stairs.json
│        │  ├─ waxed_weathered_cut_copper_stairs_from_honeycomb.json
│        │  ├─ waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting.json
│        │  ├─ waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting.json
│        │  ├─ waxed_weathered_lightning_rod_from_honeycomb.json
│        │  ├─ wayfinder_armor_trim_smithing_template.json
│        │  ├─ wayfinder_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ weathered_chiseled_copper.json
│        │  ├─ weathered_chiseled_copper_from_weathered_copper_stonecutting.json
│        │  ├─ weathered_chiseled_copper_from_weathered_cut_copper_stonecutting.json
│        │  ├─ weathered_copper_bulb.json
│        │  ├─ weathered_copper_grate.json
│        │  ├─ weathered_copper_grate_from_weathered_copper_stonecutting.json
│        │  ├─ weathered_cut_copper.json
│        │  ├─ weathered_cut_copper_from_weathered_copper_stonecutting.json
│        │  ├─ weathered_cut_copper_slab.json
│        │  ├─ weathered_cut_copper_slab_from_weathered_copper_stonecutting.json
│        │  ├─ weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting.json
│        │  ├─ weathered_cut_copper_stairs.json
│        │  ├─ weathered_cut_copper_stairs_from_weathered_copper_stonecutting.json
│        │  ├─ weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting.json
│        │  ├─ wheat.json
│        │  ├─ white_banner.json
│        │  ├─ white_bed.json
│        │  ├─ white_bundle.json
│        │  ├─ white_candle.json
│        │  ├─ white_carpet.json
│        │  ├─ white_concrete_powder.json
│        │  ├─ white_dye.json
│        │  ├─ white_dye_from_lily_of_the_valley.json
│        │  ├─ white_glazed_terracotta.json
│        │  ├─ white_harness.json
│        │  ├─ white_shulker_box.json
│        │  ├─ white_stained_glass.json
│        │  ├─ white_stained_glass_pane.json
│        │  ├─ white_stained_glass_pane_from_glass_pane.json
│        │  ├─ white_terracotta.json
│        │  ├─ white_wool_from_string.json
│        │  ├─ wild_armor_trim_smithing_template.json
│        │  ├─ wild_armor_trim_smithing_template_smithing_trim.json
│        │  ├─ wind_charge.json
│        │  ├─ wolf_armor.json
│        │  ├─ wooden_axe.json
│        │  ├─ wooden_hoe.json
│        │  ├─ wooden_pickaxe.json
│        │  ├─ wooden_shovel.json
│        │  ├─ wooden_spear.json
│        │  ├─ wooden_sword.json
│        │  ├─ writable_book.json
│        │  ├─ yellow_banner.json
│        │  ├─ yellow_bed.json
│        │  ├─ yellow_bundle.json
│        │  ├─ yellow_candle.json
│        │  ├─ yellow_carpet.json
│        │  ├─ yellow_concrete_powder.json
│        │  ├─ yellow_dye_from_dandelion.json
│        │  ├─ yellow_dye_from_sunflower.json
│        │  ├─ yellow_dye_from_wildflowers.json
│        │  ├─ yellow_glazed_terracotta.json
│        │  ├─ yellow_harness.json
│        │  ├─ yellow_shulker_box.json
│        │  ├─ yellow_stained_glass.json
│        │  ├─ yellow_stained_glass_pane.json
│        │  ├─ yellow_stained_glass_pane_from_glass_pane.json
│        │  └─ yellow_terracotta.json
│        ├─ structure
│        │  ├─ ancient_city
│        │  │  ├─ city
│        │  │  │  └─ entrance
│        │  │  │     ├─ entrance_connector.nbt
│        │  │  │     ├─ entrance_path_1.nbt
│        │  │  │     ├─ entrance_path_2.nbt
│        │  │  │     ├─ entrance_path_3.nbt
│        │  │  │     ├─ entrance_path_4.nbt
│        │  │  │     └─ entrance_path_5.nbt
│        │  │  ├─ city_center
│        │  │  │  ├─ city_center_1.nbt
│        │  │  │  ├─ city_center_2.nbt
│        │  │  │  ├─ city_center_3.nbt
│        │  │  │  └─ walls
│        │  │  │     ├─ bottom_1.nbt
│        │  │  │     ├─ bottom_2.nbt
│        │  │  │     ├─ bottom_left_corner.nbt
│        │  │  │     ├─ bottom_right_corner.nbt
│        │  │  │     ├─ bottom_right_corner_1.nbt
│        │  │  │     ├─ bottom_right_corner_2.nbt
│        │  │  │     ├─ left.nbt
│        │  │  │     ├─ right.nbt
│        │  │  │     ├─ top.nbt
│        │  │  │     ├─ top_left_corner.nbt
│        │  │  │     └─ top_right_corner.nbt
│        │  │  ├─ structures
│        │  │  │  ├─ barracks.nbt
│        │  │  │  ├─ camp_1.nbt
│        │  │  │  ├─ camp_2.nbt
│        │  │  │  ├─ camp_3.nbt
│        │  │  │  ├─ chamber_1.nbt
│        │  │  │  ├─ chamber_2.nbt
│        │  │  │  ├─ chamber_3.nbt
│        │  │  │  ├─ ice_box_1.nbt
│        │  │  │  ├─ large_pillar_1.nbt
│        │  │  │  ├─ large_ruin_1.nbt
│        │  │  │  ├─ medium_pillar_1.nbt
│        │  │  │  ├─ medium_ruin_1.nbt
│        │  │  │  ├─ medium_ruin_2.nbt
│        │  │  │  ├─ sauna_1.nbt
│        │  │  │  ├─ small_ruin_1.nbt
│        │  │  │  ├─ small_ruin_2.nbt
│        │  │  │  ├─ small_statue.nbt
│        │  │  │  ├─ tall_ruin_1.nbt
│        │  │  │  ├─ tall_ruin_2.nbt
│        │  │  │  ├─ tall_ruin_3.nbt
│        │  │  │  └─ tall_ruin_4.nbt
│        │  │  └─ walls
│        │  │     ├─ intact_corner_wall_1.nbt
│        │  │     ├─ intact_horizontal_wall_1.nbt
│        │  │     ├─ intact_horizontal_wall_2.nbt
│        │  │     ├─ intact_horizontal_wall_bridge.nbt
│        │  │     ├─ intact_horizontal_wall_passage_1.nbt
│        │  │     ├─ intact_horizontal_wall_stairs_1.nbt
│        │  │     ├─ intact_horizontal_wall_stairs_2.nbt
│        │  │     ├─ intact_horizontal_wall_stairs_3.nbt
│        │  │     ├─ intact_horizontal_wall_stairs_4.nbt
│        │  │     ├─ intact_intersection_wall_1.nbt
│        │  │     ├─ intact_lshape_wall_1.nbt
│        │  │     ├─ ruined_corner_wall_1.nbt
│        │  │     ├─ ruined_corner_wall_2.nbt
│        │  │     ├─ ruined_horizontal_wall_stairs_1.nbt
│        │  │     ├─ ruined_horizontal_wall_stairs_2.nbt
│        │  │     ├─ ruined_horizontal_wall_stairs_3.nbt
│        │  │     └─ ruined_horizontal_wall_stairs_4.nbt
│        │  ├─ bastion
│        │  │  ├─ blocks
│        │  │  │  ├─ air.nbt
│        │  │  │  └─ gold.nbt
│        │  │  ├─ bridge
│        │  │  │  ├─ bridge_pieces
│        │  │  │  │  └─ bridge.nbt
│        │  │  │  ├─ connectors
│        │  │  │  │  ├─ back_bridge_bottom.nbt
│        │  │  │  │  └─ back_bridge_top.nbt
│        │  │  │  ├─ legs
│        │  │  │  │  ├─ leg_0.nbt
│        │  │  │  │  └─ leg_1.nbt
│        │  │  │  ├─ ramparts
│        │  │  │  │  ├─ rampart_0.nbt
│        │  │  │  │  └─ rampart_1.nbt
│        │  │  │  ├─ rampart_plates
│        │  │  │  │  └─ plate_0.nbt
│        │  │  │  ├─ starting_pieces
│        │  │  │  │  ├─ entrance.nbt
│        │  │  │  │  ├─ entrance_base.nbt
│        │  │  │  │  └─ entrance_face.nbt
│        │  │  │  └─ walls
│        │  │  │     ├─ wall_base_0.nbt
│        │  │  │     └─ wall_base_1.nbt
│        │  │  ├─ hoglin_stable
│        │  │  │  ├─ air_base.nbt
│        │  │  │  ├─ connectors
│        │  │  │  │  └─ end_post_connector.nbt
│        │  │  │  ├─ large_stables
│        │  │  │  │  ├─ inner_0.nbt
│        │  │  │  │  ├─ inner_1.nbt
│        │  │  │  │  ├─ inner_2.nbt
│        │  │  │  │  ├─ inner_3.nbt
│        │  │  │  │  ├─ inner_4.nbt
│        │  │  │  │  ├─ outer_0.nbt
│        │  │  │  │  ├─ outer_1.nbt
│        │  │  │  │  ├─ outer_2.nbt
│        │  │  │  │  ├─ outer_3.nbt
│        │  │  │  │  └─ outer_4.nbt
│        │  │  │  ├─ posts
│        │  │  │  │  ├─ end_post.nbt
│        │  │  │  │  └─ stair_post.nbt
│        │  │  │  ├─ ramparts
│        │  │  │  │  ├─ ramparts_1.nbt
│        │  │  │  │  ├─ ramparts_2.nbt
│        │  │  │  │  └─ ramparts_3.nbt
│        │  │  │  ├─ rampart_plates
│        │  │  │  │  └─ rampart_plate_1.nbt
│        │  │  │  ├─ small_stables
│        │  │  │  │  ├─ inner_0.nbt
│        │  │  │  │  ├─ inner_1.nbt
│        │  │  │  │  ├─ inner_2.nbt
│        │  │  │  │  ├─ inner_3.nbt
│        │  │  │  │  ├─ outer_0.nbt
│        │  │  │  │  ├─ outer_1.nbt
│        │  │  │  │  ├─ outer_2.nbt
│        │  │  │  │  └─ outer_3.nbt
│        │  │  │  ├─ stairs
│        │  │  │  │  ├─ stairs_1_0.nbt
│        │  │  │  │  ├─ stairs_1_1.nbt
│        │  │  │  │  ├─ stairs_1_2.nbt
│        │  │  │  │  ├─ stairs_1_3.nbt
│        │  │  │  │  ├─ stairs_1_4.nbt
│        │  │  │  │  ├─ stairs_2_0.nbt
│        │  │  │  │  ├─ stairs_2_1.nbt
│        │  │  │  │  ├─ stairs_2_2.nbt
│        │  │  │  │  ├─ stairs_2_3.nbt
│        │  │  │  │  ├─ stairs_2_4.nbt
│        │  │  │  │  ├─ stairs_3_0.nbt
│        │  │  │  │  ├─ stairs_3_1.nbt
│        │  │  │  │  ├─ stairs_3_2.nbt
│        │  │  │  │  ├─ stairs_3_3.nbt
│        │  │  │  │  └─ stairs_3_4.nbt
│        │  │  │  ├─ starting_pieces
│        │  │  │  │  ├─ stairs_0_mirrored.nbt
│        │  │  │  │  ├─ stairs_1_mirrored.nbt
│        │  │  │  │  ├─ stairs_2_mirrored.nbt
│        │  │  │  │  ├─ stairs_3_mirrored.nbt
│        │  │  │  │  ├─ stairs_4_mirrored.nbt
│        │  │  │  │  ├─ starting_stairs_0.nbt
│        │  │  │  │  ├─ starting_stairs_1.nbt
│        │  │  │  │  ├─ starting_stairs_2.nbt
│        │  │  │  │  ├─ starting_stairs_3.nbt
│        │  │  │  │  └─ starting_stairs_4.nbt
│        │  │  │  └─ walls
│        │  │  │     ├─ side_wall_0.nbt
│        │  │  │     ├─ side_wall_1.nbt
│        │  │  │     └─ wall_base.nbt
│        │  │  ├─ mobs
│        │  │  │  ├─ crossbow_piglin.nbt
│        │  │  │  ├─ empty.nbt
│        │  │  │  ├─ hoglin.nbt
│        │  │  │  ├─ melee_piglin.nbt
│        │  │  │  ├─ melee_piglin_always.nbt
│        │  │  │  └─ sword_piglin.nbt
│        │  │  ├─ treasure
│        │  │  │  ├─ bases
│        │  │  │  │  ├─ centers
│        │  │  │  │  │  ├─ center_0.nbt
│        │  │  │  │  │  ├─ center_1.nbt
│        │  │  │  │  │  ├─ center_2.nbt
│        │  │  │  │  │  └─ center_3.nbt
│        │  │  │  │  └─ lava_basin.nbt
│        │  │  │  ├─ big_air_full.nbt
│        │  │  │  ├─ brains
│        │  │  │  │  └─ center_brain.nbt
│        │  │  │  ├─ connectors
│        │  │  │  │  ├─ center_to_wall_middle.nbt
│        │  │  │  │  ├─ center_to_wall_top.nbt
│        │  │  │  │  └─ center_to_wall_top_entrance.nbt
│        │  │  │  ├─ corners
│        │  │  │  │  ├─ bottom
│        │  │  │  │  │  ├─ corner_0.nbt
│        │  │  │  │  │  └─ corner_1.nbt
│        │  │  │  │  ├─ edges
│        │  │  │  │  │  ├─ bottom.nbt
│        │  │  │  │  │  ├─ middle.nbt
│        │  │  │  │  │  └─ top.nbt
│        │  │  │  │  ├─ middle
│        │  │  │  │  │  ├─ corner_0.nbt
│        │  │  │  │  │  └─ corner_1.nbt
│        │  │  │  │  └─ top
│        │  │  │  │     ├─ corner_0.nbt
│        │  │  │  │     └─ corner_1.nbt
│        │  │  │  ├─ entrances
│        │  │  │  │  └─ entrance_0.nbt
│        │  │  │  ├─ extensions
│        │  │  │  │  ├─ empty.nbt
│        │  │  │  │  ├─ fire_room.nbt
│        │  │  │  │  ├─ house_0.nbt
│        │  │  │  │  ├─ house_1.nbt
│        │  │  │  │  ├─ large_bridge_0.nbt
│        │  │  │  │  ├─ large_bridge_1.nbt
│        │  │  │  │  ├─ large_bridge_2.nbt
│        │  │  │  │  ├─ large_bridge_3.nbt
│        │  │  │  │  ├─ roofed_bridge.nbt
│        │  │  │  │  ├─ small_bridge_0.nbt
│        │  │  │  │  ├─ small_bridge_1.nbt
│        │  │  │  │  ├─ small_bridge_2.nbt
│        │  │  │  │  └─ small_bridge_3.nbt
│        │  │  │  ├─ ramparts
│        │  │  │  │  ├─ bottom_wall_0.nbt
│        │  │  │  │  ├─ lava_basin_main.nbt
│        │  │  │  │  ├─ lava_basin_side.nbt
│        │  │  │  │  ├─ mid_wall_main.nbt
│        │  │  │  │  ├─ mid_wall_side.nbt
│        │  │  │  │  └─ top_wall.nbt
│        │  │  │  ├─ roofs
│        │  │  │  │  ├─ center_roof.nbt
│        │  │  │  │  ├─ corner_roof.nbt
│        │  │  │  │  └─ wall_roof.nbt
│        │  │  │  ├─ stairs
│        │  │  │  │  └─ lower_stairs.nbt
│        │  │  │  └─ walls
│        │  │  │     ├─ bottom
│        │  │  │     │  ├─ wall_0.nbt
│        │  │  │     │  ├─ wall_1.nbt
│        │  │  │     │  ├─ wall_2.nbt
│        │  │  │     │  └─ wall_3.nbt
│        │  │  │     ├─ entrance_wall.nbt
│        │  │  │     ├─ lava_wall.nbt
│        │  │  │     ├─ mid
│        │  │  │     │  ├─ wall_0.nbt
│        │  │  │     │  ├─ wall_1.nbt
│        │  │  │     │  └─ wall_2.nbt
│        │  │  │     ├─ outer
│        │  │  │     │  ├─ bottom_corner.nbt
│        │  │  │     │  ├─ medium_outer_wall.nbt
│        │  │  │     │  ├─ mid_corner.nbt
│        │  │  │     │  ├─ outer_wall.nbt
│        │  │  │     │  ├─ tall_outer_wall.nbt
│        │  │  │     │  └─ top_corner.nbt
│        │  │  │     └─ top
│        │  │  │        ├─ main_entrance.nbt
│        │  │  │        ├─ wall_0.nbt
│        │  │  │        └─ wall_1.nbt
│        │  │  └─ units
│        │  │     ├─ air_base.nbt
│        │  │     ├─ center_pieces
│        │  │     │  ├─ center_0.nbt
│        │  │     │  ├─ center_1.nbt
│        │  │     │  └─ center_2.nbt
│        │  │     ├─ edges
│        │  │     │  └─ edge_0.nbt
│        │  │     ├─ fillers
│        │  │     │  └─ stage_0.nbt
│        │  │     ├─ pathways
│        │  │     │  ├─ pathway_0.nbt
│        │  │     │  └─ pathway_wall_0.nbt
│        │  │     ├─ ramparts
│        │  │     │  ├─ ramparts_0.nbt
│        │  │     │  ├─ ramparts_1.nbt
│        │  │     │  └─ ramparts_2.nbt
│        │  │     ├─ rampart_plates
│        │  │     │  └─ plate_0.nbt
│        │  │     ├─ stages
│        │  │     │  ├─ rot
│        │  │     │  │  └─ stage_1_0.nbt
│        │  │     │  ├─ stage_0_0.nbt
│        │  │     │  ├─ stage_0_1.nbt
│        │  │     │  ├─ stage_0_2.nbt
│        │  │     │  ├─ stage_0_3.nbt
│        │  │     │  ├─ stage_1_0.nbt
│        │  │     │  ├─ stage_1_1.nbt
│        │  │     │  ├─ stage_1_2.nbt
│        │  │     │  ├─ stage_1_3.nbt
│        │  │     │  ├─ stage_2_0.nbt
│        │  │     │  ├─ stage_2_1.nbt
│        │  │     │  ├─ stage_3_0.nbt
│        │  │     │  ├─ stage_3_1.nbt
│        │  │     │  ├─ stage_3_2.nbt
│        │  │     │  └─ stage_3_3.nbt
│        │  │     ├─ walls
│        │  │     │  ├─ connected_wall.nbt
│        │  │     │  └─ wall_base.nbt
│        │  │     └─ wall_units
│        │  │        ├─ edge_0_large.nbt
│        │  │        └─ unit_0.nbt
│        │  ├─ empty.nbt
│        │  ├─ end_city
│        │  │  ├─ base_floor.nbt
│        │  │  ├─ base_roof.nbt
│        │  │  ├─ bridge_end.nbt
│        │  │  ├─ bridge_gentle_stairs.nbt
│        │  │  ├─ bridge_piece.nbt
│        │  │  ├─ bridge_steep_stairs.nbt
│        │  │  ├─ fat_tower_base.nbt
│        │  │  ├─ fat_tower_middle.nbt
│        │  │  ├─ fat_tower_top.nbt
│        │  │  ├─ second_floor_1.nbt
│        │  │  ├─ second_floor_2.nbt
│        │  │  ├─ second_roof.nbt
│        │  │  ├─ ship.nbt
│        │  │  ├─ third_floor_1.nbt
│        │  │  ├─ third_floor_2.nbt
│        │  │  ├─ third_roof.nbt
│        │  │  ├─ tower_base.nbt
│        │  │  ├─ tower_floor.nbt
│        │  │  ├─ tower_piece.nbt
│        │  │  └─ tower_top.nbt
│        │  ├─ fossil
│        │  │  ├─ skull_1.nbt
│        │  │  ├─ skull_1_coal.nbt
│        │  │  ├─ skull_2.nbt
│        │  │  ├─ skull_2_coal.nbt
│        │  │  ├─ skull_3.nbt
│        │  │  ├─ skull_3_coal.nbt
│        │  │  ├─ skull_4.nbt
│        │  │  ├─ skull_4_coal.nbt
│        │  │  ├─ spine_1.nbt
│        │  │  ├─ spine_1_coal.nbt
│        │  │  ├─ spine_2.nbt
│        │  │  ├─ spine_2_coal.nbt
│        │  │  ├─ spine_3.nbt
│        │  │  ├─ spine_3_coal.nbt
│        │  │  ├─ spine_4.nbt
│        │  │  └─ spine_4_coal.nbt
│        │  ├─ igloo
│        │  │  ├─ bottom.nbt
│        │  │  ├─ middle.nbt
│        │  │  └─ top.nbt
│        │  ├─ nether_fossils
│        │  │  ├─ fossil_1.nbt
│        │  │  ├─ fossil_10.nbt
│        │  │  ├─ fossil_11.nbt
│        │  │  ├─ fossil_12.nbt
│        │  │  ├─ fossil_13.nbt
│        │  │  ├─ fossil_14.nbt
│        │  │  ├─ fossil_2.nbt
│        │  │  ├─ fossil_3.nbt
│        │  │  ├─ fossil_4.nbt
│        │  │  ├─ fossil_5.nbt
│        │  │  ├─ fossil_6.nbt
│        │  │  ├─ fossil_7.nbt
│        │  │  ├─ fossil_8.nbt
│        │  │  └─ fossil_9.nbt
│        │  ├─ pillager_outpost
│        │  │  ├─ base_plate.nbt
│        │  │  ├─ feature_cage1.nbt
│        │  │  ├─ feature_cage2.nbt
│        │  │  ├─ feature_cage_with_allays.nbt
│        │  │  ├─ feature_logs.nbt
│        │  │  ├─ feature_plate.nbt
│        │  │  ├─ feature_targets.nbt
│        │  │  ├─ feature_tent1.nbt
│        │  │  ├─ feature_tent2.nbt
│        │  │  ├─ watchtower.nbt
│        │  │  └─ watchtower_overgrown.nbt
│        │  ├─ ruined_portal
│        │  │  ├─ giant_portal_1.nbt
│        │  │  ├─ giant_portal_2.nbt
│        │  │  ├─ giant_portal_3.nbt
│        │  │  ├─ portal_1.nbt
│        │  │  ├─ portal_10.nbt
│        │  │  ├─ portal_2.nbt
│        │  │  ├─ portal_3.nbt
│        │  │  ├─ portal_4.nbt
│        │  │  ├─ portal_5.nbt
│        │  │  ├─ portal_6.nbt
│        │  │  ├─ portal_7.nbt
│        │  │  ├─ portal_8.nbt
│        │  │  └─ portal_9.nbt
│        │  ├─ shipwreck
│        │  │  ├─ rightsideup_backhalf.nbt
│        │  │  ├─ rightsideup_backhalf_degraded.nbt
│        │  │  ├─ rightsideup_fronthalf.nbt
│        │  │  ├─ rightsideup_fronthalf_degraded.nbt
│        │  │  ├─ rightsideup_full.nbt
│        │  │  ├─ rightsideup_full_degraded.nbt
│        │  │  ├─ sideways_backhalf.nbt
│        │  │  ├─ sideways_backhalf_degraded.nbt
│        │  │  ├─ sideways_fronthalf.nbt
│        │  │  ├─ sideways_fronthalf_degraded.nbt
│        │  │  ├─ sideways_full.nbt
│        │  │  ├─ sideways_full_degraded.nbt
│        │  │  ├─ upsidedown_backhalf.nbt
│        │  │  ├─ upsidedown_backhalf_degraded.nbt
│        │  │  ├─ upsidedown_fronthalf.nbt
│        │  │  ├─ upsidedown_fronthalf_degraded.nbt
│        │  │  ├─ upsidedown_full.nbt
│        │  │  ├─ upsidedown_full_degraded.nbt
│        │  │  ├─ with_mast.nbt
│        │  │  └─ with_mast_degraded.nbt
│        │  ├─ trail_ruins
│        │  │  ├─ buildings
│        │  │  │  ├─ group_full_1.nbt
│        │  │  │  ├─ group_full_2.nbt
│        │  │  │  ├─ group_full_3.nbt
│        │  │  │  ├─ group_full_4.nbt
│        │  │  │  ├─ group_full_5.nbt
│        │  │  │  ├─ group_hall_1.nbt
│        │  │  │  ├─ group_hall_2.nbt
│        │  │  │  ├─ group_hall_3.nbt
│        │  │  │  ├─ group_hall_4.nbt
│        │  │  │  ├─ group_hall_5.nbt
│        │  │  │  ├─ group_lower_1.nbt
│        │  │  │  ├─ group_lower_2.nbt
│        │  │  │  ├─ group_lower_3.nbt
│        │  │  │  ├─ group_lower_4.nbt
│        │  │  │  ├─ group_lower_5.nbt
│        │  │  │  ├─ group_room_1.nbt
│        │  │  │  ├─ group_room_2.nbt
│        │  │  │  ├─ group_room_3.nbt
│        │  │  │  ├─ group_room_4.nbt
│        │  │  │  ├─ group_room_5.nbt
│        │  │  │  ├─ group_upper_1.nbt
│        │  │  │  ├─ group_upper_2.nbt
│        │  │  │  ├─ group_upper_3.nbt
│        │  │  │  ├─ group_upper_4.nbt
│        │  │  │  ├─ group_upper_5.nbt
│        │  │  │  ├─ large_room_1.nbt
│        │  │  │  ├─ large_room_2.nbt
│        │  │  │  ├─ large_room_3.nbt
│        │  │  │  ├─ large_room_4.nbt
│        │  │  │  ├─ large_room_5.nbt
│        │  │  │  ├─ one_room_1.nbt
│        │  │  │  ├─ one_room_2.nbt
│        │  │  │  ├─ one_room_3.nbt
│        │  │  │  ├─ one_room_4.nbt
│        │  │  │  └─ one_room_5.nbt
│        │  │  ├─ decor
│        │  │  │  ├─ decor_1.nbt
│        │  │  │  ├─ decor_2.nbt
│        │  │  │  ├─ decor_3.nbt
│        │  │  │  ├─ decor_4.nbt
│        │  │  │  ├─ decor_5.nbt
│        │  │  │  ├─ decor_6.nbt
│        │  │  │  └─ decor_7.nbt
│        │  │  ├─ roads
│        │  │  │  ├─ long_road_end.nbt
│        │  │  │  ├─ road_end_1.nbt
│        │  │  │  ├─ road_section_1.nbt
│        │  │  │  ├─ road_section_2.nbt
│        │  │  │  ├─ road_section_3.nbt
│        │  │  │  ├─ road_section_4.nbt
│        │  │  │  └─ road_spacer_1.nbt
│        │  │  └─ tower
│        │  │     ├─ hall_1.nbt
│        │  │     ├─ hall_2.nbt
│        │  │     ├─ hall_3.nbt
│        │  │     ├─ hall_4.nbt
│        │  │     ├─ hall_5.nbt
│        │  │     ├─ large_hall_1.nbt
│        │  │     ├─ large_hall_2.nbt
│        │  │     ├─ large_hall_3.nbt
│        │  │     ├─ large_hall_4.nbt
│        │  │     ├─ large_hall_5.nbt
│        │  │     ├─ one_room_1.nbt
│        │  │     ├─ one_room_2.nbt
│        │  │     ├─ one_room_3.nbt
│        │  │     ├─ one_room_4.nbt
│        │  │     ├─ one_room_5.nbt
│        │  │     ├─ platform_1.nbt
│        │  │     ├─ platform_2.nbt
│        │  │     ├─ platform_3.nbt
│        │  │     ├─ platform_4.nbt
│        │  │     ├─ platform_5.nbt
│        │  │     ├─ stable_1.nbt
│        │  │     ├─ stable_2.nbt
│        │  │     ├─ stable_3.nbt
│        │  │     ├─ stable_4.nbt
│        │  │     ├─ stable_5.nbt
│        │  │     ├─ tower_1.nbt
│        │  │     ├─ tower_2.nbt
│        │  │     ├─ tower_3.nbt
│        │  │     ├─ tower_4.nbt
│        │  │     ├─ tower_5.nbt
│        │  │     ├─ tower_top_1.nbt
│        │  │     ├─ tower_top_2.nbt
│        │  │     ├─ tower_top_3.nbt
│        │  │     ├─ tower_top_4.nbt
│        │  │     └─ tower_top_5.nbt
│        │  ├─ trial_chambers
│        │  │  ├─ chamber
│        │  │  │  ├─ addon
│        │  │  │  │  ├─ c1_breeze.nbt
│        │  │  │  │  ├─ full_corner_column.nbt
│        │  │  │  │  ├─ full_stacked_walkway.nbt
│        │  │  │  │  ├─ full_stacked_walkway_2.nbt
│        │  │  │  │  ├─ grate_bridge.nbt
│        │  │  │  │  ├─ hanging_platform.nbt
│        │  │  │  │  ├─ lower_staircase_down.nbt
│        │  │  │  │  ├─ short_grate_platform.nbt
│        │  │  │  │  ├─ short_platform.nbt
│        │  │  │  │  └─ walkway_with_bridge_1.nbt
│        │  │  │  ├─ assembly
│        │  │  │  │  ├─ cover_1.nbt
│        │  │  │  │  ├─ cover_2.nbt
│        │  │  │  │  ├─ cover_3.nbt
│        │  │  │  │  ├─ cover_4.nbt
│        │  │  │  │  ├─ cover_5.nbt
│        │  │  │  │  ├─ cover_6.nbt
│        │  │  │  │  ├─ cover_7.nbt
│        │  │  │  │  ├─ full_column.nbt
│        │  │  │  │  ├─ hanging_1.nbt
│        │  │  │  │  ├─ hanging_2.nbt
│        │  │  │  │  ├─ hanging_3.nbt
│        │  │  │  │  ├─ hanging_4.nbt
│        │  │  │  │  ├─ hanging_5.nbt
│        │  │  │  │  ├─ left_staircase_1.nbt
│        │  │  │  │  ├─ left_staircase_2.nbt
│        │  │  │  │  ├─ left_staircase_3.nbt
│        │  │  │  │  ├─ platform_1.nbt
│        │  │  │  │  ├─ right_staircase_1.nbt
│        │  │  │  │  ├─ right_staircase_2.nbt
│        │  │  │  │  ├─ right_staircase_3.nbt
│        │  │  │  │  └─ spawner_1.nbt
│        │  │  │  ├─ assembly.nbt
│        │  │  │  ├─ chamber_1.nbt
│        │  │  │  ├─ chamber_2.nbt
│        │  │  │  ├─ chamber_4.nbt
│        │  │  │  ├─ chamber_8.nbt
│        │  │  │  ├─ entrance_cap.nbt
│        │  │  │  ├─ eruption
│        │  │  │  │  ├─ breeze_slice_1.nbt
│        │  │  │  │  ├─ center_1.nbt
│        │  │  │  │  ├─ quadrant_1.nbt
│        │  │  │  │  ├─ quadrant_2.nbt
│        │  │  │  │  ├─ quadrant_3.nbt
│        │  │  │  │  ├─ quadrant_4.nbt
│        │  │  │  │  ├─ quadrant_5.nbt
│        │  │  │  │  ├─ slice_1.nbt
│        │  │  │  │  ├─ slice_2.nbt
│        │  │  │  │  └─ slice_3.nbt
│        │  │  │  ├─ eruption.nbt
│        │  │  │  ├─ pedestal
│        │  │  │  │  ├─ center_1.nbt
│        │  │  │  │  ├─ ominous_slice_1.nbt
│        │  │  │  │  ├─ quadrant_1.nbt
│        │  │  │  │  ├─ quadrant_2.nbt
│        │  │  │  │  ├─ quadrant_3.nbt
│        │  │  │  │  ├─ slice_1.nbt
│        │  │  │  │  ├─ slice_2.nbt
│        │  │  │  │  ├─ slice_3.nbt
│        │  │  │  │  ├─ slice_4.nbt
│        │  │  │  │  └─ slice_5.nbt
│        │  │  │  ├─ pedestal.nbt
│        │  │  │  ├─ slanted
│        │  │  │  │  ├─ center.nbt
│        │  │  │  │  ├─ hallway_1.nbt
│        │  │  │  │  ├─ hallway_2.nbt
│        │  │  │  │  ├─ hallway_3.nbt
│        │  │  │  │  ├─ ominous_upper_arm_1.nbt
│        │  │  │  │  ├─ quadrant_1.nbt
│        │  │  │  │  ├─ quadrant_2.nbt
│        │  │  │  │  ├─ quadrant_3.nbt
│        │  │  │  │  ├─ quadrant_4.nbt
│        │  │  │  │  ├─ ramp_1.nbt
│        │  │  │  │  ├─ ramp_2.nbt
│        │  │  │  │  ├─ ramp_3.nbt
│        │  │  │  │  └─ ramp_4.nbt
│        │  │  │  └─ slanted.nbt
│        │  │  ├─ chests
│        │  │  │  ├─ connectors
│        │  │  │  │  └─ supply.nbt
│        │  │  │  └─ supply.nbt
│        │  │  ├─ corridor
│        │  │  │  ├─ addon
│        │  │  │  │  ├─ arrow_dispenser.nbt
│        │  │  │  │  ├─ bridge_lower.nbt
│        │  │  │  │  ├─ chandelier_upper.nbt
│        │  │  │  │  ├─ decoration_upper.nbt
│        │  │  │  │  ├─ display_1.nbt
│        │  │  │  │  ├─ display_2.nbt
│        │  │  │  │  ├─ display_3.nbt
│        │  │  │  │  ├─ head_upper.nbt
│        │  │  │  │  ├─ ladder_to_middle.nbt
│        │  │  │  │  ├─ open_walkway.nbt
│        │  │  │  │  ├─ open_walkway_upper.nbt
│        │  │  │  │  ├─ reward_upper.nbt
│        │  │  │  │  ├─ staircase.nbt
│        │  │  │  │  ├─ wall.nbt
│        │  │  │  │  └─ walled_walkway.nbt
│        │  │  │  ├─ atrium
│        │  │  │  │  ├─ bogged_relief.nbt
│        │  │  │  │  ├─ breeze_relief.nbt
│        │  │  │  │  ├─ grand_staircase_1.nbt
│        │  │  │  │  ├─ grand_staircase_2.nbt
│        │  │  │  │  ├─ grand_staircase_3.nbt
│        │  │  │  │  ├─ spider_relief.nbt
│        │  │  │  │  └─ spiral_relief.nbt
│        │  │  │  ├─ atrium_1.nbt
│        │  │  │  ├─ end_1.nbt
│        │  │  │  ├─ end_2.nbt
│        │  │  │  ├─ entrance_1.nbt
│        │  │  │  ├─ entrance_2.nbt
│        │  │  │  ├─ entrance_3.nbt
│        │  │  │  ├─ first_plate.nbt
│        │  │  │  ├─ second_plate.nbt
│        │  │  │  ├─ straight_1.nbt
│        │  │  │  ├─ straight_2.nbt
│        │  │  │  ├─ straight_3.nbt
│        │  │  │  ├─ straight_4.nbt
│        │  │  │  ├─ straight_5.nbt
│        │  │  │  ├─ straight_6.nbt
│        │  │  │  ├─ straight_7.nbt
│        │  │  │  └─ straight_8.nbt
│        │  │  ├─ decor
│        │  │  │  ├─ barrel.nbt
│        │  │  │  ├─ black_bed.nbt
│        │  │  │  ├─ blue_bed.nbt
│        │  │  │  ├─ brown_bed.nbt
│        │  │  │  ├─ candle_1.nbt
│        │  │  │  ├─ candle_2.nbt
│        │  │  │  ├─ candle_3.nbt
│        │  │  │  ├─ candle_4.nbt
│        │  │  │  ├─ cyan_bed.nbt
│        │  │  │  ├─ dead_bush_pot.nbt
│        │  │  │  ├─ disposal.nbt
│        │  │  │  ├─ empty_pot.nbt
│        │  │  │  ├─ flow_pot.nbt
│        │  │  │  ├─ gray_bed.nbt
│        │  │  │  ├─ green_bed.nbt
│        │  │  │  ├─ guster_pot.nbt
│        │  │  │  ├─ light_blue_bed.nbt
│        │  │  │  ├─ light_gray_bed.nbt
│        │  │  │  ├─ lime_bed.nbt
│        │  │  │  ├─ magenta_bed.nbt
│        │  │  │  ├─ orange_bed.nbt
│        │  │  │  ├─ pink_bed.nbt
│        │  │  │  ├─ purple_bed.nbt
│        │  │  │  ├─ red_bed.nbt
│        │  │  │  ├─ scrape_pot.nbt
│        │  │  │  ├─ undecorated_pot.nbt
│        │  │  │  ├─ white_bed.nbt
│        │  │  │  └─ yellow_bed.nbt
│        │  │  ├─ dispensers
│        │  │  │  ├─ chamber.nbt
│        │  │  │  ├─ floor_dispenser.nbt
│        │  │  │  └─ wall_dispenser.nbt
│        │  │  ├─ hallway
│        │  │  │  ├─ cache_1.nbt
│        │  │  │  ├─ corner_staircase.nbt
│        │  │  │  ├─ corner_staircase_down.nbt
│        │  │  │  ├─ corridor_connector_1.nbt
│        │  │  │  ├─ encounter_1.nbt
│        │  │  │  ├─ encounter_2.nbt
│        │  │  │  ├─ encounter_3.nbt
│        │  │  │  ├─ encounter_4.nbt
│        │  │  │  ├─ encounter_5.nbt
│        │  │  │  ├─ left_corner.nbt
│        │  │  │  ├─ long_straight_staircase.nbt
│        │  │  │  ├─ long_straight_staircase_down.nbt
│        │  │  │  ├─ lower_hallway_connector.nbt
│        │  │  │  ├─ right_corner.nbt
│        │  │  │  ├─ rubble.nbt
│        │  │  │  ├─ rubble_chamber.nbt
│        │  │  │  ├─ rubble_chamber_thin.nbt
│        │  │  │  ├─ rubble_thin.nbt
│        │  │  │  ├─ straight.nbt
│        │  │  │  ├─ straight_staircase.nbt
│        │  │  │  ├─ straight_staircase_down.nbt
│        │  │  │  ├─ trapped_staircase.nbt
│        │  │  │  └─ upper_hallway_connector.nbt
│        │  │  ├─ intersection
│        │  │  │  ├─ intersection_1.nbt
│        │  │  │  ├─ intersection_2.nbt
│        │  │  │  └─ intersection_3.nbt
│        │  │  ├─ reward
│        │  │  │  ├─ ominous_vault.nbt
│        │  │  │  └─ vault.nbt
│        │  │  └─ spawner
│        │  │     ├─ breeze
│        │  │     │  └─ breeze.nbt
│        │  │     ├─ connectors
│        │  │     │  ├─ breeze.nbt
│        │  │     │  ├─ melee.nbt
│        │  │     │  ├─ ranged.nbt
│        │  │     │  ├─ slow_ranged.nbt
│        │  │     │  └─ small_melee.nbt
│        │  │     ├─ melee
│        │  │     │  ├─ husk.nbt
│        │  │     │  ├─ spider.nbt
│        │  │     │  └─ zombie.nbt
│        │  │     ├─ ranged
│        │  │     │  ├─ poison_skeleton.nbt
│        │  │     │  ├─ skeleton.nbt
│        │  │     │  └─ stray.nbt
│        │  │     ├─ slow_ranged
│        │  │     │  ├─ poison_skeleton.nbt
│        │  │     │  ├─ skeleton.nbt
│        │  │     │  └─ stray.nbt
│        │  │     └─ small_melee
│        │  │        ├─ baby_zombie.nbt
│        │  │        ├─ cave_spider.nbt
│        │  │        ├─ silverfish.nbt
│        │  │        └─ slime.nbt
│        │  ├─ underwater_ruin
│        │  │  ├─ big_brick_1.nbt
│        │  │  ├─ big_brick_2.nbt
│        │  │  ├─ big_brick_3.nbt
│        │  │  ├─ big_brick_8.nbt
│        │  │  ├─ big_cracked_1.nbt
│        │  │  ├─ big_cracked_2.nbt
│        │  │  ├─ big_cracked_3.nbt
│        │  │  ├─ big_cracked_8.nbt
│        │  │  ├─ big_mossy_1.nbt
│        │  │  ├─ big_mossy_2.nbt
│        │  │  ├─ big_mossy_3.nbt
│        │  │  ├─ big_mossy_8.nbt
│        │  │  ├─ big_warm_4.nbt
│        │  │  ├─ big_warm_5.nbt
│        │  │  ├─ big_warm_6.nbt
│        │  │  ├─ big_warm_7.nbt
│        │  │  ├─ brick_1.nbt
│        │  │  ├─ brick_2.nbt
│        │  │  ├─ brick_3.nbt
│        │  │  ├─ brick_4.nbt
│        │  │  ├─ brick_5.nbt
│        │  │  ├─ brick_6.nbt
│        │  │  ├─ brick_7.nbt
│        │  │  ├─ brick_8.nbt
│        │  │  ├─ cracked_1.nbt
│        │  │  ├─ cracked_2.nbt
│        │  │  ├─ cracked_3.nbt
│        │  │  ├─ cracked_4.nbt
│        │  │  ├─ cracked_5.nbt
│        │  │  ├─ cracked_6.nbt
│        │  │  ├─ cracked_7.nbt
│        │  │  ├─ cracked_8.nbt
│        │  │  ├─ mossy_1.nbt
│        │  │  ├─ mossy_2.nbt
│        │  │  ├─ mossy_3.nbt
│        │  │  ├─ mossy_4.nbt
│        │  │  ├─ mossy_5.nbt
│        │  │  ├─ mossy_6.nbt
│        │  │  ├─ mossy_7.nbt
│        │  │  ├─ mossy_8.nbt
│        │  │  ├─ warm_1.nbt
│        │  │  ├─ warm_2.nbt
│        │  │  ├─ warm_3.nbt
│        │  │  ├─ warm_4.nbt
│        │  │  ├─ warm_5.nbt
│        │  │  ├─ warm_6.nbt
│        │  │  ├─ warm_7.nbt
│        │  │  └─ warm_8.nbt
│        │  ├─ village
│        │  │  ├─ common
│        │  │  │  ├─ animals
│        │  │  │  │  ├─ cat_black.nbt
│        │  │  │  │  ├─ cat_british.nbt
│        │  │  │  │  ├─ cat_calico.nbt
│        │  │  │  │  ├─ cat_jellie.nbt
│        │  │  │  │  ├─ cat_persian.nbt
│        │  │  │  │  ├─ cat_ragdoll.nbt
│        │  │  │  │  ├─ cat_red.nbt
│        │  │  │  │  ├─ cat_siamese.nbt
│        │  │  │  │  ├─ cat_tabby.nbt
│        │  │  │  │  ├─ cat_white.nbt
│        │  │  │  │  ├─ cows_1.nbt
│        │  │  │  │  ├─ horses_1.nbt
│        │  │  │  │  ├─ horses_2.nbt
│        │  │  │  │  ├─ horses_3.nbt
│        │  │  │  │  ├─ horses_4.nbt
│        │  │  │  │  ├─ horses_5.nbt
│        │  │  │  │  ├─ pigs_1.nbt
│        │  │  │  │  ├─ sheep_1.nbt
│        │  │  │  │  └─ sheep_2.nbt
│        │  │  │  ├─ iron_golem.nbt
│        │  │  │  └─ well_bottom.nbt
│        │  │  ├─ decays
│        │  │  │  ├─ grass_11x13.nbt
│        │  │  │  ├─ grass_16x16.nbt
│        │  │  │  └─ grass_9x9.nbt
│        │  │  ├─ desert
│        │  │  │  ├─ camel_spawn.nbt
│        │  │  │  ├─ desert_lamp_1.nbt
│        │  │  │  ├─ houses
│        │  │  │  │  ├─ desert_animal_pen_1.nbt
│        │  │  │  │  ├─ desert_animal_pen_2.nbt
│        │  │  │  │  ├─ desert_armorer_1.nbt
│        │  │  │  │  ├─ desert_butcher_shop_1.nbt
│        │  │  │  │  ├─ desert_cartographer_house_1.nbt
│        │  │  │  │  ├─ desert_farm_1.nbt
│        │  │  │  │  ├─ desert_farm_2.nbt
│        │  │  │  │  ├─ desert_fisher_1.nbt
│        │  │  │  │  ├─ desert_fletcher_house_1.nbt
│        │  │  │  │  ├─ desert_large_farm_1.nbt
│        │  │  │  │  ├─ desert_library_1.nbt
│        │  │  │  │  ├─ desert_mason_1.nbt
│        │  │  │  │  ├─ desert_medium_house_1.nbt
│        │  │  │  │  ├─ desert_medium_house_2.nbt
│        │  │  │  │  ├─ desert_shepherd_house_1.nbt
│        │  │  │  │  ├─ desert_small_house_1.nbt
│        │  │  │  │  ├─ desert_small_house_2.nbt
│        │  │  │  │  ├─ desert_small_house_3.nbt
│        │  │  │  │  ├─ desert_small_house_4.nbt
│        │  │  │  │  ├─ desert_small_house_5.nbt
│        │  │  │  │  ├─ desert_small_house_6.nbt
│        │  │  │  │  ├─ desert_small_house_7.nbt
│        │  │  │  │  ├─ desert_small_house_8.nbt
│        │  │  │  │  ├─ desert_tannery_1.nbt
│        │  │  │  │  ├─ desert_temple_1.nbt
│        │  │  │  │  ├─ desert_temple_2.nbt
│        │  │  │  │  ├─ desert_tool_smith_1.nbt
│        │  │  │  │  └─ desert_weaponsmith_1.nbt
│        │  │  │  ├─ streets
│        │  │  │  │  ├─ corner_01.nbt
│        │  │  │  │  ├─ corner_02.nbt
│        │  │  │  │  ├─ crossroad_01.nbt
│        │  │  │  │  ├─ crossroad_02.nbt
│        │  │  │  │  ├─ crossroad_03.nbt
│        │  │  │  │  ├─ square_01.nbt
│        │  │  │  │  ├─ square_02.nbt
│        │  │  │  │  ├─ straight_01.nbt
│        │  │  │  │  ├─ straight_02.nbt
│        │  │  │  │  ├─ straight_03.nbt
│        │  │  │  │  └─ turn_01.nbt
│        │  │  │  ├─ terminators
│        │  │  │  │  ├─ terminator_01.nbt
│        │  │  │  │  └─ terminator_02.nbt
│        │  │  │  ├─ town_centers
│        │  │  │  │  ├─ desert_meeting_point_1.nbt
│        │  │  │  │  ├─ desert_meeting_point_2.nbt
│        │  │  │  │  └─ desert_meeting_point_3.nbt
│        │  │  │  ├─ villagers
│        │  │  │  │  ├─ baby.nbt
│        │  │  │  │  ├─ nitwit.nbt
│        │  │  │  │  └─ unemployed.nbt
│        │  │  │  └─ zombie
│        │  │  │     ├─ houses
│        │  │  │     │  ├─ desert_medium_house_1.nbt
│        │  │  │     │  ├─ desert_medium_house_2.nbt
│        │  │  │     │  ├─ desert_small_house_1.nbt
│        │  │  │     │  ├─ desert_small_house_2.nbt
│        │  │  │     │  ├─ desert_small_house_3.nbt
│        │  │  │     │  ├─ desert_small_house_4.nbt
│        │  │  │     │  ├─ desert_small_house_5.nbt
│        │  │  │     │  ├─ desert_small_house_6.nbt
│        │  │  │     │  ├─ desert_small_house_7.nbt
│        │  │  │     │  └─ desert_small_house_8.nbt
│        │  │  │     ├─ streets
│        │  │  │     │  ├─ corner_01.nbt
│        │  │  │     │  ├─ corner_02.nbt
│        │  │  │     │  ├─ crossroad_01.nbt
│        │  │  │     │  ├─ crossroad_02.nbt
│        │  │  │     │  ├─ crossroad_03.nbt
│        │  │  │     │  ├─ square_01.nbt
│        │  │  │     │  ├─ square_02.nbt
│        │  │  │     │  ├─ straight_01.nbt
│        │  │  │     │  ├─ straight_02.nbt
│        │  │  │     │  ├─ straight_03.nbt
│        │  │  │     │  └─ turn_01.nbt
│        │  │  │     ├─ terminators
│        │  │  │     │  └─ terminator_02.nbt
│        │  │  │     ├─ town_centers
│        │  │  │     │  ├─ desert_meeting_point_1.nbt
│        │  │  │     │  ├─ desert_meeting_point_2.nbt
│        │  │  │     │  └─ desert_meeting_point_3.nbt
│        │  │  │     └─ villagers
│        │  │  │        ├─ nitwit.nbt
│        │  │  │        └─ unemployed.nbt
│        │  │  ├─ plains
│        │  │  │  ├─ houses
│        │  │  │  │  ├─ plains_accessory_1.nbt
│        │  │  │  │  ├─ plains_animal_pen_1.nbt
│        │  │  │  │  ├─ plains_animal_pen_2.nbt
│        │  │  │  │  ├─ plains_animal_pen_3.nbt
│        │  │  │  │  ├─ plains_armorer_house_1.nbt
│        │  │  │  │  ├─ plains_big_house_1.nbt
│        │  │  │  │  ├─ plains_butcher_shop_1.nbt
│        │  │  │  │  ├─ plains_butcher_shop_2.nbt
│        │  │  │  │  ├─ plains_cartographer_1.nbt
│        │  │  │  │  ├─ plains_fisher_cottage_1.nbt
│        │  │  │  │  ├─ plains_fletcher_house_1.nbt
│        │  │  │  │  ├─ plains_large_farm_1.nbt
│        │  │  │  │  ├─ plains_library_1.nbt
│        │  │  │  │  ├─ plains_library_2.nbt
│        │  │  │  │  ├─ plains_masons_house_1.nbt
│        │  │  │  │  ├─ plains_medium_house_1.nbt
│        │  │  │  │  ├─ plains_medium_house_2.nbt
│        │  │  │  │  ├─ plains_meeting_point_4.nbt
│        │  │  │  │  ├─ plains_meeting_point_5.nbt
│        │  │  │  │  ├─ plains_shepherds_house_1.nbt
│        │  │  │  │  ├─ plains_small_farm_1.nbt
│        │  │  │  │  ├─ plains_small_house_1.nbt
│        │  │  │  │  ├─ plains_small_house_2.nbt
│        │  │  │  │  ├─ plains_small_house_3.nbt
│        │  │  │  │  ├─ plains_small_house_4.nbt
│        │  │  │  │  ├─ plains_small_house_5.nbt
│        │  │  │  │  ├─ plains_small_house_6.nbt
│        │  │  │  │  ├─ plains_small_house_7.nbt
│        │  │  │  │  ├─ plains_small_house_8.nbt
│        │  │  │  │  ├─ plains_stable_1.nbt
│        │  │  │  │  ├─ plains_stable_2.nbt
│        │  │  │  │  ├─ plains_tannery_1.nbt
│        │  │  │  │  ├─ plains_temple_3.nbt
│        │  │  │  │  ├─ plains_temple_4.nbt
│        │  │  │  │  ├─ plains_tool_smith_1.nbt
│        │  │  │  │  └─ plains_weaponsmith_1.nbt
│        │  │  │  ├─ plains_lamp_1.nbt
│        │  │  │  ├─ streets
│        │  │  │  │  ├─ corner_01.nbt
│        │  │  │  │  ├─ corner_02.nbt
│        │  │  │  │  ├─ corner_03.nbt
│        │  │  │  │  ├─ crossroad_01.nbt
│        │  │  │  │  ├─ crossroad_02.nbt
│        │  │  │  │  ├─ crossroad_03.nbt
│        │  │  │  │  ├─ crossroad_04.nbt
│        │  │  │  │  ├─ crossroad_05.nbt
│        │  │  │  │  ├─ crossroad_06.nbt
│        │  │  │  │  ├─ straight_01.nbt
│        │  │  │  │  ├─ straight_02.nbt
│        │  │  │  │  ├─ straight_03.nbt
│        │  │  │  │  ├─ straight_04.nbt
│        │  │  │  │  ├─ straight_05.nbt
│        │  │  │  │  ├─ straight_06.nbt
│        │  │  │  │  └─ turn_01.nbt
│        │  │  │  ├─ terminators
│        │  │  │  │  ├─ terminator_01.nbt
│        │  │  │  │  ├─ terminator_02.nbt
│        │  │  │  │  ├─ terminator_03.nbt
│        │  │  │  │  └─ terminator_04.nbt
│        │  │  │  ├─ town_centers
│        │  │  │  │  ├─ plains_fountain_01.nbt
│        │  │  │  │  ├─ plains_meeting_point_1.nbt
│        │  │  │  │  ├─ plains_meeting_point_2.nbt
│        │  │  │  │  └─ plains_meeting_point_3.nbt
│        │  │  │  ├─ villagers
│        │  │  │  │  ├─ baby.nbt
│        │  │  │  │  ├─ nitwit.nbt
│        │  │  │  │  └─ unemployed.nbt
│        │  │  │  └─ zombie
│        │  │  │     ├─ houses
│        │  │  │     │  ├─ plains_animal_pen_3.nbt
│        │  │  │     │  ├─ plains_big_house_1.nbt
│        │  │  │     │  ├─ plains_butcher_shop_2.nbt
│        │  │  │     │  ├─ plains_fletcher_house_1.nbt
│        │  │  │     │  ├─ plains_medium_house_1.nbt
│        │  │  │     │  ├─ plains_medium_house_2.nbt
│        │  │  │     │  ├─ plains_meeting_point_4.nbt
│        │  │  │     │  ├─ plains_meeting_point_5.nbt
│        │  │  │     │  ├─ plains_shepherds_house_1.nbt
│        │  │  │     │  ├─ plains_small_house_1.nbt
│        │  │  │     │  ├─ plains_small_house_2.nbt
│        │  │  │     │  ├─ plains_small_house_3.nbt
│        │  │  │     │  ├─ plains_small_house_4.nbt
│        │  │  │     │  ├─ plains_small_house_5.nbt
│        │  │  │     │  ├─ plains_small_house_6.nbt
│        │  │  │     │  ├─ plains_small_house_7.nbt
│        │  │  │     │  ├─ plains_small_house_8.nbt
│        │  │  │     │  └─ plains_stable_1.nbt
│        │  │  │     ├─ streets
│        │  │  │     │  ├─ corner_01.nbt
│        │  │  │     │  ├─ corner_02.nbt
│        │  │  │     │  ├─ corner_03.nbt
│        │  │  │     │  ├─ crossroad_01.nbt
│        │  │  │     │  ├─ crossroad_02.nbt
│        │  │  │     │  ├─ crossroad_03.nbt
│        │  │  │     │  ├─ crossroad_04.nbt
│        │  │  │     │  ├─ crossroad_05.nbt
│        │  │  │     │  ├─ crossroad_06.nbt
│        │  │  │     │  ├─ straight_01.nbt
│        │  │  │     │  ├─ straight_02.nbt
│        │  │  │     │  ├─ straight_03.nbt
│        │  │  │     │  ├─ straight_04.nbt
│        │  │  │     │  ├─ straight_05.nbt
│        │  │  │     │  ├─ straight_06.nbt
│        │  │  │     │  └─ turn_01.nbt
│        │  │  │     ├─ town_centers
│        │  │  │     │  ├─ plains_fountain_01.nbt
│        │  │  │     │  ├─ plains_meeting_point_1.nbt
│        │  │  │     │  ├─ plains_meeting_point_2.nbt
│        │  │  │     │  └─ plains_meeting_point_3.nbt
│        │  │  │     └─ villagers
│        │  │  │        ├─ nitwit.nbt
│        │  │  │        └─ unemployed.nbt
│        │  │  ├─ savanna
│        │  │  │  ├─ houses
│        │  │  │  │  ├─ savanna_animal_pen_1.nbt
│        │  │  │  │  ├─ savanna_animal_pen_2.nbt
│        │  │  │  │  ├─ savanna_animal_pen_3.nbt
│        │  │  │  │  ├─ savanna_armorer_1.nbt
│        │  │  │  │  ├─ savanna_butchers_shop_1.nbt
│        │  │  │  │  ├─ savanna_butchers_shop_2.nbt
│        │  │  │  │  ├─ savanna_cartographer_1.nbt
│        │  │  │  │  ├─ savanna_fisher_cottage_1.nbt
│        │  │  │  │  ├─ savanna_fletcher_house_1.nbt
│        │  │  │  │  ├─ savanna_large_farm_1.nbt
│        │  │  │  │  ├─ savanna_large_farm_2.nbt
│        │  │  │  │  ├─ savanna_library_1.nbt
│        │  │  │  │  ├─ savanna_mason_1.nbt
│        │  │  │  │  ├─ savanna_medium_house_1.nbt
│        │  │  │  │  ├─ savanna_medium_house_2.nbt
│        │  │  │  │  ├─ savanna_shepherd_1.nbt
│        │  │  │  │  ├─ savanna_small_farm.nbt
│        │  │  │  │  ├─ savanna_small_house_1.nbt
│        │  │  │  │  ├─ savanna_small_house_2.nbt
│        │  │  │  │  ├─ savanna_small_house_3.nbt
│        │  │  │  │  ├─ savanna_small_house_4.nbt
│        │  │  │  │  ├─ savanna_small_house_5.nbt
│        │  │  │  │  ├─ savanna_small_house_6.nbt
│        │  │  │  │  ├─ savanna_small_house_7.nbt
│        │  │  │  │  ├─ savanna_small_house_8.nbt
│        │  │  │  │  ├─ savanna_tannery_1.nbt
│        │  │  │  │  ├─ savanna_temple_1.nbt
│        │  │  │  │  ├─ savanna_temple_2.nbt
│        │  │  │  │  ├─ savanna_tool_smith_1.nbt
│        │  │  │  │  ├─ savanna_weaponsmith_1.nbt
│        │  │  │  │  └─ savanna_weaponsmith_2.nbt
│        │  │  │  ├─ savanna_lamp_post_01.nbt
│        │  │  │  ├─ streets
│        │  │  │  │  ├─ corner_01.nbt
│        │  │  │  │  ├─ corner_03.nbt
│        │  │  │  │  ├─ crossroad_02.nbt
│        │  │  │  │  ├─ crossroad_03.nbt
│        │  │  │  │  ├─ crossroad_04.nbt
│        │  │  │  │  ├─ crossroad_05.nbt
│        │  │  │  │  ├─ crossroad_06.nbt
│        │  │  │  │  ├─ crossroad_07.nbt
│        │  │  │  │  ├─ split_01.nbt
│        │  │  │  │  ├─ split_02.nbt
│        │  │  │  │  ├─ straight_02.nbt
│        │  │  │  │  ├─ straight_04.nbt
│        │  │  │  │  ├─ straight_05.nbt
│        │  │  │  │  ├─ straight_06.nbt
│        │  │  │  │  ├─ straight_08.nbt
│        │  │  │  │  ├─ straight_09.nbt
│        │  │  │  │  ├─ straight_10.nbt
│        │  │  │  │  ├─ straight_11.nbt
│        │  │  │  │  └─ turn_01.nbt
│        │  │  │  ├─ terminators
│        │  │  │  │  └─ terminator_05.nbt
│        │  │  │  ├─ town_centers
│        │  │  │  │  ├─ savanna_meeting_point_1.nbt
│        │  │  │  │  ├─ savanna_meeting_point_2.nbt
│        │  │  │  │  ├─ savanna_meeting_point_3.nbt
│        │  │  │  │  └─ savanna_meeting_point_4.nbt
│        │  │  │  ├─ villagers
│        │  │  │  │  ├─ baby.nbt
│        │  │  │  │  ├─ nitwit.nbt
│        │  │  │  │  └─ unemployed.nbt
│        │  │  │  └─ zombie
│        │  │  │     ├─ houses
│        │  │  │     │  ├─ savanna_animal_pen_2.nbt
│        │  │  │     │  ├─ savanna_animal_pen_3.nbt
│        │  │  │     │  ├─ savanna_large_farm_2.nbt
│        │  │  │     │  ├─ savanna_medium_house_1.nbt
│        │  │  │     │  ├─ savanna_medium_house_2.nbt
│        │  │  │     │  ├─ savanna_small_house_1.nbt
│        │  │  │     │  ├─ savanna_small_house_2.nbt
│        │  │  │     │  ├─ savanna_small_house_3.nbt
│        │  │  │     │  ├─ savanna_small_house_4.nbt
│        │  │  │     │  ├─ savanna_small_house_5.nbt
│        │  │  │     │  ├─ savanna_small_house_6.nbt
│        │  │  │     │  ├─ savanna_small_house_7.nbt
│        │  │  │     │  └─ savanna_small_house_8.nbt
│        │  │  │     ├─ streets
│        │  │  │     │  ├─ corner_01.nbt
│        │  │  │     │  ├─ corner_03.nbt
│        │  │  │     │  ├─ crossroad_02.nbt
│        │  │  │     │  ├─ crossroad_03.nbt
│        │  │  │     │  ├─ crossroad_04.nbt
│        │  │  │     │  ├─ crossroad_05.nbt
│        │  │  │     │  ├─ crossroad_06.nbt
│        │  │  │     │  ├─ crossroad_07.nbt
│        │  │  │     │  ├─ split_01.nbt
│        │  │  │     │  ├─ split_02.nbt
│        │  │  │     │  ├─ straight_02.nbt
│        │  │  │     │  ├─ straight_04.nbt
│        │  │  │     │  ├─ straight_05.nbt
│        │  │  │     │  ├─ straight_06.nbt
│        │  │  │     │  ├─ straight_08.nbt
│        │  │  │     │  ├─ straight_09.nbt
│        │  │  │     │  ├─ straight_10.nbt
│        │  │  │     │  ├─ straight_11.nbt
│        │  │  │     │  └─ turn_01.nbt
│        │  │  │     ├─ terminators
│        │  │  │     │  └─ terminator_05.nbt
│        │  │  │     ├─ town_centers
│        │  │  │     │  ├─ savanna_meeting_point_1.nbt
│        │  │  │     │  ├─ savanna_meeting_point_2.nbt
│        │  │  │     │  ├─ savanna_meeting_point_3.nbt
│        │  │  │     │  └─ savanna_meeting_point_4.nbt
│        │  │  │     └─ villagers
│        │  │  │        ├─ nitwit.nbt
│        │  │  │        └─ unemployed.nbt
│        │  │  ├─ snowy
│        │  │  │  ├─ houses
│        │  │  │  │  ├─ snowy_animal_pen_1.nbt
│        │  │  │  │  ├─ snowy_animal_pen_2.nbt
│        │  │  │  │  ├─ snowy_armorer_house_1.nbt
│        │  │  │  │  ├─ snowy_armorer_house_2.nbt
│        │  │  │  │  ├─ snowy_butchers_shop_1.nbt
│        │  │  │  │  ├─ snowy_butchers_shop_2.nbt
│        │  │  │  │  ├─ snowy_cartographer_house_1.nbt
│        │  │  │  │  ├─ snowy_farm_1.nbt
│        │  │  │  │  ├─ snowy_farm_2.nbt
│        │  │  │  │  ├─ snowy_fisher_cottage.nbt
│        │  │  │  │  ├─ snowy_fletcher_house_1.nbt
│        │  │  │  │  ├─ snowy_library_1.nbt
│        │  │  │  │  ├─ snowy_masons_house_1.nbt
│        │  │  │  │  ├─ snowy_masons_house_2.nbt
│        │  │  │  │  ├─ snowy_medium_house_1.nbt
│        │  │  │  │  ├─ snowy_medium_house_2.nbt
│        │  │  │  │  ├─ snowy_medium_house_3.nbt
│        │  │  │  │  ├─ snowy_shepherds_house_1.nbt
│        │  │  │  │  ├─ snowy_small_house_1.nbt
│        │  │  │  │  ├─ snowy_small_house_2.nbt
│        │  │  │  │  ├─ snowy_small_house_3.nbt
│        │  │  │  │  ├─ snowy_small_house_4.nbt
│        │  │  │  │  ├─ snowy_small_house_5.nbt
│        │  │  │  │  ├─ snowy_small_house_6.nbt
│        │  │  │  │  ├─ snowy_small_house_7.nbt
│        │  │  │  │  ├─ snowy_small_house_8.nbt
│        │  │  │  │  ├─ snowy_tannery_1.nbt
│        │  │  │  │  ├─ snowy_temple_1.nbt
│        │  │  │  │  ├─ snowy_tool_smith_1.nbt
│        │  │  │  │  └─ snowy_weapon_smith_1.nbt
│        │  │  │  ├─ snowy_lamp_post_01.nbt
│        │  │  │  ├─ snowy_lamp_post_02.nbt
│        │  │  │  ├─ snowy_lamp_post_03.nbt
│        │  │  │  ├─ streets
│        │  │  │  │  ├─ corner_01.nbt
│        │  │  │  │  ├─ corner_02.nbt
│        │  │  │  │  ├─ corner_03.nbt
│        │  │  │  │  ├─ crossroad_01.nbt
│        │  │  │  │  ├─ crossroad_02.nbt
│        │  │  │  │  ├─ crossroad_03.nbt
│        │  │  │  │  ├─ crossroad_04.nbt
│        │  │  │  │  ├─ crossroad_05.nbt
│        │  │  │  │  ├─ crossroad_06.nbt
│        │  │  │  │  ├─ square_01.nbt
│        │  │  │  │  ├─ straight_01.nbt
│        │  │  │  │  ├─ straight_02.nbt
│        │  │  │  │  ├─ straight_03.nbt
│        │  │  │  │  ├─ straight_04.nbt
│        │  │  │  │  ├─ straight_06.nbt
│        │  │  │  │  ├─ straight_08.nbt
│        │  │  │  │  └─ turn_01.nbt
│        │  │  │  ├─ town_centers
│        │  │  │  │  ├─ snowy_meeting_point_1.nbt
│        │  │  │  │  ├─ snowy_meeting_point_2.nbt
│        │  │  │  │  └─ snowy_meeting_point_3.nbt
│        │  │  │  ├─ villagers
│        │  │  │  │  ├─ baby.nbt
│        │  │  │  │  ├─ nitwit.nbt
│        │  │  │  │  └─ unemployed.nbt
│        │  │  │  └─ zombie
│        │  │  │     ├─ houses
│        │  │  │     │  ├─ snowy_medium_house_1.nbt
│        │  │  │     │  ├─ snowy_medium_house_2.nbt
│        │  │  │     │  ├─ snowy_medium_house_3.nbt
│        │  │  │     │  ├─ snowy_small_house_1.nbt
│        │  │  │     │  ├─ snowy_small_house_2.nbt
│        │  │  │     │  ├─ snowy_small_house_3.nbt
│        │  │  │     │  ├─ snowy_small_house_4.nbt
│        │  │  │     │  ├─ snowy_small_house_5.nbt
│        │  │  │     │  ├─ snowy_small_house_6.nbt
│        │  │  │     │  ├─ snowy_small_house_7.nbt
│        │  │  │     │  └─ snowy_small_house_8.nbt
│        │  │  │     ├─ streets
│        │  │  │     │  ├─ corner_01.nbt
│        │  │  │     │  ├─ corner_02.nbt
│        │  │  │     │  ├─ corner_03.nbt
│        │  │  │     │  ├─ crossroad_01.nbt
│        │  │  │     │  ├─ crossroad_02.nbt
│        │  │  │     │  ├─ crossroad_03.nbt
│        │  │  │     │  ├─ crossroad_04.nbt
│        │  │  │     │  ├─ crossroad_05.nbt
│        │  │  │     │  ├─ crossroad_06.nbt
│        │  │  │     │  ├─ square_01.nbt
│        │  │  │     │  ├─ straight_01.nbt
│        │  │  │     │  ├─ straight_02.nbt
│        │  │  │     │  ├─ straight_03.nbt
│        │  │  │     │  ├─ straight_04.nbt
│        │  │  │     │  ├─ straight_06.nbt
│        │  │  │     │  ├─ straight_08.nbt
│        │  │  │     │  └─ turn_01.nbt
│        │  │  │     ├─ town_centers
│        │  │  │     │  ├─ snowy_meeting_point_1.nbt
│        │  │  │     │  ├─ snowy_meeting_point_2.nbt
│        │  │  │     │  └─ snowy_meeting_point_3.nbt
│        │  │  │     └─ villagers
│        │  │  │        ├─ nitwit.nbt
│        │  │  │        └─ unemployed.nbt
│        │  │  └─ taiga
│        │  │     ├─ houses
│        │  │     │  ├─ taiga_animal_pen_1.nbt
│        │  │     │  ├─ taiga_armorer_2.nbt
│        │  │     │  ├─ taiga_armorer_house_1.nbt
│        │  │     │  ├─ taiga_butcher_shop_1.nbt
│        │  │     │  ├─ taiga_cartographer_house_1.nbt
│        │  │     │  ├─ taiga_fisher_cottage_1.nbt
│        │  │     │  ├─ taiga_fletcher_house_1.nbt
│        │  │     │  ├─ taiga_large_farm_1.nbt
│        │  │     │  ├─ taiga_large_farm_2.nbt
│        │  │     │  ├─ taiga_library_1.nbt
│        │  │     │  ├─ taiga_masons_house_1.nbt
│        │  │     │  ├─ taiga_medium_house_1.nbt
│        │  │     │  ├─ taiga_medium_house_2.nbt
│        │  │     │  ├─ taiga_medium_house_3.nbt
│        │  │     │  ├─ taiga_medium_house_4.nbt
│        │  │     │  ├─ taiga_shepherds_house_1.nbt
│        │  │     │  ├─ taiga_small_farm_1.nbt
│        │  │     │  ├─ taiga_small_house_1.nbt
│        │  │     │  ├─ taiga_small_house_2.nbt
│        │  │     │  ├─ taiga_small_house_3.nbt
│        │  │     │  ├─ taiga_small_house_4.nbt
│        │  │     │  ├─ taiga_small_house_5.nbt
│        │  │     │  ├─ taiga_tannery_1.nbt
│        │  │     │  ├─ taiga_temple_1.nbt
│        │  │     │  ├─ taiga_tool_smith_1.nbt
│        │  │     │  ├─ taiga_weaponsmith_1.nbt
│        │  │     │  └─ taiga_weaponsmith_2.nbt
│        │  │     ├─ streets
│        │  │     │  ├─ corner_01.nbt
│        │  │     │  ├─ corner_02.nbt
│        │  │     │  ├─ corner_03.nbt
│        │  │     │  ├─ crossroad_01.nbt
│        │  │     │  ├─ crossroad_02.nbt
│        │  │     │  ├─ crossroad_03.nbt
│        │  │     │  ├─ crossroad_04.nbt
│        │  │     │  ├─ crossroad_05.nbt
│        │  │     │  ├─ crossroad_06.nbt
│        │  │     │  ├─ straight_01.nbt
│        │  │     │  ├─ straight_02.nbt
│        │  │     │  ├─ straight_03.nbt
│        │  │     │  ├─ straight_04.nbt
│        │  │     │  ├─ straight_05.nbt
│        │  │     │  ├─ straight_06.nbt
│        │  │     │  └─ turn_01.nbt
│        │  │     ├─ taiga_decoration_1.nbt
│        │  │     ├─ taiga_decoration_2.nbt
│        │  │     ├─ taiga_decoration_3.nbt
│        │  │     ├─ taiga_decoration_4.nbt
│        │  │     ├─ taiga_decoration_5.nbt
│        │  │     ├─ taiga_decoration_6.nbt
│        │  │     ├─ taiga_lamp_post_1.nbt
│        │  │     ├─ town_centers
│        │  │     │  ├─ taiga_meeting_point_1.nbt
│        │  │     │  └─ taiga_meeting_point_2.nbt
│        │  │     ├─ villagers
│        │  │     │  ├─ baby.nbt
│        │  │     │  ├─ nitwit.nbt
│        │  │     │  └─ unemployed.nbt
│        │  │     └─ zombie
│        │  │        ├─ houses
│        │  │        │  ├─ taiga_cartographer_house_1.nbt
│        │  │        │  ├─ taiga_fisher_cottage_1.nbt
│        │  │        │  ├─ taiga_large_farm_2.nbt
│        │  │        │  ├─ taiga_library_1.nbt
│        │  │        │  ├─ taiga_medium_house_1.nbt
│        │  │        │  ├─ taiga_medium_house_2.nbt
│        │  │        │  ├─ taiga_medium_house_3.nbt
│        │  │        │  ├─ taiga_medium_house_4.nbt
│        │  │        │  ├─ taiga_shepherds_house_1.nbt
│        │  │        │  ├─ taiga_small_house_1.nbt
│        │  │        │  ├─ taiga_small_house_2.nbt
│        │  │        │  ├─ taiga_small_house_3.nbt
│        │  │        │  ├─ taiga_small_house_4.nbt
│        │  │        │  ├─ taiga_small_house_5.nbt
│        │  │        │  ├─ taiga_temple_1.nbt
│        │  │        │  ├─ taiga_tool_smith_1.nbt
│        │  │        │  └─ taiga_weaponsmith_2.nbt
│        │  │        ├─ streets
│        │  │        │  ├─ corner_01.nbt
│        │  │        │  ├─ corner_02.nbt
│        │  │        │  ├─ corner_03.nbt
│        │  │        │  ├─ crossroad_01.nbt
│        │  │        │  ├─ crossroad_02.nbt
│        │  │        │  ├─ crossroad_03.nbt
│        │  │        │  ├─ crossroad_04.nbt
│        │  │        │  ├─ crossroad_05.nbt
│        │  │        │  ├─ crossroad_06.nbt
│        │  │        │  ├─ straight_01.nbt
│        │  │        │  ├─ straight_02.nbt
│        │  │        │  ├─ straight_03.nbt
│        │  │        │  ├─ straight_04.nbt
│        │  │        │  ├─ straight_05.nbt
│        │  │        │  ├─ straight_06.nbt
│        │  │        │  └─ turn_01.nbt
│        │  │        ├─ town_centers
│        │  │        │  ├─ taiga_meeting_point_1.nbt
│        │  │        │  └─ taiga_meeting_point_2.nbt
│        │  │        └─ villagers
│        │  │           ├─ nitwit.nbt
│        │  │           └─ unemployed.nbt
│        │  └─ woodland_mansion
│        │     ├─ 1x1_a1.nbt
│        │     ├─ 1x1_a2.nbt
│        │     ├─ 1x1_a3.nbt
│        │     ├─ 1x1_a4.nbt
│        │     ├─ 1x1_a5.nbt
│        │     ├─ 1x1_as1.nbt
│        │     ├─ 1x1_as2.nbt
│        │     ├─ 1x1_as3.nbt
│        │     ├─ 1x1_as4.nbt
│        │     ├─ 1x1_b1.nbt
│        │     ├─ 1x1_b2.nbt
│        │     ├─ 1x1_b3.nbt
│        │     ├─ 1x1_b4.nbt
│        │     ├─ 1x1_b5.nbt
│        │     ├─ 1x2_a1.nbt
│        │     ├─ 1x2_a2.nbt
│        │     ├─ 1x2_a3.nbt
│        │     ├─ 1x2_a4.nbt
│        │     ├─ 1x2_a5.nbt
│        │     ├─ 1x2_a6.nbt
│        │     ├─ 1x2_a7.nbt
│        │     ├─ 1x2_a8.nbt
│        │     ├─ 1x2_a9.nbt
│        │     ├─ 1x2_b1.nbt
│        │     ├─ 1x2_b2.nbt
│        │     ├─ 1x2_b3.nbt
│        │     ├─ 1x2_b4.nbt
│        │     ├─ 1x2_b5.nbt
│        │     ├─ 1x2_c1.nbt
│        │     ├─ 1x2_c2.nbt
│        │     ├─ 1x2_c3.nbt
│        │     ├─ 1x2_c4.nbt
│        │     ├─ 1x2_c_stairs.nbt
│        │     ├─ 1x2_d1.nbt
│        │     ├─ 1x2_d2.nbt
│        │     ├─ 1x2_d3.nbt
│        │     ├─ 1x2_d4.nbt
│        │     ├─ 1x2_d5.nbt
│        │     ├─ 1x2_d_stairs.nbt
│        │     ├─ 1x2_s1.nbt
│        │     ├─ 1x2_s2.nbt
│        │     ├─ 1x2_se1.nbt
│        │     ├─ 2x2_a1.nbt
│        │     ├─ 2x2_a2.nbt
│        │     ├─ 2x2_a3.nbt
│        │     ├─ 2x2_a4.nbt
│        │     ├─ 2x2_b1.nbt
│        │     ├─ 2x2_b2.nbt
│        │     ├─ 2x2_b3.nbt
│        │     ├─ 2x2_b4.nbt
│        │     ├─ 2x2_b5.nbt
│        │     ├─ 2x2_s1.nbt
│        │     ├─ carpet_east.nbt
│        │     ├─ carpet_north.nbt
│        │     ├─ carpet_south_1.nbt
│        │     ├─ carpet_south_2.nbt
│        │     ├─ carpet_west_1.nbt
│        │     ├─ carpet_west_2.nbt
│        │     ├─ corridor_floor.nbt
│        │     ├─ entrance.nbt
│        │     ├─ indoors_door_1.nbt
│        │     ├─ indoors_door_2.nbt
│        │     ├─ indoors_wall_1.nbt
│        │     ├─ indoors_wall_2.nbt
│        │     ├─ roof.nbt
│        │     ├─ roof_corner.nbt
│        │     ├─ roof_front.nbt
│        │     ├─ roof_inner_corner.nbt
│        │     ├─ small_wall.nbt
│        │     ├─ small_wall_corner.nbt
│        │     ├─ wall_corner.nbt
│        │     ├─ wall_flat.nbt
│        │     └─ wall_window.nbt
│        ├─ tags
│        │  ├─ banner_pattern
│        │  │  ├─ no_item_required.json
│        │  │  └─ pattern_item
│        │  │     ├─ bordure_indented.json
│        │  │     ├─ creeper.json
│        │  │     ├─ field_masoned.json
│        │  │     ├─ flow.json
│        │  │     ├─ flower.json
│        │  │     ├─ globe.json
│        │  │     ├─ guster.json
│        │  │     ├─ mojang.json
│        │  │     ├─ piglin.json
│        │  │     └─ skull.json
│        │  ├─ block
│        │  │  ├─ acacia_logs.json
│        │  │  ├─ air.json
│        │  │  ├─ all_hanging_signs.json
│        │  │  ├─ all_signs.json
│        │  │  ├─ ancient_city_replaceable.json
│        │  │  ├─ animals_spawnable_on.json
│        │  │  ├─ anvil.json
│        │  │  ├─ armadillo_spawnable_on.json
│        │  │  ├─ axolotls_spawnable_on.json
│        │  │  ├─ azalea_grows_on.json
│        │  │  ├─ azalea_root_replaceable.json
│        │  │  ├─ badlands_terracotta.json
│        │  │  ├─ bamboo_blocks.json
│        │  │  ├─ bamboo_plantable_on.json
│        │  │  ├─ banners.json
│        │  │  ├─ bars.json
│        │  │  ├─ base_stone_nether.json
│        │  │  ├─ base_stone_overworld.json
│        │  │  ├─ bats_spawnable_on.json
│        │  │  ├─ beacon_base_blocks.json
│        │  │  ├─ beds.json
│        │  │  ├─ beehives.json
│        │  │  ├─ bee_attractive.json
│        │  │  ├─ bee_growables.json
│        │  │  ├─ big_dripleaf_placeable.json
│        │  │  ├─ birch_logs.json
│        │  │  ├─ blocks_wind_charge_explosions.json
│        │  │  ├─ buttons.json
│        │  │  ├─ camels_spawnable_on.json
│        │  │  ├─ camel_sand_step_sound_blocks.json
│        │  │  ├─ campfires.json
│        │  │  ├─ candles.json
│        │  │  ├─ candle_cakes.json
│        │  │  ├─ can_glide_through.json
│        │  │  ├─ cauldrons.json
│        │  │  ├─ cave_vines.json
│        │  │  ├─ ceiling_hanging_signs.json
│        │  │  ├─ chains.json
│        │  │  ├─ cherry_logs.json
│        │  │  ├─ climbable.json
│        │  │  ├─ coal_ores.json
│        │  │  ├─ combination_step_sound_blocks.json
│        │  │  ├─ completes_find_tree_tutorial.json
│        │  │  ├─ concrete_powder.json
│        │  │  ├─ convertable_to_mud.json
│        │  │  ├─ copper.json
│        │  │  ├─ copper_chests.json
│        │  │  ├─ copper_golem_statues.json
│        │  │  ├─ copper_ores.json
│        │  │  ├─ corals.json
│        │  │  ├─ coral_blocks.json
│        │  │  ├─ coral_plants.json
│        │  │  ├─ crimson_stems.json
│        │  │  ├─ crops.json
│        │  │  ├─ crystal_sound_blocks.json
│        │  │  ├─ dampens_vibrations.json
│        │  │  ├─ dark_oak_logs.json
│        │  │  ├─ deepslate_ore_replaceables.json
│        │  │  ├─ diamond_ores.json
│        │  │  ├─ dirt.json
│        │  │  ├─ does_not_block_hoppers.json
│        │  │  ├─ doors.json
│        │  │  ├─ dragon_immune.json
│        │  │  ├─ dragon_transparent.json
│        │  │  ├─ dripstone_replaceable_blocks.json
│        │  │  ├─ dry_vegetation_may_place_on.json
│        │  │  ├─ edible_for_sheep.json
│        │  │  ├─ emerald_ores.json
│        │  │  ├─ enchantment_power_provider.json
│        │  │  ├─ enchantment_power_transmitter.json
│        │  │  ├─ enderman_holdable.json
│        │  │  ├─ fall_damage_resetting.json
│        │  │  ├─ features_cannot_replace.json
│        │  │  ├─ fences.json
│        │  │  ├─ fence_gates.json
│        │  │  ├─ fire.json
│        │  │  ├─ flowers.json
│        │  │  ├─ flower_pots.json
│        │  │  ├─ foxes_spawnable_on.json
│        │  │  ├─ frogs_spawnable_on.json
│        │  │  ├─ frog_prefer_jump_to.json
│        │  │  ├─ geode_invalid_blocks.json
│        │  │  ├─ goats_spawnable_on.json
│        │  │  ├─ gold_ores.json
│        │  │  ├─ guarded_by_piglins.json
│        │  │  ├─ happy_ghast_avoids.json
│        │  │  ├─ hoglin_repellents.json
│        │  │  ├─ ice.json
│        │  │  ├─ impermeable.json
│        │  │  ├─ incorrect_for_copper_tool.json
│        │  │  ├─ incorrect_for_diamond_tool.json
│        │  │  ├─ incorrect_for_gold_tool.json
│        │  │  ├─ incorrect_for_iron_tool.json
│        │  │  ├─ incorrect_for_netherite_tool.json
│        │  │  ├─ incorrect_for_stone_tool.json
│        │  │  ├─ incorrect_for_wooden_tool.json
│        │  │  ├─ infiniburn_end.json
│        │  │  ├─ infiniburn_nether.json
│        │  │  ├─ infiniburn_overworld.json
│        │  │  ├─ inside_step_sound_blocks.json
│        │  │  ├─ invalid_spawn_inside.json
│        │  │  ├─ iron_ores.json
│        │  │  ├─ jungle_logs.json
│        │  │  ├─ lanterns.json
│        │  │  ├─ lapis_ores.json
│        │  │  ├─ lava_pool_stone_cannot_replace.json
│        │  │  ├─ leaves.json
│        │  │  ├─ lightning_rods.json
│        │  │  ├─ logs.json
│        │  │  ├─ logs_that_burn.json
│        │  │  ├─ lush_ground_replaceable.json
│        │  │  ├─ maintains_farmland.json
│        │  │  ├─ mangrove_logs.json
│        │  │  ├─ mangrove_logs_can_grow_through.json
│        │  │  ├─ mangrove_roots_can_grow_through.json
│        │  │  ├─ mineable
│        │  │  │  ├─ axe.json
│        │  │  │  ├─ hoe.json
│        │  │  │  ├─ pickaxe.json
│        │  │  │  └─ shovel.json
│        │  │  ├─ mob_interactable_doors.json
│        │  │  ├─ mooshrooms_spawnable_on.json
│        │  │  ├─ moss_replaceable.json
│        │  │  ├─ mushroom_grow_block.json
│        │  │  ├─ needs_diamond_tool.json
│        │  │  ├─ needs_iron_tool.json
│        │  │  ├─ needs_stone_tool.json
│        │  │  ├─ nether_carver_replaceables.json
│        │  │  ├─ nylium.json
│        │  │  ├─ oak_logs.json
│        │  │  ├─ occludes_vibration_signals.json
│        │  │  ├─ overworld_carver_replaceables.json
│        │  │  ├─ overworld_natural_logs.json
│        │  │  ├─ pale_oak_logs.json
│        │  │  ├─ parrots_spawnable_on.json
│        │  │  ├─ piglin_repellents.json
│        │  │  ├─ planks.json
│        │  │  ├─ polar_bears_spawnable_on_alternate.json
│        │  │  ├─ portals.json
│        │  │  ├─ pressure_plates.json
│        │  │  ├─ prevent_mob_spawning_inside.json
│        │  │  ├─ rabbits_spawnable_on.json
│        │  │  ├─ rails.json
│        │  │  ├─ redstone_ores.json
│        │  │  ├─ replaceable.json
│        │  │  ├─ replaceable_by_mushrooms.json
│        │  │  ├─ replaceable_by_trees.json
│        │  │  ├─ sand.json
│        │  │  ├─ saplings.json
│        │  │  ├─ sculk_replaceable.json
│        │  │  ├─ sculk_replaceable_world_gen.json
│        │  │  ├─ shulker_boxes.json
│        │  │  ├─ signs.json
│        │  │  ├─ slabs.json
│        │  │  ├─ small_dripleaf_placeable.json
│        │  │  ├─ small_flowers.json
│        │  │  ├─ smelts_to_glass.json
│        │  │  ├─ snaps_goat_horn.json
│        │  │  ├─ sniffer_diggable_block.json
│        │  │  ├─ sniffer_egg_hatch_boost.json
│        │  │  ├─ snow.json
│        │  │  ├─ snow_layer_cannot_survive_on.json
│        │  │  ├─ snow_layer_can_survive_on.json
│        │  │  ├─ soul_fire_base_blocks.json
│        │  │  ├─ soul_speed_blocks.json
│        │  │  ├─ spruce_logs.json
│        │  │  ├─ stairs.json
│        │  │  ├─ standing_signs.json
│        │  │  ├─ stone_bricks.json
│        │  │  ├─ stone_buttons.json
│        │  │  ├─ stone_ore_replaceables.json
│        │  │  ├─ stone_pressure_plates.json
│        │  │  ├─ strider_warm_blocks.json
│        │  │  ├─ sword_efficient.json
│        │  │  ├─ sword_instantly_mines.json
│        │  │  ├─ terracotta.json
│        │  │  ├─ trail_ruins_replaceable.json
│        │  │  ├─ trapdoors.json
│        │  │  ├─ triggers_ambient_desert_dry_vegetation_block_sounds.json
│        │  │  ├─ triggers_ambient_desert_sand_block_sounds.json
│        │  │  ├─ triggers_ambient_dried_ghast_block_sounds.json
│        │  │  ├─ underwater_bonemeals.json
│        │  │  ├─ unstable_bottom_center.json
│        │  │  ├─ valid_spawn.json
│        │  │  ├─ vibration_resonators.json
│        │  │  ├─ walls.json
│        │  │  ├─ wall_corals.json
│        │  │  ├─ wall_hanging_signs.json
│        │  │  ├─ wall_post_override.json
│        │  │  ├─ wall_signs.json
│        │  │  ├─ warped_stems.json
│        │  │  ├─ wart_blocks.json
│        │  │  ├─ wither_immune.json
│        │  │  ├─ wither_summon_base_blocks.json
│        │  │  ├─ wolves_spawnable_on.json
│        │  │  ├─ wooden_buttons.json
│        │  │  ├─ wooden_doors.json
│        │  │  ├─ wooden_fences.json
│        │  │  ├─ wooden_pressure_plates.json
│        │  │  ├─ wooden_shelves.json
│        │  │  ├─ wooden_slabs.json
│        │  │  ├─ wooden_stairs.json
│        │  │  ├─ wooden_trapdoors.json
│        │  │  ├─ wool.json
│        │  │  └─ wool_carpets.json
│        │  ├─ damage_type
│        │  │  ├─ always_hurts_ender_dragons.json
│        │  │  ├─ always_kills_armor_stands.json
│        │  │  ├─ always_most_significant_fall.json
│        │  │  ├─ always_triggers_silverfish.json
│        │  │  ├─ avoids_guardian_thorns.json
│        │  │  ├─ burns_armor_stands.json
│        │  │  ├─ burn_from_stepping.json
│        │  │  ├─ bypasses_armor.json
│        │  │  ├─ bypasses_effects.json
│        │  │  ├─ bypasses_enchantments.json
│        │  │  ├─ bypasses_invulnerability.json
│        │  │  ├─ bypasses_resistance.json
│        │  │  ├─ bypasses_shield.json
│        │  │  ├─ bypasses_wolf_armor.json
│        │  │  ├─ can_break_armor_stand.json
│        │  │  ├─ damages_helmet.json
│        │  │  ├─ ignites_armor_stands.json
│        │  │  ├─ is_drowning.json
│        │  │  ├─ is_explosion.json
│        │  │  ├─ is_fall.json
│        │  │  ├─ is_fire.json
│        │  │  ├─ is_freezing.json
│        │  │  ├─ is_lightning.json
│        │  │  ├─ is_player_attack.json
│        │  │  ├─ is_projectile.json
│        │  │  ├─ mace_smash.json
│        │  │  ├─ no_anger.json
│        │  │  ├─ no_impact.json
│        │  │  ├─ no_knockback.json
│        │  │  ├─ panic_causes.json
│        │  │  ├─ panic_environmental_causes.json
│        │  │  ├─ witch_resistant_to.json
│        │  │  └─ wither_immune_to.json
│        │  ├─ dialog
│        │  │  ├─ pause_screen_additions.json
│        │  │  └─ quick_actions.json
│        │  ├─ enchantment
│        │  │  ├─ curse.json
│        │  │  ├─ double_trade_price.json
│        │  │  ├─ exclusive_set
│        │  │  │  ├─ armor.json
│        │  │  │  ├─ boots.json
│        │  │  │  ├─ bow.json
│        │  │  │  ├─ crossbow.json
│        │  │  │  ├─ damage.json
│        │  │  │  ├─ mining.json
│        │  │  │  └─ riptide.json
│        │  │  ├─ in_enchanting_table.json
│        │  │  ├─ non_treasure.json
│        │  │  ├─ on_mob_spawn_equipment.json
│        │  │  ├─ on_random_loot.json
│        │  │  ├─ on_traded_equipment.json
│        │  │  ├─ prevents_bee_spawns_when_mining.json
│        │  │  ├─ prevents_decorated_pot_shattering.json
│        │  │  ├─ prevents_ice_melting.json
│        │  │  ├─ prevents_infested_spawns.json
│        │  │  ├─ smelts_loot.json
│        │  │  ├─ tooltip_order.json
│        │  │  ├─ tradeable.json
│        │  │  └─ treasure.json
│        │  ├─ entity_type
│        │  │  ├─ accepts_iron_golem_gift.json
│        │  │  ├─ aquatic.json
│        │  │  ├─ arrows.json
│        │  │  ├─ arthropod.json
│        │  │  ├─ axolotl_always_hostiles.json
│        │  │  ├─ axolotl_hunt_targets.json
│        │  │  ├─ beehive_inhabitors.json
│        │  │  ├─ boat.json
│        │  │  ├─ burn_in_daylight.json
│        │  │  ├─ candidate_for_iron_golem_gift.json
│        │  │  ├─ cannot_be_pushed_onto_boats.json
│        │  │  ├─ can_breathe_under_water.json
│        │  │  ├─ can_equip_harness.json
│        │  │  ├─ can_equip_saddle.json
│        │  │  ├─ can_float_while_ridden.json
│        │  │  ├─ can_turn_in_boats.json
│        │  │  ├─ can_wear_horse_armor.json
│        │  │  ├─ can_wear_nautilus_armor.json
│        │  │  ├─ deflects_projectiles.json
│        │  │  ├─ dismounts_underwater.json
│        │  │  ├─ fall_damage_immune.json
│        │  │  ├─ followable_friendly_mobs.json
│        │  │  ├─ freeze_hurts_extra_types.json
│        │  │  ├─ freeze_immune_entity_types.json
│        │  │  ├─ frog_food.json
│        │  │  ├─ ignores_poison_and_regen.json
│        │  │  ├─ illager.json
│        │  │  ├─ illager_friends.json
│        │  │  ├─ immune_to_infested.json
│        │  │  ├─ immune_to_oozing.json
│        │  │  ├─ impact_projectiles.json
│        │  │  ├─ inverted_healing_and_harm.json
│        │  │  ├─ nautilus_hostiles.json
│        │  │  ├─ non_controlling_rider.json
│        │  │  ├─ not_scary_for_pufferfish.json
│        │  │  ├─ no_anger_from_wind_charge.json
│        │  │  ├─ powder_snow_walkable_mobs.json
│        │  │  ├─ raiders.json
│        │  │  ├─ redirectable_projectile.json
│        │  │  ├─ sensitive_to_bane_of_arthropods.json
│        │  │  ├─ sensitive_to_impaling.json
│        │  │  ├─ sensitive_to_smite.json
│        │  │  ├─ skeletons.json
│        │  │  ├─ undead.json
│        │  │  ├─ wither_friends.json
│        │  │  └─ zombies.json
│        │  ├─ fluid
│        │  │  ├─ lava.json
│        │  │  └─ water.json
│        │  ├─ game_event
│        │  │  ├─ allay_can_listen.json
│        │  │  ├─ ignore_vibrations_sneaking.json
│        │  │  ├─ shrieker_can_listen.json
│        │  │  ├─ vibrations.json
│        │  │  └─ warden_can_listen.json
│        │  ├─ instrument
│        │  │  ├─ goat_horns.json
│        │  │  ├─ regular_goat_horns.json
│        │  │  └─ screaming_goat_horns.json
│        │  ├─ item
│        │  │  ├─ acacia_logs.json
│        │  │  ├─ anvil.json
│        │  │  ├─ armadillo_food.json
│        │  │  ├─ arrows.json
│        │  │  ├─ axes.json
│        │  │  ├─ axolotl_food.json
│        │  │  ├─ bamboo_blocks.json
│        │  │  ├─ banners.json
│        │  │  ├─ bars.json
│        │  │  ├─ beacon_payment_items.json
│        │  │  ├─ beds.json
│        │  │  ├─ bee_food.json
│        │  │  ├─ birch_logs.json
│        │  │  ├─ boats.json
│        │  │  ├─ bookshelf_books.json
│        │  │  ├─ book_cloning_target.json
│        │  │  ├─ breaks_decorated_pots.json
│        │  │  ├─ brewing_fuel.json
│        │  │  ├─ bundles.json
│        │  │  ├─ buttons.json
│        │  │  ├─ camel_food.json
│        │  │  ├─ camel_husk_food.json
│        │  │  ├─ candles.json
│        │  │  ├─ cat_food.json
│        │  │  ├─ chains.json
│        │  │  ├─ cherry_logs.json
│        │  │  ├─ chest_armor.json
│        │  │  ├─ chest_boats.json
│        │  │  ├─ chicken_food.json
│        │  │  ├─ cluster_max_harvestables.json
│        │  │  ├─ coals.json
│        │  │  ├─ coal_ores.json
│        │  │  ├─ compasses.json
│        │  │  ├─ completes_find_tree_tutorial.json
│        │  │  ├─ copper.json
│        │  │  ├─ copper_chests.json
│        │  │  ├─ copper_golem_statues.json
│        │  │  ├─ copper_ores.json
│        │  │  ├─ copper_tool_materials.json
│        │  │  ├─ cow_food.json
│        │  │  ├─ creeper_drop_music_discs.json
│        │  │  ├─ creeper_igniters.json
│        │  │  ├─ crimson_stems.json
│        │  │  ├─ dampens_vibrations.json
│        │  │  ├─ dark_oak_logs.json
│        │  │  ├─ decorated_pot_ingredients.json
│        │  │  ├─ decorated_pot_sherds.json
│        │  │  ├─ diamond_ores.json
│        │  │  ├─ diamond_tool_materials.json
│        │  │  ├─ dirt.json
│        │  │  ├─ doors.json
│        │  │  ├─ drowned_preferred_weapons.json
│        │  │  ├─ duplicates_allays.json
│        │  │  ├─ dyeable.json
│        │  │  ├─ eggs.json
│        │  │  ├─ emerald_ores.json
│        │  │  ├─ enchantable
│        │  │  │  ├─ armor.json
│        │  │  │  ├─ bow.json
│        │  │  │  ├─ chest_armor.json
│        │  │  │  ├─ crossbow.json
│        │  │  │  ├─ durability.json
│        │  │  │  ├─ equippable.json
│        │  │  │  ├─ fire_aspect.json
│        │  │  │  ├─ fishing.json
│        │  │  │  ├─ foot_armor.json
│        │  │  │  ├─ head_armor.json
│        │  │  │  ├─ leg_armor.json
│        │  │  │  ├─ lunge.json
│        │  │  │  ├─ mace.json
│        │  │  │  ├─ melee_weapon.json
│        │  │  │  ├─ mining.json
│        │  │  │  ├─ mining_loot.json
│        │  │  │  ├─ sharp_weapon.json
│        │  │  │  ├─ sweeping.json
│        │  │  │  ├─ trident.json
│        │  │  │  ├─ vanishing.json
│        │  │  │  └─ weapon.json
│        │  │  ├─ fences.json
│        │  │  ├─ fence_gates.json
│        │  │  ├─ fishes.json
│        │  │  ├─ flowers.json
│        │  │  ├─ foot_armor.json
│        │  │  ├─ fox_food.json
│        │  │  ├─ freeze_immune_wearables.json
│        │  │  ├─ frog_food.json
│        │  │  ├─ furnace_minecart_fuel.json
│        │  │  ├─ gaze_disguise_equipment.json
│        │  │  ├─ goat_food.json
│        │  │  ├─ gold_ores.json
│        │  │  ├─ gold_tool_materials.json
│        │  │  ├─ hanging_signs.json
│        │  │  ├─ happy_ghast_food.json
│        │  │  ├─ happy_ghast_tempt_items.json
│        │  │  ├─ harnesses.json
│        │  │  ├─ head_armor.json
│        │  │  ├─ hoes.json
│        │  │  ├─ hoglin_food.json
│        │  │  ├─ horse_food.json
│        │  │  ├─ horse_tempt_items.json
│        │  │  ├─ ignored_by_piglin_babies.json
│        │  │  ├─ iron_ores.json
│        │  │  ├─ iron_tool_materials.json
│        │  │  ├─ jungle_logs.json
│        │  │  ├─ lanterns.json
│        │  │  ├─ lapis_ores.json
│        │  │  ├─ leaves.json
│        │  │  ├─ lectern_books.json
│        │  │  ├─ leg_armor.json
│        │  │  ├─ lightning_rods.json
│        │  │  ├─ llama_food.json
│        │  │  ├─ llama_tempt_items.json
│        │  │  ├─ logs.json
│        │  │  ├─ logs_that_burn.json
│        │  │  ├─ mangrove_logs.json
│        │  │  ├─ map_invisibility_equipment.json
│        │  │  ├─ meat.json
│        │  │  ├─ nautilus_bucket_food.json
│        │  │  ├─ nautilus_food.json
│        │  │  ├─ nautilus_taming_items.json
│        │  │  ├─ netherite_tool_materials.json
│        │  │  ├─ non_flammable_wood.json
│        │  │  ├─ noteblock_top_instruments.json
│        │  │  ├─ oak_logs.json
│        │  │  ├─ ocelot_food.json
│        │  │  ├─ pale_oak_logs.json
│        │  │  ├─ panda_eats_from_ground.json
│        │  │  ├─ panda_food.json
│        │  │  ├─ parrot_food.json
│        │  │  ├─ parrot_poisonous_food.json
│        │  │  ├─ pickaxes.json
│        │  │  ├─ piglin_food.json
│        │  │  ├─ piglin_loved.json
│        │  │  ├─ piglin_preferred_weapons.json
│        │  │  ├─ piglin_repellents.json
│        │  │  ├─ piglin_safe_armor.json
│        │  │  ├─ pig_food.json
│        │  │  ├─ pillager_preferred_weapons.json
│        │  │  ├─ planks.json
│        │  │  ├─ rabbit_food.json
│        │  │  ├─ rails.json
│        │  │  ├─ redstone_ores.json
│        │  │  ├─ repairs_chain_armor.json
│        │  │  ├─ repairs_copper_armor.json
│        │  │  ├─ repairs_diamond_armor.json
│        │  │  ├─ repairs_gold_armor.json
│        │  │  ├─ repairs_iron_armor.json
│        │  │  ├─ repairs_leather_armor.json
│        │  │  ├─ repairs_netherite_armor.json
│        │  │  ├─ repairs_turtle_helmet.json
│        │  │  ├─ repairs_wolf_armor.json
│        │  │  ├─ sand.json
│        │  │  ├─ saplings.json
│        │  │  ├─ shearable_from_copper_golem.json
│        │  │  ├─ sheep_food.json
│        │  │  ├─ shovels.json
│        │  │  ├─ shulker_boxes.json
│        │  │  ├─ signs.json
│        │  │  ├─ skeleton_preferred_weapons.json
│        │  │  ├─ skulls.json
│        │  │  ├─ slabs.json
│        │  │  ├─ small_flowers.json
│        │  │  ├─ smelts_to_glass.json
│        │  │  ├─ sniffer_food.json
│        │  │  ├─ soul_fire_base_blocks.json
│        │  │  ├─ spears.json
│        │  │  ├─ spruce_logs.json
│        │  │  ├─ stairs.json
│        │  │  ├─ stone_bricks.json
│        │  │  ├─ stone_buttons.json
│        │  │  ├─ stone_crafting_materials.json
│        │  │  ├─ stone_tool_materials.json
│        │  │  ├─ strider_food.json
│        │  │  ├─ strider_tempt_items.json
│        │  │  ├─ swords.json
│        │  │  ├─ terracotta.json
│        │  │  ├─ trapdoors.json
│        │  │  ├─ trimmable_armor.json
│        │  │  ├─ trim_materials.json
│        │  │  ├─ turtle_food.json
│        │  │  ├─ villager_picks_up.json
│        │  │  ├─ villager_plantable_seeds.json
│        │  │  ├─ walls.json
│        │  │  ├─ warped_stems.json
│        │  │  ├─ wart_blocks.json
│        │  │  ├─ wither_skeleton_disliked_weapons.json
│        │  │  ├─ wolf_food.json
│        │  │  ├─ wooden_buttons.json
│        │  │  ├─ wooden_doors.json
│        │  │  ├─ wooden_fences.json
│        │  │  ├─ wooden_pressure_plates.json
│        │  │  ├─ wooden_shelves.json
│        │  │  ├─ wooden_slabs.json
│        │  │  ├─ wooden_stairs.json
│        │  │  ├─ wooden_tool_materials.json
│        │  │  ├─ wooden_trapdoors.json
│        │  │  ├─ wool.json
│        │  │  ├─ wool_carpets.json
│        │  │  └─ zombie_horse_food.json
│        │  ├─ painting_variant
│        │  │  └─ placeable.json
│        │  ├─ point_of_interest_type
│        │  │  ├─ acquirable_job_site.json
│        │  │  ├─ bee_home.json
│        │  │  └─ village.json
│        │  ├─ timeline
│        │  │  ├─ in_end.json
│        │  │  ├─ in_nether.json
│        │  │  ├─ in_overworld.json
│        │  │  └─ universal.json
│        │  └─ worldgen
│        │     ├─ biome
│        │     │  ├─ allows_surface_slime_spawns.json
│        │     │  ├─ allows_tropical_fish_spawns_at_any_height.json
│        │     │  ├─ has_structure
│        │     │  │  ├─ ancient_city.json
│        │     │  │  ├─ bastion_remnant.json
│        │     │  │  ├─ buried_treasure.json
│        │     │  │  ├─ desert_pyramid.json
│        │     │  │  ├─ end_city.json
│        │     │  │  ├─ igloo.json
│        │     │  │  ├─ jungle_temple.json
│        │     │  │  ├─ mineshaft.json
│        │     │  │  ├─ mineshaft_mesa.json
│        │     │  │  ├─ nether_fortress.json
│        │     │  │  ├─ nether_fossil.json
│        │     │  │  ├─ ocean_monument.json
│        │     │  │  ├─ ocean_ruin_cold.json
│        │     │  │  ├─ ocean_ruin_warm.json
│        │     │  │  ├─ pillager_outpost.json
│        │     │  │  ├─ ruined_portal_desert.json
│        │     │  │  ├─ ruined_portal_jungle.json
│        │     │  │  ├─ ruined_portal_mountain.json
│        │     │  │  ├─ ruined_portal_nether.json
│        │     │  │  ├─ ruined_portal_ocean.json
│        │     │  │  ├─ ruined_portal_standard.json
│        │     │  │  ├─ ruined_portal_swamp.json
│        │     │  │  ├─ shipwreck.json
│        │     │  │  ├─ shipwreck_beached.json
│        │     │  │  ├─ stronghold.json
│        │     │  │  ├─ swamp_hut.json
│        │     │  │  ├─ trail_ruins.json
│        │     │  │  ├─ trial_chambers.json
│        │     │  │  ├─ village_desert.json
│        │     │  │  ├─ village_plains.json
│        │     │  │  ├─ village_savanna.json
│        │     │  │  ├─ village_snowy.json
│        │     │  │  ├─ village_taiga.json
│        │     │  │  └─ woodland_mansion.json
│        │     │  ├─ is_badlands.json
│        │     │  ├─ is_beach.json
│        │     │  ├─ is_deep_ocean.json
│        │     │  ├─ is_end.json
│        │     │  ├─ is_forest.json
│        │     │  ├─ is_hill.json
│        │     │  ├─ is_jungle.json
│        │     │  ├─ is_mountain.json
│        │     │  ├─ is_nether.json
│        │     │  ├─ is_ocean.json
│        │     │  ├─ is_overworld.json
│        │     │  ├─ is_river.json
│        │     │  ├─ is_savanna.json
│        │     │  ├─ is_taiga.json
│        │     │  ├─ mineshaft_blocking.json
│        │     │  ├─ more_frequent_drowned_spawns.json
│        │     │  ├─ polar_bears_spawn_on_alternate_blocks.json
│        │     │  ├─ produces_corals_from_bonemeal.json
│        │     │  ├─ reduce_water_ambient_spawns.json
│        │     │  ├─ required_ocean_monument_surrounding.json
│        │     │  ├─ spawns_cold_variant_farm_animals.json
│        │     │  ├─ spawns_cold_variant_frogs.json
│        │     │  ├─ spawns_coral_variant_zombie_nautilus.json
│        │     │  ├─ spawns_gold_rabbits.json
│        │     │  ├─ spawns_snow_foxes.json
│        │     │  ├─ spawns_warm_variant_farm_animals.json
│        │     │  ├─ spawns_warm_variant_frogs.json
│        │     │  ├─ spawns_white_rabbits.json
│        │     │  ├─ stronghold_biased_to.json
│        │     │  ├─ water_on_map_outlines.json
│        │     │  ├─ without_wandering_trader_spawns.json
│        │     │  └─ without_zombie_sieges.json
│        │     ├─ flat_level_generator_preset
│        │     │  └─ visible.json
│        │     ├─ structure
│        │     │  ├─ cats_spawn_as_black.json
│        │     │  ├─ cats_spawn_in.json
│        │     │  ├─ dolphin_located.json
│        │     │  ├─ eye_of_ender_located.json
│        │     │  ├─ mineshaft.json
│        │     │  ├─ ocean_ruin.json
│        │     │  ├─ on_desert_village_maps.json
│        │     │  ├─ on_jungle_explorer_maps.json
│        │     │  ├─ on_ocean_explorer_maps.json
│        │     │  ├─ on_plains_village_maps.json
│        │     │  ├─ on_savanna_village_maps.json
│        │     │  ├─ on_snowy_village_maps.json
│        │     │  ├─ on_swamp_explorer_maps.json
│        │     │  ├─ on_taiga_village_maps.json
│        │     │  ├─ on_treasure_maps.json
│        │     │  ├─ on_trial_chambers_maps.json
│        │     │  ├─ on_woodland_explorer_maps.json
│        │     │  ├─ ruined_portal.json
│        │     │  ├─ shipwreck.json
│        │     │  └─ village.json
│        │     └─ world_preset
│        │        ├─ extended.json
│        │        └─ normal.json
│        ├─ test_environment
│        │  └─ default.json
│        ├─ test_instance
│        │  └─ always_pass.json
│        ├─ timeline
│        │  ├─ day.json
│        │  ├─ early_game.json
│        │  ├─ moon.json
│        │  └─ villager_schedule.json
│        ├─ trial_spawner
│        │  └─ trial_chamber
│        │     ├─ breeze
│        │     │  ├─ normal.json
│        │     │  └─ ominous.json
│        │     ├─ melee
│        │     │  ├─ husk
│        │     │  │  ├─ normal.json
│        │     │  │  └─ ominous.json
│        │     │  ├─ spider
│        │     │  │  ├─ normal.json
│        │     │  │  └─ ominous.json
│        │     │  └─ zombie
│        │     │     ├─ normal.json
│        │     │     └─ ominous.json
│        │     ├─ ranged
│        │     │  ├─ poison_skeleton
│        │     │  │  ├─ normal.json
│        │     │  │  └─ ominous.json
│        │     │  ├─ skeleton
│        │     │  │  ├─ normal.json
│        │     │  │  └─ ominous.json
│        │     │  └─ stray
│        │     │     ├─ normal.json
│        │     │     └─ ominous.json
│        │     ├─ slow_ranged
│        │     │  ├─ poison_skeleton
│        │     │  │  ├─ normal.json
│        │     │  │  └─ ominous.json
│        │     │  ├─ skeleton
│        │     │  │  ├─ normal.json
│        │     │  │  └─ ominous.json
│        │     │  └─ stray
│        │     │     ├─ normal.json
│        │     │     └─ ominous.json
│        │     └─ small_melee
│        │        ├─ baby_zombie
│        │        │  ├─ normal.json
│        │        │  └─ ominous.json
│        │        ├─ cave_spider
│        │        │  ├─ normal.json
│        │        │  └─ ominous.json
│        │        ├─ silverfish
│        │        │  ├─ normal.json
│        │        │  └─ ominous.json
│        │        └─ slime
│        │           ├─ normal.json
│        │           └─ ominous.json
│        ├─ trim_material
│        │  ├─ amethyst.json
│        │  ├─ copper.json
│        │  ├─ diamond.json
│        │  ├─ emerald.json
│        │  ├─ gold.json
│        │  ├─ iron.json
│        │  ├─ lapis.json
│        │  ├─ netherite.json
│        │  ├─ quartz.json
│        │  ├─ redstone.json
│        │  └─ resin.json
│        ├─ trim_pattern
│        │  ├─ bolt.json
│        │  ├─ coast.json
│        │  ├─ dune.json
│        │  ├─ eye.json
│        │  ├─ flow.json
│        │  ├─ host.json
│        │  ├─ raiser.json
│        │  ├─ rib.json
│        │  ├─ sentry.json
│        │  ├─ shaper.json
│        │  ├─ silence.json
│        │  ├─ snout.json
│        │  ├─ spire.json
│        │  ├─ tide.json
│        │  ├─ vex.json
│        │  ├─ ward.json
│        │  ├─ wayfinder.json
│        │  └─ wild.json
│        ├─ wolf_sound_variant
│        │  ├─ angry.json
│        │  ├─ big.json
│        │  ├─ classic.json
│        │  ├─ cute.json
│        │  ├─ grumpy.json
│        │  ├─ puglin.json
│        │  └─ sad.json
│        ├─ wolf_variant
│        │  ├─ ashen.json
│        │  ├─ black.json
│        │  ├─ chestnut.json
│        │  ├─ pale.json
│        │  ├─ rusty.json
│        │  ├─ snowy.json
│        │  ├─ spotted.json
│        │  ├─ striped.json
│        │  └─ woods.json
│        ├─ worldgen
│        │  ├─ biome
│        │  │  ├─ badlands.json
│        │  │  ├─ bamboo_jungle.json
│        │  │  ├─ basalt_deltas.json
│        │  │  ├─ beach.json
│        │  │  ├─ birch_forest.json
│        │  │  ├─ cherry_grove.json
│        │  │  ├─ cold_ocean.json
│        │  │  ├─ crimson_forest.json
│        │  │  ├─ dark_forest.json
│        │  │  ├─ deep_cold_ocean.json
│        │  │  ├─ deep_dark.json
│        │  │  ├─ deep_frozen_ocean.json
│        │  │  ├─ deep_lukewarm_ocean.json
│        │  │  ├─ deep_ocean.json
│        │  │  ├─ desert.json
│        │  │  ├─ dripstone_caves.json
│        │  │  ├─ end_barrens.json
│        │  │  ├─ end_highlands.json
│        │  │  ├─ end_midlands.json
│        │  │  ├─ eroded_badlands.json
│        │  │  ├─ flower_forest.json
│        │  │  ├─ forest.json
│        │  │  ├─ frozen_ocean.json
│        │  │  ├─ frozen_peaks.json
│        │  │  ├─ frozen_river.json
│        │  │  ├─ grove.json
│        │  │  ├─ ice_spikes.json
│        │  │  ├─ jagged_peaks.json
│        │  │  ├─ jungle.json
│        │  │  ├─ lukewarm_ocean.json
│        │  │  ├─ lush_caves.json
│        │  │  ├─ mangrove_swamp.json
│        │  │  ├─ meadow.json
│        │  │  ├─ mushroom_fields.json
│        │  │  ├─ nether_wastes.json
│        │  │  ├─ ocean.json
│        │  │  ├─ old_growth_birch_forest.json
│        │  │  ├─ old_growth_pine_taiga.json
│        │  │  ├─ old_growth_spruce_taiga.json
│        │  │  ├─ pale_garden.json
│        │  │  ├─ plains.json
│        │  │  ├─ river.json
│        │  │  ├─ savanna.json
│        │  │  ├─ savanna_plateau.json
│        │  │  ├─ small_end_islands.json
│        │  │  ├─ snowy_beach.json
│        │  │  ├─ snowy_plains.json
│        │  │  ├─ snowy_slopes.json
│        │  │  ├─ snowy_taiga.json
│        │  │  ├─ soul_sand_valley.json
│        │  │  ├─ sparse_jungle.json
│        │  │  ├─ stony_peaks.json
│        │  │  ├─ stony_shore.json
│        │  │  ├─ sunflower_plains.json
│        │  │  ├─ swamp.json
│        │  │  ├─ taiga.json
│        │  │  ├─ the_end.json
│        │  │  ├─ the_void.json
│        │  │  ├─ warm_ocean.json
│        │  │  ├─ warped_forest.json
│        │  │  ├─ windswept_forest.json
│        │  │  ├─ windswept_gravelly_hills.json
│        │  │  ├─ windswept_hills.json
│        │  │  ├─ windswept_savanna.json
│        │  │  └─ wooded_badlands.json
│        │  ├─ configured_carver
│        │  │  ├─ canyon.json
│        │  │  ├─ cave.json
│        │  │  ├─ cave_extra_underground.json
│        │  │  └─ nether_cave.json
│        │  ├─ configured_feature
│        │  │  ├─ acacia.json
│        │  │  ├─ amethyst_geode.json
│        │  │  ├─ azalea_tree.json
│        │  │  ├─ bamboo_no_podzol.json
│        │  │  ├─ bamboo_some_podzol.json
│        │  │  ├─ bamboo_vegetation.json
│        │  │  ├─ basalt_blobs.json
│        │  │  ├─ basalt_pillar.json
│        │  │  ├─ birch.json
│        │  │  ├─ birch_bees_0002.json
│        │  │  ├─ birch_bees_0002_leaf_litter.json
│        │  │  ├─ birch_bees_002.json
│        │  │  ├─ birch_bees_005.json
│        │  │  ├─ birch_leaf_litter.json
│        │  │  ├─ birch_tall.json
│        │  │  ├─ blackstone_blobs.json
│        │  │  ├─ blue_ice.json
│        │  │  ├─ bonus_chest.json
│        │  │  ├─ cave_vine.json
│        │  │  ├─ cave_vine_in_moss.json
│        │  │  ├─ cherry.json
│        │  │  ├─ cherry_bees_005.json
│        │  │  ├─ chorus_plant.json
│        │  │  ├─ clay_pool_with_dripleaves.json
│        │  │  ├─ clay_with_dripleaves.json
│        │  │  ├─ crimson_forest_vegetation.json
│        │  │  ├─ crimson_forest_vegetation_bonemeal.json
│        │  │  ├─ crimson_fungus.json
│        │  │  ├─ crimson_fungus_planted.json
│        │  │  ├─ dark_forest_vegetation.json
│        │  │  ├─ dark_oak.json
│        │  │  ├─ dark_oak_leaf_litter.json
│        │  │  ├─ delta.json
│        │  │  ├─ desert_well.json
│        │  │  ├─ disk_clay.json
│        │  │  ├─ disk_grass.json
│        │  │  ├─ disk_gravel.json
│        │  │  ├─ disk_sand.json
│        │  │  ├─ dripleaf.json
│        │  │  ├─ dripstone_cluster.json
│        │  │  ├─ end_gateway_delayed.json
│        │  │  ├─ end_gateway_return.json
│        │  │  ├─ end_island.json
│        │  │  ├─ end_platform.json
│        │  │  ├─ end_spike.json
│        │  │  ├─ fallen_birch_tree.json
│        │  │  ├─ fallen_jungle_tree.json
│        │  │  ├─ fallen_oak_tree.json
│        │  │  ├─ fallen_spruce_tree.json
│        │  │  ├─ fallen_super_birch_tree.json
│        │  │  ├─ fancy_oak.json
│        │  │  ├─ fancy_oak_bees.json
│        │  │  ├─ fancy_oak_bees_0002_leaf_litter.json
│        │  │  ├─ fancy_oak_bees_002.json
│        │  │  ├─ fancy_oak_bees_005.json
│        │  │  ├─ fancy_oak_leaf_litter.json
│        │  │  ├─ flower_cherry.json
│        │  │  ├─ flower_default.json
│        │  │  ├─ flower_flower_forest.json
│        │  │  ├─ flower_meadow.json
│        │  │  ├─ flower_pale_garden.json
│        │  │  ├─ flower_plain.json
│        │  │  ├─ flower_swamp.json
│        │  │  ├─ forest_flowers.json
│        │  │  ├─ forest_rock.json
│        │  │  ├─ fossil_coal.json
│        │  │  ├─ fossil_diamonds.json
│        │  │  ├─ freeze_top_layer.json
│        │  │  ├─ glowstone_extra.json
│        │  │  ├─ glow_lichen.json
│        │  │  ├─ huge_brown_mushroom.json
│        │  │  ├─ huge_red_mushroom.json
│        │  │  ├─ iceberg_blue.json
│        │  │  ├─ iceberg_packed.json
│        │  │  ├─ ice_patch.json
│        │  │  ├─ ice_spike.json
│        │  │  ├─ jungle_bush.json
│        │  │  ├─ jungle_tree.json
│        │  │  ├─ jungle_tree_no_vine.json
│        │  │  ├─ kelp.json
│        │  │  ├─ lake_lava.json
│        │  │  ├─ large_basalt_columns.json
│        │  │  ├─ large_dripstone.json
│        │  │  ├─ lush_caves_clay.json
│        │  │  ├─ mangrove.json
│        │  │  ├─ mangrove_vegetation.json
│        │  │  ├─ meadow_trees.json
│        │  │  ├─ mega_jungle_tree.json
│        │  │  ├─ mega_pine.json
│        │  │  ├─ mega_spruce.json
│        │  │  ├─ monster_room.json
│        │  │  ├─ moss_patch.json
│        │  │  ├─ moss_patch_bonemeal.json
│        │  │  ├─ moss_patch_ceiling.json
│        │  │  ├─ moss_vegetation.json
│        │  │  ├─ mushroom_island_vegetation.json
│        │  │  ├─ nether_sprouts.json
│        │  │  ├─ nether_sprouts_bonemeal.json
│        │  │  ├─ oak.json
│        │  │  ├─ oak_bees_0002_leaf_litter.json
│        │  │  ├─ oak_bees_002.json
│        │  │  ├─ oak_bees_005.json
│        │  │  ├─ oak_leaf_litter.json
│        │  │  ├─ ore_ancient_debris_large.json
│        │  │  ├─ ore_ancient_debris_small.json
│        │  │  ├─ ore_andesite.json
│        │  │  ├─ ore_blackstone.json
│        │  │  ├─ ore_clay.json
│        │  │  ├─ ore_coal.json
│        │  │  ├─ ore_coal_buried.json
│        │  │  ├─ ore_copper_large.json
│        │  │  ├─ ore_copper_small.json
│        │  │  ├─ ore_diamond_buried.json
│        │  │  ├─ ore_diamond_large.json
│        │  │  ├─ ore_diamond_medium.json
│        │  │  ├─ ore_diamond_small.json
│        │  │  ├─ ore_diorite.json
│        │  │  ├─ ore_dirt.json
│        │  │  ├─ ore_emerald.json
│        │  │  ├─ ore_gold.json
│        │  │  ├─ ore_gold_buried.json
│        │  │  ├─ ore_granite.json
│        │  │  ├─ ore_gravel.json
│        │  │  ├─ ore_gravel_nether.json
│        │  │  ├─ ore_infested.json
│        │  │  ├─ ore_iron.json
│        │  │  ├─ ore_iron_small.json
│        │  │  ├─ ore_lapis.json
│        │  │  ├─ ore_lapis_buried.json
│        │  │  ├─ ore_magma.json
│        │  │  ├─ ore_nether_gold.json
│        │  │  ├─ ore_quartz.json
│        │  │  ├─ ore_redstone.json
│        │  │  ├─ ore_soul_sand.json
│        │  │  ├─ ore_tuff.json
│        │  │  ├─ pale_forest_flowers.json
│        │  │  ├─ pale_garden_vegetation.json
│        │  │  ├─ pale_moss_patch.json
│        │  │  ├─ pale_moss_patch_bonemeal.json
│        │  │  ├─ pale_moss_vegetation.json
│        │  │  ├─ pale_oak.json
│        │  │  ├─ pale_oak_bonemeal.json
│        │  │  ├─ pale_oak_creaking.json
│        │  │  ├─ patch_berry_bush.json
│        │  │  ├─ patch_brown_mushroom.json
│        │  │  ├─ patch_bush.json
│        │  │  ├─ patch_cactus.json
│        │  │  ├─ patch_crimson_roots.json
│        │  │  ├─ patch_dead_bush.json
│        │  │  ├─ patch_dry_grass.json
│        │  │  ├─ patch_fire.json
│        │  │  ├─ patch_firefly_bush.json
│        │  │  ├─ patch_grass.json
│        │  │  ├─ patch_grass_jungle.json
│        │  │  ├─ patch_grass_meadow.json
│        │  │  ├─ patch_large_fern.json
│        │  │  ├─ patch_leaf_litter.json
│        │  │  ├─ patch_melon.json
│        │  │  ├─ patch_pumpkin.json
│        │  │  ├─ patch_red_mushroom.json
│        │  │  ├─ patch_soul_fire.json
│        │  │  ├─ patch_sugar_cane.json
│        │  │  ├─ patch_sunflower.json
│        │  │  ├─ patch_taiga_grass.json
│        │  │  ├─ patch_tall_grass.json
│        │  │  ├─ patch_waterlily.json
│        │  │  ├─ pile_hay.json
│        │  │  ├─ pile_ice.json
│        │  │  ├─ pile_melon.json
│        │  │  ├─ pile_pumpkin.json
│        │  │  ├─ pile_snow.json
│        │  │  ├─ pine.json
│        │  │  ├─ pointed_dripstone.json
│        │  │  ├─ rooted_azalea_tree.json
│        │  │  ├─ sculk_patch_ancient_city.json
│        │  │  ├─ sculk_patch_deep_dark.json
│        │  │  ├─ sculk_vein.json
│        │  │  ├─ seagrass_mid.json
│        │  │  ├─ seagrass_short.json
│        │  │  ├─ seagrass_slightly_less_short.json
│        │  │  ├─ seagrass_tall.json
│        │  │  ├─ sea_pickle.json
│        │  │  ├─ single_piece_of_grass.json
│        │  │  ├─ small_basalt_columns.json
│        │  │  ├─ spore_blossom.json
│        │  │  ├─ spring_lava_frozen.json
│        │  │  ├─ spring_lava_nether.json
│        │  │  ├─ spring_lava_overworld.json
│        │  │  ├─ spring_nether_closed.json
│        │  │  ├─ spring_nether_open.json
│        │  │  ├─ spring_water.json
│        │  │  ├─ spruce.json
│        │  │  ├─ super_birch_bees.json
│        │  │  ├─ super_birch_bees_0002.json
│        │  │  ├─ swamp_oak.json
│        │  │  ├─ tall_mangrove.json
│        │  │  ├─ trees_badlands.json
│        │  │  ├─ trees_birch.json
│        │  │  ├─ trees_birch_and_oak_leaf_litter.json
│        │  │  ├─ trees_flower_forest.json
│        │  │  ├─ trees_grove.json
│        │  │  ├─ trees_jungle.json
│        │  │  ├─ trees_old_growth_pine_taiga.json
│        │  │  ├─ trees_old_growth_spruce_taiga.json
│        │  │  ├─ trees_plains.json
│        │  │  ├─ trees_savanna.json
│        │  │  ├─ trees_snowy.json
│        │  │  ├─ trees_sparse_jungle.json
│        │  │  ├─ trees_taiga.json
│        │  │  ├─ trees_water.json
│        │  │  ├─ trees_windswept_hills.json
│        │  │  ├─ twisting_vines.json
│        │  │  ├─ twisting_vines_bonemeal.json
│        │  │  ├─ underwater_magma.json
│        │  │  ├─ vines.json
│        │  │  ├─ void_start_platform.json
│        │  │  ├─ warm_ocean_vegetation.json
│        │  │  ├─ warped_forest_vegetation.json
│        │  │  ├─ warped_forest_vegetation_bonemeal.json
│        │  │  ├─ warped_fungus.json
│        │  │  ├─ warped_fungus_planted.json
│        │  │  ├─ weeping_vines.json
│        │  │  ├─ wildflowers_birch_forest.json
│        │  │  └─ wildflowers_meadow.json
│        │  ├─ density_function
│        │  │  ├─ end
│        │  │  │  ├─ base_3d_noise.json
│        │  │  │  └─ sloped_cheese.json
│        │  │  ├─ nether
│        │  │  │  └─ base_3d_noise.json
│        │  │  ├─ overworld
│        │  │  │  ├─ base_3d_noise.json
│        │  │  │  ├─ caves
│        │  │  │  │  ├─ entrances.json
│        │  │  │  │  ├─ noodle.json
│        │  │  │  │  ├─ pillars.json
│        │  │  │  │  ├─ spaghetti_2d.json
│        │  │  │  │  ├─ spaghetti_2d_thickness_modulator.json
│        │  │  │  │  └─ spaghetti_roughness_function.json
│        │  │  │  ├─ continents.json
│        │  │  │  ├─ depth.json
│        │  │  │  ├─ erosion.json
│        │  │  │  ├─ factor.json
│        │  │  │  ├─ jaggedness.json
│        │  │  │  ├─ offset.json
│        │  │  │  ├─ ridges.json
│        │  │  │  ├─ ridges_folded.json
│        │  │  │  └─ sloped_cheese.json
│        │  │  ├─ overworld_amplified
│        │  │  │  ├─ depth.json
│        │  │  │  ├─ factor.json
│        │  │  │  ├─ jaggedness.json
│        │  │  │  ├─ offset.json
│        │  │  │  └─ sloped_cheese.json
│        │  │  ├─ overworld_large_biomes
│        │  │  │  ├─ continents.json
│        │  │  │  ├─ depth.json
│        │  │  │  ├─ erosion.json
│        │  │  │  ├─ factor.json
│        │  │  │  ├─ jaggedness.json
│        │  │  │  ├─ offset.json
│        │  │  │  └─ sloped_cheese.json
│        │  │  ├─ shift_x.json
│        │  │  ├─ shift_z.json
│        │  │  ├─ y.json
│        │  │  └─ zero.json
│        │  ├─ flat_level_generator_preset
│        │  │  ├─ bottomless_pit.json
│        │  │  ├─ classic_flat.json
│        │  │  ├─ desert.json
│        │  │  ├─ overworld.json
│        │  │  ├─ redstone_ready.json
│        │  │  ├─ snowy_kingdom.json
│        │  │  ├─ the_void.json
│        │  │  ├─ tunnelers_dream.json
│        │  │  └─ water_world.json
│        │  ├─ multi_noise_biome_source_parameter_list
│        │  │  ├─ nether.json
│        │  │  └─ overworld.json
│        │  ├─ noise
│        │  │  ├─ aquifer_barrier.json
│        │  │  ├─ aquifer_fluid_level_floodedness.json
│        │  │  ├─ aquifer_fluid_level_spread.json
│        │  │  ├─ aquifer_lava.json
│        │  │  ├─ badlands_pillar.json
│        │  │  ├─ badlands_pillar_roof.json
│        │  │  ├─ badlands_surface.json
│        │  │  ├─ calcite.json
│        │  │  ├─ cave_cheese.json
│        │  │  ├─ cave_entrance.json
│        │  │  ├─ cave_layer.json
│        │  │  ├─ clay_bands_offset.json
│        │  │  ├─ continentalness.json
│        │  │  ├─ continentalness_large.json
│        │  │  ├─ erosion.json
│        │  │  ├─ erosion_large.json
│        │  │  ├─ gravel.json
│        │  │  ├─ gravel_layer.json
│        │  │  ├─ ice.json
│        │  │  ├─ iceberg_pillar.json
│        │  │  ├─ iceberg_pillar_roof.json
│        │  │  ├─ iceberg_surface.json
│        │  │  ├─ jagged.json
│        │  │  ├─ netherrack.json
│        │  │  ├─ nether_state_selector.json
│        │  │  ├─ nether_wart.json
│        │  │  ├─ noodle.json
│        │  │  ├─ noodle_ridge_a.json
│        │  │  ├─ noodle_ridge_b.json
│        │  │  ├─ noodle_thickness.json
│        │  │  ├─ offset.json
│        │  │  ├─ ore_gap.json
│        │  │  ├─ ore_veininess.json
│        │  │  ├─ ore_vein_a.json
│        │  │  ├─ ore_vein_b.json
│        │  │  ├─ packed_ice.json
│        │  │  ├─ patch.json
│        │  │  ├─ pillar.json
│        │  │  ├─ pillar_rareness.json
│        │  │  ├─ pillar_thickness.json
│        │  │  ├─ powder_snow.json
│        │  │  ├─ ridge.json
│        │  │  ├─ soul_sand_layer.json
│        │  │  ├─ spaghetti_2d.json
│        │  │  ├─ spaghetti_2d_elevation.json
│        │  │  ├─ spaghetti_2d_modulator.json
│        │  │  ├─ spaghetti_2d_thickness.json
│        │  │  ├─ spaghetti_3d_1.json
│        │  │  ├─ spaghetti_3d_2.json
│        │  │  ├─ spaghetti_3d_rarity.json
│        │  │  ├─ spaghetti_3d_thickness.json
│        │  │  ├─ spaghetti_roughness.json
│        │  │  ├─ spaghetti_roughness_modulator.json
│        │  │  ├─ surface.json
│        │  │  ├─ surface_secondary.json
│        │  │  ├─ surface_swamp.json
│        │  │  ├─ temperature.json
│        │  │  ├─ temperature_large.json
│        │  │  ├─ vegetation.json
│        │  │  └─ vegetation_large.json
│        │  ├─ noise_settings
│        │  │  ├─ amplified.json
│        │  │  ├─ caves.json
│        │  │  ├─ end.json
│        │  │  ├─ floating_islands.json
│        │  │  ├─ large_biomes.json
│        │  │  ├─ nether.json
│        │  │  └─ overworld.json
│        │  ├─ placed_feature
│        │  │  ├─ acacia.json
│        │  │  ├─ acacia_checked.json
│        │  │  ├─ amethyst_geode.json
│        │  │  ├─ bamboo.json
│        │  │  ├─ bamboo_light.json
│        │  │  ├─ bamboo_vegetation.json
│        │  │  ├─ basalt_blobs.json
│        │  │  ├─ basalt_pillar.json
│        │  │  ├─ birch_bees_0002.json
│        │  │  ├─ birch_bees_0002_leaf_litter.json
│        │  │  ├─ birch_bees_002.json
│        │  │  ├─ birch_checked.json
│        │  │  ├─ birch_leaf_litter.json
│        │  │  ├─ birch_tall.json
│        │  │  ├─ blackstone_blobs.json
│        │  │  ├─ blue_ice.json
│        │  │  ├─ brown_mushroom_nether.json
│        │  │  ├─ brown_mushroom_normal.json
│        │  │  ├─ brown_mushroom_old_growth.json
│        │  │  ├─ brown_mushroom_swamp.json
│        │  │  ├─ brown_mushroom_taiga.json
│        │  │  ├─ cave_vines.json
│        │  │  ├─ cherry_bees_005.json
│        │  │  ├─ cherry_checked.json
│        │  │  ├─ chorus_plant.json
│        │  │  ├─ classic_vines_cave_feature.json
│        │  │  ├─ crimson_forest_vegetation.json
│        │  │  ├─ crimson_fungi.json
│        │  │  ├─ dark_forest_vegetation.json
│        │  │  ├─ dark_oak_checked.json
│        │  │  ├─ dark_oak_leaf_litter.json
│        │  │  ├─ delta.json
│        │  │  ├─ desert_well.json
│        │  │  ├─ disk_clay.json
│        │  │  ├─ disk_grass.json
│        │  │  ├─ disk_gravel.json
│        │  │  ├─ disk_sand.json
│        │  │  ├─ dripstone_cluster.json
│        │  │  ├─ end_gateway_return.json
│        │  │  ├─ end_island_decorated.json
│        │  │  ├─ end_platform.json
│        │  │  ├─ end_spike.json
│        │  │  ├─ fallen_birch_tree.json
│        │  │  ├─ fallen_jungle_tree.json
│        │  │  ├─ fallen_oak_tree.json
│        │  │  ├─ fallen_spruce_tree.json
│        │  │  ├─ fallen_super_birch_tree.json
│        │  │  ├─ fancy_oak_bees.json
│        │  │  ├─ fancy_oak_bees_0002_leaf_litter.json
│        │  │  ├─ fancy_oak_bees_002.json
│        │  │  ├─ fancy_oak_checked.json
│        │  │  ├─ fancy_oak_leaf_litter.json
│        │  │  ├─ flower_cherry.json
│        │  │  ├─ flower_default.json
│        │  │  ├─ flower_flower_forest.json
│        │  │  ├─ flower_forest_flowers.json
│        │  │  ├─ flower_meadow.json
│        │  │  ├─ flower_pale_garden.json
│        │  │  ├─ flower_plain.json
│        │  │  ├─ flower_plains.json
│        │  │  ├─ flower_swamp.json
│        │  │  ├─ flower_warm.json
│        │  │  ├─ forest_flowers.json
│        │  │  ├─ forest_rock.json
│        │  │  ├─ fossil_lower.json
│        │  │  ├─ fossil_upper.json
│        │  │  ├─ freeze_top_layer.json
│        │  │  ├─ glowstone.json
│        │  │  ├─ glowstone_extra.json
│        │  │  ├─ glow_lichen.json
│        │  │  ├─ grass_bonemeal.json
│        │  │  ├─ iceberg_blue.json
│        │  │  ├─ iceberg_packed.json
│        │  │  ├─ ice_patch.json
│        │  │  ├─ ice_spike.json
│        │  │  ├─ jungle_bush.json
│        │  │  ├─ jungle_tree.json
│        │  │  ├─ kelp_cold.json
│        │  │  ├─ kelp_warm.json
│        │  │  ├─ lake_lava_surface.json
│        │  │  ├─ lake_lava_underground.json
│        │  │  ├─ large_basalt_columns.json
│        │  │  ├─ large_dripstone.json
│        │  │  ├─ lush_caves_ceiling_vegetation.json
│        │  │  ├─ lush_caves_clay.json
│        │  │  ├─ lush_caves_vegetation.json
│        │  │  ├─ mangrove_checked.json
│        │  │  ├─ mega_jungle_tree_checked.json
│        │  │  ├─ mega_pine_checked.json
│        │  │  ├─ mega_spruce_checked.json
│        │  │  ├─ monster_room.json
│        │  │  ├─ monster_room_deep.json
│        │  │  ├─ mushroom_island_vegetation.json
│        │  │  ├─ nether_sprouts.json
│        │  │  ├─ oak.json
│        │  │  ├─ oak_bees_0002_leaf_litter.json
│        │  │  ├─ oak_bees_002.json
│        │  │  ├─ oak_checked.json
│        │  │  ├─ oak_leaf_litter.json
│        │  │  ├─ ore_ancient_debris_large.json
│        │  │  ├─ ore_andesite_lower.json
│        │  │  ├─ ore_andesite_upper.json
│        │  │  ├─ ore_blackstone.json
│        │  │  ├─ ore_clay.json
│        │  │  ├─ ore_coal_lower.json
│        │  │  ├─ ore_coal_upper.json
│        │  │  ├─ ore_copper.json
│        │  │  ├─ ore_copper_large.json
│        │  │  ├─ ore_debris_small.json
│        │  │  ├─ ore_diamond.json
│        │  │  ├─ ore_diamond_buried.json
│        │  │  ├─ ore_diamond_large.json
│        │  │  ├─ ore_diamond_medium.json
│        │  │  ├─ ore_diorite_lower.json
│        │  │  ├─ ore_diorite_upper.json
│        │  │  ├─ ore_dirt.json
│        │  │  ├─ ore_emerald.json
│        │  │  ├─ ore_gold.json
│        │  │  ├─ ore_gold_deltas.json
│        │  │  ├─ ore_gold_extra.json
│        │  │  ├─ ore_gold_lower.json
│        │  │  ├─ ore_gold_nether.json
│        │  │  ├─ ore_granite_lower.json
│        │  │  ├─ ore_granite_upper.json
│        │  │  ├─ ore_gravel.json
│        │  │  ├─ ore_gravel_nether.json
│        │  │  ├─ ore_infested.json
│        │  │  ├─ ore_iron_middle.json
│        │  │  ├─ ore_iron_small.json
│        │  │  ├─ ore_iron_upper.json
│        │  │  ├─ ore_lapis.json
│        │  │  ├─ ore_lapis_buried.json
│        │  │  ├─ ore_magma.json
│        │  │  ├─ ore_quartz_deltas.json
│        │  │  ├─ ore_quartz_nether.json
│        │  │  ├─ ore_redstone.json
│        │  │  ├─ ore_redstone_lower.json
│        │  │  ├─ ore_soul_sand.json
│        │  │  ├─ ore_tuff.json
│        │  │  ├─ pale_garden_flowers.json
│        │  │  ├─ pale_garden_vegetation.json
│        │  │  ├─ pale_moss_patch.json
│        │  │  ├─ pale_oak_checked.json
│        │  │  ├─ pale_oak_creaking_checked.json
│        │  │  ├─ patch_berry_bush.json
│        │  │  ├─ patch_berry_common.json
│        │  │  ├─ patch_berry_rare.json
│        │  │  ├─ patch_bush.json
│        │  │  ├─ patch_cactus.json
│        │  │  ├─ patch_cactus_decorated.json
│        │  │  ├─ patch_cactus_desert.json
│        │  │  ├─ patch_crimson_roots.json
│        │  │  ├─ patch_dead_bush.json
│        │  │  ├─ patch_dead_bush_2.json
│        │  │  ├─ patch_dead_bush_badlands.json
│        │  │  ├─ patch_dry_grass_badlands.json
│        │  │  ├─ patch_dry_grass_desert.json
│        │  │  ├─ patch_fire.json
│        │  │  ├─ patch_firefly_bush_near_water.json
│        │  │  ├─ patch_firefly_bush_near_water_swamp.json
│        │  │  ├─ patch_firefly_bush_swamp.json
│        │  │  ├─ patch_grass_badlands.json
│        │  │  ├─ patch_grass_forest.json
│        │  │  ├─ patch_grass_jungle.json
│        │  │  ├─ patch_grass_meadow.json
│        │  │  ├─ patch_grass_normal.json
│        │  │  ├─ patch_grass_plain.json
│        │  │  ├─ patch_grass_savanna.json
│        │  │  ├─ patch_grass_taiga.json
│        │  │  ├─ patch_grass_taiga_2.json
│        │  │  ├─ patch_large_fern.json
│        │  │  ├─ patch_leaf_litter.json
│        │  │  ├─ patch_melon.json
│        │  │  ├─ patch_melon_sparse.json
│        │  │  ├─ patch_pumpkin.json
│        │  │  ├─ patch_soul_fire.json
│        │  │  ├─ patch_sugar_cane.json
│        │  │  ├─ patch_sugar_cane_badlands.json
│        │  │  ├─ patch_sugar_cane_desert.json
│        │  │  ├─ patch_sugar_cane_swamp.json
│        │  │  ├─ patch_sunflower.json
│        │  │  ├─ patch_taiga_grass.json
│        │  │  ├─ patch_tall_grass.json
│        │  │  ├─ patch_tall_grass_2.json
│        │  │  ├─ patch_waterlily.json
│        │  │  ├─ pile_hay.json
│        │  │  ├─ pile_ice.json
│        │  │  ├─ pile_melon.json
│        │  │  ├─ pile_pumpkin.json
│        │  │  ├─ pile_snow.json
│        │  │  ├─ pine.json
│        │  │  ├─ pine_checked.json
│        │  │  ├─ pine_on_snow.json
│        │  │  ├─ pointed_dripstone.json
│        │  │  ├─ red_mushroom_nether.json
│        │  │  ├─ red_mushroom_normal.json
│        │  │  ├─ red_mushroom_old_growth.json
│        │  │  ├─ red_mushroom_swamp.json
│        │  │  ├─ red_mushroom_taiga.json
│        │  │  ├─ rooted_azalea_tree.json
│        │  │  ├─ sculk_patch_ancient_city.json
│        │  │  ├─ sculk_patch_deep_dark.json
│        │  │  ├─ sculk_vein.json
│        │  │  ├─ seagrass_cold.json
│        │  │  ├─ seagrass_deep.json
│        │  │  ├─ seagrass_deep_cold.json
│        │  │  ├─ seagrass_deep_warm.json
│        │  │  ├─ seagrass_normal.json
│        │  │  ├─ seagrass_river.json
│        │  │  ├─ seagrass_swamp.json
│        │  │  ├─ seagrass_warm.json
│        │  │  ├─ sea_pickle.json
│        │  │  ├─ small_basalt_columns.json
│        │  │  ├─ spore_blossom.json
│        │  │  ├─ spring_closed.json
│        │  │  ├─ spring_closed_double.json
│        │  │  ├─ spring_delta.json
│        │  │  ├─ spring_lava.json
│        │  │  ├─ spring_lava_frozen.json
│        │  │  ├─ spring_open.json
│        │  │  ├─ spring_water.json
│        │  │  ├─ spruce.json
│        │  │  ├─ spruce_checked.json
│        │  │  ├─ spruce_on_snow.json
│        │  │  ├─ super_birch_bees.json
│        │  │  ├─ super_birch_bees_0002.json
│        │  │  ├─ tall_mangrove_checked.json
│        │  │  ├─ trees_badlands.json
│        │  │  ├─ trees_birch.json
│        │  │  ├─ trees_birch_and_oak_leaf_litter.json
│        │  │  ├─ trees_cherry.json
│        │  │  ├─ trees_flower_forest.json
│        │  │  ├─ trees_grove.json
│        │  │  ├─ trees_jungle.json
│        │  │  ├─ trees_mangrove.json
│        │  │  ├─ trees_meadow.json
│        │  │  ├─ trees_old_growth_pine_taiga.json
│        │  │  ├─ trees_old_growth_spruce_taiga.json
│        │  │  ├─ trees_plains.json
│        │  │  ├─ trees_savanna.json
│        │  │  ├─ trees_snowy.json
│        │  │  ├─ trees_sparse_jungle.json
│        │  │  ├─ trees_swamp.json
│        │  │  ├─ trees_taiga.json
│        │  │  ├─ trees_water.json
│        │  │  ├─ trees_windswept_forest.json
│        │  │  ├─ trees_windswept_hills.json
│        │  │  ├─ trees_windswept_savanna.json
│        │  │  ├─ twisting_vines.json
│        │  │  ├─ underwater_magma.json
│        │  │  ├─ vines.json
│        │  │  ├─ void_start_platform.json
│        │  │  ├─ warm_ocean_vegetation.json
│        │  │  ├─ warped_forest_vegetation.json
│        │  │  ├─ warped_fungi.json
│        │  │  ├─ weeping_vines.json
│        │  │  ├─ wildflowers_birch_forest.json
│        │  │  └─ wildflowers_meadow.json
│        │  ├─ processor_list
│        │  │  ├─ ancient_city_generic_degradation.json
│        │  │  ├─ ancient_city_start_degradation.json
│        │  │  ├─ ancient_city_walls_degradation.json
│        │  │  ├─ bastion_generic_degradation.json
│        │  │  ├─ bottom_rampart.json
│        │  │  ├─ bridge.json
│        │  │  ├─ empty.json
│        │  │  ├─ entrance_replacement.json
│        │  │  ├─ farm_desert.json
│        │  │  ├─ farm_plains.json
│        │  │  ├─ farm_savanna.json
│        │  │  ├─ farm_snowy.json
│        │  │  ├─ farm_taiga.json
│        │  │  ├─ fossil_coal.json
│        │  │  ├─ fossil_diamonds.json
│        │  │  ├─ fossil_rot.json
│        │  │  ├─ high_rampart.json
│        │  │  ├─ high_wall.json
│        │  │  ├─ housing.json
│        │  │  ├─ mossify_10_percent.json
│        │  │  ├─ mossify_20_percent.json
│        │  │  ├─ mossify_70_percent.json
│        │  │  ├─ outpost_rot.json
│        │  │  ├─ rampart_degradation.json
│        │  │  ├─ roof.json
│        │  │  ├─ side_wall_degradation.json
│        │  │  ├─ stable_degradation.json
│        │  │  ├─ street_plains.json
│        │  │  ├─ street_savanna.json
│        │  │  ├─ street_snowy_or_taiga.json
│        │  │  ├─ trail_ruins_houses_archaeology.json
│        │  │  ├─ trail_ruins_roads_archaeology.json
│        │  │  ├─ trail_ruins_tower_top_archaeology.json
│        │  │  ├─ treasure_rooms.json
│        │  │  ├─ trial_chambers_copper_bulb_degradation.json
│        │  │  ├─ zombie_desert.json
│        │  │  ├─ zombie_plains.json
│        │  │  ├─ zombie_savanna.json
│        │  │  ├─ zombie_snowy.json
│        │  │  └─ zombie_taiga.json
│        │  ├─ structure
│        │  │  ├─ ancient_city.json
│        │  │  ├─ bastion_remnant.json
│        │  │  ├─ buried_treasure.json
│        │  │  ├─ desert_pyramid.json
│        │  │  ├─ end_city.json
│        │  │  ├─ fortress.json
│        │  │  ├─ igloo.json
│        │  │  ├─ jungle_pyramid.json
│        │  │  ├─ mansion.json
│        │  │  ├─ mineshaft.json
│        │  │  ├─ mineshaft_mesa.json
│        │  │  ├─ monument.json
│        │  │  ├─ nether_fossil.json
│        │  │  ├─ ocean_ruin_cold.json
│        │  │  ├─ ocean_ruin_warm.json
│        │  │  ├─ pillager_outpost.json
│        │  │  ├─ ruined_portal.json
│        │  │  ├─ ruined_portal_desert.json
│        │  │  ├─ ruined_portal_jungle.json
│        │  │  ├─ ruined_portal_mountain.json
│        │  │  ├─ ruined_portal_nether.json
│        │  │  ├─ ruined_portal_ocean.json
│        │  │  ├─ ruined_portal_swamp.json
│        │  │  ├─ shipwreck.json
│        │  │  ├─ shipwreck_beached.json
│        │  │  ├─ stronghold.json
│        │  │  ├─ swamp_hut.json
│        │  │  ├─ trail_ruins.json
│        │  │  ├─ trial_chambers.json
│        │  │  ├─ village_desert.json
│        │  │  ├─ village_plains.json
│        │  │  ├─ village_savanna.json
│        │  │  ├─ village_snowy.json
│        │  │  └─ village_taiga.json
│        │  ├─ structure_set
│        │  │  ├─ ancient_cities.json
│        │  │  ├─ buried_treasures.json
│        │  │  ├─ desert_pyramids.json
│        │  │  ├─ end_cities.json
│        │  │  ├─ igloos.json
│        │  │  ├─ jungle_temples.json
│        │  │  ├─ mineshafts.json
│        │  │  ├─ nether_complexes.json
│        │  │  ├─ nether_fossils.json
│        │  │  ├─ ocean_monuments.json
│        │  │  ├─ ocean_ruins.json
│        │  │  ├─ pillager_outposts.json
│        │  │  ├─ ruined_portals.json
│        │  │  ├─ shipwrecks.json
│        │  │  ├─ strongholds.json
│        │  │  ├─ swamp_huts.json
│        │  │  ├─ trail_ruins.json
│        │  │  ├─ trial_chambers.json
│        │  │  ├─ villages.json
│        │  │  └─ woodland_mansions.json
│        │  ├─ template_pool
│        │  │  ├─ ancient_city
│        │  │  │  ├─ city
│        │  │  │  │  └─ entrance.json
│        │  │  │  ├─ city_center
│        │  │  │  │  └─ walls.json
│        │  │  │  ├─ city_center.json
│        │  │  │  ├─ sculk.json
│        │  │  │  ├─ structures.json
│        │  │  │  ├─ walls
│        │  │  │  │  └─ no_corners.json
│        │  │  │  └─ walls.json
│        │  │  ├─ bastion
│        │  │  │  ├─ blocks
│        │  │  │  │  └─ gold.json
│        │  │  │  ├─ bridge
│        │  │  │  │  ├─ bridge_pieces.json
│        │  │  │  │  ├─ connectors.json
│        │  │  │  │  ├─ legs.json
│        │  │  │  │  ├─ ramparts.json
│        │  │  │  │  ├─ rampart_plates.json
│        │  │  │  │  ├─ starting_pieces.json
│        │  │  │  │  └─ walls.json
│        │  │  │  ├─ hoglin_stable
│        │  │  │  │  ├─ connectors.json
│        │  │  │  │  ├─ large_stables
│        │  │  │  │  │  ├─ inner.json
│        │  │  │  │  │  └─ outer.json
│        │  │  │  │  ├─ mirrored_starting_pieces.json
│        │  │  │  │  ├─ posts.json
│        │  │  │  │  ├─ ramparts.json
│        │  │  │  │  ├─ rampart_plates.json
│        │  │  │  │  ├─ small_stables
│        │  │  │  │  │  ├─ inner.json
│        │  │  │  │  │  └─ outer.json
│        │  │  │  │  ├─ stairs.json
│        │  │  │  │  ├─ starting_pieces.json
│        │  │  │  │  ├─ walls.json
│        │  │  │  │  └─ wall_bases.json
│        │  │  │  ├─ mobs
│        │  │  │  │  ├─ hoglin.json
│        │  │  │  │  ├─ piglin.json
│        │  │  │  │  └─ piglin_melee.json
│        │  │  │  ├─ starts.json
│        │  │  │  ├─ treasure
│        │  │  │  │  ├─ bases
│        │  │  │  │  │  └─ centers.json
│        │  │  │  │  ├─ bases.json
│        │  │  │  │  ├─ brains.json
│        │  │  │  │  ├─ connectors.json
│        │  │  │  │  ├─ corners
│        │  │  │  │  │  ├─ bottom.json
│        │  │  │  │  │  ├─ edges.json
│        │  │  │  │  │  ├─ middle.json
│        │  │  │  │  │  └─ top.json
│        │  │  │  │  ├─ entrances.json
│        │  │  │  │  ├─ extensions
│        │  │  │  │  │  ├─ houses.json
│        │  │  │  │  │  ├─ large_pool.json
│        │  │  │  │  │  └─ small_pool.json
│        │  │  │  │  ├─ ramparts.json
│        │  │  │  │  ├─ roofs.json
│        │  │  │  │  ├─ stairs.json
│        │  │  │  │  ├─ walls
│        │  │  │  │  │  ├─ bottom.json
│        │  │  │  │  │  ├─ mid.json
│        │  │  │  │  │  ├─ outer.json
│        │  │  │  │  │  └─ top.json
│        │  │  │  │  └─ walls.json
│        │  │  │  └─ units
│        │  │  │     ├─ center_pieces.json
│        │  │  │     ├─ edges.json
│        │  │  │     ├─ edge_wall_units.json
│        │  │  │     ├─ fillers
│        │  │  │     │  └─ stage_0.json
│        │  │  │     ├─ large_ramparts.json
│        │  │  │     ├─ pathways.json
│        │  │  │     ├─ ramparts.json
│        │  │  │     ├─ rampart_plates.json
│        │  │  │     ├─ stages
│        │  │  │     │  ├─ rot
│        │  │  │     │  │  └─ stage_1.json
│        │  │  │     │  ├─ stage_0.json
│        │  │  │     │  ├─ stage_1.json
│        │  │  │     │  ├─ stage_2.json
│        │  │  │     │  └─ stage_3.json
│        │  │  │     ├─ walls
│        │  │  │     │  └─ wall_bases.json
│        │  │  │     └─ wall_units.json
│        │  │  ├─ empty.json
│        │  │  ├─ pillager_outpost
│        │  │  │  ├─ base_plates.json
│        │  │  │  ├─ features.json
│        │  │  │  ├─ feature_plates.json
│        │  │  │  └─ towers.json
│        │  │  ├─ trail_ruins
│        │  │  │  ├─ buildings
│        │  │  │  │  └─ grouped.json
│        │  │  │  ├─ buildings.json
│        │  │  │  ├─ decor.json
│        │  │  │  ├─ roads.json
│        │  │  │  ├─ tower
│        │  │  │  │  ├─ additions.json
│        │  │  │  │  └─ tower_top.json
│        │  │  │  └─ tower.json
│        │  │  ├─ trial_chambers
│        │  │  │  ├─ atrium.json
│        │  │  │  ├─ chamber
│        │  │  │  │  ├─ addon.json
│        │  │  │  │  ├─ assembly.json
│        │  │  │  │  ├─ end.json
│        │  │  │  │  ├─ entrance_cap.json
│        │  │  │  │  ├─ eruption.json
│        │  │  │  │  ├─ pedestal.json
│        │  │  │  │  └─ slanted.json
│        │  │  │  ├─ chambers
│        │  │  │  │  └─ end.json
│        │  │  │  ├─ chests
│        │  │  │  │  ├─ contents
│        │  │  │  │  │  └─ supply.json
│        │  │  │  │  └─ supply.json
│        │  │  │  ├─ corridor
│        │  │  │  │  └─ slices.json
│        │  │  │  ├─ corridor.json
│        │  │  │  ├─ corridors
│        │  │  │  │  └─ addon
│        │  │  │  │     ├─ lower.json
│        │  │  │  │     ├─ middle.json
│        │  │  │  │     └─ middle_upper.json
│        │  │  │  ├─ decor
│        │  │  │  │  ├─ bed.json
│        │  │  │  │  ├─ chamber.json
│        │  │  │  │  └─ disposal.json
│        │  │  │  ├─ decor.json
│        │  │  │  ├─ dispensers
│        │  │  │  │  └─ chamber.json
│        │  │  │  ├─ entrance.json
│        │  │  │  ├─ hallway
│        │  │  │  │  └─ fallback.json
│        │  │  │  ├─ hallway.json
│        │  │  │  ├─ reward
│        │  │  │  │  ├─ all.json
│        │  │  │  │  ├─ contents
│        │  │  │  │  │  └─ default.json
│        │  │  │  │  └─ ominous_vault.json
│        │  │  │  └─ spawner
│        │  │  │     ├─ all.json
│        │  │  │     ├─ breeze.json
│        │  │  │     ├─ contents
│        │  │  │     │  └─ breeze.json
│        │  │  │     ├─ melee
│        │  │  │     │  ├─ husk.json
│        │  │  │     │  ├─ spider.json
│        │  │  │     │  └─ zombie.json
│        │  │  │     ├─ melee.json
│        │  │  │     ├─ ranged
│        │  │  │     │  ├─ poison_skeleton.json
│        │  │  │     │  ├─ skeleton.json
│        │  │  │     │  └─ stray.json
│        │  │  │     ├─ ranged.json
│        │  │  │     ├─ slow_ranged
│        │  │  │     │  ├─ poison_skeleton.json
│        │  │  │     │  ├─ skeleton.json
│        │  │  │     │  └─ stray.json
│        │  │  │     ├─ slow_ranged.json
│        │  │  │     ├─ small_melee
│        │  │  │     │  ├─ baby_zombie.json
│        │  │  │     │  ├─ cave_spider.json
│        │  │  │     │  ├─ silverfish.json
│        │  │  │     │  └─ slime.json
│        │  │  │     └─ small_melee.json
│        │  │  └─ village
│        │  │     ├─ common
│        │  │     │  ├─ animals.json
│        │  │     │  ├─ butcher_animals.json
│        │  │     │  ├─ cats.json
│        │  │     │  ├─ iron_golem.json
│        │  │     │  ├─ sheep.json
│        │  │     │  └─ well_bottoms.json
│        │  │     ├─ desert
│        │  │     │  ├─ camel.json
│        │  │     │  ├─ decor.json
│        │  │     │  ├─ houses.json
│        │  │     │  ├─ streets.json
│        │  │     │  ├─ terminators.json
│        │  │     │  ├─ town_centers.json
│        │  │     │  ├─ villagers.json
│        │  │     │  └─ zombie
│        │  │     │     ├─ decor.json
│        │  │     │     ├─ houses.json
│        │  │     │     ├─ streets.json
│        │  │     │     ├─ terminators.json
│        │  │     │     └─ villagers.json
│        │  │     ├─ plains
│        │  │     │  ├─ decor.json
│        │  │     │  ├─ houses.json
│        │  │     │  ├─ streets.json
│        │  │     │  ├─ terminators.json
│        │  │     │  ├─ town_centers.json
│        │  │     │  ├─ trees.json
│        │  │     │  ├─ villagers.json
│        │  │     │  └─ zombie
│        │  │     │     ├─ decor.json
│        │  │     │     ├─ houses.json
│        │  │     │     ├─ streets.json
│        │  │     │     └─ villagers.json
│        │  │     ├─ savanna
│        │  │     │  ├─ decor.json
│        │  │     │  ├─ houses.json
│        │  │     │  ├─ streets.json
│        │  │     │  ├─ terminators.json
│        │  │     │  ├─ town_centers.json
│        │  │     │  ├─ trees.json
│        │  │     │  ├─ villagers.json
│        │  │     │  └─ zombie
│        │  │     │     ├─ decor.json
│        │  │     │     ├─ houses.json
│        │  │     │     ├─ streets.json
│        │  │     │     ├─ terminators.json
│        │  │     │     └─ villagers.json
│        │  │     ├─ snowy
│        │  │     │  ├─ decor.json
│        │  │     │  ├─ houses.json
│        │  │     │  ├─ streets.json
│        │  │     │  ├─ terminators.json
│        │  │     │  ├─ town_centers.json
│        │  │     │  ├─ trees.json
│        │  │     │  ├─ villagers.json
│        │  │     │  └─ zombie
│        │  │     │     ├─ decor.json
│        │  │     │     ├─ houses.json
│        │  │     │     ├─ streets.json
│        │  │     │     └─ villagers.json
│        │  │     └─ taiga
│        │  │        ├─ decor.json
│        │  │        ├─ houses.json
│        │  │        ├─ streets.json
│        │  │        ├─ terminators.json
│        │  │        ├─ town_centers.json
│        │  │        ├─ villagers.json
│        │  │        └─ zombie
│        │  │           ├─ decor.json
│        │  │           ├─ houses.json
│        │  │           ├─ streets.json
│        │  │           └─ villagers.json
│        │  └─ world_preset
│        │     ├─ amplified.json
│        │     ├─ debug_all_block_states.json
│        │     ├─ flat.json
│        │     ├─ large_biomes.json
│        │     ├─ normal.json
│        │     └─ single_biome_surface.json
│        └─ zombie_nautilus_variant
│           ├─ temperate.json
│           └─ warm.json
├─ schemas
│  ├─ assets
│  │  ├─ any_asset_json.schema.json
│  │  └─ minecraft
│  │     ├─ atlases
│  │     │  ├─ armor_trims.schema.json
│  │     │  ├─ banner_patterns.schema.json
│  │     │  ├─ beds.schema.json
│  │     │  ├─ blocks.schema.json
│  │     │  ├─ celestials.schema.json
│  │     │  ├─ chests.schema.json
│  │     │  └─ decorated_pot.schema.json
│  │     ├─ atlases.schema.json
│  │     ├─ blockstates.schema.json
│  │     ├─ equipment.schema.json
│  │     ├─ font.schema.json
│  │     ├─ items.schema.json
│  │     ├─ lang.schema.json
│  │     ├─ models
│  │     │  ├─ any_model.schema.json
│  │     │  ├─ block_models.schema.json
│  │     │  └─ item_models.schema.json
│  │     ├─ particles.schema.json
│  │     ├─ post_effect.schema.json
│  │     ├─ regional_compliancies.schema.json
│  │     ├─ shaders.schema.json
│  │     ├─ texts.schema.json
│  │     └─ waypoint_style.schema.json
│  ├─ data
│  │  ├─ advancements.schema.json
│  │  ├─ any_data_json.schema.json
│  │  ├─ chat_type.schema.json
│  │  ├─ damage_type.schema.json
│  │  ├─ dimension.schema.json
│  │  ├─ dimension_type.schema.json
│  │  ├─ enchantment.schema.json
│  │  ├─ enchantment_provider.schema.json
│  │  ├─ jukebox_song.schema.json
│  │  ├─ loot_table.schema.json
│  │  ├─ predicates.schema.json
│  │  ├─ recipes.schema.json
│  │  ├─ structures.schema.json
│  │  ├─ tags.schema.json
│  │  ├─ trim_pattern.schema.json
│  │  └─ worldgen
│  │     ├─ biome.schema.json
│  │     ├─ configured_carver.schema.json
│  │     ├─ configured_feature.schema.json
│  │     ├─ density_function.schema.json
│  │     ├─ flat_level_generator_preset.schema.json
│  │     ├─ multi_noise_biome_source_parameter_list.schema.json
│  │     ├─ noise.schema.json
│  │     ├─ noise_settings.schema.json
│  │     ├─ placed_feature.schema.json
│  │     ├─ processor_list.schema.json
│  │     ├─ structure.schema.json
│  │     ├─ structure_set.schema.json
│  │     └─ template_pool.schema.json
│  └─ pack
│     └─ pack_mcmeta.schema.json
├─ settings.gradle
└─ tools
   └─ schema_tool.py
```
