#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def getFebDays(year):
	if year == 1918:
		return 15
	elif year < 1917 and year % 4 == 0:
		return 29
	elif year % 400 == 0 :
		return 29
	elif year % 4 == 0 and year % 100 != 0:
		return 29
	return 28

def dayOfProgrammer(year):
    # Write your code here
	febDay = getFebDays(year)
	print(febDay)
	return f'{41 - febDay}.09.{year}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
