# Damage

`Damage` is harm caused to an `entity`. It can be modified in a number of ways, and comes in 2 variants: `magic damage` and `physical damage`. When `damage` is dealt, the minimum possible is 1.

# Hitpoints

`Hitpoints` are a number that represents how much more `damage` an `entity` can take before becoming grievously injured or dying. At 0 `hitpoints`, a `creature` gains the `dying` `status` and gains an `injury`. If they are damaged into negative `hitpoints` equal to or past half their `hitpoints`, they die. If they are damaged into negative `hitpoints` equal to or past their total `hitpoints`, their corpse is irreversably damaged (usually completely destroyed).

# Shield

`Shield` soaks `damage` before being subtracted from `hitpoints`. At the start of a `round`, all `shield` is lost.

# Hardness

`Hardness` is a property of `objects`. Unless `damage` exceeds an `objects` `hardness`, the `object` takes no `damage`.

# Injury

An `injury` is a permanent `debuff`. The first `injury` is a `minor injury`, the second a `major injury`, and the third is death. When healed, an `injury` becomes a `scar`.

## Minor Injury

Pick from the following or create your own with GM assistance:

- -1 to a `stat`
- +1 `FT`

## Major Injury

Pick from the following or create your own with GM assistance:

- Removal of `equip slot`
- Halved movement
- +3 `FT`

## Scar

When healed, an `injury` becomes a `scar` and no longer counts as an `injury`. Mechanically, a `scar` need not do anything but be a reminder of past `injury`. Tables may opt to have `scars` have a mechanical function, such as small penalties, penalties and buffs, or contextual bonuses / penalties.

# Recoveries

Each `creature` has a number of `recoveries` equal to their `health`. During `downtime`, `recoveries` are used to regain `hitpoints`. Each `recovery` heals `health` `hitpoints`. You may also use a `recovery` to entirely eliminate a `status`.
