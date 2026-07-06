def get_odd_collatz(n):
    """
    Generate the sorted odd numbers in the Collatz sequence for a given n.
    
    The Collatz sequence is defined as:
    - Start with a positive integer n.
    - If n is even, divide it by 2.
    - If n is odd, multiply it by 3 and add 1.
    - Repeat the process until n becomes 1.
    
    Parameters:
    n (int): The starting positive integer for the Collatz sequence.
    
    Returns:
    list: A sorted list of unique odd numbers in the Collatz sequence.
    """
    if n <= 0:
        return []
    
    odd_numbers = set()
    while n != 1:
        if n % 2 != 0:
            odd_numbers.add(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    odd_numbers.add(1)
    return sorted(odd_numbers)
