def split_words(text):
    """
    Splits a given string into words based on spaces, commas, or the count of 
    odd-indexed uppercase letters in the string. Words are separated by spaces 
    or commas, and the string is further split into chunks of length equal to 
    the count of uppercase letters at odd indices.

    Args:
        text (str): The input string to split.

    Returns:
        list: A list of substrings split based on the criteria.
    """
    words = []
    odd_upper_count = sum(1 for i, c in enumerate(text) if i % 2 == 1 and c.isupper())
    for part in text.replace(',', ' ').split():
        if odd_upper_count > 0:
            words.extend([part[i:i+odd_upper_count] for i in range(0, len(part), odd_upper_count)])
        else:
            words.append(part)
    return words
