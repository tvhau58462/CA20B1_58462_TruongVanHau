"""
Author: Truong Van Hau
Date: 24/09/2021
Program: project_08_page_133.py
Problem:
        Write a script named copyfile.py. This script should prompt the user for the
            names of two text files. The contents of the first file should be input and written
            to the second file.


Solution:


    ....
"""

# to prompt the user to enter the file1 which is input file
infile=input("enter the input filename with extension: ")

# to prompt the user to enter the file2 which is output file
outfile=input("enter the output filename with extension: ")

#opening the file1 in reading mode
f1=open(infile,"r")

#opening the file2 in output mode
f2=open(outfile,"w+")

#reading the content of file1 to content variable
content=f1.read()

#writing to the value of content variable to file2
f2.write(content)

#closing the file1 and file2
f1.close()
f2.close()