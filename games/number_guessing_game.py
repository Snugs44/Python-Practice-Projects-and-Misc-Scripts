"""Guess a random integer within a user-selected range from 0 to 100."""

import random


def read_int(prompt: str, minimum: int, maximum: int) -> int:
    """Prompt until an integer within the inclusive bounds is supplied."""
    if minimum > maximum:
        raise ValueError("Minimum cannot exceed maximum.")
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Please enter a number from {minimum} to {maximum}.")


def choose_number(minimum: int, maximum: int) -> int:
    """Choose a target, rejecting inverted or unsupported ranges."""
    if type(minimum) is not int or type(maximum) is not int:
        raise ValueError("Bounds must be whole numbers.")
    if not 0 <= minimum <= maximum <= 100:
        raise ValueError("Bounds must satisfy 0 <= minimum <= maximum <= 100.")
    return random.randint(minimum, maximum)


def main() -> None:
    answer = input("Welcome! Would you like to play? (yes/no): ").strip().lower()
    if answer not in {"yes", "y"}:
        print("Okay, goodbye!")
        return
    maximum = read_int("Maximum number (0-100): ", 0, 100)
    minimum = read_int(f"Minimum number (0-{maximum}): ", 0, maximum)
    target = choose_number(minimum, maximum)
    attempts = 0
    while True:
        guess = read_int(f"Your guess ({minimum}-{maximum}): ", minimum, maximum)
        attempts += 1
        if guess == target:
            print(f"You nailed it in {attempts} guess(es)!")
            return
        print("Try guessing higher!" if guess < target else "Try guessing lower!")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
