def will_it_fly(object_name, weight, weight_limit):
    """
    Determines if an object will fly based on two conditions:
    1. The object's name must be a palindrome (reads the same forward and backward).
    2. The object's weight must be less than or equal to the weight limit.

    Args:
        object_name (str): The name of the object.
        weight (int or float): The weight of the object.
        weight_limit (int or float): The maximum allowable weight.

    Returns:
        bool: True if the object will fly, False otherwise.
    """
    return object_name == object_name[::-1] and weight <= weight_limit
