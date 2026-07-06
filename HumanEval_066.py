def digitsum(s):
    """
    Returns the sum of ASCII values of uppercase characters in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII values of uppercase characters.
    """
    return sum(ord(char) for char in s if char.isupper())
