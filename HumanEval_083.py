def starts_one_ends(n):
    """
    Counts the number of n-digit numbers that start or end with the digit 1.

    Parameters:
    n (int): The number of digits.

    Returns:
    int: The count of n-digit numbers starting or ending with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 1  # Only the number 1 satisfies this for single-digit numbers
    total_numbers = 9 * 10**(n - 1)  # Total n-digit numbers
    start_with_1 = 10**(n - 1)       # Numbers starting with 1
    end_with_1 = 10**(n - 1)         # Numbers ending with 1
    overlap = 10**(n - 2)            # Numbers starting and ending with 1
    return start_with_1 + end_with_1 - overlap
