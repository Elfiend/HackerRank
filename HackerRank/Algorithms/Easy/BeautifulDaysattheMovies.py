#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def isBeautiful(day, k):
    rday = int(str(day)[::-1])
    diff = abs(day - rday)
    return diff % k == 0


def beautifulDays(i, j, k):
    # Write your code here
    assert 1 <= i <= 2e6, f"i={i} is out of range."
    assert 1 <= j <= 2e6, f"j={j} is out of range."
    assert 1 <= k <= 2e9, f"k={k} is out of range."

    result = 0
    for day in range(i, j+1):
        if isBeautiful(day, k):
            result += 1

    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
