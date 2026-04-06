# Inventory

The `inventory` consists of 20 slots to place `entities` in. Anything `equipped` does not take up space within the `inventory`. Anything that can be picked up by the `creature` owning the `inventory` can be placed within it. Some `equipment` provides bespoke slots to place things in, oftentimes with restrictions.

# Equipment

`Equipment` are `objects` that can be `equipped`, and must be in order to be properly used. They must be `equipped` in a proper `equipment slot`, specified by the `equipment`.

## Equipment Slots

The following are `equipment slots`:

- Head
- Hang
- Body
- Back
- Hands
- Wield
- Feet
- Ring

Different `creatures` have different types and quantities of `equipment slots`. `Objects` do not have `equipment slots`.

# Weapons

A `weapon` is a piece of `equipment` that is meant to make `attacks` with. `Weapons` are classified into `weapon types` which determine most of their unique characteristics.

## Weapon Type

One of `improvised`, `light`, `standard`, `reach`, `heavy`, or `ranged`. Each `weapon type` grants a special `action` that can be used with it and specifies the baseline `damage` that they deal. Whenever you `attack` using the `weapon`, the `damage` is determined in part by the `damage` specified here. These have the following attributes:

## Improvised

- Damage: major `stat` - 1
- Wield Slots: 1

Anything being used as a `weapon` that wasn't designed to be a `weapon`. Grants the following `action`:

### Slam/Scratch/Bite

- Tags: `Attack`
- Range: 1
- Area: Single

Roll: `prowess` vs `defense`

- Success: `Damage` the target
- Critical: +2 `damage`

## Light

- Damage: major `stat` - 1
- Wield Slots: 1

A smaller, highly maneuverable `weapon`. Grants the following `actions`:

### Toss

- Tags: `Attack`
- Range: 2
- Area: Single
- Uses: 3
- Cooldown: 2

Roll: `prowess` vs `defense`

- Success: `Damage` the target (-1 `damage`)
- Critical: +2 `damage`

### Strike

- Tags: `Attack`
- Range: 1
- Area: Single

Roll: `prowess` vs `defense`

- Success: `Damage` the target
- Critical: +2 `damage`

## Standard

- Damage: major `stat`
- Wield Slots: 1

A typical sized, dangerous `weapon`. Grants the following `arts`:

### Strike

- Tags: `Attack`
- Range: 1
- Area: Single

Roll: `prowess` vs `defense`

- Success: `Damage` the target
- Critical: +2 `damage`

## Reach

- Damage: major `stat`
- Wield Slots: 2

A larger `weapon` with reach. Grants the following `action`:

### Lunge

- Tags: `Attack`
- Range: 2
- Area: Single

Roll: `prowess` vs `defense`

- Success: `Damage` the target (-1 `damage` if adjacent)
- Critical: +2 `damage`

## Heavy

- Damage: major `stat` + 1
- Wield Slots: 2

A large, powerful `weapon` that is slightly slow to swing. Grants the following `actions`:

### Cleave

- Tags: `Attack`
- Range: 1
- Area: 1x3 rectangle

Roll: `prowess` vs `defense`

- Success: `Damage` the target (-1 `damage`)
- Critical: +2 `damage`

### Strike

- Tags: `Attack`
- Range: 1
- Area: Single

Roll: `prowess` vs `defense`

- Success: `Damage` the target
- Critical: +2 `damage`

## Ranged

- Damage: major `stat` - 2
- Wield Slots: 2

A `weapon` designed to deliver a payload at range. Grants the following `action`:

### Shoot

- Tags: `Attack`
- Range: 4
- Area: Single
- Uses: 1
- Cooldown: 1

Roll: `prowess` vs `defense`

- Success: `Damage` the target
- Critical: +2 `damage`

## Weapon Range

The number of `tiles` from the user the `weapon` can reach.

## Weapon Damage

The base `damage` the `weapon` deals. The attackers main `stat` of their choice is added to this value to get the total `damage`.

# Gear

`Gear` are `items` that grant special tool `activities`.

## Cooks Tools

Grants the following `activity`:

### Cook

- Tags: `Average`, `Long`

Requires cookable ingredients

Roll: `talent` vs 10

- Success: Nothing happens
- Critical: Applies one of the following effects:
  - All `creatures` who eat gain 1 `recovery`
  - +1 to a `stat` until the next `combat procedure`
  - Apply a unique effect of one of the ingredients
