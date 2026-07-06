def odd_count(numbers):
    """
    Takes a list of number strings and returns a list of strings describing the count of odd digits in each number string.
    
    Args:
    numbers (list of str): A list of strings where each string represents a number.
    
    Returns:
    list of str: A list of strings in the format "Number X has Y odd digit(s)" where X is the number string 
                 and Y is the count of odd digits in that number.
    """
    result = []
    for num in numbers:
        count = sum(1 for digit in num if digit in '13579')
        result.append(f"Number {num} has {count} odd digit(s)")
    return result
