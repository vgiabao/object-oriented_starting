#!/bin/python3


class Time:
    pass


t = Time()
t.hour = 11
t.minute = 2
t.second = 33
print('{:02d}:{:02d}:{:02d}'.format(t.hour, t.minute, t.second))
