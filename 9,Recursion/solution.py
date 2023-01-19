# Objective
# Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.

# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.

# factorial has the following paramter:

# int n: an integer
# Returns

# int: the factorial of n
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format

# A single integer, n(the argument to pass to factorial).

# Your submission must contain a recursive function named factorial.
# Sample Input

# 3
# Sample Output

# 6

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1

if __name__ == '__main__':

    n = int(input().strip())
    print(factorial(n))
