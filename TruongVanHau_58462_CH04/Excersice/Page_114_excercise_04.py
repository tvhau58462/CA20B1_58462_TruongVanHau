"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_04_page_114.py
Problem:
        Translate each of the following numbers to decimal numbers:
            a. 47
            b. 127
            c. 64

Solution:


    ....
"""

# a.47
ocString = "47"
decimal = 0
exponent = len(ocString) - 1

for digital in ocString:
    decimal = decimal + int(digital) * 8 ** exponent
    exponent = exponent - 1
print("The decimal number is", decimal)

# b. 127
ocString = "127"
decimal = 0
exponent = len(ocString) - 1

for digital in ocString:
    decimal = decimal + int(digital) * 8 ** exponent
    exponent = exponent - 1
print("The decimal number is", decimal)

# c. 64
ocString = "64"
decimal = 0
exponent = len(ocString) - 1

for digital in ocString:
    decimal = decimal + int(digital) * 8 ** exponent
    exponent = exponent - 1
print("The decimal number is", decimal)