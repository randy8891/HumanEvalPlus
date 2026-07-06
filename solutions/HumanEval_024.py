def largest_divisor(n):
    """
    Find the largest number less than n that divides n evenly.

    Parameters:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n less than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
