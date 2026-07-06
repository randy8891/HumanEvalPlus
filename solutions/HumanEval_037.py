def sort_even(lst):
    """
    Sorts the elements at even indices of the input list in ascending order,
    while leaving the elements at odd indices unchanged.

    Args:
        lst (list): The input list of elements.

    Returns:
        list: A new list with even-indexed elements sorted, odd-indexed elements unchanged.
    """
    even_indices = sorted((lst[i] for i in range(0, len(lst), 2)))
    result = lst[:]
    even_index = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            result[i] = even_indices[even_index]
            even_index += 1
    return result
