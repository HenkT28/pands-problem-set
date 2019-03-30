# Henk Tjalsma, 2019
# Solution to problem 3 - divisors.py script
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
# No user input is required.

# Setting range between 1,000 and 10,000 -> high end 10,001 so includes 10,000
for n in range(1000, 10001):

# Used prime test example as explained in the course, as template. 
# The division has to be as follows: if n%6 == 0 and n%12 != 0, then print. 
# Only used if statement here, no elif, or else (all optional), as it needs to meet the specific condition. 

        # Condition True
        if n%6 == 0 and n%12 != 0:            
            print(n)    
