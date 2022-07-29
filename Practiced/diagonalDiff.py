#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n=len(arr)
    sum1=0
    sum2=0
    count=0
    j=2
    for i in range(n):
        print(i)
        sum1 = sum1+arr[count][i]
        sum2 = sum2+arr[count][j]
        count+=1
        j-=1
    if (sum1-sum2)>0:
        return sum1-sum2
    else:
        return sum2-sum1
        

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
