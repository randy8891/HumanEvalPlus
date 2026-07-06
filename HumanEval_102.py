def choose_num(x, y):
    """
    Returns the largest even number in the range [x, y].
    If no even number exists in the range, returns -1.
    """
    if x % 2 != 0:
        x += 1
    if x > y:
        return -1
    return y if y % 2 == 0 else y - 1
