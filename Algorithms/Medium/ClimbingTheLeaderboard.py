#!/bin/python3

import math
import os
import random
import re
import sys

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
	return result

def climbingLeaderboard(ranked, player):
    # Write your code here
	rankResult = []
	rankedScoreList = removeDuplicate(ranked)
	searchIndex = len(rankedScoreList)
	for p in player:
		for i in range(searchIndex-1, -1 , -1):
			if p < rankedScoreList[i]:
				rankResult.append(i+2)
				searchIndex = i+1
				break
		if p > rankedScoreList[i]:
			rankResult.append(i+1)
			searchIndex = i+1

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
