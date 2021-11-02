"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_03_page_158.py
Problem:

            Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
                expressions that perform the following tasks:
                a. Replace the value at the key 'b' in data with that value’s negation.
                b. Add the key/value pair 'c':40 to data.
                c. Remove the value at key 'b' in data, safely.
                d. Print the keys in data in alphabetical order

Solution:

    ....
"""

data = {"b":20, "a":35}

#a. Replace the value at the key 'b' in data with that value’s negation.
data["a"]= -35

#b. Add the key/value pair 'c':40 to data.
data["c"] = 40      #{'a': -35, 'c': 40}

#c. Remove the value at key 'b' in data, safely.
print(data.pop("b", None))      #{'a': -35, 'c': 40}

#d. Print the keys in data in alphabetical order
for k in sorted(data):
    print(k,data[k])