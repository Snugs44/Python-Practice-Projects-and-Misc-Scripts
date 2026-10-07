"""Demonstrate a case-sensitive substring membership test."""


def contains(big_string: str, little_string: str) -> bool:
    """Return whether little_string occurs in big_string (empty strings match)."""
    return little_string in big_string


if __name__ == "__main__":
    print(contains("watermelon", "melon"))
