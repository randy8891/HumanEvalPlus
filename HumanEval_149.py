def sorted_list_sum(strings):
    """
    Removes odd-length strings from the input list, sorts the remaining strings
    first by length and then alphabetically, and returns the sorted list.

    Args:
        strings (list of str): A list of strings to process.

    Returns:
        list of str: A sorted list of even-length strings.
    """
    return sorted([s for s in strings if len(s) % 2 == 0], key=lambda x: (len(x), x))
