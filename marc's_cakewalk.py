#!/bin/python3

import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    total = 0

    for i, c in enumerate(calorie):
        total += (2 ** i) * c

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')
    fptr.close()
