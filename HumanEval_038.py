def encode_cyclic(s):
    """
    Encodes a string by cycling groups of three characters.
    Each group of three characters is rotated such that the first character
    becomes the last, the second becomes the first, and the third becomes the second.
    If the string length is not a multiple of three, the remaining characters
    are left unchanged.

    Args:
        s (str): The input string to encode.

    Returns:
        str: The encoded string with groups of three characters cycled.
    """
    result = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            result.append(group[1:] + group[0])
        else:
            result.append(group)
    return ''.join(result)
