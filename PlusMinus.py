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
    even=0
    odd=0
    zeros=0
    for parts in arr:
        if parts > 0:
            even+=1
        if parts == 0:
            zeros+=1
        if parts <0:
            odd+=1
    ERatio = even/len(arr)
    ORatio = odd/len(arr)
    ZRatio = zeros/len(arr)
    
    print(f"{'{:.6f}'.format(ERatio)}\n {ORatio}\n {ZRatio}")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
