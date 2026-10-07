# Remaining limitations

These are intentionally small learning projects. Passing tests establish the covered behavior, not production readiness.

- **Slot-machine prototype:** virtual-credit input and a symbol-grid preview only. There is no payout calculation, balance-update loop, persistence, or real-money functionality. Sampling resets the symbol pool for every column.
- **Calories-burned exercise:** the original equation, including its grouping, has not been validated. Input and arithmetic tests do not establish health or fitness accuracy. Positive numeric inputs can still be physiologically implausible, and the unverified equation can produce implausible results.
- **Exponentiation:** accepts nonnegative integer exponents only and intentionally uses repeated multiplication. It is a loop exercise, not an optimized general-purpose numeric library.
- **Username generator:** preserves case and internal characters, and does not guarantee uniqueness or implement an account-system naming policy.
- **Games:** terminal-only, without saved scores. Quiz matching ignores case and whitespace but expects the documented answer wording.

Validation was performed locally on Linux with Python 3.13.5. No hosted CI run, Windows run, or macOS run is claimed. Run the suite from the repository root with `python -m unittest discover -s tests -v`.
