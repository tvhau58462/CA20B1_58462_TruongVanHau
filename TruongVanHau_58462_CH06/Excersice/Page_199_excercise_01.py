"""
Author: Truong Van Hau
Date: 23/10/2021
Program: Excercise_01_page_199.py
Problem:
              Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.

Solution:


    ....
"""

# initialize list
numbers = [5, -6, 7, -8, -10]

# printing original list
print("The original list is : " + str(numbers))

# Absolute value of list elements
# using abs() + list comprehension
res = [abs(ele) for ele in numbers]

# printing result
print("Absolute value list : " + str(res))