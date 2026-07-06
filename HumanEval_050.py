def encode_shift(text):
    """
    Encodes a string by shifting each letter by 5 positions in the alphabet.
    Non-alphabetic characters remain unchanged. Wraps around for 'z' to 'a'.
    
    Args:
        text (str): The input string to encode.
    
    Returns:
        str: The encoded string.
    """
    def shift_char(c):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + 5) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + 5) % 26 + ord('A'))
        return c

    return ''.join(shift_char(c) for c in text)
