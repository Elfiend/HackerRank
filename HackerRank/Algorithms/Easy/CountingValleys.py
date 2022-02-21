#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
	seaLevel = 0
	nowLevel = 0
	mountainCount = 0
	valleyCount = 0
	for direction in path:
		if direction == 'U':
			if nowLevel == seaLevel:
				mountainCount += 1
			nowLevel +=1
		elif direction == 'D':
			if nowLevel == seaLevel:
				valleyCount += 1
			nowLevel -=1
	print(mountainCount, valleyCount)
	return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
