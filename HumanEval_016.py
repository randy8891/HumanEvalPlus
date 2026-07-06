def count_distinct_characters(s):
    """
    Counts the number of distinct characters in a string, case-insensitively.

    Args:
        s (str): The input string.

    Returns:
        int: The count of distinct characters.
    """
    return len(set(s.lower()))
