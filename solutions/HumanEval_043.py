def pairs_sum_to_zero(nums):
    """
    Check if any two distinct elements in the list sum to zero.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if there exist two distinct elements that sum to zero, False otherwise.
    """
    seen = set()
    for num in nums:
        if -num in seen:
            return True
        seen.add(num)
    return False
