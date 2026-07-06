def find_max(words):
    """
    Finds the word with the most unique characters from a list of words.
    If there is a tie, returns the word that comes first alphabetically.

    Args:
        words (list of str): A list of words.

    Returns:
        str: The word with the most unique characters, or the alphabetically first word in case of a tie.
    """
    return max(words, key=lambda word: (len(set(word)), -ord(word[0])))
