#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    n = len(s)
    
    for length in range(1, n // 2 + 1):
        first = int(s[:length])
        next_num = first
        built = ""
        
        while len(built) < n:
            built += str(next_num)
            next_num += 1
        
        if built == s:
            print("YES", first)
            return
    
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        separateNumbers(s)
