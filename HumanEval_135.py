def can_arrange(arr):
    """
    Finds the largest index where an element in the array is smaller than the one before it.
    
    Args:
    arr (list): A list of comparable elements.
    
    Returns:
    int: The largest index where arr[i] < arr[i-1], or -1 if no such index exists.
    """
    index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            index = i
    return index
