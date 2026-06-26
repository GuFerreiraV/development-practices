import unittest
from ex1.palindromo import is_palindromo

class TestPalindromo(unittest.TestCase):
    def test_palavra_palindromo(self):
        self.assertTrue(is_palindromo("Radar"))
        self.assertFalse(is_palindromo("python"))

if __name__ == "__main__":
    unittest.main()
