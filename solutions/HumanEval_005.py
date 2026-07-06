def intersperse(lst, delimiter):
    """
    Inserts a delimiter between every two consecutive elements of a list.

    Args:
        lst (list): The list of elements.
        delimiter (any): The delimiter to insert between elements.

    Returns:
        list: A new list with the delimiter interspersed between elements.
    """
    return [elem for i, elem in enumerate(lst) for _ in (0, 1) if i < len(lst) - 1 or _ == 0] + [delimiter] * (len(lst) - 1)
