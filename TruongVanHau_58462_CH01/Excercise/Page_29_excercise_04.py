"""
Author: Truong Van Hau
Date: 27/08/2021
Program: exersice_04_page_29.py
Problem:
   Explain what goes on behind the scenes when your computer runs a Python program.

Solution:
    1. The interpreter reads a Python expression or statement, also called the source
        code, and verifies that it is well formed. In this step, the interpreter behaves like a
        strict English teacher who rejects any sentence that does not adhere to the grammarrules, or syntax, of the language.
        As soon as the interpreter encounters such an error, it halts translation with an error message.
    2. If a Python expression is well formed, the interpreter then translates it to an equivalent
        form in a low-level language called byte code. When the interpreter runs a script, it completely translates it to byte code.
    3. This byte code is next sent to another software component, called the python virtual machine (pVM), where it is executed.
        If another error occurs during this step, execution also halts with an error message.
    ....
"""