#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
import fileinput


def countCost(inputSquare, posibleSquare):
    cost = 0
    for i in range(len(inputSquare)):
        cost = cost + abs(inputSquare[i] - posibleSquare[i])
    return cost


def formingMagicSquare(s):
    # Write your code here
    posibleSquareList = [
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
    ]
    inputSquare = list(itertools.chain(*s))
    costList = []
    for posibleSquare in posibleSquareList:
        costList.append(countCost(inputSquare, posibleSquare))
    print(costList)
    return min(costList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
