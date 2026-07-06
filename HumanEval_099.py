def closest_integer(float_str):
    """
    Rounds a float string to the nearest integer, rounding away from zero for .5.

    Args:
        float_str (str): A string representation of a floating-point number.

    Returns:
        int: The rounded integer.
    """
    num = float(float_str)
    if num > 0:
        return int(num + 0.5)
    else:
        return int(num - 0.5)
