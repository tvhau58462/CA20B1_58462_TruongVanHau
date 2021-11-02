"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_01_page_132.py
Problem:
        Write a script that inputs a line of plaintext and a distance value and outputs an
            encrypted text using a Caesar cipher. The script should work for any printable
            characters.


Solution:


    ....
"""

# prompt user to enter a message
def ceasar_elegant():
    alphabits = "truongdaihocdonga"
    string_input = input("Enter a message: ")

# prompt user to enter a shift
    key = int(input("Enter your key: "))

# print the emcrypted message
    n = len(string_input)
    string_output = ""
    for char in string_input:
        string_output += chr(ord(char) + key)
    print(string_output)

ceasar_elegant()


