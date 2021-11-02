"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Project_03_page_99.py
Problem:
        Modify the guessing-game program of Section 3.5 so that the user thinks of a number that the computer must guess.
        The computer must make no more than the minimum number of guesses, and it must prevent the user from cheating by entering misleading hints.
        (Hint: Use the math.log function to compute the minimum number of guesses needed after the lower and upper bounds are entered.)


Solution:


    ....
"""

import random
import math

Smaller = int(input("Enter the smaller number: "))
Larger = int(input("Enter the larger number: "))

count = 0
while True:
#update the value of count
    count += 1
#calculate the average
    number = (Smaller + Larger) // 2
#display number on console
    print("%d %d" %(Smaller, Larger))
#display number on console
    print("Your number is %d" %number)
#prompt the user to enter a character
    ch = input("Enter =, <, or >:")
#check the condition
    if ch == "=":
        print("Correct!, I've got it in %d tries"% count)
        break
#check the condition
    elif Smaller == Larger:
        print("I'm out of guesses, and you cheated.")
        break
#check the condition
    elif ch == "<":
        Larger = number - 1
    else:
        Smaller = number + 1
