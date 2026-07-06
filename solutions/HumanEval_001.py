def separate_paren_groups(s):
    """
    Separates groups of nested parentheses into separate strings.

    Args:
        s (str): A string containing nested parentheses.

    Returns:
        list: A list of strings, where each string is a group of nested parentheses.
    """
    result = []
    stack = []
    current_group = ""

    for char in s:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            if stack:
                stack.pop()
            current_group += char
            if not stack:
                result.append(current_group)
                current_group = ""

    return result
