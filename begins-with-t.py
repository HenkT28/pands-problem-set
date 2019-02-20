# Henk Tjalsma, 2019
# Write a program that outputs whether or not today is a day that begins with the letter T.
# Verbatim: https://stackoverflow.com/a/9847269 - Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
# Tuesday equals 1, and Thursday 3.

import datetime

if (datetime.date.today().weekday == 1) or (datetime.date.today().weekday == 3):
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")    