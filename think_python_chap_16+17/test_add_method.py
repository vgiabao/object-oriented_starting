#!/bin/python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, second=0):
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        hour //= 24
        return ('{:02d}:{:02d}:{:02d}'.format(hour, minute,
                                              second))

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        print(seconds)
        return self.int_to_time(seconds)


if __name__ == '__main__':
    p = Time(0, 6, 7)
    duration = Time(0, 9, 2)
    print(p + duration)