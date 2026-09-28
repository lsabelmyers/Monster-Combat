# Monster Combat

A turn-based RPG where you fight a dragon in the terminal.

## About

Monster Combat is a turn-based combat game written in Python. Each round, you
choose one of four actions: attack the dragon, heal yourself, summon an ally,
or poison the monster. The dragon fights back after every turn, so you have to
think about which move makes sense instead of just attacking over and over.

The dragon's starting health is randomized, and so is the damage from every
action, so no two playthroughs go the same way. Summon three allies in one
fight and you get a bonus 10 damage attack. Every action you take is logged to
a file so you can look back at what worked.

## How to run it

You need Python 3 installed.

```
python monster_combat.py
```

Everything runs in the terminal. Your HP, the dragon's HP, and your options
are shown every turn.

## Features

- Object-oriented design with a `Fight` class managing player state, monster
  state, and combat modifiers
- Randomized monster HP and damage ranges for replayability
- A poison mechanic that deals damage over time and decays each turn
- An ally mechanic that blocks incoming damage and rewards a bonus attack at
  three summons
- Input validation so invalid choices don't skip your turn
- A replay loop that tracks your win/loss record across rounds
- Action logging to `gamelog.txt` for reviewing past games

## Project background

This started as a project for Cornerstone of Engineering at Northeastern
University, and I've since cleaned it up and expanded it with input
validation and a replay system.
