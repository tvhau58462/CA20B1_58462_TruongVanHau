"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_01_page_114.py
Problem:
        1. Translate each of the following numbers to decimal numbers:
            a. 11001
            b. 100000
            c. 11111

Solution:


    ....
"""
# a. 11001
bitString = "11001"
decimal = 0
exponent = len(bitString) - 1

for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)

# a. 100000
bitString = "100000"
decimal = 0
exponent = len(bitString) - 1

for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
# c. 11111
bitString = "11111"
decimal = 0
exponent = len(bitString) - 1

for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
