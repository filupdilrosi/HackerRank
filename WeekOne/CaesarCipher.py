import math
import os
import random
import re
import sys
import sys
import string
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
        else:
            res.append(c)
                       
    return "".join(map(str, res))
