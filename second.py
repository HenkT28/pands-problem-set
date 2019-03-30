# Henk Tjalsma, 2019
# Solution to problem 9 - second.py moby-dick.txt
# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

# http://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
# I will only cover, Title: Moby Dick; or The Whale, CHAPTER 1, as example -> see moby-dick.txt file

# Initially I was reading the file in my python code directly rather than calling the text file in as an argument on the command line. 
# https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments
# https://stackoverflow.com/questions/18047879/opening-files-with-python

# Rewritten script, as the program should take the filename from an argument on the command line.
# https://docs.python.org/3/library/sys.html
# The sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
# https://www.pythonforbeginners.com/system/python-sys-argv

# Importing sys module
import sys

# sys.argv is a list in Python, which contains the command-line arguments passed to the script. 
# sys.argv[0] is the name of the python script while sys.argv[1] is the file name (moby-dick.txt).
script = sys.argv[0]
filename = sys.argv[1]

# Reading the file - moby-dick.txt
infile = open(sys.argv[1], "r")
lines = infile.readlines()

# Script starts at beginning of the file, count 0.
count = 0
# For line in file.      
for line in lines:
    #  The script goes through each of the lines, count+=1
    count+=1
    # Below is the remainder operator (the condition, count % 2 == 0, checks if a number is even). It has to output every second line.        
    if count % 2 == 0: 
        # Print line 
        print (line)
# Closing the file.        
infile.close()
           