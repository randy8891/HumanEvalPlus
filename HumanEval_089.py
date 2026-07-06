def is_sorted(lst):
    """
    Check if a list is sorted in non-decreasing order with no more than one duplicate for any element.
    
    Args:
        lst (list): The list to check.
        
    Returns:
        bool: True if the list is sorted and meets the duplicate condition, False otherwise.
    """
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
        if i > 1 and lst[i] == lst[i - 1] == lst[i - 2]:
            return False
    return True
