"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_01_page_92.py
Problem:
        Translate the following for loops to equivalent while loops:
        a. for count in range(100):
            print(count)
        b. for count in range(1, 101):
            print(count)
        c. for count in range(100, 0, –1):
            print(count)

Solution:

    ....
"""
# Translate the following for loops to equivalent while loops:
#         a. for count in range(100):
#             print(count)
count = 0
while count < 100:
    print(count)
    count = count + 1

# Translate the following for loops to equivalent while loops:
#     b. for count in range(1, 101):
#         print(count)
count = 1
while count < 101:
    print(count)
    count = count + 1

# Translate the following for loops to equivalent while loops:
#     c.for count in range(100,0,–1):
#         print(count)
count = 100
while count >= 1:
    print(count)
    count = count - 1 


