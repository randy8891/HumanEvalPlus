def fizz_buzz(n):
    """
    Counts the occurrences of the digit 7 in integers below n that are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The count of the digit 7 in the qualifying integers.
    """
    return sum(str(x).count('7') for x in range(n) if x % 11 == 0 or x % 13 == 0)
