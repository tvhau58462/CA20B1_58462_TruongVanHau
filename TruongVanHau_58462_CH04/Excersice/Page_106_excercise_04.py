"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_04_page_106.py
Problem:
       Assume that the variable myString refers to a string, and the variable reversedString refers to an empty string.
       Write a loop that adds the characters from myString to reversedString in reverse order.


Solution:


    ....
"""

myString = "vanhau"
reversedString = ""

for ch in myString[::-1]:
    reversedString = reversedString + ch

print(reversedString)