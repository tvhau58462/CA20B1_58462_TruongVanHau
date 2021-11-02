"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_04_page_125.py
Problem:
        Write a code segment that prints the names of all of the items in the current
            working directory.

Solution:


    ....
"""

import os
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)