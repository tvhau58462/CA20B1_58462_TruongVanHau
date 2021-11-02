"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_04_page_132.py
Problem:
        Octal numbers have a base of eight and the digits 0–7. Write the scripts oct al To-
            Decimal.py and decimalToOctal.py, which convert numbers between the octal
            and decimal representations of integers. These scripts use algorithms that are
            similar to those of the binaryToDecimal and decimalToBinary scripts developed
            in Section
            4-3.


Solution:


    ....
"""

# octalToDecimal.py

#input

o_t_n=int(input('Enter a string of octal digits: '))

#required variables

i = 1

dc = 0

#loop for conversion

while (o_t_n != 0):

    #to find remainder

    rmd = o_t_n % 10

    o_t_n //= 10

    dc += rmd * i

    i *= 8

#print the results

print('The integer value is ',dc)

# decimalToOctal.py

#input

d_c_n=int(input('Enter a decimal integer: '))

print("Quotient Remainder Octal")

#required variables

i = 1

o_c_n = 0

num=""

#loop for conversion

while (d_c_n != 0):

    #to find remainder

    rm = d_c_n % 8

    d_c_n //= 8

    o_c_n = o_c_n + rm * i

    i *= 10

    num = str(rm)+num

    print("%5d%8d%12s" % (d_c_n, rm, num))

#print the results

print('The octal representation is ',o_c_n)