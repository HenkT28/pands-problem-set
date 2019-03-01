# Henk Tjalsma, 2019
# Solution to problem 8 - datetime.py
# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
# Verbatim: https://www.guru99.com/date-time-and-datetime-classes-in-python.html
# https://tecadmin.net/get-current-date-time-python/
# https://www.robjwells.com/2013/10/date-suffixes-in-python/
# http://strftime.net/
# https://www.tutorialspoint.com/python/time_strftime.htm

# https://kapeli.com/cheat_sheets/strftime_Format_Codes.docset/Contents/Resources/Documents/index
# https://www.programcreek.com/python/example/351/datetime.strptime


import time
import datetime

from time import strftime
from datetime import date
from datetime import datetime

# %A, %B %e %Y %H %M %r

today = datetime.now()

time_string = str(today.hour) + str(today.minute)
time_structure = datetime.strptime(time_string,"%H%M")
    # time_structure is a datetime.datetime object

time_string_reform = time_structure.strftime("%I%M%p")
    # ^ set_time comes in format "HH MM am/pm"

day = today.day  

if (3 < day < 21) or (23 < day < 31):
  day = str(day) + 'th'
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  day = str(day) + suffixes[day % 10]


date_string = today.strftime("%A, %B # %Y at %I:%M%p")  

print(date_string.replace('#', day), end='')



