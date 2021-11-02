"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Casestudy_01_page_73.py
Problem:
            It has been said that compound interest is the eighth wonder of the world.
            Our next case study, which computes an investment report, shows why.
            Write a program that computes an investment report.

Solution:
            1. The inputs are starting investment amount number of years interest rate (an integer percent)
            2. The report is displayed in tabular form with a header.
            3. Computations and outputs:
                for each year
                    compute the interest and add it to the investment
                    print a formatted row of results for that year
            4. The ending investment and interest earned are also displayed.

    ....
"""

#Accept the inputs
starBalance = float(input("Enter the investment amount: "))
years = int(input("Enter number of years: "))
rate = int(input("Enter the rate as a %: "))

#convert the rate to a decimal number
rate = rate / 100

#Initialize the accumulator for the interest
totalInterest = 0.0

#Display the header for the table
print("%4s%18s%10s%16s" %("year", "Staring balance", "Interest", "Ending balance"))

#Compute and display the results for each year
for year in range(1, years + 1):
    interest = starBalance * rate
    endBalance = starBalance + interest
    print("%4d%18.2f%10.2f%16.2f" %(year, starBalance, interest, endBalance))
    starBalance = endBalance
    totalInterest += interest

#Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)
