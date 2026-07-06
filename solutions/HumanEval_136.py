def largest_smallest_integers(numbers):
    """
    Returns the largest negative integer and the smallest positive integer
    from a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the largest negative integer and the smallest
               positive integer. If no such integers exist, returns None for
               that position in the tuple.
    """
    largest_negative = None
    smallest_positive = None

    for num in numbers:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num

    return largest_negative, smallest_positive
