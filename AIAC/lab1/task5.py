def count_lines_in_file(filename):
    """
    Reads the specified file and returns the number of lines.

    Parameters:
    filename (str): The path to the file.

    Returns:
    int: Number of lines in the file.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
file_path = 'EXAMPLE.txt'  # Replace with your actual file path
line_count = count_lines_in_file(file_path)
print(f"The file '{file_path}' has {line_count} lines.")
