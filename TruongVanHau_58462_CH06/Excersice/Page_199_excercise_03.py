"""
Author: Truong Van Hau
Date: 23/10/2021
Program: Excercise_03_page_199.py
Problem:
              Write the code for a reducing that creates a single string from a list of strings named words.


Solution:


    ....
"""


def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new


# driver code
s = ['v', 'a', 'n', 'h', 'a', 'u']
print(convert(s))