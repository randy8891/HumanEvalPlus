def intersection(interval1, interval2):
    """
    Determines if the intersection of two intervals has a prime length.
    
    Args:
        interval1 (tuple): A tuple (a, b) representing the first interval [a, b].
        interval2 (tuple): A tuple (c, d) representing the second interval [c, d].
    
    Returns:
        str: 'YES' if the intersection has a prime length, otherwise 'NO'.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    length = max(0, end - start + 1)
    
    return 'YES' if is_prime(length) else 'NO'
