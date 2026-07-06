def parse_nested_parens(s):
    """
    Given a string `s` containing groups of parentheses, return a list of integers
    where each integer represents the deepest level of nesting for each group of parentheses.

    Args:
        s (str): A string containing groups of parentheses.

    Returns:
        list: A list of integers representing the deepest level of nesting for each group.
    """
    depths = []
    current_depth = 0
    for char in s:
        if char == '(':
            current_depth += 1
        elif char == ')':
            depths.append(current_depth)
            current_depth -= 1
    return depths
