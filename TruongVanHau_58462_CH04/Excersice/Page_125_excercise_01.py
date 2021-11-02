"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_01_page_125.py
Problem:
        Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file.


Solution:


    ....
"""
f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if line == "":
        break
    print(line)
