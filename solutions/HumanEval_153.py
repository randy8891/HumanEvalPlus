def Strongest_Extension(extensions):
    """
    Determines the strongest class extension based on the difference between the count of uppercase
    and lowercase letters in each extension. The strongest extension is the one with the highest
    difference (uppercase - lowercase). If there is a tie, the first extension in the list is chosen.

    Args:
        extensions (list of str): A list of strings representing class extensions.

    Returns:
        str: The strongest class extension.
    """
    def strength(extension):
        upper_count = sum(1 for char in extension if char.isupper())
        lower_count = sum(1 for char in extension if char.islower())
        return upper_count - lower_count

    return max(extensions, key=strength)
