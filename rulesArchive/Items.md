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

One of `improvised`, `light`, `standard`, `control`, `heavy`, or `ranged`. These have the following attributes:

## Improvised

Anything being used as a `weapon` that wasn't designed to be a `weapon`. Grants the following `arts`:

### Slam/Scratch/Bite

- Tags: `Attack`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 2)
- Critical: Deal +2 `damage`

### Throw Projectile

- Tags: `Attack`, `Slow`
- Range: 3
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 3)
- Critical: Deal +2 `damage`

### Grapple

- Tags: `Attack`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: Inflict `tangled` (`aggregate` 1d4, `severity` 1)
- Critical: `Aggregate` +2 or `severity` + 1

## Light

A smaller, highly maneuverable `weapon`. Grants the following `arts`:

### Toss

- Tags: `Attack`
- Range: 2
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 2)
- Critical: Deal +2 `damage`

### Strike

- Tags: `Attack`, `Quick`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 1)
- Critical: Deal +2 `damage`

### Blitz

- Tags: `Attack`, `Movement`, `Quick`
- Range: 1
- Area: Single
- Cost: 2 `AP`

Move up to half `speed`, then `attack`.

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 2)
- Critical: Deal +2 `damage`

## Standard

A typical sized, dangerous `weapon`. Grants the following `arts`:

### Strike

- Tags: `Attack`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat`)
- Critical: Deal +2 `damage`

### Charge

- Tags: `Attack`, `Movement`
- Range: 1
- Area: Single
- Cost: 2 `AP`

Move 2 `tiles` in a straight line, then `attack`. Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 1 + `tiles` moved)
- Critical: Deal +2 `damage`

### Counter

- Tags: `Buff`, `Quick`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll for a `total` using `defense`. Gain `shield` equal to the `total` and deal 2 `damage` to any `creature` that `damages` you but doesn't break your `shield`. If your `shield` reaches 0, become `stunned` (`severity` 1).

## Control

A larger `weapon` with reach. Grants the following `arts`:

### Lunge

- Tags: `Attack`
- Range: 2
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat`)
- Critical: Deal +2 `damage`

### Point Guard

- Tags: `Attack`, `Spotlight`
- Range: Self
- Area: Single
- Cost: 2 `AP`

Roll: `prowess` vs 10

- Success: Gain `overwatch` (`severity` 1)
- Critical: +1 `severity`

### Sweep

- Tags: `Attack`
- Range: 1
- Area: 2x2 square
- Cost: 2 `AP`

Roll: `control` vs `defense`

- Success: `Damage` the target(s) (main `stat` - 1)
- Critical: Deal +2 `damage`

## Heavy

A large, powerful `weapon` that is slightly slow to swing. Grants the following `arts`:

### Crush

- Tags: `Attack`
- Range: 2
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` + 1)
- Critical: Deal +2 `damage`

### Cleave

- Tags: `Attack`
- Range: 1
- Area: 1x3 rectangle
- Cost: 2 `AP`

Can hit a target more than once.

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main `stat` - 1)
- Critical: Deal +2 `damage`

### Slam

- Tags: `Attack`, `Movement`
- Range: 3
- Area: 3x3 square
- Cost: 2 `AP`

You leap to the target position, `forcing` back its occupant if possible and dealing 2 `damage`. If not possible, you take 5 `true damage` and are yourself `forced`.

Roll: `control` vs `defense`

- Success: `Damage` the target (main stat - 1)
- Critical: Deal +2 `damage`

## Ranged

A `weapon` designed to deliver a payload at range. Grants the following `arts`:

### Shoot

- Tags: `Attack`
- Range: 4
- Area: Single
- Cost: 1 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main stat - 2)
- Critical: Deal +2 `damage`

### Snipe

- Tags: `Attack`
- Range: 5
- Area: Single
- Cost: 2 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main stat - 3)
- Critical: Deal +2 `damage`

### Steady Shot

- Tags: `Attack`, `Precise`
- Range: 3
- Area: Single
- Cost: 2 `AP`

Roll: `prowess` vs `defense`

- Success: `Damage` the target (main stat - 3)
- Critical: Deal +2 `damage`

## Weapon Range

The number of `tiles` from the user the `weapon` can reach.

## Weapon Priority

The bracket of order for an `attack` with the `weapon`. In a `priority` tie, the higher `speed` acts first. Otherwise, the higher `priority` acts first.

## Weapon Damage

The base `damage` the `weapon` deals. The attackers main `stat` of their choice is added to this value to get the total `damage`.
