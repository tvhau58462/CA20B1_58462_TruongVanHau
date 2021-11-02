"""
Author: Truong Van Hau
Date: 08/10/2021
Program: Excercise_04_page_149.py
Problem:
        Define a function named summation. This function expects two numbers, named
            low and high, as arguments. The function computes and returns the sum of the
            numbers between low and high, inclusive


Solution:

    ....
"""
public static int summation(int low, int high)
{
    int sum = 0;        for(int i=low; i<=high; i++) {            sum += i;        }        return sum;    }

