from os import path
import json
from datetime import datetime
from config import LOGS_FILE_NAME

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