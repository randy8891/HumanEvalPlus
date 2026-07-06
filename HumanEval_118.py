def get_closest_vowel(s):
    """
    Finds the closest vowel from the right between two consonants in the given string.
    
    Parameters:
    s (str): The input string to search.
    
    Returns:
    str: The closest vowel between two consonants from the right, or an empty string if not found.
    """
    vowels = "aeiou"
    consonants = set("bcdfghjklmnpqrstvwxyz")
    for i in range(len(s) - 2, -1, -1):
        if s[i] in vowels and s[i - 1] in consonants and s[i + 1] in consonants:
            return s[i]
    return ""
