"""Build a username from name slices; no uniqueness guarantee is implied."""


def username_generator(first_name: str, last_name: str) -> str:
    """Use 3 + 4 characters, or full names when either name is too short."""
    first_name = first_name.strip()
    last_name = last_name.strip()
    if not first_name or not last_name:
        raise ValueError("Both names must contain non-whitespace characters.")
    if len(first_name) < 3 or len(last_name) < 4:
        return first_name + last_name
    return first_name[:3] + last_name[:4]


if __name__ == "__main__":
    print(username_generator("Abe", "Simpson"))
