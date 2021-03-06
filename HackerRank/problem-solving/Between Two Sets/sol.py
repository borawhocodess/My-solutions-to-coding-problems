#!/bin/python3

import math
import os
import random
import re
import sys

def checkA(a, x):
    for i in a:
        if x % i != 0:
            return False
    return True

def checkB(b, x):
    for i in b:
        if i % x != 0:
            return False
    return True
    
def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b)+1):
        if(checkA(a, i) and checkB(b, i)):
            count += 1
        print(i)
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
