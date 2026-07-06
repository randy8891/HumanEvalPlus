def file_name_check(file_name):
    """
    Validates a file name based on the following rules:
    1. The file name must not be empty.
    2. The file name must not contain any of the following characters: \ / : * ? " < > |
    3. The file name must not exceed 255 characters.
    4. The file name must have an extension (e.g., .txt, .jpg) and the extension must be at least 2 characters long.

    Args:
        file_name (str): The file name to validate.

    Returns:
        bool: True if the file name is valid, False otherwise.
    """
    invalid_chars = set(r'\/:*?"<>|')
    if not file_name or len(file_name) > 255:
        return False
    if any(char in invalid_chars for char in file_name):
        return False
    if '.' not in file_name or file_name.startswith('.') or file_name.endswith('.'):
        return False
    name, ext = file_name.rsplit('.', 1)
    if len(ext) < 2 or not name:
        return False
    return True
