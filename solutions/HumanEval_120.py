def maximum(lst, k):
    """
    Return the k largest elements of a list sorted in ascending order.

    Parameters:
    lst (list): The input list of elements.
    k (int): The number of largest elements to return.

    Returns:
    list: A list of the k largest elements sorted in ascending order.
    """
    return sorted(lst)[-k:]
