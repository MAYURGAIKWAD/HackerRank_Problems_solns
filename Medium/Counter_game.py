#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    count=0
    while n>1:
        if math.log2(n)==int(math.log2(n)):
            #power of 2
            n=n/2
            count+=1
            continue
        else:
            n=n-math.pow(2,int(math.log2(n)))
            count+=1
            continue
    if count%2==0:
        return "Richard"
    else:
        return "Louise"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

   
