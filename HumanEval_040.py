def triples_sum_to_zero(nums):
    """
    Check if any three distinct elements in the list sum to zero.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if there exist three distinct elements that sum to zero, False otherwise.
    """
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1
    return False
