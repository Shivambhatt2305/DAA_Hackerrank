#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_plus=0
    count_minus=0
    count_zero=0
    for i in range(len(arr)):
        if arr[i]<0:
            count_minus=count_minus+1
        elif arr[i]>0:
            count_plus=count_plus+1
        else:
            count_zero=count_zero+1
    print(count_plus/len(arr))
    print(count_minus/len(arr))
    print(count_zero/len(arr))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
