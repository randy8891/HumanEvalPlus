def get_positive(numbers):
    """
    Returns a list of positive numbers from the given list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list containing only the positive numbers from the input list.
    """
    return [num for num in numbers if num > 0]
