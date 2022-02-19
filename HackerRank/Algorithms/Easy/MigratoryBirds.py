#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
class Bird:
	def __init__(self, obj):
		self.type = obj
	def __eq__(self, other):
		return other.type == self.type
	def __lt__(self, other):
		return other.type < self.type

def migratoryBirds(arr):
    # Write your code here

	BirdTypes = list(set(arr))
#	compareResult = sorted(BirdTypes,key=lambda bird:(arr.count(bird), -bird))
	compareResult = sorted(BirdTypes,key=lambda bird:(arr.count(bird), Bird(bird)))
	return compareResult[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
