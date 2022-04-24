#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
def l2str(s,a):
    temp=""
    temp1=""
    for i in range(len(s)):
        # print (i, len(s))
        if s[i]>a:
            temp1=s.pop(i)
            break
    temp+=temp1
    for i in s:
        temp+=i
    return temp
def biggerIsGreater(w):
    # Write your code here
    ans=""
    # a="zedfr"
    # print(sorted(a))
    for i in range(len(w)-1,0,-1):
        print(i)
        if ord(w[i])>ord(w[i-1]) and i!= len(w)-1 and i!=1:
            ans=w[:i-1]+l2str(sorted(w[i-1:]),w[i-1])
            return ans
        elif ord(w[i])>ord(w[i-1]) and i!= len(w)-1 and i==1:
            ans=l2str(sorted(w[i-1:]),w[i-1])
            return ans
        elif ord(w[i])>ord(w[i-1]) and i== len(w)-1:
            ans=w[:i-1]+w[i]+w[i-1]
            return ans
    return "no answer"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
