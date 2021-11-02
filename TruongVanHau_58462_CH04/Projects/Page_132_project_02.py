"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_02_page_132.py
Problem:
        Write a script that inputs a line of encrypted text and a distance value and outputs
            plaintext using a Caesar cipher. The script should work for any printable characters.


Solution:


    ....
"""

text = input("enter coded text: ")
distance = int(input("enter value: "))
plainText = ""
for ch in text:
  ordvalue = ord(ch)
  ciphervalue = ordvalue - distance
  if ciphervalue < ord('a'):
    ciphervalue = ord('z') - (distance - (ord('a')-ordvalue - 1))
  plainText += chr(ciphervalue)
print(plainText)

