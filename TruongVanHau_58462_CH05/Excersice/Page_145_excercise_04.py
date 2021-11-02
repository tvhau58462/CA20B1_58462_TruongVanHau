"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_01_page_145.py
Problem:
        Write a loop that accumulates the sum of the numbers in a list named data


Solution:

    ....
"""
data = [1, 2, 3]

sum = 0

for i in data:
    sum = i + sum
    print(sum)