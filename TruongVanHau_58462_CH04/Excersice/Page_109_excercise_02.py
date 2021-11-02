"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_02_page_109.py
Problem:
        Consult the Table of ASCII values in Chapter 2 and suggest how you would modify
            the encryption and decryption scripts in this section to work with strings
            containing all of the printable characters.

Solution:
        The main shortcoming of this encryption strategy is that the plaintext is encrypted one character at a time
            and each encrypted character depend on that single character and a fixed distance value.
            In a sence, the structure of the original text is reserved in the cipher text, so it might
            not be hard to discover a key by visual inspection.


     ....
"""