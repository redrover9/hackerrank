#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = 0
    ar.sort()
    for i in range(0, n-1):
        try:        
            if ar[i] == ar[i+1]:
                socks += 1
                del ar[i+1:i+2]
        except IndexError:
            print("IndexError")
    return socks
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()