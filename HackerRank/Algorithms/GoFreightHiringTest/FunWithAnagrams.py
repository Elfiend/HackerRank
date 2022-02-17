#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#

def funWithAnagrams(text):
    # Write your code here
    wordArray = []
    result = []
    for word in text:
        anagrams = ''.join(sorted(word))
        if not (anagrams in wordArray):
            wordArray.append(anagrams)
            result.append(word)
    return sorted(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
