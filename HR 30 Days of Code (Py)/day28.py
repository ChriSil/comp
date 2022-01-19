#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
    maildict = dict()
    namelist = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        # Own Idea: store in Dict, then extract keyvaluepairs
        #maildict.update({firstName: emailID})
    # print(maildict)
        if emailID.find("@gmail.com") != -1:  # .find returns -1 if not  found
            namelist.append(firstName)
        namelist.sort()
        for i in namelist:
            print(i)
