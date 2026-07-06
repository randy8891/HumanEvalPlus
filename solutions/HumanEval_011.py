def string_xor(bin_str1, bin_str2):
    """
    XOR two binary strings and return the result as a binary string.
    
    Args:
        bin_str1 (str): The first binary string.
        bin_str2 (str): The second binary string.
        
    Returns:
        str: The result of XOR operation as a binary string.
        
    Raises:
        ValueError: If the input strings are not of the same length.
    """
    if len(bin_str1) != len(bin_str2):
        raise ValueError("Binary strings must be of the same length.")
    
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin_str1, bin_str2))
