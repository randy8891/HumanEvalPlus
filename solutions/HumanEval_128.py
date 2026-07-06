def prod_signs(numbers):
    """
    Calculate the sum of magnitudes of numbers, where the sign of each magnitude
    matches the product of all signs in the input list.

    Args:
        numbers (list of float): A list of numbers.

    Returns:
        float: The sum of magnitudes with the sign equal to the product of signs.
    """
    if not numbers:
        return 0

    product_sign = 1
    for num in numbers:
        if num < 0:
            product_sign *= -1
        elif num == 0:
            return 0

    return product_sign * sum(abs(num) for num in numbers)
