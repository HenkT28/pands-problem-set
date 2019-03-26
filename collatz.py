# Henk Tjalsma, 2019
# Solution to problem 4 - collatz.py
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value:
# ...if it is even, divide it by two
# ...but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

n = int(input("Please enter a positive integer: "))

# The condition for this loop is n != 1, so it will continue until n is 1, which will make the condition false.    

# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.

# https://stackoverflow.com/questions/17651384/python-remove-division-decimal

while n != 1:
    print (n, end=' ')
    # The script kept producing a decimal while requesting a positive integer -> integer division with // that always give a int    
    if n % 2 == 0: 
        n = n // 2   # n is even
    else:  
        n = n * 3 + 1   # n is odd
else:
    print (n, end=' ')      