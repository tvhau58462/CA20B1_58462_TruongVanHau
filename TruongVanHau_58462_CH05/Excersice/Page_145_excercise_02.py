"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_02_page_145.py
Problem:
        Assume that the variable data refers to the list [5, 3, 7]. Write the expressions that perform the following tasks:
            a. Replace the value at position 0 in data with that value’s negation.
            b. Add the value 10 to the end of data.
            c. Insert the value 22 at position 2 in data.
            d. Remove the value at position 1 in data
            e. Add the values in the list newData to the end of data.
            f. Locate the index of the value 7 in data, safely.
            g. Sort the values in data.


Solution:

    ....
"""
data = [5, 3, 7]

#a. Replace the value at position 0 in data with that value’s negation.
data[0] = -5    #[-5, 3, 7]

#b. Add the value 10 to the end of data.
data.append(10) #[-5, 3, 7, 10]

#c. Insert the value 22 at position 2 in data.
data.insert(2, 22)  #[-5, 3, 22, 7, 10]

#d. Remove the value at position 1 in data
data.pop(1)     #3

#e. Add the values in the list newData to the end of data.
data.extend([1, 2, 4, 6])   #[-5, 22, 7, 10, 1, 2, 4, 6]

#f. Locate the index of the value 7 in data, safely.
data[2]

#g. Sort the values in data.
data.sort()     #[-5, 1, 2, 4, 6, 7, 10, 22]

