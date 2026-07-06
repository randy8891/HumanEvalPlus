def max_element(lst):
    """
    Returns the maximum element in a list.
    
    Parameters:
    lst (list): A list of comparable elements.
    
    Returns:
    The maximum element in the list, or None if the list is empty.
    """
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val
