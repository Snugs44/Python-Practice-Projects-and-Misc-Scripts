"""Demonstrate exponentiation using repeated multiplication."""


def raise_to_power(base_num: int | float, power_num: int) -> int | float:
    """Return base_num raised to a nonnegative integer power."""
    if type(power_num) is not int or power_num < 0:
        raise ValueError("The exponent must be a nonnegative integer.")
    result = 1
    for _ in range(power_num):
        result *= base_num
    return result


if __name__ == "__main__":
    print(raise_to_power(5, 3))
