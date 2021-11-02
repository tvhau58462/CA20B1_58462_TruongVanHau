"""
Author: Truong Van Hau
Date: 17/10/2021
Program: Excercise_04_page_218.py
Problem:
         The functions that draw polygons in the polygons module have the same pattern, varying
            only in the number of sides (iterations of the loop). Factor this pattern into a more general
            function named polygon, which takes the number of sides as an additional argument.


Solution:


    ....
"""

import turtle

# Tạo Turtle
t = turtle.Turtle()

# Nhập số cạnh của Polygon
n = int(input("Enter the no of the sides of the polygon : "))

# Nhập độ dài cạnh Polygon
l = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)