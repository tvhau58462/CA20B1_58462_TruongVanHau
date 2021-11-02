"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Page_99_project_01.py
Problem:
        Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is an equilateral triangle.

Solution:

    ....
"""

x = float(input("Nhập vào độ dài cạnh thứ nhất: "))
y = float(input("Nhập vào độ dài cạnh thứ hai: "))
z = float(input("Nhập vào độ dài cạnh thứ ba: "))

if x == y == z:
    print("Đây là tam giác đều.")
else:
    print("Đây không phải là tam giác đều.")