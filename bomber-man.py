#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    grid = [list(row) for row in grid]

    if n == 1:
        return ["".join(row) for row in grid]

    if n % 2 == 0:
        return ["O" * c for _ in range(r)]

    def explode(current):
        result = [["O"] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if current[i][j] == 'O':
                    result[i][j] = '.'
                    if i > 0: result[i-1][j] = '.'
                    if i < r-1: result[i+1][j] = '.'
                    if j > 0: result[i][j-1] = '.'
                    if j < c-1: result[i][j+1] = '.'
        return result

    first = explode(grid)
    second = explode(first)

    if n % 4 == 3:
        ans = first
    else:
        ans = second

    return ["".join(row) for row in ans]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    grid = []
    for _ in range(r):
        grid.append(input())

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
