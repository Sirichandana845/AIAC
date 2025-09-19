def convert_date_format(date_str):
    """
    Converts a date string from "YYYY-MM-DD" to "DD-MM-YYYY" format.

    Args:
        date_str (str): Date string in "YYYY-MM-DD" format.

    Returns:
        str: Date string in "DD-MM-YYYY" format.
    """
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format.")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"

# Example usage:
if __name__ == "__main__":
    date = "2023-10-15"
    date1 = "2024-01-20"
    date2 = "2025-12-05"
    date3 = "2026-07-30"
    print(convert_date_format(date))  # Output: 15-10-2023
    print(convert_date_format(date1))  # Output: 20-01-2024
    print(convert_date_format(date2))  # Output: 05-12-2025
    print(convert_date_format(date3))  # Output: 30-07-2026