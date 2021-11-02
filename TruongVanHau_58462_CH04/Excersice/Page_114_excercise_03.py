"""
Author: Truong Van Hau
Date: 24/09/2021
Program: Excercise_03_page_114.py
Problem:
        Translate each of the following numbers to binary numbers:
            a. 47
            b. 127
            c. 64

Solution:


    ....
"""
# a. 47
octnum = int(47)
rev = 0
chk = 0
while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    rev = rem + (rev*10)
    octnum = int(octnum/10)

if chk == 0:
    octnum = rev
    binnum = ""

    while octnum!=0:
        rem = octnum%10
        if rem==0:
            binnum = binnum + "000"
        elif rem==1:
            binnum = binnum + "001"
        elif rem==2:
            binnum = binnum + "010"
        elif rem==3:
            binnum = binnum + "011"
        elif rem==4:
            binnum = binnum + "100"
        elif rem==5:
            binnum = binnum + "101"
        elif rem==6:
            binnum = binnum + "110"
        elif rem==7:
            binnum = binnum + "111"
        octnum = int(octnum/10)

    print("\nEquivalent Binary Value = ", binnum)

# b. 127
octnum = int(127)
rev = 0
chk = 0
while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    rev = rem + (rev*10)
    octnum = int(octnum/10)

if chk == 0:
    octnum = rev
    binnum = ""

    while octnum!=0:
        rem = octnum%10
        if rem==0:
            binnum = binnum + "000"
        elif rem==1:
            binnum = binnum + "001"
        elif rem==2:
            binnum = binnum + "010"
        elif rem==3:
            binnum = binnum + "011"
        elif rem==4:
            binnum = binnum + "100"
        elif rem==5:
            binnum = binnum + "101"
        elif rem==6:
            binnum = binnum + "110"
        elif rem==7:
            binnum = binnum + "111"
        octnum = int(octnum/10)

    print("\nEquivalent Binary Value = ", binnum)

# c. 64
octnum = int(64)
rev = 0
chk = 0
while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    rev = rem + (rev*10)
    octnum = int(octnum/10)

if chk == 0:
    octnum = rev
    binnum = ""

    while octnum!=0:
        rem = octnum%10
        if rem==0:
            binnum = binnum + "000"
        elif rem==1:
            binnum = binnum + "001"
        elif rem==2:
            binnum = binnum + "010"
        elif rem==3:
            binnum = binnum + "011"
        elif rem==4:
            binnum = binnum + "100"
        elif rem==5:
            binnum = binnum + "101"
        elif rem==6:
            binnum = binnum + "110"
        elif rem==7:
            binnum = binnum + "111"
        octnum = int(octnum/10)

    print("\nEquivalent Binary Value = ", binnum)