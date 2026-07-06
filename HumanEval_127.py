def intersection_v2(range1, range2):
    """
    Determines if the intersection of two ranges has a length divisible by 2.

    Args:
        range1 (tuple): A tuple (start1, end1) representing the first range (inclusive).
        range2 (tuple): A tuple (start2, end2) representing the second range (inclusive).

    Returns:
        bool: True if the length of the intersection is divisible by 2, False otherwise.
    """
    start1, end1 = range1
    start2, end2 = range2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start <= intersection_end:
        intersection_length = intersection_end - intersection_start + 1
        return intersection_length % 2 == 0
    return False
