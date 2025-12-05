#!/bin/python3

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    min_diff = float('inf')

    # Find minimum difference
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    # Collect pairs
    result = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == min_diff:
            result.extend([arr[i], arr[i+1]])

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
