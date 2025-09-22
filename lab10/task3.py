def calculate_percentage(amount: float, percent: float) -> float:
    """
    Calculate the percentage of a given amount.

    Args:
        amount (float): The base amount.
        percent (float): The percentage to calculate.

    Returns:
        float: The calculated percentage value.

    Example:
        >>> calculate_percentage(200, 15)
        30.0
    """
    return amount * percent / 100

amount: float = 200
percent: float = 15
print(calculate_percentage(amount, percent))
