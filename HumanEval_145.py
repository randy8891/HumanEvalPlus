def order_by_points(numbers):
    """
    Sorts a list of integers based on the sum of their digits. 
    If two numbers have the same digit sum, their original order is preserved.

    Args:
        numbers (list of int): The list of integers to sort.

    Returns:
        list of int: The sorted list of integers.
    """
    return sorted(numbers, key=lambda x: (sum(int(digit) for digit in str(abs(x))), numbers.index(x)))
