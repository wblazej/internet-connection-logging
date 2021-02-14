from datetime import timedelta
from math import floor

def convert_time(time: timedelta):
    microseconds = time.microseconds
    seconds = time.seconds

    hours = floor(seconds / 3600)
    seconds -= 3600 * hours

    minutes = floor(seconds / 60)
    seconds -= 60 * minutes

    if seconds < 10:
        seconds = f'0{seconds}'

    if minutes < 10:
        minutes = f'0{minutes}'

    if hours < 10:
        hours = f'0{hours}'

    return f'{hours}:{minutes}:{seconds}.{microseconds}'