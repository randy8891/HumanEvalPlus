def iscube(n):
    """
    Check if the given integer n is a perfect cube.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is a perfect cube, False otherwise.
    """
    if n < 0:
        return round(abs(n) ** (1/3)) ** 3 == abs(n)
    return round(n ** (1/3)) ** 3 == n
