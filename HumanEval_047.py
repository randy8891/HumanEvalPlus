def median(numbers):
    """
    Calculate and return the median of a list of numbers.
    
    Parameters:
    numbers (list): A list of numerical values.
    
    Returns:
    float: The median value of the list.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
