def is_happy(s):
    """
    Checks if every 3 consecutive characters in the given string are distinct.

    Args:
        s (str): The input string.

    Returns:
        bool: True if every 3 consecutive characters are distinct, False otherwise.
    """
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) < 3:
            return False
    return True
