"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_06_page_146.py
Problem:
        Write a loop that replaces each number in a list named data with its absolute value.


Solution:

    ....
"""

# initialize list
data = [5, -6, 7, -8, -10]

# printing original list
print("The original list is : " + str(data))

# Absolute value of list elements
# using abs() + list comprehension
res = [abs(ele) for ele in data]

# printing result
print("Absolute value list : " + str(res))