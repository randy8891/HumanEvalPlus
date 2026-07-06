def is_simple_power(x, n):
    """
    Determines if n is a simple power of x, meaning there exists an integer k >= 0 such that x^k = n.

    Args:
        x (int): The base number, must be greater than 1.
        n (int): The number to check, must be greater than 0.

    Returns:
        bool: True if n is a simple power of x, False otherwise.
    """
    if x <= 1 or n <= 0:
        return False
    while n > 1:
        if n % x != 0:
            return False
        n //= x
    return n == 1
