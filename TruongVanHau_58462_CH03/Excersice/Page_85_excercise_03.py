"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_03_page_85.py
Problem:
        Write a loop that counts the number of space characters in a string.
        Recall that the space character is represented as ' '.

Solution:

    ....
"""

count = 0           #khởi tạo biến count = 0
mystring = str(input("Nhập chuỗi của bạn vào đây: ")) #khởi tạo chuỗi từ người dùng nhập vào
for i in mystring:  #cho i chạy trong chuỗi
    if i == " ":    #nếu i là khoảng trắng
        count += 1  #biến count sẽ tăng thêm 1
print(count)        #in ra số khoảng trắng

