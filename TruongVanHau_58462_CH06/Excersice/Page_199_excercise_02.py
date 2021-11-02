"""
Author: Truong Van Hau
Date: 23/10/2021
Program: Excercise_02_page_199.py
Problem:
              Write the code for a filtering that generates a list of the positive numbers in a list named numbers.
              You should use a lambda to create the auxiliary function.


Solution:


    ....
"""

# list of numbers 
numbers = [-10, 21, 4, -45, -66, 93, -11]

# we can also print positive no's using lambda exp.
pos_nos = list(filter(lambda x: (x >= 0), numbers))

print("Positive numbers in the list: ", *pos_nos)