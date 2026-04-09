# Space

The world's `space` is defined in `tiles`, `zones`, and `regions`. Each correspond to a level of detail to be shown on a `map`.

_Dungeoneers_ is designed to be played on a visual grid, but there are certain times when a `map` is not used (called theater of the mind). When theater of the mind is used, work with your GM to understand distance and the environment.

# Map

There are 2 levels of detail to a `map`: the `world map` and the `dungeon map`. Each are divided into squares or hexes that represent some unit of `space`. Each square or hex on the `world map` is a `region` and on the `dungeon map` they are `tiles`.

# Tile

A `tile` is the smallest unit of space, roughly 1 yard (or 1 meter, for metric). Each square or hex on a `dungeon map` is a `tile`.

# Region

A `region` is a large space, representing one square or hex on the `world map` and is about 1 mile (or 1 kilometer, for metric); 1 `region` is about 1,000 `tiles`.

# Zone

A `zone` is the extent of the visual range of a `creature` and roughly corresponds to a room/hallway in a dungeon. When sightlines are not constrained, a `zone` is about 10 yards (or 10 meters, for metric); 1 `zone` is max 10 `tiles`.

# Obstacles

An `obstacle` is an `object` in the world that is non-trivial to move past. There are two types of `obstacle`: `light obstacles` and `heavy obstacles`.

## Light Obstacle

A `light obstacle` requires 2 `tiles` of `movement` in order to `move` into. While within a `light obstacle`, you gain `evasive` 1.

## Heavy Obstacle

A `heavy obstacle` cannot be `moved` through and must be circumvented.

# Moving

A `creature` can `move` through `space` during a `procedure`. During a `combat procedure`, an `action` is used to `move`. Outside of `combat procedures`, `moving` is a given and done freely as part of an `action` in order to best complete it.

# Movement Types

A `movement type` can be applied when you `move`. It will change the target of certain terrain types based on the `movement type`. Unless otherwise noted, a `creature` only has the `walk` and `jump` `movement types`.

When `moving` into a `tile` with a certain `terrain type`, `roll` for a `total` using `speed`. This `total` must meet or exceed the target given in the table for the `movement type`, otherwise the `move` ends immediately and the `creature` `falls` (if applicable). If the `total` exceeds the target by 5 or more, there is no additional cost, otherwise it requires 2 `tiles` of movement.

## Walk

The standard `movement type`.

| Terrain Type   | Target |
| -------------- | ------ |
| Normal         | 0      |
| Light Obstacle | 5      |
| Water          | 5      |
| Wall           | 10     |
| Ceiling        | 15     |
| Air            | 99     |

## Jump

You leap through the air and land at a spot.

| Terrain Type   | Target |
| -------------- | ------ |
| Normal         | 0      |
| Light Obstacle | 0      |
| Water          | 0      |
| Wall           | 10     |
| Ceiling        | 15     |
| Air            | 99     |

## Burrow

Movement through a surface. In order to do so, your `weapon` must be capable of overcoming the `hardness` of the surface (most commonly the ground) before factoring any bonuses from `criticals`. You may end your `move` underground and you may move at half distance in order to leave behind a hole that can be followed.

| Terrain Type   | Target |
| -------------- | ------ |
| Normal         | 0      |
| Light Obstacle | 0      |
| Water          | 5      |
| Wall           | 0      |
| Ceiling        | 15     |
| Air            | 99     |

## Flight

Movement through the air via wings or similar propulsion. Must be space for your propulsion to occur. When harmed in the air, roll 1d6. On a 1, you `fall`.

| Terrain Type   | Target |
| -------------- | ------ |
| Normal         | 0      |
| Light Obstacle | 0      |
| Water          | 0      |
| Wall           | 10     |
| Ceiling        | 15     |
| Air            | 0      |

## Levitation

Magically controlled movement through the air.

| Terrain Type   | Target |
| -------------- | ------ |
| Normal         | 0      |
| Light Obstacle | 0      |
| Water          | 0      |
| Wall           | 10     |
| Ceiling        | 15     |
| Air            | 0      |
