# Henk Tjalsma, 2019
# Solution to problem 10 - functions.py script
# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].
# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/1.4.2/users/pyplot_tutorial.html
# https://stackoverflow.com/questions/46513843/plot-math-function-fx-with-varying-values-of-x-and-for-different-values-of-n
# https://techmonger.github.io/2/simple-parabola-matplotlib/
# https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib

# import numpy
import numpy
# import math
import math
#import matplotlib
import matplotlib.pyplot as plt

x_cords = range(0,4)
y_x = [x for x in x_cords]
y_2x = [2*x for x in x_cords]
y_x2 = [x*x for x in x_cords]

plt.plot(x_cords, y_x, 'r')
plt.plot(x_cords, y_2x, 'g')
plt.plot(x_cords, y_x2, 'b')

# plt.scatter(x_cords, y_x)
# plt.scatter(x_cords, y_2x)
# plt.scatter(x_cords, y_x2)
plt.show()