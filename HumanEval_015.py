def string_sequence(n):
    """
    Returns a string of space-delimited numbers from 0 to n.

    Args:
    n (int): The upper limit of the sequence (inclusive).

    Returns:
    str: A space-delimited string of numbers from 0 to n.
    """
    return ' '.join(str(i) for i in range(n + 1))
