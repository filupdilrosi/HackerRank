#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    a = max(arr)
    arr.remove(a)
    b = sum(arr)
    arr.insert(1, a)
    x = min(arr)
    arr.remove(x)
    y = sum(arr)
    print(f"{b} {y}")
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
