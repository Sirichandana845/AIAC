def compute_squares(nums):
    """
    Compute the squares of a list of numbers efficiently.

    Args:
        nums (list of int): List of integers to square.

    Returns:
        list of int: List containing the squares of the input numbers.

    Example:
        >>> compute_squares([1, 2, 3])
        [1, 4, 9]

    Hints:
        - Use list comprehensions for faster execution and concise code.
        - Avoid appending in a loop when you can use a single expression.
        - For very large ranges, consider using generators if you don't need all results at once.
    """
    return [n ** 2 for n in nums]

if __name__ == "__main__":
    # Find squares of numbers efficiently
    nums = list(range(1, 1000000))
    squares = compute_squares(nums)
    print(len(squares))
