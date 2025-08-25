def is_valid_indian_mobile(number):
    """
    Validates if the input is a valid Indian mobile number:
    - Exactly 10 digits
    - Starts with 6, 7, 8, or 9
    """
    num_str = str(number).strip()
    return len(num_str) == 10 and num_str.isdigit() and num_str[0] in {'6', '7', '8', '9'}

mobile = input("Enter mobile number: ")
if is_valid_indian_mobile(mobile):
    print(f"{mobile} is a valid Indian mobile number")
else:
    print(f"{mobile} is an invalid Indian mobile number")

