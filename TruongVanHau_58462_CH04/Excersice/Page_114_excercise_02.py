"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_02_page_114.py
Problem:
        Translate each of the following numbers to binary numbers:
            a. 47
            b. 127
            c. 64

Solution:


    ....
"""
# a. 47
decimal = int("47")
bitString = ""
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
    print("%5d%8d%12s"%(decimal, remainder, bitString))
print("The binary number is:", bitString)

# b. 127
decimal = int("127")
bitString = ""
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
    print("%5d%8d%12s"%(decimal, remainder, bitString))
print("The binary number is:", bitString)

# c. 64
decimal = int("64")
bitString = ""
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
    print("%5d%8d%12s"%(decimal, remainder, bitString))
print("The binary number is:", bitString)
