# Tier 1 Adversaries

## Skeleton Soldier

_Medium Undead Grunt, D1_

- HP: 3
- Damage: 2
- Move: 2

| Speed | Defense | Prowess | Control |
| ----- | ------- | ------- | ------- |
| 1     | 1       | 1       | 1       |

### Passive - Shielder

Gain `shield` 3 at the start of every `round`.

### Strike

- Range: 1
- Area: Single

`Adversary roll`

- Success: Deal `damage`
- Critical: +1 `damage`

### Clatter

- Range: Self
- Area: Aura 3

`React`: `control` vs 3

- Fail: `Fear` 1
- Success: Resist

## Skeleton Archer

_Medium Undead Grunt, D1_

- HP: 3
- Damage: 1
- Move: 1

| Speed | Defense | Prowess | Control |
| ----- | ------- | ------- | ------- |
| 1     | 1       | 1       | 1       |

### Passive - Executioner

Gain +1 `damage` to targets without full `hitpoints`

### Strike

- Range: 4
- Area: Single

`Adversary roll`

- Success: Deal `damage`
- Critical: +1 `damage`

### Mark

- Range: 4
- Area: Single

`Marked` 1 (1d6 `aggregate`)

## Zombie

_Medium Undead Bruiser, D2_

- HP: 5
- Damage: 3
- Move: 1

| Speed | Defense | Prowess | Control |
| ----- | ------- | ------- | ------- |
| -1    | 0       | 0       | 0       |

## Passive - Weak Spot

Can only be killed by a hit to the `weakness` `mark`, which instantly kills it. Being reduced to 0 `hitpoints` lowers the `FT` to hit a `mark` by 1 and regenerates all `hitpoints`

### Rend

- Range: 1
- Area: Single

`Adversary roll`

- Success: Deal `damage`
- Critical: `poisoned` 1

### Bite

- Range: 1
- Area: Single
- Cooldown: 2

If this kills the target, their mana coalesces as a `zombie`.

`Adversary roll`

- Success: Deal `damage` + 2
- Critical: `bruise` 1
