#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    colorUnpair = []
    for i in range(n):
        color = ar[i]
        if color not in colorUnpair:
            colorUnpair.append(color)
        else:
            colorUnpair.remove(color)
    print(colorUnpair)
    return (n - len(colorUnpair))//2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
