# Henk Tjalsma, 2019
# Solution to problem 1 - sumupto.py script
# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line. 
# http://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
# I will only cover, Title: Moby Dick; or The Whale, CHAPTER 1, as example.

# Open a file, for reading.
f = open('moby-dick.txt', 'r')

# To read the file.
s=f.read()

print(s)

# And you have to close it afterwards.
f.close()