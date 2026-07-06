def encode(message):
    """
    Encodes a message by swapping the case of vowels and shifting consonants by 2.
    Non-alphabetic characters remain unchanged.
    
    Parameters:
    message (str): The input string to encode.
    
    Returns:
    str: The encoded message.
    """
    def shift_consonant(char):
        if char.islower():
            shifted = chr(((ord(char) - ord('a') + 2) % 26) + ord('a'))
        else:
            shifted = chr(((ord(char) - ord('A') + 2) % 26) + ord('A'))
        return shifted if shifted.lower() not in 'aeiou' else chr(ord(shifted) + 1)

    result = []
    for char in message:
        if char.lower() in 'aeiou':
            result.append(char.swapcase())
        elif char.isalpha():
            result.append(shift_consonant(char))
        else:
            result.append(char)
    return ''.join(result)
