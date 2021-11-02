"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_05_page_70.py
Problem:
        Assume that the variable teststring refers to a string.
        Write a loop that prints  each character in this string, followed by its ASCII value.

Solution:


    ....
"""

str1 = input("Please Enter your Own String:")
for i in range(len(str1)):  #Hàm len() trả về số lượng ký tự của chuỗi đầu vào
    print("The ASCII Value of character %c = %d" %(str1[i], ord(str1[i])))  #Ord() trả về một số nguyên đại diện cho mã Unicode của ký tự được chỉ định.
