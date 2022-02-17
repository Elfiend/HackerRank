#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_right

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def removeDuplicate(itemsList):
	isExist = set()
	result = []
	for item in itemsList:
		key = int(item)
		if key not in isExist:
			result.append(item)
			isExist.add(key)
	
	return sorted(result)

def climbingLeaderboard(ranked, player):
    # Write your code here
	rankResult = []
	rankedScoreList = removeDuplicate(ranked)

	totalRanked = len(rankedScoreList)
	for i in player:
		biPos = bisect_right(rankedScoreList,i)
		rankResult.append(totalRanked - biPos +1)

	print(rankResult)
	return rankResult

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
