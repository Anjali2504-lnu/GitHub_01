from datetime import datetime

def is_valid_date(date_str, date_format="%Y-%m-%d"):

    try:
        datetime.strptime(date_str, date_format)
        return True
    except (ValueError, TypeError):
        return False

def validate_date_range(date_str, start_date=None, end_date=None, date_format="%Y-%m-%d"):

    if not is_valid_date(date_str, date_format):
        return False, f"Invalid date format: {date_str}"
    
    date_obj = datetime.strptime(date_str, date_format)
    
    if start_date:
        start_obj = datetime.strptime(start_date, date_format)
        if date_obj < start_obj:
            return False, f"Date {date_str} is before start date {start_date}"
    
    if end_date:
        end_obj = datetime.strptime(end_date, date_format)
        if date_obj > end_obj:
            return False, f"Date {date_str} is after end date {end_date}"
    
    return True, ""
