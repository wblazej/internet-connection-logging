from lib.check import check
from time import sleep
import json
from os import path
from datetime import datetime
from pythonping import ping

LOGS_FILE_NAME = "results.json"

def log(internet_connection: str):
    if not path.exists(LOGS_FILE_NAME):
        open(LOGS_FILE_NAME, 'w').write(json.dumps({"logs": []}, indent=4))

    result_json = json.loads(open(LOGS_FILE_NAME, 'r').read())

    result_json['logs'].append({
        "internet_connection": internet_connection,
        "timestamp": datetime.now().timestamp()
    })

    open(LOGS_FILE_NAME, 'w').write(json.dumps(result_json, indent=4))

    if not internet_connection:
        print(f"[{datetime.now()}] Connection lost")
    else:
        print(f"[{datetime.now()}] Connection restored")


def check():
    try:
        result = ping('google.com', timeout=0.5, count=1)
        return result.success()
    except RuntimeError:
        return False


if __name__ == "__main__":
    print("Starting...")

    internet_connection = None

    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            print('\n\nStopping...')
            break

        result = check()

        if internet_connection == None:
            internet_connection = result
        elif internet_connection and not result:
            internet_connection = False
            log(internet_connection)
        elif not internet_connection and result:
            internet_connection = True
            log(internet_connection)