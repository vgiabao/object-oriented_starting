#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
class Rotation:
    def __init__(self, array, k, queries):
        self.array = array
        self.k = k
        self.queries = queries

    def rotate(self):
        while self.k > 0:
            for counting in range(len(self.array) - 1, 0, -1):
                self.array[counting], self.array[counting - 1] =\
                    self.array[counting - 1], self.array[counting]
            self.k -= 1
        return self.array


if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = Rotation(a, k, queries)
    rotating = result.rotate()
    for index_number in queries:
        print(rotating[index_number])
