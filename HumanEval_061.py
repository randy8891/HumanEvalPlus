def correct_bracketing_parens(s):
    """
    Checks if every '(' in the input string has a matching ')'.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if every '(' has a matching ')', False otherwise.
    """
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0
