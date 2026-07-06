def correct_bracketing(s):
    """
    Checks if every '<' in the string has a matching '>' and they are properly nested.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the bracketing is correct, False otherwise.
    """
    balance = 0
    for char in s:
        if char == '<':
            balance += 1
        elif char == '>':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0
