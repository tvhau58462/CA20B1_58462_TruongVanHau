"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_04_page_72.py
Problem:
        Write a loop that outputs the numbers in a list named salaries.
        The outputs should be formatted in a column that is right-justified, with a field width of 12 and a precision of 2

Solution:

    ....
"""

salaries = [1.1,2.22,3.333,4.4444,5.55555,6.666666,7.7777777,8.88888888]
for item in salaries:
    print("%16.2f" % (item))