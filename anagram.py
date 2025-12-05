#!/bin/python3

import math
import os
import random
import re
import sys

def anagram(s):
    n = len(s)
    if n % 2 == 1:
        return -1

    half = n // 2
    left = s[:half]
    right = s[half:]

    from collections import Counter
    count_left = Counter(left)
    count_right = Counter(right)

    changes = 0

    for ch in count_left:
        if count_left[ch] > count_right[ch]:
            changes += count_left[ch] - count_right[ch]

    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()
