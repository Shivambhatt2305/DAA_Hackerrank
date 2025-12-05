#!/bin/python3

import math
import os
import random
import re
import sys

def is_pal(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if is_pal(s, left + 1, right):
                return left
            if is_pal(s, left, right - 1):
                return right
        left += 1
        right -= 1

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')

    fptr.close()
