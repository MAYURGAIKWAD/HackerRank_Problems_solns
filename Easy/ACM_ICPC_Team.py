#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#
def str_or(arr1,arr2):
    temp=0
    for i in range(len(arr1)):
        if arr1[i] =="0" and arr2[i] == "0":
            temp+=0
        else:
            temp+=1
    # print ("Str_or results: ", arr1, arr2, temp)
    return temp
        
def known(arr):
    count=0
    for i in arr:
        if i=="1":
            count+=1
    return count
        
def acmTeam(topic):
    n=len(topic)
    m=len(topic[0])
    max_or=0
    n_teams=0
    for i in range(n):
        for j in range(i+1,n):
            temp_or=str_or(topic[i],topic[j])
            if temp_or> max_or:
                max_or=temp_or
                n_teams=1
            elif temp_or== max_or:
                n_teams+=1
    return [max_or,n_teams]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
