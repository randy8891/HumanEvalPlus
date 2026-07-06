def is_multiply_prime(n):
    """
    Check if the given number n is the product of exactly 3 prime numbers.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is the product of exactly 3 prime numbers, False otherwise.
    """
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def prime_factors_count(num):
        count = 0
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                if is_prime(i):
                    count += 1
                num //= i
        if num > 1 and is_prime(num):
            count += 1
        return count

    return prime_factors_count(n) == 3
