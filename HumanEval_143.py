def words_in_sentence(sentence):
    """
    Returns a list of words from the given sentence whose lengths are prime numbers.
    
    Args:
        sentence (str): The input sentence.
        
    Returns:
        list: A list of words with lengths that are prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    return [word for word in words if is_prime(len(word))]
