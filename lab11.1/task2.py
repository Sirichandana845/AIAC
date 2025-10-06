def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"IO error occurred: {e}")
# example_usage:
print(read_file("existing_file.txt"))  # Should print the file contents
print(read_file("non_existing_file.txt"))  # Should print an error message