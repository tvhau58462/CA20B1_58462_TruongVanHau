"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_02_page_158.py
Problem:

            Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
                values of the following expressions:
                a. data['a']
                b. data.get('c', None)
                c. len(data)
                d. data.keys()
                e. data.values()
                f. data.pop('b')
                g. data # After the pop above

Solution:

    ....
"""

data = {"b":20, "a":35}

#a. data['a']
data["a"]       #35

#b. data.get('c', None)
data.get("c", None)

#c. len(data)
len(data)       #2

#d. data.keys()
data.keys()     #dict_keys(['b', 'a'])

#e. data.values()
data.values()   #dict_values([20, 35])

#f. data.pop('b')
data.pop('b')   #20





