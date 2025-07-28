#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    freq = {}

    for bird in arr:
        if bird in freq:
            freq[bird]+=1
        else:
            freq[bird]=1
    max_count = 0
    bird_type = None

    for bird_id in sorted(freq.keys()): 
        if freq[bird_id]>max_count:
            max_count=freq[bird_id]
            bird_type=bird_id

    return bird_type

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
