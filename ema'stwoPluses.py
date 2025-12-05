#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])

    G = [[cell == 'G' for cell in row] for row in grid]

    def plus_cells(r, c, size):
        cells = {(r, c)}
        for d in range(1, size + 1):
            cells.add((r + d, c))
            cells.add((r - d, c))
            cells.add((r, c + d))
            cells.add((r, c - d))
        return cells

    pluses = []

    for r in range(n):
        for c in range(m):
            if not G[r][c]:
                continue

            size = 0
            while True:
                if (r - size < 0 or r + size >= n or
                    c - size < 0 or c + size >= m):
                    break

                if (not G[r - size][c] or not G[r + size][c] or
                    not G[r][c - size] or not G[r][c + size]):
                    break

                cells = plus_cells(r, c, size)
                area = 4 * size + 1
                pluses.append((area, cells))

                size += 1

    pluses.sort(reverse=True, key=lambda x: x[0])

    max_product = 0
    for i in range(len(pluses)):
        area1, c1 = pluses[i]
        if area1 * area1 < max_product:
            break
        for j in range(i + 1, len(pluses)):
            area2, c2 = pluses[j]
            if area1 * area2 < max_product:
                break
            if c1.isdisjoint(c2):
                max_product = area1 * area2
                break

    return max_product


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    grid = []
    for _ in range(n):
        grid.append(input())

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
