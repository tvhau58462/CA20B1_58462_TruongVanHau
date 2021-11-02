"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_09_page_63.py
Problem:
        Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.
        Use the following approximations:
            • A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
            • There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
            • A nautical mile is 1 minute of an arc.


Solution:


    ....
"""
# Yêu cầu ngõ vào
klicks = float(input("Enter the number of kilometers: "))

# Tính toán kết quả
nauts = klicks * 90 * 60 / 10000.0

# Hiển thị kết quả
print("The number of nautical miles is: ", nauts)
