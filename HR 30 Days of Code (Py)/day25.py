from asyncore import loop
from sqlite3 import enable_callback_tracebacks
import time as t
from math import sqrt


def isPrimeLin(n):  # Linear complexity I think O(n). How to make faster?
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True

    else:  # 1 is not actually a prime number. lol
        return False


def isPrimeLog(n):
    if n > 1:
        for i in range(2, int(sqrt(n))+1):  # compile only until wurzel N, fewer calcs
            if (n % i) == 0:
                return False
        else:
            return True

    else:  # 1 is not actually a prime number. lol
        return False


T = int(input())

for i in range(T):
    n = int(input())
    # startTime = t.time()
    boo = isPrimeLin(n)  # timeout at hr submit
    boo = isPrimeLog(n)  # faster
    # endTime = t.time()-startTime
    print('Prime' if boo == True else 'Not prime')
    # print('this took', endTime, 'seconds')
