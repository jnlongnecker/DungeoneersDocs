# Blessings

A gift from the gods. You can have a number of `blessings` equal to your `faith` score. If you lose `favor` with the god whose `blessing` you have accepted, you lose the `blessing` but may choose another `blessing` from a god whose `favor` you have.

# Favor

You gain `favor` with a god if you do things to show your worship & devotion. You lose `favor` with a god by gaining `favor` with a rival god. Each god has something specific they want to show their devotion, but you may show your devotion to any god by performing any of the following `activities`:

## Prayer

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You make a genuine, bespoke prayer to a god at a shrine, temple, statue, or other similar holy place of relevance to the god. In return, you gain 2 `favor` with the god. Each time you repeat the prayer at the same location, the `favor` you gain is reduced by 1 until you do this prayer at a new location.

## Make Offering

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You partake in a ritual offering to a god. You offer something that the god values (specified on the god), which is divinely consumed upon completion. In return, you gain 2 `favor` with the god. Each time you offer the same thing, the `favor` you gain is reduced by 1 until you offer something new.

# God of War

Values weapons of fallen foes, treasure taken in conquest, and armor that has suffered many blows.

## Dirge of a Worthy Combatant

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual to offer the corpse of a powerful, fallen foe. You must have taken part in its demise, and it must have dealt `damage` to you. In return, you gain 3 `favor`.

## Crimson Offering

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You partake in the ritual consumption of the blood of your foes. You bleed a `creature` you have killed recently and drink its blood in ritual. Until the end of your next `downtime`, you deal 1 additional `damage`.

## Blessings

### Berserk

- Prerequisite: 5 `favor`
- Tags: `Interact`
- Range: Self
- Area: Single

You enter a fury for `faith` `rounds`. During this time, you forfeit all `shield` and in exchange, you gain 2 `speed` and deal 1 additional `damage` per 3 `hitpoints` lost.

### Bloodthirst

- Prerequisite: 5 `favor`
- Tags: `Interact`
- Range: Self
- Area: Single
- Cost: 1 `mana`

Your `attacks` inflict `leech` 1d6 for the remainder of the `procedure`.

### Bloodletter

- Prerequisite: 5 `favor`
- Tags: `Interact`
- Range: Self
- Area: Single
- Cost: 2 `mana`

Your `attacks` inflict `bleed` 1d6 for the remainder of the `procedure`.

### Blood Spike

- Prerequisite: 5 `favor`
- Tags: `Attack`
- Range: 3
- Area: Single
- Cost: 1 `mana`

Pick a target within `range` 4 from a `creature` with blood in `range`. The `creature` the `attack` uses takes 2 `damage`.

Roll: `prowess` vs `defense`

- Success: Deal `damage` -1
- Critical: Inflict `bleed` 1d6 to both `creatures`

### Blood Burst

- Prerequisite: 10 `favor`
- Tags: `Attack`
- Range: 5
- Area: Circle 3
- Cost: 5 `mana`

Target a `bleeding` `creature`

Roll: `control` vs 10

- Success: Deal `damage`
- Critical: If the `creature` occupies multiple `tiles`, an additional explosion occurs from a different occupied `tile`

### Exsanguinate

- Prerequisite: 10 `favor`
- Tags: `Attack`
- Range: 3
- Area: Single
- Cost: 3 `mana`

Roll: `control` vs `defense`

- Success: Deal `damage` -2; heal that number of `hitpoints`
- Critical: Inflict `bleed` 1d6

`Creatures` killed by this leave no usable corpse.

### Fury

- Prerequisite: 10 `favor`
- Tags: `Attack`, `Inherit`
- Range: Self
- Area: Single
- Cooldown: 20
- Cost: 4 `mana`

Use an `attack` twice. Your `base damage` is halved. On each `critical`, you `attack` an additional time

### Blade Storm

- Prerequisite: 15 `favor`
- Tags: `Attack`
- Range: `faith`
- Area: Single
- Cooldown: 20
- Cost: 5 `mana`

Roll: `prowess` vs 5

- Success: Deal `damage` and land adjacent to the target. If this kills the target, make this `action` again
- Critical: Trigger the `success` again, selecting a new target in `range` from the new location

### Crimson Baptism

- Prerequisite: 15 `favor`
- Tags: `Attack`
- Range: 2
- Area: Single
- Cooldown: 20
- Cost: 5 `mana`

Roll: `faith` vs `hitpoints`

- Success: Inflict `bleed` `faith`d6
- Critical: Target dies and you regain their `hitpoints`

# God of Death

Values fungi, bones, and incense.

## Black Sacrament

- Tags: `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual sacrament over the recent death of a group (i.e. more than 1) of `creatures`. Upon completion, all flesh is stripped from the corpses, restoring 1 `hitpoint` per `creature`. In exchange, you gain 1 `favor`.

## Servant of Death

- Tags: `Ritual`, `Short`
- Range: Self
- Area: Single
- Cost: 2 `mana`

You perform this rite over the corpse of a `creature`. You compel any remaining mana to eternally serve as a `shadow servant`. You have a limit of `faith` `shadow servants` to imbue in this way.

You can instantly, trivially, and at will, recall the `shadow servants` into your shadow at the start of a `round`. Unless you will it otherwise, they automatically step out of your shadow at the start of a `combat procedure` or `chase procedure`. Otherwise, it is an `action` to release any number of them from your shadow.

## Blessings

### Path to the Grave

- Prerequisite: 5 `favor`
- Tags: `Attack`
- Range: 3
- Area: Single
- Cost: 1 `mana`

Roll: `control` vs `defense`

- Success: Inflict `decay` 1d6
- Critical: +1d6 `aggregate`

### Death Hungers

- Prerequisite: 5 `favor`
- Tags: `Interact`
- Range: Self
- Area: Single
- Cost: 1 `mana`

You and 1 `creature` of your choice you can see gain `decay` 1 at the start of every `round` of this `procedure`.

### Bonelegion

- Prerequisite: 5 `favor`
- Tags: `Interact`, `Quick`
- Range: Self
- Area: Single
- Cost: 2 `mana`

You compel all `shadow servants` under your control to `move` 1 `tile` immediately.

### Bonesavior

- Prerequisite: 5 `favor`
- Tags: `Interact`, `Quick`
- Range: Self
- Area: Single
- Cost: 2 `mana`

You grant all `shadow servants` under your control `faith` `shield`

### Bonekeeper

- Prerequisites: 10 `favor`
- Tags: `Interact`, `Quick`
- Range: Self
- Area: Single
- Cost: 3 `mana`

You grant all `shadow servants` under your control a +2 bonus to `base damage` for this `round`

### Mortal Infliction

- Prerequisite: 10 `favor`
- Tags: `Passive`
- Cost: 1 `mana`

Your `statuses` ignore `undead` `immunities`.

### Force of Decay

- Prerequisites: 10 `favor`
- Tags: `Attack`
- Range: 4
- Area: Single
- Cooldown: 3
- Cost: 2 `mana`

Select a `creature` with `decay`.

Roll: `prowess` vs `defense`

- Success: Inflict `decay` 1; trigger `decay` `damage`
- Critical: +1 `decay`

### Wave of Decay

- Prerequisites: 15 `favor`
- Tags: `Attack`
- Range: Self
- Area: Cone `faith`
- Cooldown: 10
- Cost: 5 `mana`

Roll: `control` vs `defense`

- Success: Deal 1 `damage`; inflict `faith` `decay`. Deal `faith` `damage` instead if target has `decay`
- Critical: +2 `damage`

### Bonemeal

- Prerequisites: 15 `favor`
- Tags: `Interact`
- Range: Self
- Area: Single
- Cooldown: 20
- Cost: Varies

Per `mana` you spend, restore `faith` `hitpoints` to one `shadow servant` under your control.

# God of Chaos

Values anything. When making an offering, roll 1d6. On a 4 or higher, your offering is accepted. Otherwise, you take 1 `true damage`.

## Sow Confusion

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You defile an orderly place with the element of chaos. You change labels, scatter organizations, move furniture, and place anything and everything in disarray. In exchange, you gain 2 `favor`.

## O Fickle Faith

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You gain a bane and a boon from the following table. Roll 1d6 for each to determine your result.

| Boon                                                       | Bane                                                        | Roll |
| ---------------------------------------------------------- | ----------------------------------------------------------- | ---- |
| Gain `thorns` 1 for the next `combat procedure`            | Gain `bruise` 3 at the start of the next `combat procedure` | 1    |
| Gain `sharp` 3 at the start of the next `combat procedure` | Gain `blind` 3 at the start of the next `combat procedure`  | 2    |
| Restore `faith` `hitpoints`                                | Lose 5 `hitpoints` (bringing you to a min of 1)             | 3    |
| Gain full `mana`                                           | Lose all `mana`                                             | 4    |
| Regain 1 `recovery`                                        | Lose 1 `recovery`                                           | 5    |
| Gain `ghost` 1 at the start of the next `combat procedure` | Nothing happens                                             | 6    |

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Darkness

Values cursed things, forgotten relics, and all things touched by the void.

## Blackout

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual to envelop a bright location in the purest dark. Upon completion, an unnatural darkness decends in a radius 4 sphere. In exchange, you gain 3 `favor`.

## Void Communion

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Circle (6 radius)

In a place of pure darkness, you may perform this ritual. You send yourself and everything in the `area` to the void for a moment. You may exchange 5 `hitpoints` to ask about something that came with you to the void, or to let an `item` in your possession to become `void-touched`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Light

Values light sources, once cursed items, and sun-dried fruits

## Purify the Darkness

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

At the site of an unspeakable evil or foul conduct, you perform a purification ritual. In exchange, you gain 3 `favor`.

## Beacon in the Dark

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform an illumination ritual, causing you to shed light for 1 hour.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Life

Values seeds, fruits & vegetables, and bone meal

## Foster the Youth

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a fertility ritual, centered on a fragile form of new life (seed in plagued soil, lone cracked egg, abandoned infant animal). Unless defiled by equally powerful darkness, this life will be sustained for its natural duration. In exchange, you gain 3 `favor`.

## Expedited Recovery

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

Once per day, you may perform a ritual of vitality. All `creatures` within the same `zone` regain `faith` (your `faith`) `hitpoints` and may expend up to 2 `recoveries`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Redemption

Values prayer beads, murder weapons, and stolen goods

## Save a Soul

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of divine redemption on a `creature` that has committed a foul act. You explain that this ritual will resign their soul to your god and they will have a permanent compulsion to repent for their sins. If the `creature` is willing, you perform and complete the ritual. In exchange, you gain 5 `favor`.

## Emissary of Peace

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of peace, marking yourself as a peacful individual. All `creatures` you meet for the remainder of the day will innately understand this about you and act accordingly. Should you or your allies violate this covenant and do harm to those who are not harming you, you will lose 10 `favor`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Justice

Values law books, gavels, and chains that have held criminals

## Pass Judgement

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of judgement on a `creature` that has been captured. Upon completing this ritual, you learn the judgement and punishment passed down by your god. You gain 3 `favor` by carrying out this punishment.

## Smite the Sinner

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of retribution. You gain 3 `thorns` until the end of the next `combat procedure`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

---

# God of Knowledge

Values books, scrolls, and artifacts

## Donation to the Communal Library

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of sacrificial knowledge to offer information to the great library. You offer knowledge that can be accessed by any worshipper of your god, forgetting it in the process. You gain between 0-5 `favor` depending on how rare the knowledge is, and an equal number of `library credits`.

## Checkout from the Communal Library

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of knowledge retrieval from the great library. You must exchange `library credits` or `favor` in exchange for the knowledge you seek; between 0-5 depending on how rare the knowledge is. If the knowledge has not been checked into the library, it will not be available.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Crafts

Values things built by the offerer and used for its original purpose

## Masterwork Study

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of study by using a masterwork item. Doing so imprints the story of the masterwork in your mind. There are 3 parts to each story, and each part requires its own ritual. Once you know all 3 parts, you can no longer gain `favor` from the masterwork. In exchange, you gain 3 `favor`.

## Impromptu Workshop

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual to turn the `zone` you are in into a makeshift workshop. All tools you need for your craft can be found here. This effect ends when you leave the `zone`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Nature

Values flowers, trees, and overgrowth

## Grove

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a communion ritual in a place untouched by civilization. You mark it as a site to be protected and your god ushers in a steward to maintain the area. In exchange, you gain 3 `favor`.

## Guardian

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a protection ritual to mark yourself as a friend to nature. Animals will recognize your benevolence and plants will not impede your progress for the remainder of the day. You are not hindered by natural `light obstacles`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# God of Storms

Values shells, sea foam, and brine

## Embrace the Storm

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a reverence ritual in the middle of a storm. In a rain, snow, or thunder storm, tornado, hail, or similar extreme weather, you embrace the elements for the duration of the ritual. In exchange, you gain 5 `favor`.

## Shelter

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You perform a ritual of protection from the elements. For an entire day after the completion of the ritual, the `zone` your performed this ritual in is protected from any weather or extreme temperatures.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

---

# Spiritualism

Instead of offerings & prayers, you meditate using incense and any item(s) you find of spritual significance.

## Spiritual Connection

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You immerse yourself in a moment of peace in an attempt to connect with yourself on a deeper level. You gain 1 `favor`.

## Mind and Body

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You focus your spirituality and hone your body and mind as one. You gain `magic` `mana`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15

# Atheism

You practice no faith and instead turn to inward yourself. You do not pray or provide offerings.

## Reflection

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You take a moment to deeply reflect on yourself, your emotions, and your betterment. You gain 1 `favor`. You may perform this once per day.

## Insight

- Tags: `Activity`, `Ritual`, `Short`
- Range: Self
- Area: Single

You exert your command over your learnings in a moment of focus. You gain `brace` 1 until the end of the next `combat procedure`.

## Blessings

### Favor 5

### Favor 5

### Favor 5

### Favor 5

### Favor 10

### Favor 10

### Favor 10

### Favor 15

### Favor 15
