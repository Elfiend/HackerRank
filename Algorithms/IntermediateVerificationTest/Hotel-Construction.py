#!/bin/python3

import math
import os
import random
import re
import sys

#from itertools import product

#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY roads as parameter.
#

def countCityDistance(city, roadMapping, distance, count):
    distance[city] = count
    for nextCity in roadMapping[city] :
        if not (nextCity in distance):
            countCityDistance(nextCity, roadMapping, distance, count+1)
    return distance

def generateCityDistance(roadMapping, cityList):
    distance = {}
    for city in cityList:
        distance[city] = countCityDistance(city, roadMapping, {}, 0)
    return distance

def generateRoadMap(roads):
    roadMapping = {}
    cityList = []
    for startCity, endCity in roads:
        print(startCity, endCity)
        if not (startCity in roadMapping) :
            roadMapping[startCity] =[endCity]
        else:
            roadMapping[startCity].append(endCity)
        if not (endCity in roadMapping) :
            roadMapping[endCity] =[startCity]
        else:
            roadMapping[endCity].append(startCity)
        if not (startCity in cityList):
            cityList.append(startCity)
        if not (endCity in cityList):
            cityList.append(endCity)
    
    cityList.sort()
    return roadMapping, cityList


def numberOfWays(roads):
    roadMapping, cityList = generateRoadMap(roads)
    distance = generateCityDistance(roadMapping, cityList)
    citySize = len(cityList)
    minCount = 0
    for i in range(citySize - 2):
        for j in range(i + 1, citySize - 1):
            for k in range(j + 1, citySize):
                firstCity = cityList[i]
                sencondCity = cityList[j]
                thirdCity = cityList[k]
                if distance[firstCity][sencondCity] != distance[sencondCity][thirdCity]:
                    continue
                if distance[firstCity][thirdCity] != distance[thirdCity][sencondCity]:
                    continue
                minCount += 1
    print(minCount)
    return minCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    roads_rows = int(input().strip())
    roads_columns = int(input().strip())

    roads = []

    for _ in range(roads_rows):
        roads.append(list(map(int, input().rstrip().split())))

    result = numberOfWays(roads)

    fptr.write(str(result) + '\n')

    fptr.close()