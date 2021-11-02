"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Casestudy_02_page_93.py
Problem:
        Users of pocket calculators or Python’s math module do not have to think about how
to compute square roots, but the people who built those calculators or wrote the
code for that module certainly did. In this case study, we open the hood and see how
this might be done.
        Write a program that computes square roots.

Solution:
        Compute the square root of a number.
            1. The input is a number.
            2. The outputs are the program's estimate of the square root
                using Newton's method of successive approximations, and
                Python's own estimate using math.sqrt.
    ....
"""

import math

#Recive the input number from the user
x = float(input("Enter a positive number: "))

#Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

#Perform the successive approximations
while True:
    estimate = (estimate + x/estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

#Output the result
print("The program's estimate: ", estimate)
print("Python's estimate:      ", math.sqrt(x))