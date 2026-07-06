def change_base(number, base):
    """
    Converts an integer to a string representation in a given base (2-9).
    
    Args:
        number (int): The integer to convert.
        base (int): The base to convert to (must be between 2 and 9).
        
    Returns:
        str: The string representation of the number in the given base.
        
    Raises:
        ValueError: If the base is not between 2 and 9.
    """
    if not (2 <= base <= 9):
        raise ValueError("Base must be between 2 and 9.")
    
    if number == 0:
        return "0"
    
    result = ""
    is_negative = number < 0
    number = abs(number)
    
    while number > 0:
        result = str(number % base) + result
        number //= base
    
    if is_negative:
        result = "-" + result
    
    return result
