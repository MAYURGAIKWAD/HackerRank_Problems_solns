#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def diffchar(s):
    d={}
    l=[]
    for i in s:
        if i not in d:
            d[i]=1
            l.append(i)
    return l

def adjacent(a,b,s):
    found=0
    ans=0
    next_=""
    prev_=""
    for i in s:
        if found==0:
            if i==a:
                next_=b
                prev_=a
                ans+=1
                found=1
            elif i==b:
                next_ =a
                prev_=b
                ans+=1
                found=1
        else:
            if i ==prev_:
                return 0
            elif i==next_:
                ans+=1
                prev_,next_ = next_, prev_
            else:
                continue
    return ans
                
                
            
    
    
def alternate(s):
    # Write your code here
    c=diffchar(s)
    count=0
    print(c)
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            count=max(count,adjacent(c[i],c[j],s))
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
