def remove_vowels(input_string):
    """
    Removes all vowels (a, e, i, o, u) from the given string.

    Args:
        input_string (str): The string from which vowels will be removed.

    Returns:
        str: The input string with all vowels removed.
    """
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)
