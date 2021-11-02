"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Project_06_page_100.py
Problem:
        The German mathematician Gottfried Leibniz developed the following method to approximate the value of π:
            π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
        Write a program that allows the user to specify the number of iterations used in
            this approximation and that displays the resulting value.


Solution:


    ....
"""

sum = 0
float(sum)

#denominator Count
denoCount = 1
int(denoCount)

#iterations
inter = int(input("Enter number of interations: "))

if inter >= 0:
    for count in range(inter):
        sum = sum + (1/denoCount)
        denoCount = -1 * (denoCount + 2)
else:
    print("Number of iterations must be an integer greater than 0")
valueOfpi = sum * 4
print("The approximate value of Pi: ", valueOfpi)


