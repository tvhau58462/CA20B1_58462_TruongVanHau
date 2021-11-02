"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Excercise_02_page_72.py
Problem:
        Write a code segment that displays the values of the integers x, y, and z on a single line,
        such that each value is right-justified with a field width of 6

Solution:

    ....
"""
x,y,z = 1,2,3
print("%-6d %-6d %-6d"%(x,y,z))  #%6d: căn lề phải 6 ký tự với %d dùng để thay thế số, %-6d: căn lề trái 6 ký tự