def welcome_student(student_name: str) -> None:
    """
    Print a welcome message for a given student.
    Args:
        student_name (str): The name of the student to welcome.

    Returns:
        None

    Example:
        >>> welcome_student("Alice")
        Welcome Alice

    Hint:
        - Use this function to avoid repeating print statements for each student.
        - Pass the student's name as an argument to the function.
    """
    print("Welcome", student_name)

students = ["Alice", "Bob", "Charlie"]
for student in students:
    welcome_student(student)
