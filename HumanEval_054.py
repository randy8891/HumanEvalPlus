def same_chars(str1, str2):
    """
    Check if two strings have the same character set.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if both strings have the same character set, False otherwise.
    """
    return set(str1) == set(str2)
