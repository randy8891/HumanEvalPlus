def has_close_elements(numbers, threshold):
    """
    Checks if any two numbers in the list are closer than the given threshold.

    Args:
        numbers (list of float): The list of numbers to check.
        threshold (float): The threshold distance.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
