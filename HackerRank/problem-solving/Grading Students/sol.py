#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    rounded = []
    
    for i in grades:
        if i >= 38:
            if i % 10 == 8 or i % 10 == 3:
                i += 2
            elif i % 10 == 9 or i % 10 == 4:
                i += 1
        
        rounded.append(i)
    
    return rounded
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
