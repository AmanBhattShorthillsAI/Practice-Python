import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_basic(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("No Lemon, no melon"))
        
    def test_non_palindrome_basic(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
    
    def test_palindrome_edge_cases(self):
        self.assertTrue(is_palindrome("a"))  # Single character
        self.assertTrue(is_palindrome("A"))  # Single character, case insensitive
        self.assertTrue(is_palindrome("12321"))  # Numeric palindrome
        self.assertTrue(is_palindrome("1a2b3b2a1"))  # Alphanumeric palindrome
        
    def test_non_palindrome_edge_cases(self):
        self.assertFalse(is_palindrome(""))  # Empty string
        self.assertFalse(is_palindrome("  "))  # Whitespace only
        self.assertFalse(is_palindrome("1a2b3b2c1"))  # Alphanumeric, not a palindrome
        self.assertFalse(is_palindrome("!@#"))  # Special characters only
        
    def test_special_characters(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("Madam, in Eden, I’m Adam."))
        
if __name__ == '__main__':
    unittest.main()