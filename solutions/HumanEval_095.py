def check_dict_case(d):
    """
    Check if all keys in the dictionary are either all-lowercase or all-uppercase strings.

    Args:
        d (dict): The dictionary to check.

    Returns:
        bool: True if all keys are all-lowercase or all-uppercase strings, False otherwise.
    """
    if not all(isinstance(key, str) for key in d.keys()):
        return False
    all_lower = all(key.islower() for key in d.keys())
    all_upper = all(key.isupper() for key in d.keys())
    return all_lower or all_upper
