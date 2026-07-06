def modp(n, p):
    """
    Calculate 2^n mod p efficiently.
    
    Parameters:
    n (int): The exponent.
    p (int): The modulus.
    
    Returns:
    int: The result of 2^n mod p.
    """
    return pow(2, n, p)
