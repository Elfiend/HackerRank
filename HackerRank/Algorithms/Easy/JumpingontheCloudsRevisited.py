#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
	index = 0
	energy = 100
	while True:
		index += k
		energy -= 1

		print(index)
		index = index % len(c)
		print("%",index)
		if c[index] > 0:
			energy -= 2
		if index == 0:
			break
		elif energy <= 0:
			break

	return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
