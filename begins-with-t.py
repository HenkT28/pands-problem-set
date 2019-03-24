# Henk Tjalsma, 2019
# Solution to problem 2 - begins-with-t.py script
# Write a program that outputs whether or not today is a day that begins with the letter T.
# Verbatim: https://stackoverflow.com/a/9847269 - Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
# https://www.pythonprogramming.in/date-time/get-the-day-of-week-from-given-a-date-in-python.html

# import Python's datetime module
import datetime

# Tuesday and Thursday - both begin with T, weekday 1, and weekday 3
# Using single or statement
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
   print("Yes - today begins with a T.")
# This can be uncommented in case you want to know weekday and isoweekday    
   # print("weekday():", datetime.datetime.today().weekday())   
   # print("isoweekday()", datetime.datetime.today().isoweekday())
else:
   print("No - today does not begin with a T.")
# This can be uncommented in case you want to know weekday and isoweekday     
   # print("weekday():", datetime.datetime.today().weekday())   
   # print("isoweekday()", datetime.datetime.today().isoweekday())    


