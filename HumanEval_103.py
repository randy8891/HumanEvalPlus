def rounded_avg(n, m):
    """
    Calculate the average of integers in the range [n, m], round it to the nearest integer,
    and return the result as a binary string.

    Args:
    n (int): The starting integer of the range.
    m (int): The ending integer of the range.

    Returns:
    str: The binary string representation of the rounded average.
    """
    avg = round((n + m) / 2)
    return bin(avg)[2:]
