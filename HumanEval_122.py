def add_elements_v2(arr):
    """
    Adds the elements at even positions (0-based index) of the given array.

    Args:
        arr (list): A list of numbers.

    Returns:
        int or float: The sum of elements at even positions.
    """
    return sum(arr[i] for i in range(0, len(arr), 2))
