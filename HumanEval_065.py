def circular_shift(n, shift):
    """
    Performs a circular shift on the digits of an integer n. If the absolute value of the shift
    is greater than the number of digits in n, the digits are reversed instead.

    Args:
        n (int): The integer whose digits are to be circularly shifted.
        shift (int): The number of positions to shift. Positive for right shift, negative for left shift.

    Returns:
        int: The resulting integer after the circular shift or reversal.
    """
    n_str = str(abs(n))
    length = len(n_str)
    shift = shift % length if abs(shift) <= length else 0

    if shift == 0:
        result = int(n_str[::-1])
    else:
        shift = shift if shift >= 0 else length + shift
        result = int(n_str[-shift:] + n_str[:-shift])

    return result if n >= 0 else -result
