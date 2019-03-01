# Henk Tjalsma, 2019
# Solution to problem 3 - divisors.py script
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

for n in range(1000, 10001):

# Used prime test example as template, explained in the course. The division has to be without remainder: if i%6 == 0 and i%12 != 0, then print. 
# Only if statement, no else, as it needs to meet condition. 

        if n%6 == 0 and n%12 != 0:
            print(n)
        
