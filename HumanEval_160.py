def do_algebra(expression: str) -> float:
    """
    Evaluates an algebraic expression given as a string and returns the result.
    
    The expression can contain numbers, parentheses, and the operators +, -, *, /.
    Assumes the input is a valid mathematical expression.
    
    Args:
        expression (str): The algebraic expression to evaluate.
        
    Returns:
        float: The result of the evaluated expression.
    """
    return eval(expression)
