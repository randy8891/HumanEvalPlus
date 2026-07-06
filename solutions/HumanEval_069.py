def search(arr):
    """
    Finds the largest integer in the array whose frequency is greater than or equal to its value.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The largest integer satisfying the condition, or -1 if no such integer exists.
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    result = -1
    for num, count in freq.items():
        if count >= num:
            result = max(result, num)

    return result
