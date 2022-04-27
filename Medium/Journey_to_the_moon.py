#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
def createAdjacencylist(n,arr):
    d={}
    for i in range(n):
        d[i]=[]
    for i in range(len(arr)):
        if arr[i][1] not in d[arr[i][0]]:
            d[arr[i][0]].append(arr[i][1])
        if arr[i][0] not in d[arr[i][1]]:
            d[arr[i][1]].append(arr[i][0])
    return d

def findclusters(d):
    stack=[]
    visited={}
    count=0
    ans=[]
    
    for i in d.keys():
        stack.append(i)
        while len(stack)>0:
            curr=stack.pop()
            if curr in visited.keys():
                continue
            visited[curr]=1
            count+=1
            if len(d[curr])>0:
                for _ in d[curr]:
                    stack.append(_)
            # print(stack)
        ans.append(count)
        count=0
    return ans
    
def journeyToMoon(n, astronaut):
    # Write your code here
    d=createAdjacencylist(n,astronaut)
    # print(d)
    country=findclusters(d)
    # print("countries: ", country)
    sum1=0
    for i in range(len(country)):
        sum1+=country[i]*(n-country[i])
    return int(sum1/2) #dividing by 2 due to double counting
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
