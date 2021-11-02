"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_05_page_62.py
Problem:
        An object’s momentum is its mass multiplied by its velocity.
        Write a program that accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and then outputs its momentum.

Solution:

    ....
"""

# Yêu cầu các ngõ vào
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# Tính toán kết quả
momentum = mass * velocity

# Hiển thị kết quả
print("The object's momentum is:", momentum)
