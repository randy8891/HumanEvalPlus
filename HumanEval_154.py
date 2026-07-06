def cycpattern_check(a: str, b: str) -> bool:
    """
    Check if any rotation of string b is a substring of string a.

    Args:
    a (str): The string to check within.
    b (str): The string to rotate and check as a substring.

    Returns:
    bool: True if any rotation of b is a substring of a, False otherwise.
    """
    if not b:
        return True
    doubled_b = b + b
    return any(a.find(doubled_b[i:i+len(b)]) != -1 for i in range(len(b)))
