def valid_date(date_str):
    """
    Validates if a given date string is in the format 'mm-dd-yyyy' and represents a valid calendar date.
    
    Args:
        date_str (str): The date string to validate.
        
    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        month, day, year = map(int, date_str.split('-'))
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        if year < 1:
            return False
        if month in {4, 6, 9, 11} and day > 30:
            return False
        if month == 2:
            if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):  # Leap year
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True
    except (ValueError, AttributeError):
        return False
