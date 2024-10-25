import unittest

from password_checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_digit,
    check_special_char,
    evaluate_password_strength,
    generate_feedback,
)


class TestPasswordChecker(unittest.TestCase):

    def test_check_length(self):
        self.assertTrue(check_length("abcdefgh"))
        self.assertFalse(check_length("abc"))

    def test_check_uppercase(self):
        self.assertTrue(check_uppercase("Abc"))
        self.assertFalse(check_uppercase("abc"))

    def test_check_lowercase(self):
        self.assertTrue(check_lowercase("aBc"))
        self.assertFalse(check_lowercase("ABC"))

    def test_check_digit(self):
        self.assertTrue(check_digit("abc123"))
        self.assertFalse(check_digit("abcdef"))

    def test_check_special_char(self):
        self.assertTrue(check_special_char("abc!"))
        self.assertFalse(check_special_char("abcdef"))

    def test_evaluate_password_strength(self):
        self.assertEqual(evaluate_password_strength("Abc123!@"), (5, "Very Strong"))
        self.assertEqual(evaluate_password_strength("Abc123"), (3, "Moderate"))
        self.assertEqual(evaluate_password_strength("abc"), (1, "Very Weak"))

    def test_generate_feedback(self):
        self.assertEqual(
            generate_feedback("abc"),
            "Increase the length to at least 8 characters. Add at least one uppercase letter. Include at least one number. Use at least one special character (e.g., !@#$%^&*()).",
        )
        self.assertEqual(generate_feedback("Abc123!@"), "No improvements needed.")


if __name__ == "__main__":
    unittest.main()
