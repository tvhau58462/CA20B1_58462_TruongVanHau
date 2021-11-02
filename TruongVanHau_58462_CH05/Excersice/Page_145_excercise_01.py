"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_01_page_145.py
Problem:
        Assume that the variable data refers to the list [5, 3, 7]. Write the values of the following expressions:
            a. data[2]
            b. data[-1]
            c. len(data)
            d. data[0:2]
            e. 0 in data
            f. data + [2, 10, 5]
            g. tuple(data)


Solution:

    ....
"""

data = [5, 3, 7]

#data[2]
data[2]     #7

#b. data[-1]
data[-1]    #7

#c. len(data)
len(data)   #3

#d. data[0:2]
data[0:2]   #[5, 3]

#e. 0 in data
0 in data   #False

#f. data + [2, 10, 5]
data + [2, 10, 5]   #[5, 3, 7, 2, 10, 5]

#g. tuple(data)
tuple(data) #(5, 3, 7)