"""
Author: Truong Van Hau
Date: 23/10/2021
Program: Excercise_02_page_182.py
Problem:
              The factorial of a positive integer n, fact(n), is defined recursively as follows:
                 fact(n) = 5 , when n = 1
                 fact(n) = n * fact(n-1) , otherwise
                 Define a recursive function fact that returns the factorial of a given positive integer


Solution:


    ....
"""

def fact(n):
   if n == 1 or n==0:
       return 1
   else :
       return n*fact(n-1)

print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))