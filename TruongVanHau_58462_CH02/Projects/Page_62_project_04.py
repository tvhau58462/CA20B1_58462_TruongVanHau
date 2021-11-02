"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_04_page_62.py
Problem:
        Write a program that takes the radius of a sphere (a floating-point number) as
        input and then outputs the sphere’s diameter, circumference, surface area, and
        volume.

Solution:
        Given the radius conpute the diameter, circumference, and volume of a shere.
        Useful facts:
            diameter = 2 * radius
            circumference = diameter * 3.14
            surface area = 4 * pi * radius * radius
            volume = 4/3 * pi * radius * radius * radius

    ....
"""

import math
# request the input
radius = float(input("Enter the sphere's radius: "))

# Tính toán kết quả
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4 / 3.0 * math.pi * radius * radius * radius

# Hiển thị kết quả
print("Diameter      :", diameter)
print("Circumference :", circumference)
print("Surface area  :", surfaceArea)
print("Volume        :", volume)
