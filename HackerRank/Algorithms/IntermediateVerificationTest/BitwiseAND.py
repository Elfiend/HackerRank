#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def isAndTwoPower(a, b):
    andNum = a & b
    if andNum == 0:
        return False
    # 2^n = 1000...000
    return (andNum & (andNum-1)) == 0


def countPairs(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if isAndTwoPower(arr[i], arr[j]):
                count += 1
    print(count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
