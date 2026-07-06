def multiply(a, b):
    """
    Multiplies the unit digits of two integers and returns the result.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The product of the unit digits of the two integers.
    """
    return (a % 10) * (b % 10)
