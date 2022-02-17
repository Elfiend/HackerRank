#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#

def countPairs(numbers, k):
    # Write your code here
	firstNumber = set()
	secondNumber = set()
	result = 0
	for num in numbers:
		firstNumber.add(num)
		secondNumber.add(num+k)
	for num in secondNumber:
		if num in firstNumber:
			result +=1
	
	print(result)
	return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    result = countPairs(numbers, k)

    fptr.write(str(result) + '\n')

    fptr.close()
