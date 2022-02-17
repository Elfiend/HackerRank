#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMin(s):
    # Write your code here
    brackets = [" "]
    for i in range(len(s)):
        if s[i] == '(':
            brackets.append('(')
        elif s[i] == ')':
            if brackets[-1] == '(':
                brackets.pop()
            else:
                brackets.append(')')

    return len(brackets)-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMin(s)

    fptr.write(str(result) + '\n')

    fptr.close()
