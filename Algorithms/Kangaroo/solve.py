#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    x1x2 = x2 - x1
    v1v2 = v1 - v2

    if not v1v2:
        return 'NO'
        
    rest_k = x1x2 % v1v2
    k = x1x2 // v1v2

    if rest_k or k <= 0:
        return 'NO'
    else :
        return 'YES' 


    


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
