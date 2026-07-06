def x_or_y(n, x, y):
    """
    Returns x if n is a prime number, otherwise returns y.

    Args:
        n (int): The number to check for primality.
        x: The value to return if n is prime.
        y: The value to return if n is not prime.

    Returns:
        x if n is prime, otherwise y.
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x
