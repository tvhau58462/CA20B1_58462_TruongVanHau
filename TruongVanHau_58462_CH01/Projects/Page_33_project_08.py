"""
Author: Truong Van Hau
Date: 27/08/2021
Program: Project_08_page_33.py
Problem:
        Enter an input statement using the input function at the shell prompt.
        When the prompt asks you for input, enter a number. Then, attempt to add 1 to that number,observe the results, and explain what happened.

Solution:
An input statement using the input function at the shell prompt is as follows:
If a prompt asks for a input, a number is to be added
num = input ('Number: ')
num = num + 1
print(num)
Explanation of results: This gives error at line num= num + 1 as cannot convert int object to str implicitly
    ....
"""
num = input ('Number: ')    #nhập vào số nên kiểu là int
num = num + 1   #kiểu str
print(num)      #num = num + 1 vừa kiểu int vừa kiểu str