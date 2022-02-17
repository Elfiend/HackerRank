import math
import os
import random
import re
import sys
from collections import defaultdict


def longestSubarray(arr):
    # Write your code here
    result = []
    for i in range(len(arr)):
        num = arr[i]
        longest = 1
        numlist = set()
        numlist.add(num)
        for j in range(i+1, len(arr)):
            if abs(num - arr[j]) > 1:
                break
            numlist.add(arr[j])
            if len(numlist) > 2:
                break
            longest += 1
        result.append(longest)
    print(result)
    return max(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()