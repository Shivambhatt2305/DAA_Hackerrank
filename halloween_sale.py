#!/bin/python3

import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    count = 0
    price = p
    total = 0

    # Buy games while price >= m and total cost fits
    while total + price <= s:
        total += price
        count += 1
        price = max(price - d, m)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
