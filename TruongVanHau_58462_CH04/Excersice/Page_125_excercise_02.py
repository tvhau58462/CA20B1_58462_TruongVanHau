"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_02_page_125.py
Problem:
        Write a code segment that opens a file for input and prints the number of four-letter words in the file.


Solution:


    ....
"""

filename = input("Enter name of file: ")
file = open(filename, 'r')
file1 = open(filename, 'w')
i = 0
for element in file:
    words = element.split()
    for i in range(len(words)):
        if len(words[i]) == 4:
            file1 = element.replace(i, "xxxx")
            i = i + 1
file.close()