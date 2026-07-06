import hashlib

def string_to_md5(input_string):
    """
    Returns the MD5 hash of a given string. If the input string is empty, returns None.
    
    Args:
        input_string (str): The string to hash.
        
    Returns:
        str or None: The MD5 hash of the string, or None if the input is empty.
    """
    if not input_string:
        return None
    return hashlib.md5(input_string.encode()).hexdigest()
