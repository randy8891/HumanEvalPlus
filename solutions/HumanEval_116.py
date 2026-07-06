def sort_array(arr):
    """
    Sorts an array first by the number of 1s in the binary representation of each number,
    and then by the numerical value in case of ties.

    Args:
    arr (list): A list of non-negative integers.

    Returns:
    list: A sorted list based on the described criteria.
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
