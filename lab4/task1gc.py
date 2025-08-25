def is_valid_indian_mobile(number):
    """
    Validates if the input string is a valid Indian mobile number.
    - Must be exactly 10 digits.
    - Must start with 6, 7, 8, or 9.
    """
    if len(number) == 10 and number.isdigit() and number[0] in '6789':
        return True
    return False

# Example usage:
mobile = input("Enter mobile number: ")
if is_valid_indian_mobile(mobile):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")