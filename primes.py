# Henk Tjalsma, 2019
# Solution to problem 5 - primes.py script
# Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
# Used prime test example as template, with range, explained in the course. 
# Verbatim: https://inventwithpython.com/hacking/chapter23.html
# A prime number is an integer (that is, a whole number) that is greater than 1 and has only two factors: 1 and itself (note that 1 is not considered a prime number)
# https://www.programiz.com/python-programming/examples/prime-number
# https://www.numbers.education/

n = int(input("Please enter a positive integer: "))

# Prime Numbers are greater than 1.
if n > 1:
   for x in range(2,n):
       if n % x == 0:
           print(n,"is not a prime number")
           print(n, 'equals', x, '*', n//x)
           break
   else:
       print('That is a prime.')
       
# If input number is less than or equal to 1, it is not a prime number.
else:
   print(n,"is not a prime number")     
    