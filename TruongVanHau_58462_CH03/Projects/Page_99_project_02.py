"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Project_02_page_99.py
Problem:
        Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is a right triangle.
        Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares the other two sides.


Solution:


    ....
"""

x = float(input("Nhập độ dài cạnh thứ nhất: "))
y = float(input("Nhập độ dài cạnh thứ hai: "))
z = float(input("Nhập độ dài cạnh thứ ba: "))

if x*x == y*y + z*z or y*y == x*x + z*z or z*z == x*x + y*y:
    print("Đây là tam giác vuông.")
else:
    print("Đây không phải là tam giác vuông")