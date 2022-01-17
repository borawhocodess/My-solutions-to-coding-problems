#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    if s[-2] == "P":
        if int(s[0:2]) != 12:
            s = str(12+int(s[0:2])) + s[2:]
    else:
        if int(s[0:2]) == 12:
            s = "00" + s[2:]
    
    return s[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
