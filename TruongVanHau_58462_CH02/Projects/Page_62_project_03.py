"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_03_page_62.py
Problem:
        Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums.
        The store rents new videos for $3.00 a night, and oldies for $2.00 a night.
        Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals.
        The program should prompt the user for the number of each type of video and output the total cost.

Solution:
        Calculate the total charge for a customer's video rentals,
        given the number of each type of video.

        New video rental = $3.00
        Oldie video rental = $2.00

    ....
"""

# Khởi tạo các hằng số
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00

# Yêu cầu các ngõ vào
newOnes = int(input("Enter the number of new videos: "))
oldOnes = int(input("Enter the number of oldies: "))

# Tính toán kết quả
totalCost = NEW_RENTAL * newOnes + OLDIE_RENTAL * oldOnes

# Hiển thị kết quả
print("The total cost is $" + str(round(totalCost, 2)))