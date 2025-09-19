import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    main()
#test
def test_is_valid_email():
    assert is_valid_email("user@example.com")
    assert not is_valid_email("user@example")
    assert not is_valid_email("user@.com")
    assert not is_valid_email("@example.com")
    assert not is_valid_email("user@com")