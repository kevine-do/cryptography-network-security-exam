import unittest
from src.security_toolkit import encrypt_file


class TestErrorHandling(unittest.TestCase):

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            encrypt_file("missing_file.txt", "results/test.bin")


if __name__ == "__main__":
    unittest.main()