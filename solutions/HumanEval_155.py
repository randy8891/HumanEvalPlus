def even_odd_count(number):
    """
    Counts the number of even and odd digits in an integer.

    Args:
        number (int): The integer whose digits are to be analyzed.

    Returns:
        tuple: A tuple (even_count, odd_count) where:
               even_count is the number of even digits,
               odd_count is the number of odd digits.
    """
    even_count = 0
    odd_count = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
