def is_palindrome(s):
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same backward as forward,
    ignoring case and non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
