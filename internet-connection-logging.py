from time import sleep
from lib.check import check
from lib.log import log

if __name__ == "__main__":
    print("Starting...")

    internet_connection = None

    while True:
        spleep_time = 1
        if not internet_connection:
            spleep_time = 0.1

        try:
            sleep(spleep_time)
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