def exchange(list1, list2):
    """
    Determines if elements from list2 can be swapped with elements in list1 
    to make all elements in list1 even.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        bool: True if the swap is possible, False otherwise.
    """
    odd_in_list1 = [x for x in list1 if x % 2 != 0]
    even_in_list2 = [x for x in list2 if x % 2 == 0]
    return len(odd_in_list1) <= len(even_in_list2)
