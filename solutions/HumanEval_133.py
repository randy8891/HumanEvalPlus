def sum_squares(numbers):
    """
    Calculates the sum of the squares of the ceiling of each float in a list.

    Args:
        numbers (list): A list of float or integer numbers.

    Returns:
        int: The sum of the squares of the ceiling of each number.
    """
    return sum((int(num) + (1 if num % 1 != 0 else 0))**2 for num in numbers)
