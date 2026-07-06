def solve_string(s):
    """
    Reverses the string if it contains no letters; otherwise, swaps the case of each letter.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The modified string based on the conditions.
    """
    if any(c.isalpha() for c in s):
        return ''.join(c.swapcase() if c.isalpha() else c for c in s)
    else:
        return s[::-1]
