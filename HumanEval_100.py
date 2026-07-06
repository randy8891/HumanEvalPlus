def make_a_pile(n):
    """
    Creates a pile of n levels of stones following an odd/even pattern.
    Odd levels contain odd numbers of stones, starting from 1.
    Even levels contain even numbers of stones, starting from 2.
    
    Args:
        n (int): The number of levels in the pile.
    
    Returns:
        list: A list where each element represents the number of stones in a level.
    """
    return [i if i % 2 == 1 else i for i in range(1, n + 1)]
