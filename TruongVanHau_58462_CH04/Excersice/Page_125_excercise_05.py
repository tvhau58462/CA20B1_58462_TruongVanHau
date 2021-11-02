"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_05_page_125.py
Problem:
        Write a code segment that prompts the user for a filename. If the file exists, the
            program should print its contents on the terminal. Otherwise, it should print an
            error message.


Solution:


    ....
"""

fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()
for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)