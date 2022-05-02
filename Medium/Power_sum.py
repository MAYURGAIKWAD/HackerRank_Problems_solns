#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def count(x,arr,visited,curr):
    if x==0:
        temp2=("".join(str(x) for x in sorted(curr)))
        if temp2 in visited.keys():
            return 0
        else:
            visited[temp2]=1 
            return 1
    if x<0:
        return 0
    if (len(arr)==0 and x>0):
        return 0
    temp=0
    for i in arr.keys():
        temp1=arr.copy()
        del temp1[i]
        curr.append(i)
        temp+=count(x-arr[i],temp1,visited,curr)
        curr.pop()
    return temp


def powerSum(total, power, num):
    
    value=total-pow(num,power)
    if value<0:
        return 0
    elif value==0:
        return 1 
    else: 
        return powerSum(value , power, num + 1) +powerSum(total,power, num+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N,1)

    fptr.write(str(result) + '\n')

    fptr.close()
