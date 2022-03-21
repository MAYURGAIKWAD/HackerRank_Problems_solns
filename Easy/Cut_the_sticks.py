#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    ans=[]
    while(True):
        ans.append(len(arr))
        if max(arr)==min(arr):
            break
        temp=[]
        for i in range(len(arr)):
            if arr[i]-min(arr)==0:
                continue
            temp.append(arr[i]-min(arr))
        arr=temp
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
