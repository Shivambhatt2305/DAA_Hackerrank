#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period=s[-2:]
    hour=int(s[0:2])
    rest=s[2:-2]
    if period=='PM':
        if hour!=12:
            hour+=12
    else:
        if hour==12:
            hour=0
    return f"{hour:02d}{rest}"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
