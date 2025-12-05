#!/bin/python3

import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    ops = 0
    left = 0
    right = len(s) - 1

    while left < right:
        ops += abs(ord(s[left]) - ord(s[right]))
        left += 1
        right -= 1

    return ops

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')

    fptr.close()
