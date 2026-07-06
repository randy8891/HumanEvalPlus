def digits(n):
    """
    Returns the product of odd digits in the given number n.
    If there are no odd digits, returns 0.
    
    Parameters:
    n (int): The input number.
    
    Returns:
    int: The product of odd digits or 0 if none exist.
    """
    product = 1
    has_odd = False
    for digit in str(abs(n)):
        if int(digit) % 2 != 0:
            product *= int(digit)
            has_odd = True
    return product if has_odd else 0
