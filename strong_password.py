#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    required = 0

    has_digit = any(c.isdigit() for c in password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in "!@#$%^&*()-+" for c in password)

    if not has_digit:
        required += 1
    if not has_lower:
        required += 1
    if not has_upper:
        required += 1
    if not has_special:
        required += 1

    return max(required, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')
    fptr.close()
