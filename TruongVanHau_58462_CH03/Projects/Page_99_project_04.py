"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Project_04_page_99.py
Problem:
        A standard science experiment is to drop a ball and see how high it bounces.
        Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index.
        For example, if a ball dropped from a height of 10 feet bounces 6 feet high,
            the index is 0.6, and the total distance traveled by the ball is 16 feet after one bounce.
        If the ball were to continue bouncing, the distance after two bounces would be 10ft + 6ft + 6ft + 3.6 = 25.6ft .
        Note that the distance traveled for each successive bounce is the distance to the
            floor plus 0.6 of that distance as the ball comes back up.
        Write a program that lets the user enter the initial height from which the ball
            is dropped and the number of times the ball is allowed to continue bouncing.
        Output should be the total distance traveled by the ball.


Solution:


    ....
"""
height = int(input("Enter the height: "))
bounce = int(input("Enter the bounce: "))
total = 0
app = (0.6)
x = height
y = int(x / app)
z = int(x + y)

if bounce >0:
    bounce -= 1
    total = (z * bounce)

    print("The total distance traveled by the ball: %-0.1f" %total)
