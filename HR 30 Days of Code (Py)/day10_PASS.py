#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    num = int(input().strip())

# def binToDec(val):  # does not work. int does not convert, is just states which base it is. val that you input does not denote its OG base, therefore you can't do a conversion like that.
#    return int(val, 2)
#num = int(input())
# Every odd values, Increment 1
result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0
    num //= 2
print(maximum)
