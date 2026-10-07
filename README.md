# Python Practice Projects

Small Python programs from my programming studies: terminal games, focused language exercises, and an early symbol-grid prototype. These are learning projects, not production applications.

## Project guide

| Area | Programs | Concepts |
| --- | --- | --- |
| Games | [Animal guessing](games/animal_guessing_game.py), [number guessing](games/number_guessing_game.py), [hardware quiz](games/quiz_game.py), [rock-paper-scissors](games/rock_paper_scissors.py) | Input validation, conditionals, loops, random selection |
| Dictionaries | [Month lookup](exercises/dictionaries/month_lookup.py) | Key/value lookup and error handling |
| Functions | [Exponentiation](exercises/functions/exponentiation.py) | Returning values and repeated multiplication |
| Strings | [Username generator](exercises/strings/username_generator.py), [substring check](exercises/strings/substring_check.py) | Slicing and membership tests |
| Calculators | [Calories-burned exercise](calculators/calories_burned.py) | Numeric input and arithmetic; unverified equation |
| Prototypes | [Slot-machine prototype](prototypes/slot_machine.py) | Virtual-credit input and symbol sampling; no payout system |

## Run an exercise

Use **Python 3.10 or newer**. Run commands from the repository root. No third-party packages are required.

```sh
python games/rock_paper_scissors.py
python games/number_guessing_game.py
python exercises/functions/exponentiation.py
```

Use `python3` where that is your Python 3 command, or `py -3` on Windows. Interactive programs accept terminal input and exit cleanly on Ctrl+C or end-of-input. Rock-paper-scissors and animal guessing also accept `q` to quit.

## Run the tests

```sh
python -m unittest discover -s tests -v
```

The standard-library test suite covers game outcomes, invalid inputs, scoring, function return values, symbol sampling, import safety, and direct execution of all ten scripts. It includes 42 test methods, with additional parameterized cases inside them. The suite was run locally using Python 3.13.5 on Linux; other operating systems and Python versions have not been validated in this cleanup.

## Repository layout

```text
calculators/              Numeric-input exercises
exercises/
  dictionaries/           Lookup examples
  functions/              Function and loop examples
  strings/                String manipulation examples
games/                    Interactive terminal games
prototypes/               Unfinished experiments
tests/                    Standard-library regression and smoke tests
docs/                     Change notes, limitations, and rename map
```

Use descriptive lowercase `snake_case.py` filenames. Keep concept demonstrations small and run each script directly; importing a module does not start a game or print demonstration output.

## Changes and scope

The first cleanup commit reorganizes the original files without changing their contents. A separate follow-up commit fixes existing bugs and improves input handling, naming, docstrings, and testability. The original work remains in Git history; [the rename map](docs/renamed_files.md) traces every old path.

See [code improvements](docs/code_improvements.md) for behavior changes and [remaining limitations](docs/known_limitations.md) for scope. In particular, the slot-machine program remains a prototype and the calorie equation remains unvalidated.
