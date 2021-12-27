#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

for i in range(1, len(arr)+1):
    # end='' makes it so the print statement ends with a space, not a new line. Thus the loop continues to print in the same line, delimited by a space
    print(arr[-i], end='')
