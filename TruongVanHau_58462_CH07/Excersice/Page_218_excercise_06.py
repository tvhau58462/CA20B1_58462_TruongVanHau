"""
Author: Truong Van Hau
Date: 17/10/2021
Program: Excercise_06_page_218.py
Problem:
        The Turtle class includes a method named circle. Import the Turtle class, run
            help(Turtle.circle), and study the documentation. Then use this method to
            draw a filled circle and a half moon.


Solution:


    ....
"""

import turtle

turtle.Screen()
turtle.bgcolor("magenta")

turtle.color("yellow")  #màu Turtle vàng
turtle.begin_fill() # bắt đầu vẽ
turtle.circle(130, 180)
turtle.end_fill()   # kết thúc vẽ
turtle.hideturtle() # ẩn Turtle