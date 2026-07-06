def how_many_times(string, substring):
    """
    Counts how many times a substring appears in a string, including overlaps.

    Args:
        string (str): The string to search within.
        substring (str): The substring to count.

    Returns:
        int: The number of times the substring appears in the string, including overlaps.
    """
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count
