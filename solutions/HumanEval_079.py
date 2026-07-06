def decimal_to_binary(decimal_number):
    """
    Convert a decimal number to a binary string with 'db' prefix and suffix.

    Args:
        decimal_number (int): The decimal number to convert.

    Returns:
        str: The binary string with 'db' prefix and suffix.
    """
    return f"db{bin(decimal_number)[2:]}db"
