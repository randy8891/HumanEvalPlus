def greatest_common_divisor(a, b):
    """
    Calculate and return the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return abs(a)
