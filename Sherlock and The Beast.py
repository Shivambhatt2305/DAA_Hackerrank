#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    fives = n

    while fives % 3 != 0:
        fives -= 5

    if fives < 0:
        print(-1)
    else:
        threes = n - fives
        print("5" * fives + "3" * threes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)
