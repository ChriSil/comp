#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nten = int(input().strip())

# def binToDec(val):  # does not work. int does not convert, is just states which base it is. val that you input does not denote its OG base, therefore you can't do a conversion like that.
#    return int(val, 2)


def decimalToBinary(n):  # I have zero clue how TF this works. figure it out.
    # its the format function. 0:b means binary format. its easy.
    return "{0:b}".format(int(n))


ntwo = decimalToBinary(nten)
res = 0
max = 0
for dig in ntwo:
    # print(dig)
    if dig == "1":
        res += 1
    elif max <= res:  # needed the elif to reset when its not 1, and to keep the max
        max = res
        res = 0

print(nten, ntwo)
# print(res)
print(max)
# I am failing some cases, like 439
# Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .
