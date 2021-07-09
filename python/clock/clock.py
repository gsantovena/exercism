class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

        while self.hour < 0:
            self.hour += 24

        while self.minute < 0:
            self.minute += 60
            self.hour = (self.hour - 1) % 24

        self.hour = (self.hour + int(self.minute / 60)) % 24
        self.minute = self.minute % 60

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
