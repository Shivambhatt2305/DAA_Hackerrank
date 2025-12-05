#!/bin/python3

import math
import os
import random
import re
import sys

def gridChallenge(grid):
    sorted_grid = [''.join(sorted(row)) for row in grid]

    n = len(sorted_grid)
    for c in range(len(sorted_grid[0])):
        for r in range(1, n):
            if sorted_grid[r][c] < sorted_grid[r - 1][c]:
                return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        fptr.write(result + '\n')

    fptr.close()
