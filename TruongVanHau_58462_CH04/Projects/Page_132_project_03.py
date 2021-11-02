"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_03_page_132.py
Problem:
        Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.


Solution:


    ....
"""

decode(encrypted_text, distance)
    output = ""
    for i in encrypted_text:
        x = ord(i) - (distance % 26)
        if i.isalpha():
            if i.isupper():
                if x > ord('Z'):
                    x = x -26
                elif x < ord ('A'):
                    x = x + 26
            output += chr(x)
        else:
            output += chr(x)
    return output
encrypted_text = input("Enter the coded text: ")
distance = int(input("Enter distance value: "))
print(decode(encrypted_text, distance))