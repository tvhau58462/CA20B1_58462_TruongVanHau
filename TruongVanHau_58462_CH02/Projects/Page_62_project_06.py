"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_06_page_62.py
Problem:
        The kinetic energy of a moving object is given by the formula KE = (1/2)mv^2 where m is the object’s mass and v is its velocity.
        Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Solution:

    ....
"""
# Yêu cầu các ngõ vào
mass = float(input("Enter the object's mass: "))
velolity = float(input("Enter the object's velolity"))

# Tính toán kết quả
momentum = mass * velolity
kineticEnergy = (mass * velolity ** 2) / 2

# Hiển thị kết quả
print("The object's momentum is: ", momentum)
print("The object's kinetic enery is: ", kineticEnergy)