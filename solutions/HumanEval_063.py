def fibfib(n):
    """
    Compute the nth element of the FibFib sequence.

    The FibFib sequence is defined recursively:
    - FibFib(0) = 0
    - FibFib(1) = 1
    - FibFib(n) = Fib(FibFib(n-1)) where Fib is the Fibonacci sequence.

    Parameters:
    n (int): The index of the FibFib sequence to compute.

    Returns:
    int: The nth element of the FibFib sequence.
    """
    def fibonacci(k):
        if k <= 1:
            return k
        a, b = 0, 1
        for _ in range(2, k + 1):
            a, b = b, a + b
        return b

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(fibfib(n - 1))
