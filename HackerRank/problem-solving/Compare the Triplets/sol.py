#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    list = [0,0]
    for i in [0,1,2]:
        if a[i] > b[i]:
            list[0] += 1
        elif a[i] < b[i]:
            list[1] += 1
    return list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
