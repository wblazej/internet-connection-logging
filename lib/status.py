from datetime import datetime
from lib.convert_date import convert_date
from lib.convert_time import convert_time

class Status:
    def __init__(self):
        self.internet_connection = None
        self.internet_connection_lost_timestamp = None

    def change(self, status: bool):
        if self.internet_connection == None:
            self.internet_connection = status
            if not status:
                self.internet_connection_lost_timestamp = datetime.now().timestamp()
                self.__print_connection_break_starting__()

        if self.internet_connection and not status:
            self.internet_connection = False
            self.internet_connection_lost_timestamp = datetime.now().timestamp()
            self.__print_connection_break_starting__()

        if not self.internet_connection and status:
            self.internet_connection = True
            begin = datetime.fromtimestamp(self.internet_connection_lost_timestamp)
            end = datetime.fromtimestamp(datetime.now().timestamp())

            print(f"\033[31m  End time: \033[0m{convert_date(end)}")
            print(f"\033[31m\033[1m    Lasted: \033[0m{convert_time(end - begin)}\n")

    def __print_connection_break_starting__(self):
        date = datetime.fromtimestamp(self.internet_connection_lost_timestamp)
        print(f"\n\033[31mStart time: \033[0m{convert_date(date)}")