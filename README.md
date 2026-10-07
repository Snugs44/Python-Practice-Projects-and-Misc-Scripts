# Python Practice Projects

A collection of small Python programs from my programming studies: terminal games, focused language exercises, and early prototypes. These are learning projects rather than production applications.

## Project guide

| Area | Programs | Concepts |
| --- | --- | --- |
| Games | [Animal guessing](games/animal_guessing_game.py), [number guessing](games/number_guessing_game.py), [quiz](games/quiz_game.py), [rock-paper-scissors](games/rock_paper_scissors.py) | Input, conditionals, loops, random selection |
| Dictionaries | [Month lookup](exercises/dictionaries/month_lookup.py) | Key/value lookup |
| Functions | [Exponentiation](exercises/functions/exponentiation.py) | Functions and repeated multiplication |
| Strings | [Username generator](exercises/strings/username_generator.py), [substring check](exercises/strings/substring_check.py) | Slicing and membership tests |
| Calculators | [Calories-burned exercise](calculators/calories_burned.py) | Numeric input and arithmetic |
| Prototypes | [Slot-machine prototype](prototypes/slot_machine.py) | Input validation and nested collections; unfinished |

## Run an exercise

Install Python 3 and run a file directly from the repository root. The existing scripts use only the standard library; no third-party packages are required.

```sh
python games/animal_guessing_game.py
python exercises/dictionaries/month_lookup.py
python exercises/functions/exponentiation.py
```

Use `python3` instead of `python` where that is your Python 3 command, or `py -3` on Windows. Interactive programs prompt in the terminal; Ctrl+C stops a running program.

## Current status

The original scripts are preserved unchanged during this organization pass. Some contain unfinished behavior or known bugs; see [known limitations](docs/known_limitations.md) before treating them as reference implementations. The calorie calculation is an unvalidated programming exercise, not a health tool.

## Repository layout

```text
calculators/              Small numeric-input exercises
exercises/
  dictionaries/           Lookup examples
  functions/              Function and loop examples
  strings/                String manipulation examples
games/                    Interactive terminal games
prototypes/               Unfinished experiments
docs/                     Maintenance notes and original-to-current paths
```

Use lowercase `snake_case.py` filenames that describe the program. Keep short concept demonstrations in `exercises/`, interactive games in `games/`, and incomplete experiments in `prototypes/`. No Python package layout is imposed on these independent scripts.

The [rename map](docs/renamed_files.md) records every original filename so older bookmarks and coursework references are easy to trace.
