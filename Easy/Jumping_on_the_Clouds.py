#!/bin/python3

import math
import os
import random
import re
import sys


def hopping(c,k,i,e):
    if i==0 and e!=100:
        #end reached and not start
        return e
    elif c[i]==0:
        #cumulus cloud
        # print("CUMULUS")
        return hopping(c,k,(i+k)%n,e-1)
    elif c[i]==1:
        #Thunderous cloud
        # print("thunderous")
        return hopping(c,k,(i+k)%n,e-3)
        
    # else:
        # print("HEHEHE.... YOU MISSED SOMETHING!...")
    
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    ans=hopping(c,k,0,e)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
