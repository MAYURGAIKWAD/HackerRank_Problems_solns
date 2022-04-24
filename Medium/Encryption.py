#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def removeSpaces(s):
    temp=""
    for i in s:
        if i==" ":
            continue
        else:
            temp+=i
    return temp

def encryption(s):
    # Write your code here
    L=removeSpaces(s)
    # print(L)
    l=len(L)
    m=0
    n=0
    if math.ceil(math.sqrt(l))*math.floor(math.sqrt(l))>=l:
        m=math.floor(math.sqrt(l))
        n=math.ceil(math.sqrt(l))
    else:
        m=math.ceil(math.sqrt(l))
        n=math.ceil(math.sqrt(l))
    grid=[[0 for i in range(n)] for i in range(m)]
    # print(grid)
    # print("m,n are: ", m,n)
    for i in range(m):
        for j in range(n):
            if i*n+j >= l:
                break
            # print(i*n+j)
            grid[i][j]=s[i*n+j]
    # print (grid)
    ans=""
    for i in range(n):
        for j in range(m):
            if grid[j][i]!=0:
                ans+= grid[j][i]
            if j==m-1 and i!=n:
                ans+=" "
    # print(ans)
    return ans
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
