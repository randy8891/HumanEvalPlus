def simplify(x, n):
    """
    Checks if the product of two fractions x and n is a whole number.

    Args:
        x (str): A fraction represented as a string (e.g., "3/4").
        n (str): A fraction represented as a string (e.g., "2/5").

    Returns:
        bool: True if the product of x and n is a whole number, False otherwise.
    """
    def to_fraction(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator, denominator

    x_num, x_den = to_fraction(x)
    n_num, n_den = to_fraction(n)

    product_num = x_num * n_num
    product_den = x_den * n_den

    return product_num % product_den == 0
