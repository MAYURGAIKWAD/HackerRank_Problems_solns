#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    e=arr[-1]
    if n==1:
        print(str(arr[0]))
    found=0
    for i in range(n-2,-1,-1):
        # print(i)
        if e>=arr[i]:
            arr[i+1]=e
            print(" ".join(str(x) for x in arr))
            found=1
            break
        else:
            arr[i+1]=arr[i]
            print(" ".join(str(x) for x in arr))
    if not found:
        arr[0]=e
        print(" ".join(str(x) for x in arr))

            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
