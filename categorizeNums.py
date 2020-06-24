#!/bin/python

import math
import os
import random
import re
import sys

"""
Task
Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird
Input Format

A single line containing a positive integer, n .

"""

if __name__ == '__main__':
    print("Please enter a positive integer:")
    n = int(input())
    if(1<=n and n<=100):
        if (n%2 == 1):
            print("Weird")
        elif(n%2==0):
            if(2<=n and n<=5):
                print("Not Weird")
            elif(6<=n and n<=20):
                print("Weird")
            elif(n>20):
                print("Not Weird")
    else:
        print("Entered number not in range")
                      
