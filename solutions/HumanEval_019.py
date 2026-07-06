def sort_numbers(number_words):
    """
    Sorts a space-delimited string of number words in ascending numerical order.
    
    Args:
        number_words (str): A space-delimited string of number words (e.g., "three one two").
        
    Returns:
        str: A space-delimited string of number words sorted in ascending numerical order.
    """
    word_to_num = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    num_to_word = {v: k for k, v in word_to_num.items()}
    words = number_words.split()
    sorted_words = sorted(words, key=lambda word: word_to_num[word])
    return " ".join(sorted_words)
