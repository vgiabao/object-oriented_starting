#!/bin/python3


class CompareTime:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def handle_time(self):
        if self.t1[0] > self.t2[0]:
            return True
        elif self.t1[0] == self.t2[0]:
            if self.t1[1] > self.t2[1]:
                return True
            elif self.t1[1] == self.t2[1]:
                if self.t1[2] > self.t2[2]:
                    return True
        return False


t1 = input().split(':')
t2 = input().split(':')
p = CompareTime(t1, t2)
print(p.handle_time())
