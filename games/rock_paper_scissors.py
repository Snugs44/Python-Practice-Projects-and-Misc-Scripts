"""Play rock-paper-scissors in the terminal."""

import random

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'loss', or 'tie' for a valid pair of choices."""
    player = player.strip().lower()
    computer = computer.strip().lower()
    if player not in CHOICES or computer not in CHOICES:
        raise ValueError("Choices must be rock, paper, or scissors.")
    if player == computer:
        return "tie"
    return "win" if BEATS[player] == computer else "loss"


def main() -> None:
    scores = {"win": 0, "loss": 0, "tie": 0}
    messages = {"win": "You won!", "loss": "The computer won.", "tie": "It's a tie!"}
    try:
        while True:
            player = input("Rock, paper, scissors, or q to quit: ").strip().lower()
            if player in {"q", "quit"}:
                break
            if player not in CHOICES:
                print("Please choose rock, paper, or scissors.")
                continue
            computer = random.choice(CHOICES)
            outcome = determine_winner(player, computer)
            scores[outcome] += 1
            print(f"The computer picked {computer}. {messages[outcome]}")
    except (EOFError, KeyboardInterrupt):
        print()
    print(f"Wins: {scores['win']} | Losses: {scores['loss']} | Ties: {scores['tie']}")
    print("Goodbye!")


if __name__ == "__main__":
    main()
