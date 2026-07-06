def is_sorted_v2(lst):
    """
    Check if a list is sorted in ascending order and contains no repeated triplets.
    
    A triplet is defined as three consecutive identical elements in the list.
    
    Args:
        lst (list): The list to check.
    
    Returns:
        bool: True if the list is sorted in ascending order and has no repeated triplets, False otherwise.
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    for i in range(len(lst) - 2):
        if lst[i] == lst[i + 1] == lst[i + 2]:
            return False
    return True
