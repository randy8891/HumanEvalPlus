def monotonic(lst):
    """
    Check if a list is monotonically increasing or decreasing.

    Args:
        lst (list): A list of comparable elements.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
