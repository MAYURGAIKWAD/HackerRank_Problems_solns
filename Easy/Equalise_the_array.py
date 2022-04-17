#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    c=Counter(arr)
    # print(c)
    a=c.most_common(1)
    # print(a)
    # print(a[0][0], a[0][1])
    return (len(arr) - a[0][1])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
