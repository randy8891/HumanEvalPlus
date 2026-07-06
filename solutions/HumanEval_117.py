def select_words(words, n):
    """
    Select words from a list that have exactly n consonants.

    Args:
        words (list of str): A list of words to filter.
        n (int): The exact number of consonants a word must have to be selected.

    Returns:
        list of str: A list of words with exactly n consonants.
    """
    vowels = set("aeiouAEIOU")
    
    def count_consonants(word):
        return sum(1 for char in word if char.isalpha() and char not in vowels)
    
    return [word for word in words if count_consonants(word) == n]
