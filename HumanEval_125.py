def split_words_v2(sentence):
    """
    Splits a given sentence into words and counts the number of letters in each word.
    
    Args:
        sentence (str): The input sentence to be split into words.
    
    Returns:
        list of tuples: A list where each tuple contains a word and its letter count.
    """
    return [(word, len(word)) for word in sentence.split()]
