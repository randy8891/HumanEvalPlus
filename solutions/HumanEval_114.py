def minSubArraySum(arr):
    """
    Finds the minimum sum of any contiguous subarray in the given array.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The minimum sum of any contiguous subarray.
    """
    if not arr:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    
    for num in arr:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    
    return min_sum
