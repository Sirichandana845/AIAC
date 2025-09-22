def grade(score):
    """
    Returns the letter grade for a given score.

    Args:
        score (int or float): The numeric score to grade.

    Returns:
        str: The letter grade ("A", "B", "C", "D", or "F").

    Example:
        >>> grade(95)
        'A'
        >>> grade(82)
        'B'
        >>> grade(75)
        'C'
        >>> grade(65)
        'D'
        >>> grade(50)
        'F'

    Hints:
        - Use simple if-elif-else statements to avoid deep nesting.
        - Check the highest grade first and proceed in descending order.
        - You can return as soon as a condition is met.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(grade(95))
print(grade(82))
print(grade(75))
print(grade(65))
print(grade(50))