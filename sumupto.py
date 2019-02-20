# Henk Tjalsma, 2019
# Solution to problem 1 - sumupto.py script
# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number. 
# The number is recognized as a text string, and has to be converted to integer. Input from user has to be converted to integer.
# Using while loop instead.
i = int(input("Please enter a positive integer: "))

total = 0

while i > 0:
# The new total value is on left hand side, old total on the right hand side.    
    total = total + i
    i = i -1

print(total)    
