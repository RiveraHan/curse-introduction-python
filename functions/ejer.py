"""The function that validates if is palindrome"""


def is_palindrome(text):
    """is_palindrome is the function that validates whether is palindrome

        Args:
            text(string) text to validate for is_palindrome
    """
    text_clean = text.strip().lower()
    text_reverse = text_clean[::-1]

    for i, char in enumerate(text_clean):
        if char != text_reverse[i]:
            return False
    return True


print(is_palindrome('Abba'))
print(is_palindrome('Hello'))
