def is_equal_to_sum_even(n):
    """
    Check if the given integer n can be written as a sum of exactly 4 even positive numbers.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n can be expressed as a sum of 4 even positive numbers, False otherwise.
    """
    return n >= 8 and n % 2 == 0
