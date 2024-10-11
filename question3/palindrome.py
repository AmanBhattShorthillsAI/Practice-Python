import re  # Import the regular expression module

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string is empty
    if not cleaned_s:
        return False  # Empty string or only whitespace is not a palindrome
    
    left, right = 0, len(cleaned_s) - 1
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False  # Not a palindrome
        left += 1
        right -= 1
    
    return True  # It is a palindrome

# # Example usage:
# print(is_palindrome("A man a plan a canal Panama"))  # Output: True
# print(is_palindrome("No lemon, no melon"))            # Output: True
# print(is_palindrome("hello"))                          # Output: False
# print(is_palindrome("  "))                             # Output: False
# print(is_palindrome("12321"))                          # Output: True
# print(is_palindrome(""))                               # Output: False