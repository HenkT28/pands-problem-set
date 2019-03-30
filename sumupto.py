# Henk Tjalsma, 2019
# Solution to problem 1 - sumupto.py script
# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number. 
# Using while loop to accomplish the task.

# The input is recognized as a text string, and has to be converted to integer. 
i = int(input("Please enter a positive integer: "))

total = 0

while i > 0:
# The new total value is on left hand side, old total on the right hand side.    
    total = total + i
# Below condition ensures while loop does not continue indefinitely. 
    i = i - 1

print(total)    
