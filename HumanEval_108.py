def count_nums(numbers):
    """
    Counts the numbers in the given list whose digit sum (considering the sign of the number) is positive.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        int: The count of numbers with a positive digit sum.
    """
    def digit_sum(n):
        n = abs(n)
        return sum(int(d) for d in str(n))
    
    return sum(1 for num in numbers if (num >= 0 and digit_sum(num) > 0) or (num < 0 and digit_sum(num) > 0))
