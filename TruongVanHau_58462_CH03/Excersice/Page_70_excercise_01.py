"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_01_page_70.py
Problem:
        Write the outputs of the following loops:
        a.for count in range(5):
                     print(count + 1, end = " ")
        b. for count in range(1, 4):
                    print(count, end = " ")
        c. for count in range(1, 6, 2):
                    print(count, end = " ")
        d. for count in range(6, 1, –1):
                    print(count, end = " ")

Solution:

    ....
"""
#in số từ 1-5, nếu count không có +1 thì in 0-4
for count in range(5):
    print(count + 1, end = " ")

#in số từ 1-3
for count in range(1, 4):
    print(count, end = " ")

#in ra số 2 bước bắt đầu từ 1 và nhỏ hơn 6(1,3,5)
for count in range(1, 6, 2):
    print(count, end = " ")

#in ra số từ 6-2
for count in range(6, 1, -1):
    print(count, end = " ")