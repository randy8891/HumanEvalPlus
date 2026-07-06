def sum_product(numbers):
    """
    Calculate and return the sum and product of all integers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num
    return total_sum, total_product
