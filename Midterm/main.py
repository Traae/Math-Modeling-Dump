"""
# Traae Bloxham
# Daniel Korytowski
# MATH 3310
# 3/6/22

# Midterm
"""
import random

import matplotlib.pyplot as plot
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from scipy.optimize import curve_fit


def degree5_polynomial_graph(x_data, y_data, length, after):
    plot.scatter(x_data, y_data, c='blue')

    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length - 1], 1000)
    y = np.array(y_data)

    def func(x, a, b, c, d, e, f):
        return a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f

    popt, pcov = curve_fit(func, x, y)

    ybar = 0
    for i in y_data:
        ybar += i
    ybar = ybar / length

    y_hat = []
    for i in x_data:
        y_hat.append(func(i, *popt))

    topsum = 0
    bottomsum = 0
    count = 0
    while count < length:
        topsum += (y_data[count] - y_hat[count])**2
        bottomsum += (y_data[count] - ybar)**2
        count += 1

    r_squared = 1 - (topsum / bottomsum)

    plot.plot(x_linspace, func(x_linspace, *popt), label='Degree 5')

    after = np.array(after)
    after_linspace = np.linspace(after[0], after[after.size - 1], 1000)
    plot.plot(after_linspace, func(after_linspace, *popt), label='after')

    plot.xlabel('X , R^2: ' + str(r_squared))
    plot.ylabel('Y')
    plot.legend()
    plot.show()
    plot.figure()


def degree4_polynomial_graph(x_data, y_data, length, after):
    plot.scatter(x_data, y_data, c='blue')

    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length - 1], 1000)
    y = np.array(y_data)

    def func(x, a, b, c, d, e):
        return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e

    popt, pcov = curve_fit(func, x, y)
    plot.plot(x_linspace, func(x_linspace, *popt), label='Degree 4')

    ybar = 0
    for i in y_data:
        ybar += i
    ybar = ybar / length

    y_hat = []
    for i in x_data:
        y_hat.append(func(i, *popt))

    topsum = 0
    bottomsum = 0
    count = 0
    while count < length:
        topsum += (y_data[count] - y_hat[count]) ** 2
        bottomsum += (y_data[count] - ybar) ** 2
        count += 1

    r_squared = 1 - (topsum / bottomsum)

    after = np.array(after)
    after_linspace = np.linspace(after[0], after[after.size - 1], 1000)
    plot.plot(after_linspace, func(after_linspace, *popt), label='after')

    plot.xlabel('X , R^2: ' + str(r_squared))
    plot.ylabel('Y')
    plot.legend()
    plot.show()
    plot.figure()


def degree3_polynomial_graph(x_data, y_data, length, after):
    plot.scatter(x_data, y_data, c='blue')

    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length - 1], 1000)
    y = np.array(y_data)

    def func(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d

    popt, pcov = curve_fit(func, x, y)
    ybar = 0
    for i in y_data:
        ybar += i
    ybar = ybar / length

    y_hat = []
    for i in x_data:
        y_hat.append(func(i, *popt))

    topsum = 0
    bottomsum = 0
    count = 0
    while count < length:
        topsum += (y_data[count] - y_hat[count]) ** 2
        bottomsum += (y_data[count] - ybar) ** 2
        count += 1

    r_squared = 1 - (topsum / bottomsum)
    plot.plot(x_linspace, func(x_linspace, *popt), label='Degree 3')

    after = np.array(after)
    after_linspace = np.linspace(after[0], after[after.size - 1], 1000)
    plot.plot(after_linspace, func(after_linspace, *popt), label='after')

    plot.xlabel('X , R^2: ' + str(r_squared))
    plot.ylabel('Y')
    plot.legend()
    plot.show()
    plot.figure()


def degree2_polynomial_graph(x_data, y_data, length, after):
    plot.scatter(x_data, y_data, c='blue')

    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length - 1], 1000)
    y = np.array(y_data)

    correlation = np.corrcoef(x_data, y_data)
    correlation_xy = correlation[0, 1]
    r_squared = correlation_xy ** 2

    def func(x, a, b, c):
        return a * x ** 2 + b * x + c

    popt, pcov = curve_fit(func, x, y)
    ybar = 0
    for i in y_data:
        ybar += i
    ybar = ybar / length

    y_hat = []
    for i in x_data:
        y_hat.append(func(i, *popt))

    topsum = 0
    bottomsum = 0
    count = 0
    while count < length:
        topsum += (y_data[count] - y_hat[count]) ** 2
        bottomsum += (y_data[count] - ybar) ** 2
        count += 1

    r_squared = 1 - (topsum / bottomsum)
    plot.plot(x_linspace, func(x_linspace, *popt), label='Degree 2')

    after = np.array(after)
    after_linspace = np.linspace(after[0], after[after.size - 1], 1000)
    plot.plot(after_linspace, func(after_linspace, *popt), label='after')

    plot.xlabel('X , R^2: ' + str(r_squared))
    plot.ylabel('Y')
    plot.legend()
    plot.show()
    plot.figure()

def monty_hall_sim():
    trials = 1000
    success_count = 0

    while trials > 0:
        trials -= 1
        door = random.randint(1, 3)        # pick the door with the prize
        choice = random.randint(1, 3)      # pick the contestants choice
        switch = random.randint(1, 6)      # decide if the contestant was 'me' and thus would switch
        # The door revealed doesn't matter, so we shift up by 1
        if switch == 1:
            if choice == 3:
                choice = 1
            else:
                choice += 1
        # check for success
        if choice == door:
            success_count += 1

    print('Monty Hall\n The number of successful choices our of 1000:\n ' + str(success_count))



def main():
    #2 Data
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [50, 80, 250, 700, 2000, 3999, 5000, 7000]
    post_x = [9, 10, 11, 12]
    length = 8
    degree2_polynomial_graph(x, y, length, post_x)
    degree3_polynomial_graph(x, y, length, post_x)
    degree4_polynomial_graph(x, y, length, post_x)
    degree5_polynomial_graph(x, y, length, post_x)

    monty_hall_sim()
    monty_hall_sim()
    monty_hall_sim()



if __name__ == '__main__':
    main()
