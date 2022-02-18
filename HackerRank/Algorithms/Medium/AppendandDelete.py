#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    sLength = len(s)
    tLength = len(t)
    minLength = min(sLength, tLength)
    sameLength = 0
    for i in range(minLength):
        if s[i] != t[i]:
            break
        sameLength += 1

    diff = (sLength-sameLength)+(tLength-sameLength)
    print(diff)
    if diff > k:
        return 'No'
    elif sLength+ tLength <= k:
        return 'Yes'
    elif (abs(diff - k))%2 == 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
