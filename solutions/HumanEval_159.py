def eat(carrots, amount_to_eat):
    """
    Calculate the food eaten and the remaining carrots after eating.

    Parameters:
    carrots (int): The initial number of carrots available.
    amount_to_eat (int): The number of carrots to eat.

    Returns:
    tuple: A tuple containing the number of carrots eaten and the number of carrots remaining.
    """
    eaten = min(carrots, amount_to_eat)
    remaining = carrots - eaten
    return eaten, remaining
