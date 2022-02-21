#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.


def catAndMouse(x, y, z):
    assert 1 <= x <= 1e2, f"x={x} is out of range."
    assert 1 <= y <= 1e2, f"y={y} is out of range."
    assert 1 <= z <= 1e2, f"z={z} is out of range."

    aDistance = abs(x-z)
    bDistance = abs(y-z)
    if aDistance < bDistance:
        return "Cat A"
    elif aDistance > bDistance:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
