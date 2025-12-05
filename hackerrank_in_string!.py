#!/bin/python3

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    target = "hackerrank"
    i = 0

    for ch in s:
        if ch == target[i]:
            i += 1
            if i == len(target):
                return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        fptr.write(result + '\n')

    fptr.close()
