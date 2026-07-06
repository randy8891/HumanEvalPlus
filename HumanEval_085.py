def add_elements(lst, k):
    """
    Sums elements with at most 2 digits from the first k elements of the list.

    Args:
        lst (list): A list of integers.
        k (int): The number of elements from the start of the list to consider.

    Returns:
        int: The sum of elements with at most 2 digits from the first k elements.
    """
    return sum(x for x in lst[:k] if -99 <= x <= 99)
