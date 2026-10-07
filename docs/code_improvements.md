# Code improvements

Structural moves and behavior changes are kept in separate commits for review.

| Program | Improvement |
| --- | --- |
| Rock-paper-scissors | Normalize both choices, resolve all nine matchups, track ties separately, ignore invalid choices, support quitting, and print reachable final scores. |
| Number guessing | Validate integer input and inclusive bounds, reject inverted ranges, support equal bounds including zero, and count only valid guesses. |
| Animal guessing | Normalize input, keep an explicit five-guess limit, and support quitting. |
| Hardware quiz | Honor declining to play, use one consistent scoring loop, normalize whitespace/case, and replace the joke/incorrect answer entries with a four-question hardware quiz. |
| Month lookup | Expose a reusable case-insensitive lookup with an explicit error for unknown abbreviations. |
| Exponentiation | Return the value instead of printing inside the function; reject negative or noninteger exponents while preserving the loop-based exercise. The direct-run example still prints `125`. |
| Username generator | Trim surrounding whitespace and reject empty names while retaining the original short-name fallback. |
| Substring check | Return the membership expression directly and document its case-sensitive/empty-string behavior. |
| Calories-burned exercise | Validate positive finite inputs, handle arithmetic overflow, and isolate the calculation. Preserve the original equation and its parentheses; no physiological validation is claimed. |
| Slot-machine prototype | Return correctly sized columns, sample from available symbol copies without replacement within a column, validate counts, prevent unaffordable input combinations, and display a grid preview. No payout rules are invented. |

All ten modules can be imported without prompting or printing. Terminal entry points handle end-of-input and interruption. Functions have focused docstrings and type hints without adding a framework or third-party dependencies.

## Why these changes work

Separating game rules from terminal input makes outcomes directly testable. Validating input before random-number generation or arithmetic prevents the original invalid-state errors. Regression tests exercise both helper functions and actual script entry points, so improvements are checked beyond syntax alone.
