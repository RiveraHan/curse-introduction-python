def is_palindrome(text):
    text_clean = text.strip().lower()
    text_reverse = text_clean[::-1]

    for i, t in enumerate(text_clean):
        if t != text_reverse[i]:
            return False
    return True


print(is_palindrome('Abba'))
print(is_palindrome('Hello'))
