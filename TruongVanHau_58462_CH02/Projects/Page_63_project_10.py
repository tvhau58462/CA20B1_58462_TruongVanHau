"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_10_page_63.py
Problem:
        An employee’s total weekly pay equals the hourly wage multiplied by the total
        number of regular hours plus any overtime pay. Overtime pay equals the total
        overtime hours multiplied by 1.5 times the hourly wage. Write a program that
        takes as inputs the hourly wage, total regular hours, and total overtime hours and
        displays an employee’s total weekly pay.


Solution:
        1 year = 365 days (we ignore leap years)
        1 day  = 24 hours
        1 hour = 60 minutes

    ....
"""

# Yêu cầu các ngõ vào
wage = float(input("Enter the wage: $"))
regularHours = float(input("Enter the regular hours: "))
overtimeHours = float(input("Enter the overtime hours: "))

# tính toán kết quả
totalpay = regularHours * wage + overtimeHours * wage * 1.5

# Hiển thị kết quả
print("The total weekly pay is $" + str(round(totalpay, 2)))
