"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_01_page_117.py
Problem:
       Assume that the variable data refers to the string "Python rules!". Use a string method from Table 4-2 to perform the following tasks:
            a. Obtain a list of the words in the string.
            b. Convert the string to uppercase.
            c. Locate the position of the string "rules".
            d. Replace the exclamation point with a question mark.


Solution:

    ....
"""
# a. Obtain a list of the words in the string.
data = "Python rules!"
for i in range(len(data)):
    print(i, data[i])

# b. Convert the string to uppercase.
data.upper()

# c.Locate the position of the string "rules".
data.find("rule")

# d. Convert the string to uppercase.
data.replace('!', '?')