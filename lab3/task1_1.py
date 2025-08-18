def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        num = int(input("Enter an integer: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

