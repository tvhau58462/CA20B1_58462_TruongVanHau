"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_08_page_85.py
Problem:
        The variables x and y refer to numbers.
        Write a code segment that prompts the user for  an arithmetic operator and prints the value obtained by applying that operator to x and y.

Solution:

    ....
"""
x = int(input("Nhập số thứ nhất của bạn vào đây: "))
y = int(input("Nhập số thứ hai của bạn vào đây: "))
toantu = input("Nhập phép toán tử của bạn vào đây: ")

sum = 0
if toantu == "+":
    sum = x + y
elif toantu == "-":
    sum = x - y
elif toantu == "*":
    sum = x * y
elif toantu == "/":
    sum = x / y
else:
    print("toán tử không hợp lệ: ")
print("Kết quả là:", x, toantu,  y, "=", sum)