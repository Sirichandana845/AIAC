from datetime import datetime
import platform

def convert_date_format(date_str):
    """
    Converts a date from 'YYYY-MM-DD' to 'Month Day, Year' format.
    Example: '2024-06-01' -> 'June 1, 2024'
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Handle platform-specific formatting for day without leading zero
        if platform.system() == "Windows":
            return date_obj.strftime("%B %#d, %Y")  # Windows uses %#d
        else:
            return date_obj.strftime("%B %-d, %Y")  # Unix/Linux/Mac uses %-d
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

# Test cases
test_dates = [
    "2024-06-01",
    "1999-12-31",
    "2000-01-01",
    "2023-02-28",
    "2020-02-29",  # Leap year
    "2021-11-09",
    "1980-07-15",
    "2010-10-10",
    "2022-03-05",
    "2024-12-25"
]

# Run tests
for date_str in test_dates:
    try:
        result = convert_date_format(date_str)
        print(f"Input: {date_str} -> Output: {result}")
    except Exception as e:
        print(f"Input: {date_str} -> Error: {e}")