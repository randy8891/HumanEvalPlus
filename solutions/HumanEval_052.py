def below_threshold(values, threshold):
    """
    Check if all values in the list are below the given threshold.

    Args:
        values (list): A list of numerical values.
        threshold (float): The threshold value.

    Returns:
        bool: True if all values are below the threshold, False otherwise.
    """
    return all(value < threshold for value in values)
