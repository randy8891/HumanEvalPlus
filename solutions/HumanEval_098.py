def count_upper(s):
    """
    Counts the number of uppercase vowels ('A', 'E', 'I', 'O', 'U') 
    present at even indices in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The count of uppercase vowels at even indices.
    """
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)
