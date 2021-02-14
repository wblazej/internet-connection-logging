from time import sleep
from lib.check import check
from lib.status import Status

if __name__ == "__main__":
    print("Starting...")

    connection_status = Status()

    while True:
        spleep_time = 1
        if connection_status.internet_connection == False:
            spleep_time = 0.1

        try:
            sleep(spleep_time)
        except KeyboardInterrupt:
            print('\n\nStopping...')
            break

        connection_status.change(check())