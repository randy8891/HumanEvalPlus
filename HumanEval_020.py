def find_closest_elements(nums):
    """
    Finds the two closest numbers in a list and returns them as a tuple.
    
    Args:
        nums (list): A list of numbers.
        
    Returns:
        tuple: A tuple containing the two closest numbers.
    """
    if len(nums) < 2:
        return None
    
    nums.sort()
    min_diff = float('inf')
    closest_pair = None
    
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (nums[i], nums[i + 1])
    
    return closest_pair
