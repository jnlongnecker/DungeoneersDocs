# Rolls

Whenever a `roll` is called for, a six-sided dice is used (1d6). Roll 1d6 and record the result. If it is at or below the `failure threshold`, the roll fails. On anything else, add the number rolled to the `stat` score called for, then any other bonuses such as `boons` and `banes`. If this `total` is greater than the `difficulty` (and every 5 greater thereafter), the `roll` is a `critical` and gains additional or improved effects. Otherwise, the `roll` is simply a normal `success`.

GMs should use discretion when calling for a `roll` outside of when the rules explicitly require one and use their judgement on whether the character making the would-be `roll` could actually, realistically fail it. Dungeoneers are competent experts; most `rolls` are to see how _successful_ the outcome is rather than whether or not it succeeds.

# Total Roll

Sometimes, you will just be asked to `roll` for a `total`. In this case, there's no `difficulty` to `roll` against. The only purpose of the `roll` is to get a randomized number for some use by an ability. These `rolls` look a little different and use this language:

Roll for a `total` using [`stat`].

# Reaction Roll

Dangerous things in the world may give need for a player character to need to react and avoid harm. In these instances, a `reaction roll` is called for. As a player, you won't see any `reaction rolls` but to the `GM`, they will look like this:

`React`: [`stat`] vs [`target`]

- Fail: What happens if you don't beat the `target`
- Success: What happens if you do beat the `target`

`Reaction rolls` have a binary outcome; either you pass or you don't. There is no `failure threshold` with these `rolls`, but there's also no guaranteed success. You must `roll` equal to or greater than the `target` in order to succeed.

# Failure Threshold

Normally, the `failure threshold` (`FT`) is 0 meaning the `roll` cannot fail. For `rolls` that could realistically fail, the `failure threshold` is usually 1. Increasing beyond this should only occur when the outcome is extremely uncertain or there are features that explicitly raise this value. Regardless of any features, the `failure threshold` cannot exceed 5.

For GMs, should you desire a scenario where the `failure threshold` _does_ exceed 5, calling for a `roll` has no point. A `roll` only makes sense when there is a possibility of multiple results.

# Explosion Threshold

Whenever a `roll` is made, the `luck` `stat` is consulted. Calculate 10 - `luck`; this is your `explosion threshold`. If the roll of the die is at or above the `explosion threshold`, you roll an additional die. For this new die, reduce your `luck` by 6 and repeat the initial calculation for your new `explosion threshold`.

# Difficulty

The `difficulty` of a `roll` is the number that must be exceeded in order to turn the `roll` into a `critical`. `Difficulty` comes along with a natural language name to better translate the number into in-world meaning:

| Difficulty Number | Natural Language Description |
| ----------------- | ---------------------------- |
| 5                 | Easy                         |
| 10                | Average                      |
| 15                | Hard                         |
| 20                | Insane                       |
| 25                | Nearly Impossible            |
| 30                | Impossible                   |

# Notation of Rolls

`Failure threshold` is notated if it is different than normal.

Roll: [`stat` to add] vs [`difficulty`] (`FT` \_)

- Success: What happens when you succeed
- Critical: What happens on each `critical`
