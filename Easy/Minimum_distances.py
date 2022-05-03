#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    d={}
    for i in range(len(a)):
        if a[i] not in d.keys():
            d[a[i]]=[i]
        else:
            d[a[i]].append(i)
    # print(d)
    count=len(a)+1
    for i in d.keys():
        if len(d[i])<2:
            continue
        else:
            prev=-2
            for j in d[i]:
                if prev==-2:
                    prev=j
                    continue
                count=min(count,j-prev)
                prev=j
    if count== len(a)+1:
        return -1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
