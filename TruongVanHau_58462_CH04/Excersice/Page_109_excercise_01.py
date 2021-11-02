"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_01_page_109.py
Problem:
       Write the encrypted text of each of the following words using a Caesar cipher with a distance value of 3:
            a. python
            b. hacker
            c. wow

Solution:

    ....
"""

code = input("Enter the code text: ")
distance = int(input("Enter the distance value: "))
Plaintext = ""
for ch in code:
    ordvalue = ord(ch)
    cirphervalue = ordvalue - distance
    if cirphervalue < ord('a'):
        cirphervalue = ord('z') - (distance - (ord('a') - ordvalue -1 ))
        Plaintext += chr(cirphervalue)
print(Plaintext)
