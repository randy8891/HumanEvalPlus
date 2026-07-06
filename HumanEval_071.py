def triangle_area_heron(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    a (float): Length of the first side of the triangle.
    b (float): Length of the second side of the triangle.
    c (float): Length of the third side of the triangle.

    Returns:
    float: The area of the triangle, or None if the sides do not form a valid triangle.
    """
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return None
