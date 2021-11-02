"""
Author: Truong Van Hau
Date: 17/10/2021
Program: Excercise_03_page_218.py
Problem:
        Add a function named circle to the polygons module. This function expects the
            same arguments as the square and hexagon functions. The function should draw a
            circle. (Hint: the loop iterates 360 times.)


Solution:


    ....
"""

import turtle

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360 / n)

bob = turtle.Turtle()

bob.penup()
bob.sety(-270)
bob.pendown()
polygon(bob, 30, 60)
turtle.mainloop()