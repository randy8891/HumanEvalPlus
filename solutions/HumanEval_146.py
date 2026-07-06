def specialFilter(numbers):
    """
    Counts the numbers in the given list that are greater than 10 and have both their first and last digits as odd.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The count of numbers meeting the criteria.
    """
    def is_odd_digit(digit):
        return int(digit) % 2 != 0

    count = 0
    for num in numbers:
        if num > 10:
            str_num = str(num)
            if is_odd_digit(str_num[0]) and is_odd_digit(str_num[-1]):
                count += 1
    return count
