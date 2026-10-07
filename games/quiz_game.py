"""A small computer-hardware quiz with case-insensitive answers."""

QUESTIONS = (
    ("What does RAM stand for?", "random access memory"),
    ("What does GPU stand for?", "graphics processing unit"),
    ("Can you download physical RAM? (yes/no)", "no"),
    ("What does CPU stand for?", "central processing unit"),
)


def is_correct_answer(answer: str, expected: str) -> bool:
    """Ignore capitalization and surrounding or repeated whitespace."""
    return " ".join(answer.casefold().split()) == " ".join(expected.casefold().split())


def main() -> None:
    playing = input("Welcome to the hardware quiz! Play? (yes/no): ").strip().lower()
    if playing not in {"yes", "y"}:
        print("Okay, goodbye!")
        return
    score = 0
    for question, expected in QUESTIONS:
        answer = input(f"{question} ")
        if is_correct_answer(answer, expected):
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The answer is: {expected}.")
    print(f"Score: {score}/{len(QUESTIONS)} ({score / len(QUESTIONS):.0%})")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
