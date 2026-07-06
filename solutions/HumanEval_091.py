def func_string_count(s):
    """
    Counts the occurrences of lowercase and uppercase letter pairs in a string.
    A pair is defined as a lowercase letter immediately followed by its corresponding uppercase letter.

    Args:
        s (str): The input string.

    Returns:
        int: The count of lowercase-uppercase letter pairs.
    """
    count = 0
    for i in range(len(s) - 1):
        if s[i].islower() and s[i + 1].isupper() and s[i].upper() == s[i + 1]:
            count += 1
    return count
