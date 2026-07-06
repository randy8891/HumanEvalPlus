def filter_integers(mixed_list):
    """
    Filters and returns only the integers from a mixed list.

    Args:
        mixed_list (list): A list containing elements of various data types.

    Returns:
        list: A list containing only the integer elements from the input list.
    """
    return [item for item in mixed_list if isinstance(item, int)]
