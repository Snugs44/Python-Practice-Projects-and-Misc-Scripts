"""Look up a month by its three-letter English abbreviation."""

MONTH_CONVERSIONS = {
    "Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April",
    "May": "May", "Jun": "June", "Jul": "July", "Aug": "August",
    "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December",
}


def get_month_name(abbreviation: str) -> str:
    """Return the full month name, or raise ValueError for an unknown key."""
    key = abbreviation.strip().title()
    if key not in MONTH_CONVERSIONS:
        raise ValueError("Use a three-letter month abbreviation, such as Jan.")
    return MONTH_CONVERSIONS[key]


if __name__ == "__main__":
    print(get_month_name("Jun"))
