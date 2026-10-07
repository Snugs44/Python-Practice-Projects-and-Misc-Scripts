# Known limitations

These notes describe the original learning scripts. The organization pass deliberately preserves their behavior; fixes can be reviewed separately from file moves.

| File | Existing behavior to revisit |
| --- | --- |
| `games/rock_paper_scissors.py` | Computer choices are capitalized, while winning comparisons use lowercase strings, so the win branches do not match. Ties count as losses. There is no exit branch, making the final summary unreachable during normal play. |
| `games/number_guessing_game.py` | The program does not check that the minimum is less than or equal to the maximum before calling `random.randint`; an inverted range raises an error. |
| `games/quiz_game.py` | The opening conditions repeat the same expression and do not implement a proper decline/exit path. Some questions and accepted answers are jokes, not a technical knowledge assessment. |
| `games/animal_guessing_game.py` | Guesses are case-sensitive because input is not normalized. |
| `prototypes/slot_machine.py` | This is unfinished: the current entry point collects a deposit and bet but does not play a round. The spin helper does not return its result, starts with extra empty columns, and selects from the original pool while removing from a separate pool. No payout or balance-update loop is implemented. |
| `calculators/calories_burned.py` | Numeric input is not validated. The original calculation, including its grouping, is retained without validating the equation or its assumptions. Do not interpret it as a calibrated health or fitness estimator. |
| `exercises/functions/exponentiation.py` | Intended for nonnegative integer exponents. It prints a result rather than returning one, and does not reject negative exponents. |

Several scripts execute demonstration code or start prompting as soon as they are imported. Run them directly rather than importing them as a reusable package. A future behavior-focused cleanup could introduce `main()` guards and tests without obscuring this structural change.
