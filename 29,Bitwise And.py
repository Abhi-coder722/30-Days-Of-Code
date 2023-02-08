# Objective
# Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

# Function Description
# Complete the bitwiseAnd function in the editor below.

# bitwiseAnd has the following paramter(s):
# - int N: the maximum integer to consider
# - int K: the limit of the result, inclusive

# Returns
# - int: the maximum value of  within the limit.

# Input Format

# The first line contains an integer, , the number of test cases.
# Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.

# Constraints

# Sample Input

# STDIN   Function
# -----   --------
# 3       T = 3
# 5 2     N = 5, K = 2
# 8 5     N = 8, K = 5
# 2 2     N = 8, K = 5
# Sample Output

# 1
# 4
# 0
# Explanation

 

# All possible values of  and  are:

# The maximum possible value of  that is also  is , so we print  on a new line.
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        f = input().rstrip().split()
        N = int(f[0])
        K = int(f[1])
        kk=0
        for i in range(N,1,-1):
            for j in range (i-1,0,-1):
                c=i&j
                if (c<K and c>kk):
                    kk=c
                elif(kk+1==K):
                    break
            if(kk+1==K):
                break
        print(kk)

