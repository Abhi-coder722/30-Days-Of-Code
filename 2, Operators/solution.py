#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

# def solve(meal_cost, tip_percent, tax_percent):
#     # Write your code here

if __name__ == '__main__':
    m = float(input().strip())

    tip = int(input().strip())

    tax = int(input().strip())
    print(round(m+(m*tip/100.0)+(m*tax/100.0)))
