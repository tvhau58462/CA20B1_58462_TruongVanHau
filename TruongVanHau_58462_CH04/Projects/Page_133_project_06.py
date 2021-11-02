"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_06_page_133.py
Problem:
        Use the strategy of the decimal to binary conversion and the bit shift left operation
        defined in Project 5 to code a new encryption algorithm.
        The algorithm should add 1 to each character’s numeric ASCII value, convert it to a bit string,
            and shift the bits of this string one place to the left.
        A single-space character in the encrypted string separates the resulting bit strings.


Solution:
        1. Add 1 to each character’s numeric ASCII value.

        2. Convert it to a bit string.

        3. Shift the bits of this string one place to the left.

        4. A single-space character in the encrypted string separates the resulting bit strings.

    ....
"""

#converting int to binary
def binary_string(num):
    bit_strng="{0:b}".format(num);
    return bit_strng

#taking string as input from the user
str=input("Enter a string:")
bit_list=[]
for i in str:
    bits=binary_string(ord(i)+1)
    bits=bits[1:]+bits[0]
    bit_list.append(bits)
output=""
#displaying result
for bit in bit_list:
    output+=bit+" "
print(output)

