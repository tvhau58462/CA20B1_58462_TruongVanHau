"""
Author: Truong Van Hau
Date: 10/09/2021
Program: Project_07_page_100.py
Problem:
       Teachers in most school districts are paid on a schedule that provides a salary based on their number of years of teaching experience.
       For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year.
       For each year of experience after this first year, up to 10 years, the teacher receives a 2% increase over the preceding value.
       Write a program that displays a salary schedule, in tabular format, for teachers in a school district.
       The inputs are the starting salary, the percentage increase, and the number of years in the schedule.
       Each row in the schedule should contain the year number and the salary for that year.


Solution:


    ....
"""
startSalary = int(input("Enter starting salary: "))
percentIncrease = int(input("Enter percentage increase of salary: "))
year = int(input("Enter the number year in the schedule: "))
salary = startSalary
if year <=10:
    for i in range(1,year + 1):
        if i == 1:
            salary = startSalary
            print("year ", i, ", salary: ", salary)
        else:
            salary = salary + salary*(percentIncrease/100)
            print("year ", i, ", salary: ", salary)

elif year >10:
    for i in range(2,11):
        salary = salary + salary*(percentIncrease/100)
        print("year ", i, ", salary: ", salary)
