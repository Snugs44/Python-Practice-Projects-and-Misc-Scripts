"""A virtual-credit input and symbol-grid prototype, not a complete game.

There is no payout calculation or balance-update loop. No money is involved.
"""

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
SYMBOL_COUNTS = {"A": 2, "B": 4, "C": 6, "D": 8}


def get_slot_machine_spin(rows: int, cols: int, symbols: dict[str, int]) -> list[list[str]]:
    """Return columns sampled without replacement within each column.

    Counts represent separate copies of a symbol; the pool resets per column.
    """
    if type(rows) is not int or type(cols) is not int or rows < 1 or cols < 1:
        raise ValueError("Rows and columns must be positive integers.")
    if not symbols or any(type(count) is not int or count < 1 for count in symbols.values()):
        raise ValueError("Symbol counts must be positive integers.")
    pool = [symbol for symbol, count in symbols.items() for _ in range(count)]
    if rows > len(pool):
        raise ValueError("There are not enough symbol copies for one column.")
    return [random.sample(pool, rows) for _ in range(cols)]


def read_amount(prompt: str, minimum: int, maximum: int | None = None) -> int:
    """Prompt for an integer amount within the supplied inclusive bounds."""
    if maximum is not None and minimum > maximum:
        raise ValueError("Minimum cannot exceed maximum.")
    while True:
        try:
            amount = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if amount >= minimum and (maximum is None or amount <= maximum):
            return amount
        limit = f"{minimum}-{maximum}" if maximum is not None else f"at least {minimum}"
        print(f"Enter {limit} credits/lines.")


def deposit() -> int:
    return read_amount("Starting virtual credits: ", 1)


def get_number_of_lines(maximum: int = MAX_LINES) -> int:
    return read_amount(f"Lines to select (1-{maximum}): ", 1, maximum)


def get_bet(maximum: int = MAX_BET) -> int:
    return read_amount(f"Virtual credits per line ({MIN_BET}-{maximum}): ", MIN_BET, maximum)


def main() -> None:
    print("Symbol-grid prototype: virtual credits only; no payout system.")
    balance = deposit()
    # Restrict lines and bet size so even the minimum bet is affordable.
    lines = get_number_of_lines(min(MAX_LINES, balance // MIN_BET))
    bet = get_bet(min(MAX_BET, balance // lines))
    print(f"Selected {bet} credits on {lines} line(s): {bet * lines} credits total.")
    columns = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNTS)
    for row in zip(*columns):
        print(" | ".join(row))
    print("Preview only: no credits were deducted and no payout was calculated.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
