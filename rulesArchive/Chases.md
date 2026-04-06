# Chase

A `chase procedure` begins with all `creatures` determining their `stamina`. At the end of every `round`, the fleeing group determines which `zone` to next move into. Divide the `zone` in half; the pursuing group occupies the half closest to the last `zone` and the fleeing group occupies the half furthest. If there is an obstacle, each individual must be able to clear it and do so in order to remain in the chase; otherwise their `stamina` falls to 0. If there isn't an adjacent `zone` to move into, the fleeing group is cornered and the `procedure` ends.

If a `creature` falls to 0 `stamina`, they can no longer participate in the chase. If they are in the pursuing group, the target gets away. If they are being chased, they are caught up to and cannot re-initiate a `chase procedure`. Those pursuing may choose whether to continue to pursue `creatures` that are still fleeing or start a new `procedure` with any `creatures` that stop fleeing. Those fleeing may choose whether to stop fleeing and remain with the `creature` with 0 `stamina`.

# Stamina

`Creatures` begin a `chase procedure` with `stamina` equal to their remaining `hitpoints` + their `speed`. At the end of each `round`, every `creature` participating in the chase loses 2 `stamina`. If a `creature` takes `damage`, they lose `stamina` equal to the `damage` they take.
