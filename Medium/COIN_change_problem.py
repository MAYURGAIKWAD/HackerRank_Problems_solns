#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    m=len(c)
    c=sorted(c) 
    # print(c)
    mat=[[0 for i in range(n+1)] for j in range(m)]
    for i in range(m):
        mat[i][0]=1 # 1 way to make 0 using all coins
    for i in range(1,n+1):
        if i%c[0]==0:
            mat[0][i]=1
    # print (mat)
    for i in range(1,m):
        for j in range(n+1):
            if j<c[i]:
                mat[i][j]=mat[i-1][j]
            else:
                mat[i][j]=mat[i-1][j]+mat[i][j-c[i]]  
    # print(mat)
    return mat[m-1][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
