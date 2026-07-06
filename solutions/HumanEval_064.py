def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
