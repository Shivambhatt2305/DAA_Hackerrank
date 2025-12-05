#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    letters = set()

    for ch in s.lower():
        if 'a' <= ch <= 'z':
            letters.add(ch)

    return "pangram" if len(letters) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = pangrams(s)

    fptr.write(result + '\n')
    fptr.close()
