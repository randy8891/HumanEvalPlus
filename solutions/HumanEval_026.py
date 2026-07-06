def remove_duplicates(lst):
    """
    Removes all elements that appear more than once in the input list.
    
    Args:
        lst (list): The input list of elements.
        
    Returns:
        list: A new list containing only the elements that appear exactly once in the input list.
    """
    return [item for item in lst if lst.count(item) == 1]
