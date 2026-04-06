# Skills

A `skill` is something that the `creature` has special training in. This allows them to be better at tasks that can utilize the `skill` than they otherwise would be. A `creature` has a number of `ranks` in `skills` equal to their `talent` score, plus 1.

When a `skill` applies to a `roll`, you may add the number of `ranks` you have in the `skill` to the `result`.

## Crafting

Used to create mundane crafts, like weapons, armor, and jewelry.

### Spot Weakness (Rank 1)

- Tags: `Attack`
- Range: 5
- Area: Single
- Cost: 1 `AP`

Roll: `crafting` vs `defense` (`FT` 1)

- Success: Inflict `marked` (`aggregate` 1d6 + `ranks`, `ranks` `severity`)
- Critical: `Aggregate` +2

### Reinforcer (Rank 2)

- Tags: `Passive`

Whenever you would gain `shield`, you gain `ranks` additional `shield`.

### Sharpen (Rank 3)

- Tags: `Interact`
- Range: 2
- Area: Single
- Cost: 1 `AP`

Roll: `crafting` vs 15

- Success: Inflict `sharp` (2 `severity`)
- Critical: `Severity` +1

## Bushcraft

Used for survival tasks in the wilderness, like shelter, identifying edible things, and tracking.

### Blend (Rank 1)

- Tags: `Interact`
- Range: Self
- Area: Single
- Cost: 2 `AP`

Only usable if no hostile `creatures` are adjacent.

Roll: `bushcraft` vs 15 (`FT` 1)

- Success: Gain `evasive` (`ranks` `severity`)
- Critical: `Severity` +1

### Jungler (Rank 2)

- Tags: `Passive`

Moving through `light obstacles` does not cost additional movement.

### Flicker (Rank 3)

- Tags: `Movement`, `Quick`
- Range: 4
- Area: Single
- Cost: 2 `AP`

Move to the unoccupied target location, passing through `light obstacles` and `creatures`. Gain `evasive` (1 `severity`).

## Lore

Used for general knowledge of the world.

### Identify (Rank 1)

- Tags: `Interact`
- Range: 20
- Area: Single
- Cost: 1 `AP`

Roll: `lore` vs 5

- Success: Learn nothing
- Critical: Learn one thing of your choice from the following categories:
  - Traits
  - Actions
  - Stats
  - Other (specify to the GM)

### Convey Tactics (Rank 2)

- Tags: `Passive`

When you roll a `critical` (but not for each `critical`) with Identify, you inflict `marked` (`ranks` `severity`).

### Informed Defense (Rank 3)

- Tags: `Movement`, `Quick`
- Range: Self
- Area: Single
- Cost: 3 `AP`

Until the end of the `round`, you may move 1 `tile` in response to any `action` (no `ap` required). If you do, any `attack` will miss you.

## Alchemy

Used to gather alchemy reagents and create potions.

### Speed Drinker (Rank 1)

- Tags: `Interact`, `Spotlight`
- Range: Self
- Area: Single
- Cost: Varies

Roll: `alchemy` vs 15

- Success: Drink a potion using 1 `ap`
- Critical: This `action` costs 0 `ap`

### Sipper (Rank 2)

- Tags: `Passive`

Potions you drink have 2 uses instead of 1.

### Topical Application (Rank 3)

- Tags: `Interact`
- Range: 4
- Area: Single
- Cost: 1 `AP`

You attempt to apply a potion at range.

Roll: `alchemy` vs 10 (`FT` 1)

- Success: You apply the potion to the target
- Critical: Your potion splashes to 1 adjacent target

## Arcana

Used to identify magic and perform enchantments.

### Mana Battery (Rank 1)

- Tags: `Interact`
- Range: 3
- Area: Single
- Cost: 2

Roll: `arcana` vs 15

- Success: You lose 3 `mana` and your target gains 3 `mana`
- Critical: You lose 1 `mana` and your target gains `ranks` `mana`

If you don't have enough `mana`, your target only gains as much as you have. You may choose to instead reverse the flow if the target is willing.

### Mana Siphon (Rank 2)

- Tags: `Passive`

Your `attacks` steal 1 `mana` from your target.

### Foretell (Rank 3)

- Tags: `Interact`
- Range: Self
- Area: Single
- Cost: 2 `AP`

Roll: `arcana` vs 10

- Success: You gain 5 `mana` at the start of the next `round`
- Critical: You gain 3 `mana` at the start of the next `round`

## Navigation

Used to accurately travel long distances and protect from getting lost.

### Declare the Path (Rank 1)

- Tags: `Movement`, `Spotlight`
- Range: 0
- Area: Aura 2
- Cost: 2 `AP`

Roll: `navigation` vs 15

- Success: Move up to your `speed`. `Creatures` move in the same path as you
- Critical: All `creatures` affected gain 1 `speed` until the end of the next `round`

### Optimized Pathing (Rank 2)

- Tags: `Passive`

You may move diagonally around obstacles.

### Quick Recall (Rank 3)

- Tags: `Movement`
- Range: Self
- Area: Single
- Cost: 1 `AP`

You mark your current location as a recall spot and may move up to 3 `tiles`. At any point before the end of the `round` (even between `action` resolutions), you may return to this spot instantly for 0 `ap`.

## Harvesting

Used to harvest natural resources, like fish, ore, and `creature` parts.

### Soft Spot (Rank 1)

- Tags: `Attack`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `harvesting` vs `defense`

- Success: `Damage` the target (main `stat` -1), and inflict `bruise` (`aggregate` 1d6, `severity` 1)
- Critical: `Severity` +1

### Crippler (Rank 2)

- Tags: `Passive`

When targeting a `mark` other than `body`, the `FT` raises by 1 less.

### Soften (Rank 3)

- Tags: `Attack`
- Range: 1
- Area: Single
- Cost: 2 `AP`

Roll: `harvesting` vs `defense`

- Success: Inflict `bruise` 3
- Critical: `Severity` +2

## Searching

Used to look for non-obvious things.

### Quick Spot (Rank 1)

- Tags: `Interact`, `Spotlight`
- Range: 20
- Area: Circle (`ranks` x 2 radius)
- Cost: 1 `AP`

Roll: `searching` vs 10

- Success: Reveal anything in the area
- Critical: Gain `swift` 1

### Sharp Eyes (Rank 2)

- Tags: `Passive`

You are `resistant` to `blind`.

### Precognition (Rank 3)

- Tags: `Interact`
- Range: 10
- Area: Single
- Cost: 2 `AP`

Pick a target in range. The `priority` of your `actions` used against this `creature` is enhanced by 1. You may only have this active for a single `creature` at a time.

## Locksmithing

Used to open or break locks.

### Smash & Grab (Rank 1)

- Tags: `Interact`, `Quick`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `locksmithing` vs 10 (`FT` 2)

- Success: Undo and open something locked
- Critical: Gain `swift` 1

### Pass (Rank 2)

- Tags: `Passive`

You can move through the space of hostile `creatures`.

### Steal (Rank 3)

- Tags: `Interact`
- Range: 1
- Area: Single
- Cost: 2 `AP`

Roll: `locksmithing` vs `defense`

- Success: Nothing happens
- Critical: Acquire 1 `item` the `creature` had

## Medicine

Used to treat injuries and maladies.

## Field Aid

- Tags: `Interact`
- Range: 1
- Area: Single
- Cost: 1 `AP`

Roll: `medicine` vs 10

- Success: Reduce a `status` by `ranks` `severity`
- Critical: `Severity` reduction increased by 1

### Combat Medic (Rank 2)

- Tags: `Passive`

When using `Field Aid`, you may use these effects instead:

- Success: Inflict `regen` 3
- Critical: `Severity` +1

### Patch Up (Rank 3)

- Tags: `Interact`
- Range: 1
- Area: Single
- Cost: 2 `AP`

Roll for a total using `medicine`. You heal that number of `hitpoints` to the target and they expend 1 `recovery`.
