def greet_user(name, gender):
    """
    Greets the user with a gender-inclusive message.

    Args:
        name (str): The user's name.
        gender (str): The user's gender ("Male", "Female", or any other value for gender-neutral).

    Returns:
        str: A greeting message.
    """
    gender = gender.strip().lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = "Mx."
    return f"Hello, {title} {name}!"

# Example usage:
print(greet_user("Alex", "Male"))      # Output: Hello, Mr. Alex!
print(greet_user("Sam", "Female"))     # Output: Hello, Ms. Sam!
print(greet_user("Taylor", "Nonbinary")) # Output: Hello, Mx. Taylor!
