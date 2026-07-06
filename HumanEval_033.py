def sort_third(lst):
    """
    Sorts every third element of the input list in ascending order, leaving other elements unchanged.
    
    Parameters:
    lst (list): The input list of elements.
    
    Returns:
    list: A new list with every third element sorted, while other elements remain in their original positions.
    """
    third_elements = lst[2::3]
    third_elements_sorted = sorted(third_elements)
    result = lst[:]
    for i, val in enumerate(third_elements_sorted):
        result[2 + i * 3] = val
    return result
