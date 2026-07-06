def filter_by_substring(strings, substring):
    """
    Filters a list of strings, returning only those that contain the given substring.

    Args:
        strings (list of str): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        list of str: A list of strings from the input that contain the substring.
    """
    return [s for s in strings if substring in s]
