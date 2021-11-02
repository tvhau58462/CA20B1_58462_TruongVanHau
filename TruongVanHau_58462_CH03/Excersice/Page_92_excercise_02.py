"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_02_page_92.py
Problem:
        The factorial of an integer N is the product of the integers between 1 and N, inclusive.
        Write a while loop that computes the factorial of a given integer.

Solution:

    ....
"""

num = int(input("Nhập 1 số bất kỳ vào đây: "))
fac = 1
i = 1

while i <= num:
    fac = fac * i
    i = i + 1
print("factorial of ", num, " is ", fac)