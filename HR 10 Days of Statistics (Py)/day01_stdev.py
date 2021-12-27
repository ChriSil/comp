#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):
    sd = 0
    mean = 0
    mean = statistics.mean(arr)
    data = [(val-mean)**2 for val in arr]
    return (sum(data)/float(len(data)))**0.5
    # Print your answers to 1 decimal place within this function


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))
    print(stdDev(vals))
