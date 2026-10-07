"""An arithmetic exercise retaining an unverified historical calorie equation.

This is not a validated health estimator. The original equation and its
parentheses are deliberately preserved rather than silently corrected.
"""

import math


def calculate_calories(age: float, weight: float, heart_rate: float, minutes: float) -> float:
    """Evaluate the original expression using positive, finite inputs.

    Units from the original exercise: years, pounds, beats/minute, and minutes.
    Tests verify input handling and arithmetic, not physiological accuracy.
    """
    values = (age, weight, heart_rate, minutes)
    if any(not math.isfinite(value) or value <= 0 for value in values):
        raise ValueError("Inputs must be positive, finite numbers.")
    calories = (
        age * 0.2757
        + weight * 0.03295
        + (heart_rate * 1.0781 - 75.4991) * (minutes / 8.368)
    )
    if not math.isfinite(calories):
        raise ValueError("The calculation overflowed; use smaller inputs.")
    return calories


def read_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if math.isfinite(value) and value > 0:
            return value
        print("Please enter a positive, finite number.")


def main() -> None:
    print("Arithmetic exercise only: the calorie equation is unverified.")
    age = read_positive_float("Age in years: ")
    weight = read_positive_float("Weight in pounds: ")
    heart_rate = read_positive_float("Average heart rate in beats/minute: ")
    minutes = read_positive_float("Exercise duration in minutes: ")
    try:
        calories = calculate_calories(age, weight, heart_rate, minutes)
    except ValueError as error:
        print(f"Unable to calculate: {error}")
        return
    print(f"Original-equation result: {calories:.2f} calories (unvalidated)")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
