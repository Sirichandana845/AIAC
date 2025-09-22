def area_of_rect(length: int, breadth: int) -> int:
    """
    Calculate the area of a rectangle.

    Args:
        length (int): The length of the rectangle.
        breadth (int): The breadth (width) of the rectangle.

    Returns:
        int: The area of the rectangle.

    Example:
        >>> area_of_rect(10, 20)
        200

    Hint:
        - Area of a rectangle = length * breadth
        - Both length and breadth should be positive integers.
    """
    return length * breadth

if __name__ == "__main__":
    # Example usage
    print("Area of rectangle with length 10 and breadth 20:", area_of_rect(10, 20))