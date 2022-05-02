#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sillyGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def isPrime(n,prim):
    if n==1:
        return False
    for i in prim:
        if n%i==0:
            return False
        if i>int(math.sqrt(n)):
            break
    return True
def sillyGame(n,prim):
    # Write your code here.
    count=0
    for i in prim:
        if i<=n:
            count+=1
            
    if ( (count)%2==0):
        return("Bob")
    else:
        return("Alice")
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())
    
    temp=[]
    for i in range(1,100000+1):
        if isPrime(i,temp):
            temp.append(i)
    #temp is the array containing all the prime elements till max_n
    
    for g_itr in range(g):
        n = int(input().strip())

        result = sillyGame(n,temp)

        fptr.write(result + '\n')

    fptr.close()
