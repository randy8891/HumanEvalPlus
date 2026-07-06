def find_zero(coefficients, x0=0, tolerance=1e-7, max_iterations=1000):
    """
    Finds a zero of a polynomial defined by its coefficients using Newton's method.

    Parameters:
        coefficients (list): List of coefficients of the polynomial in descending order of powers.
        x0 (float): Initial guess for the root. Default is 0.
        tolerance (float): Convergence tolerance. Default is 1e-7.
        max_iterations (int): Maximum number of iterations. Default is 1000.

    Returns:
        float: A root of the polynomial if found within tolerance, otherwise None.
    """
    def evaluate_polynomial(coeffs, x):
        return sum(c * (x ** i) for i, c in enumerate(reversed(coeffs)))

    def evaluate_derivative(coeffs, x):
        return sum(i * c * (x ** (i - 1)) for i, c in enumerate(reversed(coeffs)) if i > 0)

    for _ in range(max_iterations):
        f_x = evaluate_polynomial(coefficients, x0)
        f_prime_x = evaluate_derivative(coefficients, x0)
        if abs(f_prime_x) < 1e-12:  # Avoid division by zero
            return None
        x1 = x0 - f_x / f_prime_x
        if abs(x1 - x0) < tolerance:
            return x1
        x0 = x1

    return None
