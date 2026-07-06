def prime_fib(n):
    """
    Returns the nth Fibonacci number that is also prime.

    Args:
        n (int): The position of the prime Fibonacci number to return.

    Returns:
        int: The nth Fibonacci number that is also prime.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib_gen = fibonacci()
    prime_fibs = []
    while len(prime_fibs) < n:
        fib_num = next(fib_gen)
        if is_prime(fib_num):
            prime_fibs.append(fib_num)
    return prime_fibs[-1]
