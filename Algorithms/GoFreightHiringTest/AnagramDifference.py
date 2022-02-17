#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#
def getAnagramDiff(firstWord, secondWord):

    firstAnagrams = ''.join(sorted(firstWord))
    secondAnagrams = ''.join(sorted(secondWord))
    if firstAnagrams == secondAnagrams:
        return 0

    diff = 0
    firstWordDict = {}
    secondWordDict = {}
    for ch in firstAnagrams:
        if ch in firstWordDict:
            firstWordDict[ch] += 1
        else:
            firstWordDict[ch] = 1
    for ch in secondAnagrams:
        if ch in secondWordDict:
            secondWordDict[ch] += 1
        else:
            secondWordDict[ch] = 1

    for ch in firstWordDict.keys():
        if not(ch in secondWordDict):
            diff += firstWordDict[ch]
        elif firstWordDict[ch] > secondWordDict[ch]:
            diff += firstWordDict[ch] - secondWordDict[ch]
			
    return diff


def getMinimumDifference(a, b):
    # Write your code here

    result = []
    for firstWord, secondWord in zip(a, b):
        if len(firstWord) != len(secondWord):
            result.append(-1)
            continue
        result.append(getAnagramDiff(firstWord, secondWord))

    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = getMinimumDifference(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
