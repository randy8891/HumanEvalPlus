def generate_integers(start, end):
    """
    Returns a list of even digits between two single-digit integers (inclusive) in ascending order.
    
    Parameters:
    start (int): The starting single-digit integer.
    end (int): The ending single-digit integer.
    
    Returns:
    list: A list of even digits between start and end in ascending order.
    """
    return [i for i in range(min(start, end), max(start, end) + 1) if i % 2 == 0]
