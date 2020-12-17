class Time:
    def __init__(self, time):
        self.year = int(time[0:4])
        self.month = int(time[5] + time[6])
        self.day = int(time[8] + time[9])
        self.hour = int(time[11] + time[12])
        self.min = int(time[14] + time[15])
        self.sec = float(time[17:])

    def print_all(self):
        print(self.year, ".", self.month, ".", self.day, ":", self.hour, ".", self.min, ",", self.sec)


