#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getSubstringCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getSubstringCount(s):
    # Write your code here
    previousCount = 0
    CurrentCounter = 1 
    result = 0

    for i in range(1, len(s)):
        if s[i-1] ==s[i]:
            CurrentCounter += 1
        else:
            result += min(previousCount,CurrentCounter)
            previousCount = CurrentCounter   
                
            CurrentCounter = 1
    result += min(previousCount,CurrentCounter)

    print(result)
    return result              



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getSubstringCount(s)

    fptr.write(str(result) + '\n')

    fptr.close()
