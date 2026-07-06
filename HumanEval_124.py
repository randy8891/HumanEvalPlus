from datetime import datetime

def valid_date_v2(date_string):
    """
    Validates a date string in the format 'YYYY-MM-DD' and returns the day of the week.
    If the date is invalid, returns None.

    Args:
        date_string (str): The date string to validate.

    Returns:
        str or None: The day of the week if valid, otherwise None.
    """
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%A")
    except ValueError:
        return None
