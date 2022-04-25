#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def isKaprekar(i):
    D=(str(i))
    K=str(i*i)
    k=len(K)
    d=len(D)
    # print("Check:  ",i,K[:0])
    if(i==1):
        return True
    # print(i,K, int(K[k-d:],base=10), int(K[:k-d], base=10))
    if K[:k-d]=="":
        return False
    if (int(K[k-d:],base=10)+int(K[:k-d], base=10))==i:
        return True
    else:
        return False
    

def kaprekarNumbers(p, q):
    # Write your code here
    ans=[]
    for i in range(p,q+1):
        if isKaprekar(i):
            ans.append(i)
    # print("Kaprekar numbers are: ", ans)
    if len(ans)==0:
        print("INVALID RANGE")
    else:
        print (" ".join(str(x) for x in ans))

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
