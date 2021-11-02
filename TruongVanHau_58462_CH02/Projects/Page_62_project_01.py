"""
Author: Truong Van Hau
Date: 02/09/2021
Program: Project_01_page_62.py
Problem:
        The tax calculator program of the case study outputs a floating-point number that might show more than two digits of precision.
        Use the round function to modify the program to display at most two digits of precision in the output number

Solution:
        1. Significant constants tax rate standard deduction deduction per dependent
        2. The inputs are gross income number of dependents
        3. Computations: taxable income = gross income - the standard deduction - a
            deduction for each dependent income tax = is a fixed percentage of the taxable income
        4. The outputs are the income tax, rounded to two figures

    ....
"""
# Initialize the constants / khởi tạo nhập vào các hằng số
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs / khai báo cho các dữ liệu đầu vào
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax / tính thuế thu nhập
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
            DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# Display the income tax / Hiển thị thuế thu nhập của bạn
print("The income tax is $" + str(round(incomeTax, 2)))