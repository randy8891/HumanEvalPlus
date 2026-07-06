def solution(arr):
    """
    Returns the sum of odd elements at even positions in the given list.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of odd elements at even positions.
    """
    return sum(arr[i] for i in range(0, len(arr), 2) if arr[i] % 2 != 0)
