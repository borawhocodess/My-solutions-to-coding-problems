import math
import os
import random
import re
import sys

def plusMinus(arr):
    out = [0, 0 , 0]
    for i in arr:
        if i > 0:
            out[0] += 1
        elif i < 0:
            out[1] += 1
        else:
            out[2] += 1
    
    for i in out:
        print("{:.6f}".format(i/len(arr)))

        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
