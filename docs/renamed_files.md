# File rename map

All ten original exercises remain represented. The first cleanup commit changes paths only; the subsequent code-improvement commit updates their implementations and adds tests. Original versions remain in Git history.

| Previous path | Current path |
| --- | --- |
| `Calories_burned.py` | `calculators/calories_burned.py` |
| `Monkey_guessing_game.py` | `games/animal_guessing_game.py` |
| `number_guesser.py` | `games/number_guessing_game.py` |
| `quiz_game.py` | `games/quiz_game.py` |
| `rock_paper_scissors.py` | `games/rock_paper_scissors.py` |
| `simple_dic_month_conversion.py` | `exercises/dictionaries/month_lookup.py` |
| `simple_exponent_func.py` | `exercises/functions/exponentiation.py` |
| `simple_username_generator.py` | `exercises/strings/username_generator.py` |
| `slot_machine_basic.py` | `prototypes/slot_machine.py` |
| `string_check_within_string.py` | `exercises/strings/substring_check.py` |

Update saved run configurations and bookmarks to the new paths. The original scripts had no imports of one another or repository-relative file reads. The new tests reference the organized paths. See [behavior changes](code_improvements.md) before reusing the updated functions in other code.
