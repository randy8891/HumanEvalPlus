def match_parens(s1, s2):
    """
    Check if two parenthesis strings can be concatenated into a valid sequence.

    Args:
        s1 (str): The first parenthesis string.
        s2 (str): The second parenthesis string.

    Returns:
        bool: True if the concatenated string is a valid sequence, False otherwise.
    """
    def is_valid(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    return is_valid(s1 + s2)
