def truncate_number(num):
    """
    Given a positive float, return the decimal part of the number.

    Args:
        num (float): A positive floating-point number.

    Returns:
        float: The decimal part of the input number.
    """
    return num - int(num)
