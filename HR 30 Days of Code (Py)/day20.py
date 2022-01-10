#!/bin/python3

import math
import os
import random
import re
import sys

numSwaps = 0


def swapPositions(list, pos1, pos2):

    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)  # need -1 because previous is popped already

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)
    return list


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here

    for i in range(0, a.__len__()):
        for j in range(0, a.__len__()-1):
            if a[j] > a[j+1]:
                swapPositions(a, j, j+1)
                numSwaps += 1
            else:
                pass
firstElement = a[0]
lastElement = a[-1]

print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', firstElement)
print('Last Element:', lastElement)
