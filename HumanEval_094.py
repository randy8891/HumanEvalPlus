def skjkasdkd(numbers):
    """
    Finds the largest prime number in a list and returns the sum of its digits.
    If no prime number exists in the list, returns 0.
    
    :param numbers: List of integers
    :return: Sum of the digits of the largest prime number, or 0 if no prime exists
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(num)]
    if not primes:
        return 0
    largest_prime = max(primes)
    return sum(int(digit) for digit in str(largest_prime))
