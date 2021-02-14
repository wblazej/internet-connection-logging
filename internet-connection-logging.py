from time import sleep
from lib.check import check
from lib.status import Status
from config import PINGS_BREAK_ONLINE, PINGS_BREAK_OFFLINE

if __name__ == "__main__":
    print("Starting...")

    connection_status = Status()

    while True:
        spleep_time = PINGS_BREAK_ONLINE
        if connection_status.internet_connection == False:
            spleep_time = PINGS_BREAK_OFFLINE

        try:
            sleep(spleep_time)
        except KeyboardInterrupt:
            print('\n\nStopping...')
            break

        connection_status.change(check())