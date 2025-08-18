def register_user(users_db):
    """
    Registers a new user by asking for a username and password.
    Adds the user to the users_db dictionary.
    """
    username = input("Enter a new username: ").strip()
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return False
    password = input("Enter a new password: ").strip()
    users_db[username] = password
    print("Registration successful!")
    return True

def login_user(users_db):
    """
    Logs in a user by verifying the username and password.
    """
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Example usage:
if __name__ == "__main__":
    users = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
