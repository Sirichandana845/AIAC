def is_valid_email(email):
    if email.count('@') != 1:
        return False
    if '.' not in email:
        return False
    if email[0] in {'@', '.'} or email[-1] in {'@', '.'}:
        return False

    local, domain = email.split('@')

    if not local or not domain:
        return False

    if local[0] == '.' or local[-1] == '.':
        return False

    if domain[0] == '.' or domain[-1] == '.':
        return False

    if '.' not in domain:
        return False

    return True

import unittest

class TestEmailValidator(unittest.TestCase):
    def check_and_print(self, email, expected):
        result = is_valid_email(email)
        print(f"is_valid_email('{email}') = {result}")
        self.assertEqual(result, expected)

    def test_valid_emails(self):
        self.check_and_print("user@example.com", True)
        self.check_and_print("john.doe@domain.co.uk", True)
        self.check_and_print("a_b.c@d.e", True)

    def test_missing_at(self):
        self.check_and_print("userexample.com", False)
        self.check_and_print("user.example.com", False)

    def test_missing_dot(self):
        self.check_and_print("user@examplecom", False)
        self.check_and_print("user@domain", False)

    def test_multiple_at(self):
        self.check_and_print("user@@example.com", False)
        self.check_and_print("user@ex@ample.com", False)

    def test_starts_or_ends_with_special(self):
        self.check_and_print("@user@example.com", False)
        self.check_and_print("user@example.com.", False)
        self.check_and_print(".user@example.com", False)
        self.check_and_print("user.@example.com", False)
        self.check_and_print("user@example.com@", False)
        self.check_and_print("user@.example.com", False)
        self.check_and_print("user@domain.com.", False)

    def test_at_at_start_or_end(self):
        self.check_and_print("@example.com", False)
        self.check_and_print("example.com@", False)

    def test_dot_at_start_or_end(self):
        self.check_and_print(".example@domain.com", False)
        self.check_and_print("example@domain.com.", False)
        self.check_and_print("example@.domain.com", False)
        self.check_and_print("example.@domain.com", False)

if __name__ == "__main__":
    unittest.main()
