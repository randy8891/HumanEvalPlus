def prime_length(s):
    """
    Return True if the length of the input string is a prime number, otherwise False.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return is_prime(len(s))
