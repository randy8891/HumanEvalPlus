def unique_digits(numbers):
    """
    Return a sorted list of integers from the input list that contain no even digits.
    
    Args:
        numbers (list of int): A list of integers to filter.
    
    Returns:
        list of int: A sorted list of integers with no even digits.
    """
    def has_no_even_digits(num):
        return all(int(digit) % 2 != 0 for digit in str(abs(num)))
    
    return sorted(filter(has_no_even_digits, numbers))
