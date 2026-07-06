def double_the_difference(numbers):
    """
    Takes a list of numbers and returns double the sum of the squares of odd numbers,
    ignoring negative numbers and non-integer values.
    
    Parameters:
    numbers (list): A list of numbers.
    
    Returns:
    int: Double the sum of the squares of odd numbers.
    """
    return 2 * sum(x**2 for x in numbers if isinstance(x, int) and x > 0 and x % 2 != 0)
