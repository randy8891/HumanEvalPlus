def total_match(list1, list2):
    """
    Return the list with fewer total characters. If both lists have the same total characters,
    return the first list.
    
    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.
    
    Returns:
        list: The list with fewer total characters.
    """
    total1 = sum(len(item) for item in list1)
    total2 = sum(len(item) for item in list2)
    return list1 if total1 <= total2 else list2
