def flip_case(s):
    """
    Flips the case of each character in the input string.
    Uppercase characters are converted to lowercase and vice versa.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with flipped case for each character.
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)
