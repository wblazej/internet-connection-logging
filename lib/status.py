from datetime import datetime

class Status:
    def __init__(self):
        self.internet_connection = None
        self.internet_connection_lost = None

    def change(self, status: bool):
        if self.internet_connection == None:
            self.internet_connection = status
            if not status:
                self.internet_connection_lost = datetime.now()
                self.__print_connection_break_starting()

        if self.internet_connection and not status:
            self.internet_connection = False
            self.internet_connection_lost = datetime.now()
            self.__print_connection_break_starting()

        if not self.internet_connection and status:
            self.internet_connection = True
            end = datetime.now()

            print(f"\033[31m  End time: \033[0m{self.__convert_date(end)}")
            print(f"\033[31m\033[1m    Lasted: \033[0m{(end - self.internet_connection_lost)}\n")

    def __print_connection_break_starting(self):
        print(f"\n\033[31mStart time: \033[0m{self.__convert_date(self.internet_connection_lost)}")

    def __convert_date(self, date: datetime):
        return date.strftime("%A %d.%m.%Y %H:%M:%S.%f")