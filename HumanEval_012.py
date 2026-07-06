def longest(strings):
    """
    Returns the longest string from a list of strings. If the list is empty, returns None.

    Args:
        strings (list): A list of strings.

    Returns:
        str or None: The longest string in the list, or None if the list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)
