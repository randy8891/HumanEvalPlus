def get_odd_collatz_v2(n):
    """
    Returns the number of even elements in the Collatz sequence starting from n.
    
    The Collatz sequence is defined as:
    - If n is even, the next number is n / 2.
    - If n is odd, the next number is 3 * n + 1.
    - The sequence ends when it reaches 1.
    
    Parameters:
    n (int): The starting number of the Collatz sequence (must be a positive integer).
    
    Returns:
    int: The count of even numbers in the Collatz sequence.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    even_count = 0
    while n != 1:
        if n % 2 == 0:
            even_count += 1
            n //= 2
        else:
            n = 3 * n + 1
    return even_count
