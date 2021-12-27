#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())


if 1 <= N <= 100:
    pass

if N % 2 == 1:  # %2 >0 seems more elegant
    print('Weird')
elif 2 <= N <= 5:
    print('Not Weird')
elif 6 <= N <= 20:
    print('Weird')
elif N > 20:
    print('Not Weird')

'''

/#!/bin/python3

#Better Solution found online: 
#elif covers two cases: 
#Else covers all the others, as opposed to defining elif states

import sys
N = int(input().strip())

# If nn is odd, print WeirdWeird.
if N % 2 > 0:
    print("Weird")
elif N % 2 == 0 and (6 <= N <= 20):
    print("Weird")
else:
    print("Not Weird")

'''
