import json
from datetime import datetime
from lib.convert_date import convert_date
from lib.convert_time import convert_time
from config import LOGS_FILE_NAME

results = json.loads(open(LOGS_FILE_NAME, 'r').read())

internet_breaks = []

internet_connection = None
internet_lost_connection_timestamp = None

for r in results['logs']:
    if internet_connection == None:
        internet_connection = r['internet_connection']
        if not r['internet_connection']:
            internet_lost_connection_timestamp = r['timestamp']

    if internet_connection and not r['internet_connection']:
        internet_connection = False
        internet_lost_connection_timestamp = r['timestamp']

    if not internet_connection and r['internet_connection']:
        internet_connection = True
        begin = datetime.fromtimestamp(internet_lost_connection_timestamp)
        end = datetime.fromtimestamp(r['timestamp'])
        internet_breaks.append({
            "start": convert_date(begin),
            "end": convert_date(end),
            "lasted": convert_time(end - begin)
        })

for i in reversed(internet_breaks):
    print(i)