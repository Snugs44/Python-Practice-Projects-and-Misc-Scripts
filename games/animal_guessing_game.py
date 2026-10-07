"""A five-guess animal guessing game."""

SECRET_WORD = "monkey"
GUESS_LIMIT = 5


def main() -> None:
    print("Let's play guess the animal! Hint: it really likes bananas.")
    for attempt in range(1, GUESS_LIMIT + 1):
        guess = input(f"Guess {attempt}/{GUESS_LIMIT} (q to quit): ").strip().lower()
        if guess in {"q", "quit"}:
            print("Goodbye!")
            return
        if guess == SECRET_WORD:
            print("You got it!")
            return
        print("Not quite.")
    print(f"Out of guesses! The animal was {SECRET_WORD}.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
