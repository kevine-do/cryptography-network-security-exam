import unittest
from src.security_toolkit import calculate_sha256, check_password_strength


class TestSecurityToolkit(unittest.TestCase):

    def test_sha256(self):
        result = calculate_sha256("sample-data")
        self.assertEqual(
            result,
            "c45df724cba87ac84892bf3eeb910393d69d163e9ad96cac2e2074487eaa907b"
        )

    def test_password_strength(self):
        self.assertEqual(check_password_strength("abc"), "Weak")
        self.assertEqual(check_password_strength("Example123!"), "Strong")


if __name__ == "__main__":
    unittest.main()