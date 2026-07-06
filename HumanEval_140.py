def fix_spaces(text):
    """
    Replaces spaces in the given text with underscores, but replaces sequences
    of 3 or more consecutive spaces with a single dash.

    Args:
        text (str): The input string to process.

    Returns:
        str: The processed string with spaces replaced as described.
    """
    result = []
    i = 0
    while i < len(text):
        if text[i] == ' ':
            space_count = 0
            while i < len(text) and text[i] == ' ':
                space_count += 1
                i += 1
            if space_count >= 3:
                result.append('-')
            else:
                result.append('_' * space_count)
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)
