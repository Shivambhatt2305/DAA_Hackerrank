#!/bin/python3

import math
import os
import random
import re
import sys

def balancedSums(arr):
    total = sum(arr)
    left_sum = 0

    for x in arr:
        if left_sum == total - left_sum - x:
            return "YES"
        left_sum += x

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + '\n')

    fptr.close()
