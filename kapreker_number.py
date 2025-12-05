#!/bin/python3

import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    kaprekars = []

    for n in range(p, q + 1):
        sq = str(n * n)
        d = len(str(n))

        right = int(sq[-d:]) if len(sq) >= d else 0
        left = int(sq[:-d]) if len(sq) > d else 0

        if left + right == n:
            kaprekars.append(n)

    if kaprekars:
        print(*kaprekars)
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
