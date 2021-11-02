"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_04_page_85.py
Problem:
        Assume that the variables x and y refer to strings.
        Write a code segment that prints these strings in alphabetical order.
        You should assume that they are not equal.

Solution:

    ....
"""

mystring = str(input("Enter a string: "))
x = [word.lower() for word in mystring.split()]
x.sort()
for word in x:
    print(word)
print("The sorted words are:")