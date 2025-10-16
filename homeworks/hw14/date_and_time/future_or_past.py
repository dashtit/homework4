from datetime import datetime


def is_future(date):
    try:
        if datetime.strptime(date, '%Y-%m-%d').date() > datetime.now().date():
            return True
        if datetime.strptime(date, '%Y-%m-%d').date() == datetime.now().date():
            return None
        return False
    except ValueError:
        return 'Wrong datetime format or incorrect date'
