def all_prefixes(s):
    """
    Return a list of all prefixes of a string, shortest first.

    Args:
        s (str): The input string.

    Returns:
        list: A list of prefixes of the string in ascending order of length.
    """
    return [s[:i] for i in range(1, len(s) + 1)]
