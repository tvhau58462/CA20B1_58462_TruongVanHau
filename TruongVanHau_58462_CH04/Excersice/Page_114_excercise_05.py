"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_05_page_114.py
Problem:
        Translate each of the following numbers to decimal numbers:
            a. 47
            b. 127
            c. AA

Solution:


    ....
"""
A = 10
B = 11
C = 12
D = 13

# a. 47
hex = "47"
decimal = 0
exponent = len(hex) - 1

for digital in hex:
    decimal = decimal + int(digital) * 16 ** exponent
    exponent = exponent - 1
print("The decimal number is", decimal)

# b. 127
hex = "127"
decimal = 0
exponent = len(hex) - 1

for digital in hex:
    decimal = decimal + int(digital) * 16 ** exponent
    exponent = exponent - 1
print("The decimal number is", decimal)

# c. AA
# hex = 1313
# decimal = 0
# exponent = len(hex) - 1
#
# for digital in hex:
#     decimal = decimal + int(digital) * 16 ** exponent
#     exponent = exponent - 1
# print("The decimal number is", decimal)