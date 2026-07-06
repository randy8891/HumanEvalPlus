def strange_sort_list(lst):
    """
    Sorts a list by alternating between the smallest and largest elements.
    
    Args:
        lst (list): A list of numbers to be sorted.
        
    Returns:
        list: A list sorted by alternating min and max values.
    """
    sorted_lst = sorted(lst)
    result = []
    while sorted_lst:
        if sorted_lst:
            result.append(sorted_lst.pop(0))  # Add the smallest element
        if sorted_lst:
            result.append(sorted_lst.pop(-1))  # Add the largest element
    return result
