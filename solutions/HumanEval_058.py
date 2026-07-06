def common(list1, list2):
    """
    Returns a sorted list of unique common elements between two input lists.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.
    """
    return sorted(set(list1) & set(list2))
