#!/bin/python3
class Time:
    pass


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.sec = t1.sec + t2.sec
    return sum


def modify_time(sum):
    if sum.hour >= 24:
        sum.hour -= 24
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    if sum.sec >= 60:
        sum.sec -= 60
        sum.minute += 1
    if sum.hour >= 24 or sum.minute >= 60 or sum.sec >= 60:
        return modify_time(sum)
    return sum


if __name__ == '__main__':
    start = Time()
    start.hour = 9
    start.minute = 250
    start.sec = 180
    duration = Time()
    duration.hour = 1
    duration.minute = 58
    duration.sec = 35
    previous_time = add_time(start, duration)
    correct_time = modify_time(previous_time)
    print('{:02d}:{:02d}:{:02d}'.format(correct_time.hour, correct_time.minute,
                                        correct_time.sec))
