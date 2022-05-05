#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    len_val=0
    num_val=0
    lc_val=0
    uc_val=0
    sc_val=0 
    if n>=6:
        len_val=1
    for i in range(n):
        if password[i] in numbers:
            num_val=1
        elif password[i] in lower_case:
            lc_val=1
        elif password[i] in upper_case:
            uc_val=1
        elif password[i] in special_characters:
            sc_val=1
    temp=(1-num_val)+(1-lc_val)+(1-uc_val)+(1-sc_val)
    return ((max(6-(n+temp),0)+temp))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
