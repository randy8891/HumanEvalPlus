def compare(guess, solution):
    """
    Returns the element-wise absolute difference between two lists, guess and solution.

    Args:
        guess (list of int/float): The first list of numbers.
        solution (list of int/float): The second list of numbers.

    Returns:
        list of int/float: A list containing the absolute differences between corresponding elements of guess and solution.
    """
    return [abs(g - s) for g, s in zip(guess, solution)]
