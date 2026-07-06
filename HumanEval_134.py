def check_if_last_char_is_a_letter(s):
    """
    Checks if the last character of a word-separated string is a letter.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the last character is a letter, False otherwise.
    """
    s = s.strip()
    return s[-1].isalpha() if s else False
