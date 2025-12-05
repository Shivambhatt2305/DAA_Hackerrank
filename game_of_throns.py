#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    from collections import Counter
    freq = Counter(s)

    odd_count = sum(1 for c in freq if freq[c] % 2 == 1)

    return "NO" if odd_count > 1 else "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')
    fptr.close()
