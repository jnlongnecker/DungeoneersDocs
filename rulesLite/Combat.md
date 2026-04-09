# Attacks

Any `action` that deals `damage` or applies a `condition` is an `attack`. Each `attack` is either `targeted` or `area of effect` (`AoE`).

## Area of Effect Attacks

`Area of effect` (`AoE`) `attacks` are spread across a wide area in some specified shape (sphere, cube, cylinder, cone, rectangle, line, etc). `AoE` `attacks` cannot `critical hit`.

Whenever a `roll` is made during an `AoE` `attack`, you `roll` once and compare the `total` for each target.

## Targeted Attacks

`Targeted` `attacks` are launched at a specific, single target. `Targeted` `attacks` have the possibility to `critical hit` and may choose what to target, called your `mark`.

## Marks

A `targeted` `attack` can have 1 of 3 `marks`:

1. Body
2. Limbs
3. Weakness

The `body` `mark` does nothing special. The `limb` `mark` disables a limb of choice on a `critical` until the end of the next `round` and increases the `FT` by 2. The `weakness` `mark` results in doubled `damage` on a `critical` and increases the `FT` by 5.

# Damage

`Damage` is harm done to an `entity`. All `damage` is associated with a `class`.

## Damage Class

The `class` of `damage` is either `magic` or `physical`, and determines efficacy against certain types of `buffs`.

# Critical Hits

When you score a `critical hit`, your `damage` ignores all `buffs` and `shield`. A `critical hit` occurs when a `targeted attack` rolls a `critical`.

# Combat Speed Order

When multiple interactions happen at the same time, the `combat speed order` determines which order to resolve the interactions. First, the `priority` of the interaction is determined. The highest `priority` goes first. If both interactions have the same `priortity`, the `creature` with the higher `speed` resolves first. It is possible for one outcome to nullify the other, such as moving out of range of an `attack`.

# Cooldown & Uses

Some `actions` have to have their `cooldown` reset before they can be used again. Others have a certain number of `uses` before they can't be used anymore. `Actions` with both have their `uses` reset when their `cooldown` is reset.

`Cooldown` must be explicitly restored, either restored outright or rolled for. If an ability specifies to roll to restore an amount of `cooldown`, this means to distribute the amount amongst possible `cooldowns`.

> Example: You have 2 `actions` on `cooldown`, one with a `cooldown` of 2 and another with a `cooldown` of 3. Suppose you can restore 4 `cooldown` from an `action`. You may distribute that 4 amongst your `actions` on `cooldown`; resulting in one `cooldown` refreshed and the other at `cooldown` 1.

# Flanking

When you deal `damage` to a `creature` from a `targeted attack`, draw a line between yourself and one of your allies. If this line intersects your target, it takes 2 additional `damage`.

# Common Actions

`Common actions` are known by all `creatures`.

## Step

- Tags: `Movement`
- Range: Self
- Area: Single

You move up to 3 `tiles`.

## Leap

- Tags: `Movement`
- Range: Self
- Area: Single
- Uses: `Speed`
- Cooldown: 1

You move up to 3 `tiles`.

## Defend

- Tags: `Interact`
- Range: Self
- Area: Single

You gain `defense` `shield`.

## Interact

- Tags: `Interact`
- Range: 1
- Area: Single

You perform some interaction with something in range. This can be one of many things; e.g. opening a door, pulling a lever, retrieving an `item` from a container, picking up an `object`, or accepting/handing off something to someone else.

## Help

- Tags: `Interact`, `Quick`
- Range: 2
- Area: Single

You lower the `FT` by 1 for another `creature's` `roll`.

## Channel

- Tags: `Interact`
- Range: 1
- Area: Single

Gain 2 `mana`.

## Reasses

- Tags: `Interact`
- Range: Self
- Area: Single

Roll for a `total` using `speed`. You restore `cooldown` equal to the `total`.

## Flee/Pursue

- Tags: `Movement`, `Quick`
- Range: Self
- Area: Single

You attempt to flee from `combat`, or pursue after another `creature` who has fled. This `action` causes a `chase procedure` to begin if it results in a flee-er and a pursuer.

If you flee and are not pursued, you may not partake in the `combat procedure` until it is over.
