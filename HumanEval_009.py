def rolling_max(sequence):
    """
    Returns the running maximum of a sequence of integers.

    Args:
        sequence (list): A list of integers.

    Returns:
        list: A list containing the running maximum at each position.
    """
    if not sequence:
        return []
    
    max_so_far = sequence[0]
    result = [max_so_far]
    
    for num in sequence[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result
