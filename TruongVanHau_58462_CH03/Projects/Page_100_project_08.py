"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Project_08_page_100.py
Problem:
        The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them.
        Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers.
        You can use this algorithm in the following manner:
        a. Compute the remainder of dividing the larger number by the smaller number.
        b. Replace the larger number with the smaller number and the smaller number with the remainder.
        c. Repeat this process until the smaller number is zero.

The larger number at this point is the GCD of A and B. Write a program that lets
the user enter two integers and then prints each step in the process of using the
Euclidean algorithm to find their GCD.


Solution:


    ....
"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd = 0
while b!= 0:
    gcd = b
    b = a % b
    a = gcd
print("thier GCD is: ", gcd)
