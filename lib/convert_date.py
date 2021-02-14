from datetime import datetime

def convert_date(date: datetime):
    microseconds = date.microsecond
    seconds = date.second
    minutes = date.minute
    hours = date.hour
    day = date.day
    month = date.month
    year = date.year

    if seconds < 10: seconds = f'0{seconds}'
    if minutes < 10: minutes = f'0{minutes}'
    if hours < 10: hours = f'0{hours}'
    if day < 10: day = f'0{day}'
    if month < 10: month = f'0{month}'

    return f'{day}.{month}.{year} {hours}:{minutes}:{seconds}.{microseconds}'