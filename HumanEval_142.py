def sum_squares_v2(numbers):
    """
    Takes a list of integers and returns the sum of squares of numbers divisible by 3,
    the sum of cubes of numbers divisible by 4, and the sum of values not divisible by 3 or 4.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing three integers:
               (sum of squares of numbers divisible by 3,
                sum of cubes of numbers divisible by 4,
                sum of values not divisible by 3 or 4).
    """
    sum_squares = sum(n**2 for n in numbers if n % 3 == 0)
    sum_cubes = sum(n**3 for n in numbers if n % 4 == 0)
    sum_others = sum(n for n in numbers if n % 3 != 0 and n % 4 != 0)
    return sum_squares, sum_cubes, sum_others
