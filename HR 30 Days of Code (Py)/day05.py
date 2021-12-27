#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
for mul in range(1, 11):
    res = n*mul
    print(n, 'x', mul, '=', res)
