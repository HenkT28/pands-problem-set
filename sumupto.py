# Solution to problem 1
# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number. 
# The number is recognized as a text string, and has to be converted to integer. Input from user has to be converted to integer.
# Consider negative numbers, and strings in the code.
x = int(input("Please enter an integer: "))

if x >= 0:
    print('That is posive integer')
else:
    print('That is not a posive integer. Try again!')
