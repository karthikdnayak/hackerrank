#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        print(("#" * (i + 1)).rjust(n))

        # Alternate solutions
        # print(f"{('#' * (i + 1)): >{n}}")
        # print("{0: >{1}}".format('#' * (i + 1), n))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
