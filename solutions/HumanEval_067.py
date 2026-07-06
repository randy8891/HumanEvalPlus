def fruit_distribution(sentence):
    """
    Extracts and calculates the number of mangoes mentioned in a fruit distribution sentence.
    
    The function assumes the sentence contains a phrase like 'X mangoes' where X is an integer.
    If no such phrase is found, it returns 0.

    Args:
        sentence (str): The input sentence describing the fruit distribution.

    Returns:
        int: The number of mangoes found in the sentence, or 0 if not mentioned.
    """
    words = sentence.split()
    for i in range(len(words) - 1):
        if words[i + 1].lower() == "mangoes" and words[i].isdigit():
            return int(words[i])
    return 0
