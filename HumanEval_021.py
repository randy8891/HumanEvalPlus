def rescale_to_unit(numbers):
    """
    Rescales a list of numbers to the unit interval [0, 1].

    Parameters:
        numbers (list of float): A list of numerical values to be rescaled.

    Returns:
        list of float: A list of numbers rescaled to the range [0, 1].
    """
    if not numbers:
        return []
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        return [0.5] * len(numbers)
    
    return [(x - min_val) / (max_val - min_val) for x in numbers]
