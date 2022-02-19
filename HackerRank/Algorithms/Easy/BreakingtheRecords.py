#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
	minData = [ sys.maxsize, -1]
	maxData = [ -sys.maxsize-1, -1]

	for score in scores:
		if score > maxData[0]:
			maxData[0] = score
			maxData[1] += 1
		if score < minData[0]:
			minData[0] = score
			minData[1] += 1

	print(maxData, minData)
	return (maxData[1],minData[1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
