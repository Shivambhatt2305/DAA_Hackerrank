#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    k = k % 26
    result = []

    for ch in s:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            rotated = chr(base + (ord(ch) - base + k) % 26)
            result.append(rotated)
        else:
            result.append(ch)

    return "".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    s = input()
    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')
    fptr.close()
