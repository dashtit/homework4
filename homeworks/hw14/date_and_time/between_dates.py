from datetime import datetime


def calculate_days_between(date1: str, date2: str):
    for date in (date1, date2):
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return 'Wrong datetime format or incorrect date'
    data_one = datetime.strptime(date1, '%Y-%m-%d')
    data_two = datetime.strptime(date2, '%Y-%m-%d')
    return abs((data_two - data_one).days)
