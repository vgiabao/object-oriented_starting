#!/bin/python3
from test1 import Point
from copy import deepcopy, copy


class Rectangle:
    pass


box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


center = find_center(box)
print(center.x, center.y)
box3 = deepcopy(box)
box4 = copy(box)
print(box3.corner == box.corner)
print(box4.corner == box.corner)
print(hasattr(box3, 'corner'))
