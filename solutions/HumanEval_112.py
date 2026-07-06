def reverse_delete(s: str, c: str) -> bool:
    """
    Removes all characters from string s that appear in string c, 
    then checks if the resulting string is a palindrome.
    
    Args:
    s (str): The input string to process.
    c (str): The string containing characters to remove from s.
    
    Returns:
    bool: True if the resulting string is a palindrome, False otherwise.
    """
    filtered_s = ''.join(char for char in s if char not in c)
    return filtered_s == filtered_s[::-1]
