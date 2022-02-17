import math
import os
import random
import re
import sys

from collections import defaultdict


def minOperations(arr, threshold, d):
    # Write your code here
    print(arr, threshold, d)

    desiredNumberStep = defaultdict(lambda: [0, 0])
    minStep = sys.maxsize
    for num in arr:
        divisionTimes = int(num/d)+2
        for step in range(divisionTimes):
            desiredNumberStep[num][0] += 1
            desiredNumberStep[num][1] += step
            if desiredNumberStep[num][0] >= threshold:
                minStep = min(minStep, desiredNumberStep[num][1])
            num //=d
    return minStep


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    threshold = int(input().strip())

    d = int(input().strip())

    result = minOperations(arr, threshold, d)

    fptr.write(str(result) + '\n')

    fptr.close()
