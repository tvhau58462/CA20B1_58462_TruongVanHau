"""
Author: Truong Van Hau
Date: 23/10/2021
Program: Excercise_06_page_182.py
Problem:
              Explain what happens when the following recursive function is called with the values "hello" and 0 as arguments:
                def example(aString, index):
                   if index < len(aString):
                     example(aString, index + 1)
                     print(aString[index], end = "")


Solution:
        #olleh

    ....
"""

def example(aString, index):
    if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end="")


example("hello", 0)