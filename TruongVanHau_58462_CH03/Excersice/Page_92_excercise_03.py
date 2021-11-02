"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_03_page_92.py
Problem:
            The log 2 of a given number N is given by M in the equation N 5 M2 .
            Using integer arithmetic, the value of M is approximately equal to
                the number of times N can be evenly divided by 2 until it becomes 0.
            Write a loop that computes this approximation of the log 2 of a given number N.
            You can check your code by importing the math.
            log function and evaluating the expression round(math.log(N, 2)) (note that the math.
            log function returns a floating-point value).

Solution:


    ....
"""
#Chèn thư viện toán
import math
n = float(input("Nhập N: "))
m = 0
original = n
while n != 0:
    print(n)
    m += 1
    n //= 2
print("Nhật ký khoảng " + str(round(math.log(original),2)))