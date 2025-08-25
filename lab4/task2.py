def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Returns an error message if n is negative or not an integer.
    By convention, 0! = 0 as per the example.
    """
    if not isinstance(n, int):
        return "Input must be an integer."
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a positive integer: "))
    res = factorial(num)
    if isinstance(res, str):
        print(res)
    else:
        print(f"{num}! = {res}")
except ValueError:
    print("Invalid input. Please enter an integer.")
