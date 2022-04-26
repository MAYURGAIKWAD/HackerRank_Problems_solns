#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    #
    x1=sorted(x)
    print(x1)
    count=0
    i=0
    n=len(x1)
    while i<n:
        temp=x1[i]+k
        while i<n and x1[i]<= temp:
            i=i+1
        i=i-1 #place the transmitter here
        temp1=x1[i]+k
        while i<n and x1[i]<=temp1:
            i=i+1
        count+=1
    return count

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
