"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_0_page_125.py
Problem:
        Assume that a file contains integers separated by newlines.
        Write a code segment that opens the file and prints the average value of the integers.


Solution:


    ....
"""


count = 0
sum = 0

# Open file myfile.txt
inputFile = open("myfile.txt",'r')

for line in inputFile:

    sum +=int(line.strip())

    count += 1

if count == 0:

    average = 0

else:

    average = sum /count

print("The average is", average)