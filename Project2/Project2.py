"""
# Traae Bloxham
# Daniel Korytowski
# MATH 3310
# 4/30/22

# Project 2

# I set it up to print it all out again; Thank you, and have a good summer.
"""
import random
import math
import nashpy as nash
import numpy as np
from scipy.optimize import linprog
from tabulate import tabulate


def problem1_total_conflict_size2_oddments():
    # step 1, set up the table:
    top = [" ", "Alice", " ", "Oddments", "Probability"]
    row1 = ["Bob", 2, 3, 0, 0]
    row2 = [" ", 5, 7, 0, 0]
    row3 = ["Oddments", 0, 0, " ", " "]
    bottom = ["Probability", 0, 0, " ", " "]

    row3[1] = abs(row1[2] - row2[2])
    row3[2] = abs(row1[1] - row2[1])

    row1[3] = abs(row2[1] - row2[2])
    row2[3] = abs(row1[1] - row1[2])

    allRows = [top, row1, row2, row3, bottom]

    row1[4] = row1[3] / (row1[3] + row2[3])
    row2[4] = 1 - row1[4]

    bottom[1] = row3[1] / (row3[1] + row3[2])
    bottom[2] = 1 - bottom[1]

    gameValue = ((row1[1] * row1[3]) + (row2[1] * row2[3])) / (row1[3] + row2[3])

    print("Total conflict Values via Oddments method: (just using the simple value representation)\n")
    print(tabulate(allRows))
    print("\nGame Value = " + str(gameValue))


def problem2_total_conflict_size3_nash():
    A = np.array([[1, 2, 3],
                  [8, 9, 4],
                  [7, 6, 5]])

    B = np.array([[9, 8, 7],
                  [2, 1, 6],
                  [3, 4, 5]])

    nashReports(A, B)

    print("The optimal choice is the equilibrium at position 3,3\n")
    print("Both players benefit and minimize loss by tie-ing at 5")


def problem3_threats_promises():
    A = np.array([[1, 2, 3],
                  [8, 9, 4],
                  [7, 6, 5]])

    B = np.array([[9, 8, 7],
                  [2, 1, 6],
                  [3, 4, 5]])
    print("Back to our starting values:")
    print(tabulate(creat3x3grid(A, B)))

    A = A - 5
    B = B - 5

    print("Now, lets reduce the values of the game by five to better illustrate the risks:")
    print(tabulate(creat3x3grid(A, B)))

    print("For the sake of the exercise lets assume Column Players chooses first,\n" +
          "and Row player get to make threats and promises.\n")
    print("Because position 3,3 is the only safe point for either player in a Total Conflict game\n" +
          "any amount of threats and promises made will never be able to establish reduction of risk\n" +
          "while improving benefit for both players.\n")

    print("If we make a promise to deliberately remove 3,3 from the game:\n")
    print("Promise: If you do not choose column 3, I will not choose row 3. \n")
    print("This functionally eliminates all other elements of row and column 3.\n" +
          "But it doesn't eliminate position 3,3 itself from being viable," +
          " because the inner 2x2 grid has the most risk")

    print("\n How about: \n")
    print("Promise: If you do not choose column 2, I will not choose row 2.\n")
    print("This would eliminates Column players biggest risk, but if Row play chooses 1.\n" +
          "They suffer, so they would choose row 3 and to suffer minimize loss, but still loose.\n")
    print("Thus, 3,3 is always the best option\n")

    print("\n An arbitrary number of threats and promises could be made, but any and all would either\n" +
          "illogically cause loss for the Row player, or still be less safe then 3,3.")


def nashReports(A, B):
    game = nash.Game(A, B)
    # print(game)

    grid = creat3x3grid(A, B)

    print("The grid:")
    print(tabulate(grid))

    print("The probabilities are:")
    print(tabulate(game.support_enumeration()))


def creat3x3grid(A, B):
    grid = [
        [[A[0][0], B[0][0]], [A[0][1], B[0][1]], [A[0][2], B[0][2]]],
        [[A[1][0], B[1][0]], [A[1][1], B[1][1]], [A[1][2], B[1][2]]],
        [[A[2][0], B[2][0]], [A[2][1], B[2][1]], [A[2][2], B[2][2]]],
    ]
    return grid


def main():
    print("PROBLEM 1:\n")
    problem1_total_conflict_size2_oddments()

    print("\nPROBLEM 2: \n")
    print("Total Conflict with equilibrium: \n")
    problem2_total_conflict_size3_nash()

    print("\nPROBLEM 3: \n")
    print("Same game with Promises:\n")
    problem3_threats_promises()


if __name__ == '__main__':
    main()
