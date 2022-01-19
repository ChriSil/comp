#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#


def bitwiseAnd(N, K):  # works but too slow, given nested loop
    maxi = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            xn = i & j
            #print(i, j)
            if K > xn > maxi:
                maxi = xn
    return maxi


def bitwiseAndf(n, k):  # fast solution, not fully comprehend yet
    return(k-1 if ((k-1) | k) <= n else k-2)

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAndf(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
