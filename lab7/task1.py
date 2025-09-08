import hashlib
import getpass
import os
import json

USERS_FILE = "users.json"

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + pwd_hash.hex()

def verify_password(stored_hash, password):
    salt = bytes.fromhex(stored_hash[:32])
    stored_pwd_hash = stored_hash[32:]
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return pwd_hash.hex() == stored_pwd_hash

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def register():
    users = load_users()
    username = input("Choose a username: ").strip()
    if username in users:
        print("Username already exists.")
        return
    password = getpass.getpass("Choose a password: ")
    password_confirm = getpass.getpass("Confirm password: ")
    if password != password_confirm:
        print("Passwords do not match.")
        return
    hashed = hash_password(password)
    users[username] = hashed
    save_users(users)
    print("Registration successful.")

def login():
    users = load_users()
    username = input("Username: ").strip()
    if username not in users:
        print("User not found.")
        return
    password = getpass.getpass("Password: ")
    if verify_password(users[username], password):
        print("Login successful!")
    else:
        print("Incorrect password.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
