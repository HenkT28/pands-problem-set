# Henk Tjalsma, 2019
# Solution to problem 4 - collatz.py
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value:
# -> If it is even, divide it by two.
# -> But if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

# Entering a positive integer by user.
n = int(input("Please enter a positive integer: "))

# The condition for this loop is n != 1, so it will continue until n is 1, which will make the condition false.    

# A number is even if division by 2 gives a remainder of 0.
# If remainder is 1, it is an odd number.
# While statement requires else, otherwise 1 will not be included in the output, and break condition.

# https://stackoverflow.com/questions/17651384/python-remove-division-decimal

while n != 1:
    print (n, end=' ')
    # The script will start producing a decimal during the loop while inputting a positive integer -> integer division with // that always give a int    
    if n % 2 == 0: 
        # n is even
        n = n // 2   
    else:
        # n is odd  
        n = n * 3 + 1   
else:
    print (n, end=' ')      