#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    n = len(arr)
    i = 0
    count = 0

    while i < n:
        placed = False
        start = min(n - 1, i + k - 1)
        end = max(0, i - k + 1)

        # Try to place the tower as far right as possible
        for pos in range(start, end - 1, -1):
            if arr[pos] == 1:
                count += 1
                i = pos + k
                placed = True
                break

        if not placed:
            return -1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
