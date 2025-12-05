#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    freq = [0] * 100

    for num in arr:
        freq[num] += 1

    result = []
    for value, count in enumerate(freq):
        result.extend([value] * count)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
