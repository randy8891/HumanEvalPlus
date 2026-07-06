def pluck(branch):
    """
    Plucks the smallest even-valued node from a tree branch.
    
    A branch is represented as a list of integers. The function finds the smallest
    even-valued node in the branch, removes it from the branch, and returns the value.
    If no even-valued node exists, the function returns None.
    
    Args:
        branch (list): A list of integers representing the tree branch.
    
    Returns:
        int or None: The smallest even-valued node removed from the branch, or None if no even-valued node exists.
    """
    smallest_even = None
    for value in branch:
        if value % 2 == 0 and (smallest_even is None or value < smallest_even):
            smallest_even = value
    if smallest_even is not None:
        branch.remove(smallest_even)
    return smallest_even
