# Manual Archipelago for The Binding of Isaac: Rebirth - Greed Mode

## Options
`available_characters`: List of characters that **can** be chosen to be played with.
`character_amount`: Amount of characters from the above list to be **actually included**.
`starting_characters`: Amount of characters to start with.
`ultra_greed_kills_goal`: Amount of Ultra Greed kills (with different characters) needed to win the game.

## Locations
For each included character, you have :
- Hold 9/18/27/36/45/54/63/72 coins 
- Clear Enemy Waves (Floor 1 - Floor 6)
- Clear Boss Waves (Floor 1 - Floor 6)
- Clear Nightmare Waves (Floor 1 - Floor 6)
- Defeat Miniboss (the one just before Ultra Greed)
- Defeat Ultra Greed
- Greed Counter (see the goal explanation)

## Items
For each included character, you have:
### Progression
- Progressive Floor x6
> Unlocks next floor
- Progressive Shop x6
> Unlocks using the shop
- Progressive Golden Item x5
> Unlocks golden room's item
- Progressive Silver Item x5
> Unlock silver room's item
### Filler
- Extra Coin x15

Those extra coins work just as a Bonus Point in Yacht Dice: extra coins that are out of logic and should help completing the "Hold X coins" checks (you may just choose to ignore it as well, it's up to you, just needed something to fill the filler slots)

## Goal (+ explanation)
The goal is to defeat Ultra Greed a determined amount of times, chosen in the `ultra_greed_kills_goal` yaml option.

The way I did it is that whenever you kill Ultra Greed, you should send 2 checks: `Defeat Ultra Greed` and `Greed Counter`.
- `Defeat Ultra Greed` is a normal check: it sends a random item from the pool to a random game.
- `Greed Counter`, however, is a fixed check: it sends a Greed Counter to yourself, and you need these to logically access your victory location.
