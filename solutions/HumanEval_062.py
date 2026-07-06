def derivative(coefficients):
    """
    Compute the derivative of a polynomial given its coefficients.

    The input is a list of coefficients where the i-th element represents the coefficient
    of the x^i term. The output is a list of coefficients for the derivative of the polynomial.

    Example:
        derivative([3, 2, 1]) -> [2, 2]
        Explanation: The polynomial 3 + 2x + x^2 has a derivative of 2 + 2x.

    Args:
        coefficients (list): List of integers or floats representing polynomial coefficients.

    Returns:
        list: List of integers or floats representing the coefficients of the derivative.
    """
    return [i * coefficients[i] for i in range(1, len(coefficients))]
