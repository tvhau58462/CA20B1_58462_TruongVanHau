"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_08_page_63.py
Problem:
            Light travels at 3*10^8 Projects meters per second. A light-year is the distance a light beam travels in one year.
            Write a program that calculates and displays the value of a light-year.


Solution:
            rate = 3 * 10 ** 8 meters per second
            seconds in a year = 365 * 24 * 60 ** 2
    ....
"""
# Tính kết quả
rate = 3 * 10 ** 8
seconds = 365 * 24 * 60 ** 2
distance = rate * seconds

# Hiển thị kết quả
print("Light travels", distance, "meters in a year.")