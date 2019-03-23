# Henk Tjalsma, 2019
# Solution to problem 9 - second.py moby-dick.txt
# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

# http://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
# I will only cover, Title: Moby Dick; or The Whale, CHAPTER 1, as example.

# Rewriting script, as the program should take the filename from an argument on the command line.
# Initially I was reading the file in my python code directly rather than calling the text file in as an argument on the command line. 

# https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments
# https://stackoverflow.com/questions/18047879/opening-files-with-python

import sys

script = sys.argv[0]
filename = sys.argv[1]

infile = open(sys.argv[1], "r")
lineList = infile.readlines()

count = 0
# For line in file.      
for line in lineList:
    count+=1
    # Below is the remainder operator (the condition, count % 2 == 0, checks if a number is even).        
    if count % 2 == 0: 
        # Print line 
        print (line)
infile.close()
           