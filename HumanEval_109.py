def move_one_ball(arr):
    """
    Determines if a list can become sorted in ascending order by performing at most one right shift.
    
    A right shift moves the last element of the list to the front.
    
    Args:
        arr (list): The input list of integers.
    
    Returns:
        bool: True if the list can become sorted by at most one right shift, False otherwise.
    """
    n = len(arr)
    if n <= 1:
        return True
    
    for i in range(n):
        shifted = arr[-i:] + arr[:-i]
        if shifted == sorted(arr):
            return True
    
    return False
