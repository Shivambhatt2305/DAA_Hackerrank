#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s = s.replace(" ", "")
    L = len(s)

    rows = int(math.floor(math.sqrt(L)))
    cols = int(math.ceil(math.sqrt(L)))

    if rows * cols < L:
        rows += 1

    result = []
    for c in range(cols):
        word = ""
        for r in range(rows):
            idx = r * cols + c
            if idx < L:
                word += s[idx]
        result.append(word)

    return " ".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
