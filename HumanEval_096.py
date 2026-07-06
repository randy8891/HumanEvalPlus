def count_up_to(n):
    """
    Return a list of all prime numbers less than n.
    
    Args:
    n (int): The upper limit (exclusive) to find primes.
    
    Returns:
    list: A list of prime numbers less than n.
    """
    if n <= 2:
        return []
    
    primes = []
    for num in range(2, n):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
