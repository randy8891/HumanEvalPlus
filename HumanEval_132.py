def is_nested(s):
    """
    Check if a string has at least one nested pair of brackets.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if there is at least one nested pair of brackets, False otherwise.
    """
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                if stack and stack[-1] == '(':
                    return True
            else:
                return False
    return False
