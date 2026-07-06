def int_to_mini_roman(num):
    """
    Convert an integer (1-1000) to its Roman numeral representation in lowercase.
    
    Args:
        num (int): An integer between 1 and 1000 (inclusive).
        
    Returns:
        str: The Roman numeral representation in lowercase.
    """
    if not (1 <= num <= 1000):
        raise ValueError("Input must be an integer between 1 and 1000.")
    
    roman_map = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]
    
    result = []
    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)
