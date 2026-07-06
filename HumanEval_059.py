def largest_prime_factor(n):
    """
    Return the largest prime factor of the given integer n.
    
    Parameters:
    n (int): The number to find the largest prime factor of.
    
    Returns:
    int: The largest prime factor of n.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n
