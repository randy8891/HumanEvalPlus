def right_angle_triangle(a, b, c):
    """
    Determines if three sides form a right triangle.

    Args:
        a (float): The length of the first side.
        b (float): The length of the second side.
        c (float): The length of the third side.

    Returns:
        bool: True if the sides form a right triangle, False otherwise.
    """
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
