def filter_by_prefix(strings, prefix):
    """
    Filters a list of strings, returning only those that start with the given prefix.

    Args:
        strings (list of str): The list of strings to filter.
        prefix (str): The prefix to filter strings by.

    Returns:
        list of str: A list of strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)]
