def histogram(sentence):
    """
    Returns the most common letter(s) and their count from a sentence.
    
    Parameters:
        sentence (str): The input sentence.
        
    Returns:
        tuple: A tuple containing a list of the most common letter(s) and their count.
    """
    letter_counts = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    if not letter_counts:
        return [], 0
    
    max_count = max(letter_counts.values())
    most_common = [char for char, count in letter_counts.items() if count == max_count]
    
    return most_common, max_count
