"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_02_page_62.py
Problem:
        You can calculate the surface area of a cube if you know the length of an edge.
        Write a program that takes the length of an edge (an integer) as input and prints
            the cube’s surface area as output.

Solution:
        1. compute the surface area of a cube.
        2. The input is the cube's edge.
        3. The output is the surface area of the cube.
    ....
"""

# Yêu cầu ngõ vào
edge = float(input("Enter the cube's edge: "))

# Tính toán diện tích bề mặt
surfaceArea = edge * edge * 6

#  Hiển thị diện tích bề mặt
print("The surface area is: ", surfaceArea, "square units.")