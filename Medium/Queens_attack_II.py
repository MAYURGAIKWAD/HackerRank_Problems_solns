#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    stack=[]
    #dfs
    visited={}
    stack.append([r_q,c_q])
    visited[r_q]=[c_q]
    obs={}
    count=0
    for i,j in obstacles:
        if i not in obs.keys():
            obs[i]=[j]
        else:
            obs[i].append(j)
    print(obs)
    direction=1
    while(len(stack)>0):
        r,c=stack.pop()
        if (r<=0 or r>n) or (c<=0 or c>n):
            #row out of bounds
            stack.append([r_q,c_q])
            direction+=1
            continue
        if r in visited.keys() and c in visited[r] and (r !=r_q and c!=c_q):
            #already visited
            continue
        if r not in visited.keys() and (r !=r_q and c!=c_q) :
            visited[r]=[c]
        elif r in visited.keys() and (r !=r_q and c!=c_q):
            visited[r].append(c)
        if r in obs.keys() and c in obs[r]:
            #its and obstacle dont travel further
            stack.append([r_q,c_q])
            direction+=1
            continue
        if not (r == r_q and c==c_q):
            count+=1
        if direction==1:
            stack.append([r+1,c])
        elif direction==2:
            stack.append([r+1,c-1])
        elif direction==3:
            stack.append([r,c-1])
        elif direction==4:
            stack.append([r-1,c-1])
        elif direction==5:
            stack.append([r-1,c])
        elif direction==6:
            stack.append([r-1,c+1])
        elif direction==7:
            stack.append([r,c+1])
        elif direction==8:
            stack.append([r+1,c+1])
    return count
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
