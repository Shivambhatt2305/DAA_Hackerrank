#!/bin/python3

import math
import os
import random
import re
import sys

def happyLadybugs(b):
    from collections import Counter

    counts = Counter(b)

    # If no empty spaces, must already be happy
    if "_" not in counts:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i-1]) or (i < len(b)-1 and b[i] == b[i+1]):
                continue
            else:
                return "NO"
        return "YES"

    # If empty spaces exist, ensure every color appears at least twice
    for color, freq in counts.items():
        if color != "_" and freq == 1:
            return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        fptr.write(result + '\n')

    fptr.close()
