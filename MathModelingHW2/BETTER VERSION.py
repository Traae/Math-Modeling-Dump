"""
# Traae Bloxham
# Daniel Korytowski
# MATH 3310
# 2/22/20

# Homework 2 FINAL VERSION

This code should produce 7 graphs.
In order:
    - The overlay graph or all three
    - The Lagrange graph
    - the 3rd Degree Polynomial graph
    - the 2nd Degree Polynomial Graph
    - The Lagrange graph + and extension
    - the 3rd Degree Polynomial graph + extension
    - the 2nd Degree Polynomial Graph + extension


   ANSWERS TO THE QUESTIONS

   #1: The lagrange has some weird anomalous behavior once smoothed out.
   Without even addressing it's insane extrapolation, I already don't like it.

   #2: Degree 3 is a fantastic fit, however
   the extrapolation has a pretty steep incline.

   Of course, this extrapolation means nothing, but I'm still wary
   about how far out this model can be trusted.

   #3: The 2nd degree polynomial misses several of out data points completely,
   However its extrapolation isn't as drastic.


   Overall, I'd say the 3rd degree Polynomial is the correct line for
   this data set, but if we were to receive more going into high c values,
   I'd want to test out the 2nd degree Polynomial again.

   Naturally, if we had more data these polynomials would end up being different anyway.


"""


import matplotlib.pyplot as plot
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from scipy.optimize import curve_fit


# #1 Lagrange Polynomial
def lagrange_polynomial_graph(x_data, y_data, length, line_name, should_extrapolate, e):
    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length - 1], 1000)
    poly = lagrange(x, y_data)
    poly = Polynomial(poly).coef

    def lagrange_poly(x_array, coef):
        l = length - 1
        sum = 0
        for i in coef:
            sum += i * x_array**l
            l-=1
        return sum

    plot.plot(x_linspace, lagrange_poly(x_linspace, poly), label=line_name)
    if should_extrapolate:
        e = np.array(e)
        e_linspace = np.linspace(e[0], e[e.size - 1], 1000)
        plot.plot(e_linspace, lagrange_poly(e_linspace, poly), label=(line_name + 'extended'))


# #2 3rd Degree Polynomial
def degree3_polynomial_graph(x_data, y_data, length, line_name, should_extrapolate, e):
    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length - 1], 1000)
    y = np.array(y_data)

    def func(x, a, b, c, d):
        return a * x ** 3 + b * x**2 + c * x + d

    popt, pcov = curve_fit(func, x, y)
    plot.plot(x_linspace, func(x_linspace, *popt), label=line_name)
    if should_extrapolate:
        e = np.array(e)
        e_linspace = np.linspace(e[0], e[e.size - 1], 1000)
        plot.plot(e_linspace, func(e_linspace, *popt), label=(line_name + 'extended'))


# #3 2nd Degree Polynomial
def degree2_polynomial_graph(x_data, y_data, length, line_name, should_extrapolate, e):

    x = np.array(x_data)
    x_linspace = np.linspace(x[0], x[length-1], 1000)
    y = np.array(y_data)

    def func(x, a, b, c):
        return a * x ** 2 + b * x + c

    popt, pcov = curve_fit(func, x, y)
    plot.plot(x_linspace, func(x_linspace, *popt), label=line_name)
    if should_extrapolate:
        e = np.array(e)
        e_linspace = np.linspace(e[0], e[e.size-1], 1000)
        plot.plot(e_linspace, func(e_linspace, *popt), label=(line_name + 'extended'))


def main():
    # The DATA
    c = [1, 2, 3, 4, 5, 6, 7, 8]
    e = [9, 10, 11, 12, 13, 14, 15, 16]
    f = [9, 10]
    y = [36, 70, 100, 150, 250, 502, 800, 1224]
    length = 8

    # The COMBO PLOT
    plot.clf()
    plot.scatter(c, y)
    lagrange_polynomial_graph(c, y, length, 'lagrange', False, e)
    degree3_polynomial_graph(c, y, length, 'Degree 3', False, e)
    degree2_polynomial_graph(c, y, length, 'Degree 2', False, e)
    plot.xlabel('Combo Graph - X = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()

    # THE LAGRANGE ONLY
    plot.scatter(c, y, c='blue')
    lagrange_polynomial_graph(c, y, length, 'Lagrange', False, e)
    plot.xlabel('c = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()
    # 3rd DEGREE ONLY
    plot.scatter(c, y, c='blue')
    degree3_polynomial_graph(c, y, length, 'Degree 3', False, e)
    plot.xlabel('c = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()
    # 2nd DEGREE ONLY
    plot.scatter(c, y, c='blue')
    degree2_polynomial_graph(c, y, length, 'Degree 2,', False, e)
    plot.xlabel('c = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()


    # THE LAGRANGE ONLY
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plot.scatter(c, y, c='blue')
    lagrange_polynomial_graph(c, y, length, 'Lagrange', True, f)
    plot.xlabel('c = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()
    # 3rd DEGREE ONLY
    plot.scatter(c, y, c='blue')
    degree3_polynomial_graph(c, y, length, 'Degree 3', True, e)
    plot.xlabel('c = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()
    # 2nd DEGREE ONLY
    plot.scatter(c, y, c='blue')
    degree2_polynomial_graph(c, y, length, 'Degree 2,', True, e)
    plot.xlabel('c = c')
    plot.ylabel('y = y')
    plot.legend()
    plot.show()
    plot.figure()

if __name__ == '__main__':
    main()


