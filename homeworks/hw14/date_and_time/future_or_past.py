from datetime import datetime, date


def is_future(date1):
    try:
        user_date = datetime.strptime(date1, "%Y-%m-%d").date()
        today = date.today()
        if user_date > today:
            return True
        elif user_date < today:
            return False
        else:
            return None
    except ValueError:
        return 'Wrong datetime format or incorrect date'
