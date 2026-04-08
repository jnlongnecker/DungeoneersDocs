# Aggregates

If an `attack` has an `aggregate`, roll the `aggregate` against the targets `aggregate defense`.

Aggregate Roll: [`aggregate`] vs `aggregate defense`

- Failure: Reduce `aggregate defense` by 1
- Success: Inflict the `status` at `severity` 1
- Critical: Increase `severity` by 1

## Aggregate Rolls

`Aggregate rolls` are slightly different than normal `rolls`. A `failure` occurs when the `total` is less than the `aggregate defense`. A `success` occurs when the `total` meets or beats the `aggregate defense`. A `critical` occurs when the `total` meets or beats each multiple of the `aggregate defense`.

## Aggregate Defense

A `creatures` max `aggregate defense` is equal to their `defense`, unless boosted. `Aggregate defense` cannot fall below 0.

## Aggregate Resistance

If a `creature` is `resistant` to a `status`, its `aggregate defense` is always treated to be at max.

## Aggregate Weakness

If a `creature` is `weak` to a `status`, its `aggregate defense` is always treated to be at 0.

# Status

A `status` is a condition that persists over time until cured. A `status` that `ticks` has its `severity` reduced by 1 at the end of every `round`. A `status` lasts until reduced to 0 `severity`.

## Severity

The `severity` of a `status` is a number representing how bad the `status` is. Each `status` scales in some way based on its `severity`.

## Exhaustion

`FT` increases by 1 per `severity`. At `severity` 6, the `creature` dies.

## Asleep

`Creature` is feebly aware of their surroundings and cannot take `actions`. Cured upon being interacted with in any way (shaken, harmed, moved, etc), or after `severity` `rounds` unless naturally caused.

## Burned

`Creature` is weakened by heat and takes `true damage` equal to `severity` at the end of the `round`. Anything flammable gets set on fire through contact. Cured by becoming `damp`. `Ticks`.

## Forced

`Creature` is moved against their will a number of `tiles` equal to the `severity` in a direction of choosing by the inflictor(s). Ends when the movement takes place; immediately upon being inflicted.

## Damp

`Creature` is wet and cannot be `burned`. `Cold` becomes `freeze`.

## Cold

`Creature` is cold and their `speed` score is reduced by 1. Cured upon being `burned`. `Ticks`.

## Freeze

`Creature` is frozen and has `severity` fewer `speed`. Becomes `damp` upon being `burned`. `Ticks`.

## Zapped

`Creature` has difficulty with fine motor control and their `defense`, `control` and `precision` are reduced by `severity`. `Ticks`.

## Tangled

`Creature` is caught in a tangle, causing them to be unable to move. Cured by becoming `forced`. `Ticks`.

## Poisoned

`Creature` is afflicted with a toxin, causing them to take 1 `true damage` at the end of every `round`, ignoring `shield`.

## Bleed

`Creature` is bleeding, causing them to take `severity` `true damage` if they `attack` or `move`. Cannot be applied if the `creature` has `shield`. `Ticks` _up_ at the end of the `round`.

## Blinded

`Creature` has faltering vision, increasing their `FT` by `severity`. `Ticks`.

## Taunted

`Creature` is duped into targeting their taunter; `targeted attacks` must target them, and `AoE attacks` must be centered on them. `Ticks`.

## Bruise

`Creature` is bruised, causing them to take `severity` additional `damage` when they take `physical damage`.

## Marked

`Attacks` against you have their `FT` reduced by 1 and deal 1 additional `damage`. `Ticks`.

# Buffs

## Brace

Take 1 fewer `physical damage` per `severity`. `Ticks`.

## Sharp

Deal 1 additional `physical damage` per `severity`. `Ticks`.

## Regen

Gain 1 `hitpoint` after taking a `turn`. `Ticks`.

## Swift

Gain 1 `speed` per `severity`. `Ticks`.

## Evasive

`Attacks` against you have their `FT` increased by 1 per `severity`. `Ticks`.

## Camoflauged

Until you `move` or `attack`, nothing can see you. `Ticks` when you `move`, `attack`, or are `damaged`.
