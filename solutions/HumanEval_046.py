def fib4(n):
    """
    Compute the nth element of the fib4 sequence, where each element is the sum of the last 4 elements.
    The sequence starts with [0, 1, 1, 2] as the first four elements.
    
    Args:
        n (int): The index (0-based) of the element to compute in the fib4 sequence.
    
    Returns:
        int: The nth element of the fib4 sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    fib_sequence = [0, 1, 1, 2]
    if n < 4:
        return fib_sequence[n]
    for i in range(4, n + 1):
        fib_sequence.append(sum(fib_sequence[-4:]))
    return fib_sequence[n]
