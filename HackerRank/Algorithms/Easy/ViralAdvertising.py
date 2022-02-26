#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    # Write your code here
    assert 1 <= n <= 50, f"n={n} is out of range."

    cumulative = 0
    gotAd = 5
    for i in range(n):
        gotAd //= 2
        cumulative += gotAd
        print(gotAd, cumulative)
        gotAd *= 3

    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
