#!/bin/python3

import math
import os
import random
import re
import sys

def strangeCounter(t):
    cycle_start = 3

    # Move through cycles until we reach the correct one
    while t > cycle_start:
        t -= cycle_start
        cycle_start *= 2

    return cycle_start - t + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    result = strangeCounter(t)

    fptr.write(str(result) + '\n')
    fptr.close()
