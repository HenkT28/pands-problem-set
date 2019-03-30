# Henk Tjalsma, 2019
# Solution to problem 7 - squareroot.py script
# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

# What is a floating number?
# It is a number containing one fractional (this is the post-decimal part of a number) part where there are no limitations on the number of digits after the decimal point. 
# A few examples are -25.52, 15.567845321, 3.0 etc.

# https://www.geeksforgeeks.org/python-math-function-sqrt/
# https://www.programiz.com/python-programming/examples/square-root
# https://docs.python.org/3/tutorial/floatingpoint.html
# https://stackoverflow.com/questions/3400965/python-getting-only-1-decimal-place

# Enter positive floating point number as input.
n = float(input('Please enter a positive number: '))

# You store the number in n and find the square root using the ** exponent operator.
if n < 0:
    print("Please enter a positive number.")
else:
   n_sqrt = n ** 0.5

# Getting only 1 decimal place -> print("{:.1f}".format(number)) # Python3
# print("The square root of {} is {} ".format(n,n_sqrt))

print('The square root of %0.1f is approx. %0.1f.'%(n,n_sqrt))