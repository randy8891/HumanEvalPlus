def any_int(a: float, b: float, c: float) -> bool:
    """
    Check if any one of the three floats is the sum of the other two.

    Args:
        a (float): The first float.
        b (float): The second float.
        c (float): The third float.

    Returns:
        bool: True if any one of the floats is the sum of the other two, False otherwise.
    """
    return a == b + c or b == a + c or c == a + b
