#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    rem=s
    for i in range(len(s)):
        rem[i]=s[i]%k
    # print(rem)
    count=Counter(rem)
    # print(count)
    x=sorted(count, key=count.get, reverse=True)
    ld={}
    rd={}
    
    if k%2!=0:
        taken=0
        for i in x:
            print(i)
            if i==0 and taken==0:
                ld[0]=1
                rd[0]=1
                taken=1
            elif ((k-i) not in ld.keys()) and i!=0:
                ld[i]=count[i]
            elif ((k-i) in ld.keys()) and i!=0:
                rd[i]=count[i]
            elif i==0 and taken==1:
                continue
            else:
                print("something is missing")
    else:
        taken=0
        taken1=0
        for i in x:
            if i==0 and taken==0:
                ld[0]=1
                rd[0]=1
                taken=1
            elif ((k-i) not in ld.keys()) and i!=0 and i!=k//2:
                ld[i]=count[i]
            elif ((k-i) in ld.keys()) and i!=0 and i!=k//2:
                rd[i]=count[i]
            elif i==k//2 and taken1 ==0:
                ld[i]=1
                rd[i]=1
                taken1=1
            elif i==0 and taken==1:
                continue
            elif i==k//2 and taken1 ==1:
                continue
            else:
                print("something is missing")    
    print(ld,rd)
    return max(sum(ld.values()), sum(rd.values()))

                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
