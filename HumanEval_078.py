def hex_key(hex_string):
    """
    Counts the number of prime hexadecimal digits (2, 3, 5, 7) in a given hex string.

    Args:
        hex_string (str): A string containing hexadecimal characters.

    Returns:
        int: The count of prime hexadecimal digits in the input string.
    """
    prime_hex_digits = {'2', '3', '5', '7'}
    return sum(1 for char in hex_string if char in prime_hex_digits)
