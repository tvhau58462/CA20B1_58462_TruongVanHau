"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_07_page_133.py
Problem:
        Write a script that decrypts a message coded by the method used in Project 6.

Solution:
        1. Add 1 to each character’s numeric ASCII value.

        2. Convert it to a bit string.

        3. Shift the bits of this string one place to the left.

        4. A single-space character in the encrypted string separates the resulting bit strings.

    ....
"""

#Implementation of bits2String method
def bits2String(b=''):

    return chr(int(b,2) - 1)

#Implementation of shift method
def shift(n=''):

    temp = list(n)

    new = (temp[-1:] + temp[0:-1])

    ret = ''

    for i in new:

        ret += i

    return ret

#Get the input from user
coded = input('Enter the coded text:')

#split the code
process = coded.split()

decoded = ''

for q in process:

    decoded += bits2String(shift(q))

#Display the decoded message
print(decoded)