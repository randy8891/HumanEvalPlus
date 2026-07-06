def factorize(n):
    """
    Return the prime factorization of an integer as a list of prime factors.
    
    Parameters:
    n (int): The integer to factorize. Must be greater than 1.
    
    Returns:
    list: A list of prime factors of the integer in ascending order.
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
