#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    print(format(len(list(filter(lambda x: x > 0, arr))) / n, ".6f"))
    print(format(len(list(filter(lambda x: x < 0, arr))) / n, ".6f"))
    print(format(len(list(filter(lambda x: x == 0, arr))) / n, ".6f"))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
