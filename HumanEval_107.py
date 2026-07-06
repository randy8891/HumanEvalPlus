def even_odd_palindrome(n):
    """
    Counts the number of even and odd palindromes in the range [1, n].
    
    A palindrome is a number that reads the same backward as forward.
    An even palindrome is a palindrome that is even, and an odd palindrome is a palindrome that is odd.
    
    Args:
        n (int): The upper limit of the range (inclusive).
        
    Returns:
        tuple: A tuple (even_count, odd_count) where:
               - even_count is the count of even palindromes in the range.
               - odd_count is the count of odd palindromes in the range.
    """
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return even_count, odd_count
