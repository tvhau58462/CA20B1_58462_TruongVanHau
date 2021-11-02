"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Project_01_page_165.py
Problem:
        In Chapter 4, we developed an algorithm for converting from binary to decimal.
        You can generalize this algorithm to work for a representation in any base.
            Instead of using a power of 2, this time you use a power of the base. Also, you use
            digits greater than 9, such as A . . . F, when they occur. Define a function named
            repToDecimal that expects two arguments, a string, and an integer. The second
            argument should be the base. For example, repToDecimal("10", 8) returns
            8, whereas repToDecimal("10", 16) returns 16. The function should use a
            lookup table to find the value of any digit. Make sure that this table (it is actually
            a dictionary) is initialized before the function is defined. For its keys, use the 10
            decimal digits (all strings) and the letters A . . . F (all uppercase). The value stored
            with each key should be the integer that the digit represents.
            (The letter 'A' associates with the integer value 10, and so on.) The main loop of the function should
            convert each digit to uppercase, look up its value in the table, and use this value
            in the computation. Include a main function that tests the conversion function
            with numbers in several bases.


Solution:

    ....
"""

conversionLibrary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":10, "C":11, "D":13, "E":14, "F":15}
n = input("Nhap 1 so de chuyen qua ma dec: ")
frombase = int(input("Nhap co so ban muon chuyen doi: "))
n = n.upper()
def reptodecimal(n, frombase):
 tonumber = 0
 power = 0
 for i in range((len(n)),0, -1):
  tonumber += conversionLibrary[n[i-1]] * (int(frombase) ** power)
  power += 1
 return(tonumber)
def main():
 print(reptodecimal('10', 10))
 print(reptodecimal('10', 8))
 print(reptodecimal('101', 2))
 print(reptodecimal('10', 16))
main()