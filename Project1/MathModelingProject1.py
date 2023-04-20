"""
# Traae Bloxham
# Daniel Korytowski
# MATH 3310
# 3/29/22

# Project 1 - spring break

1. I used the carpenter example data & 'Another Example' from Linear Programming 4 pdf
2. The code works with any tableu format data (well, the format I made with my arrays),
    as long as the matrix is consistent and non-singular I think it'll work.

    I left 2 versions of the 3d in the print out, each is a copy of the 2d examples,
    but with some improvised 3rd constraint equation and x3.

1. I printed out the tables inbetween each step, choosing the pivot, finding the ratios,
    dividing the chosen row, and reducing the other rows.
    It will print these for each iteration of solving the matrix
2. The final table prints,
3.  and just below that is another table showing the solutions for each variable.

The printout is fairly verbose, but it's spaced out and notated enough to follow, I hope.
"""

from tabulate import tabulate


def printTable(names, data):
    print(tabulate(data, headers=names))
# End of function

def choosePivot(data):
    # this functions iterates through the bottom row and finds the lowest negative number.
    lowest = 0
    column = 1
    count = 0
    while count < len(data):
        i = data[len(data)-1][count]
        if i < lowest:
            lowest = i
            column = count
        count += 1
    return column
# End of function

def clearRatios(data):
    i = 0
    while i < len(data):
        data[i][len(data[i])-1] = 0
        i += 1
# End of function

def checkRatios(data, pivot):
    # this function grabs the pivot element of each row, divides the RHS by it, then returns the
    # index of the row with the lowest ratio
    ratioIndex = len(data[0])-1
    rows = len(data)-1
    pivotRow = 0
    count = 0
    minimumRatio = 0
    while count < rows:
        data[count][ratioIndex] = data[count][ratioIndex-1] / data[count][pivot]
        if minimumRatio == 0:
            minimumRatio = data[count][ratioIndex]
            pivotRow = count
        else:
            if minimumRatio > data[count][ratioIndex]:
                pivotRow = count
        count += 1
    return pivotRow
# End of function

def printSolution(data, names):
    # this function just grabs the data it needs and prints out the solution.

    rows = len(data)
    columns = len(data[0])

    solutions = []
    count = 0
    while count < columns:
        if (str(names[count]).__contains__('x')) | (str(names[count]).__contains__('z')):
            sol = [names[count], count, 0]
            solutions.append(sol)
        count += 1

    for s in solutions:
        for r in data:
            if r[s[1]] == 1:
                s[2] = r[columns-2]

    for s in solutions:
        s[1] = '='

    print("\n  FINAL TABLE: \n")
    printTable(names, data)
    print("\n Solution to the variables: \n")
    print(tabulate(solutions))
# End of function



def reduceOtherRowsTo0(data, row, column):
    # reduce the choosen column of all other rows down to 0, by using the chosen row.
    # grab some values for readable code.
    rowCount = len(data)
    columnCount = len(data[row])
    count = 0
    # go through the rows
    while count < rowCount:
        # if the row isn't the chosen row
        if count != row:
            i = 0
            x = data[count][column]
            # iterate through each element in that row and subtract and amount
            # equal to the chosen row's element X the current row's pivot column element)
            while i < columnCount:
                data[count][i] = data[count][i] - (x * data[row][i])
                i += 1
        count += 1
# End of function


def reduceRowTo1(data, row, column):
    # divide a row such that the pivot colum becomes 1
    # first grab that value, then iterate through the row and divide everything by it
    divideby = data[row][column]
    count = 0
    while count < len(data[row]):
        data[row][count] = data[row][count] / divideby
        count += 1
# End of function

def simplexMethod(varibles, data):
    # set up some variables for tracking what we're doing. Non-essential to the math.
    pivotColumn = []
    pivotRows = []
    pcount = 0

    # our while breaker, changes based on there being any negative numbers in the bottom row,
    # aka the function row
    needToReduceagain = True

    while needToReduceagain:
        # choose our pivot and row, appending them to the tracking list
        pivotColumn.append(choosePivot(data))
        pivotRows.append(checkRatios(data, pivotColumn[pcount]))
        # print the current status
        print("\nPivoting on column " + str(pivotColumn[pcount] + 1))
        print("Row " + str(pivotRows[pcount] + 1) + " chosen for smallest ratio\n")
        printTable(varibles, data)
        # divide the pivot row so the pivot colum point is 1
        reduceRowTo1(data, pivotRows[pcount], pivotColumn[pcount])
        # print the current status
        print("\nChosen row divided so that pivot = 1.")
        printTable(varibles, data)
        # reduce the other rows pivot colum values to 0
        reduceOtherRowsTo0(data, pivotRows[pcount], pivotColumn[pcount])
        print("\nothers reduced to 0.")
        printTable(varibles, data)

        # check to see if there are any negatives in the bottom row and go again if needed.
        pcount += 1
        needToReduceagain = False
        for i in data[len(data)-1]:
            if i < 0:
                needToReduceagain = True
                print("\n REPEATING THE PROCESS\n")

    printSolution(data, varibles)
# End of Simplex method function


def main():
    # data for the Carpenter problem
    # row x1  x2 y1 y2  z RHS  RATIO
    variables = ["x1", "x2", "y1", "y2", "z", "RHS", "Ratio"]
    r1 = [20, 30, 1, 0, 0, 690, 0]
    r2 = [ 5,  4, 0, 1, 0, 120, 0]
    fx = [-25, -30, 0, 0, 1, 0, 0]
    CarpenterData = [r1, r2, fx]

    print("EXAMPLE 1: carpenter example:")
    printTable(variables, CarpenterData)
    simplexMethod(variables, CarpenterData)

    v = ["x1", "x2", "y1", "y2", "z", "RHS", "Ratio"]
    a1 = [ 2,  1, 1, 0, 0, 6, 0]
    a2 = [ 1,  3, 0, 1, 0, 9, 0]
    gx = [-3, -1, 0, 0, 1, 0, 0]
    anotherData = [a1, a2, gx]
    print("\n\nEXAMPLE 2: the 'Another Example' from Linear Programming 4 pdf ")
    printTable(v, anotherData)
    simplexMethod(v, anotherData)


    w = ["x1", "x2", "x3", "y1", "y2", "y3", "z", "RHS", "Ratio"]
    b1 = [20, 30, 15, 1, 0, 0, 0, 780, 0]
    b2 = [ 5,  4,  3, 0, 1, 0, 0, 200, 0]
    b3 = [ 2,  5,  1, 0, 0, 1, 0,  47, 0]
    hx = [-25, -30, -23, 0, 0, 0, 1, 0, 0]
    evenMoreData = [b1, b2, b3, hx]
    print("\n\n 3 Variable and 3 Constraint Equations: \n Added some stuff to the carpenter example")
    printTable(w, evenMoreData)
    simplexMethod(w, evenMoreData)

    w = ["x1", "x2", "x3", "y1", "y2", "y3", "z", "RHS", "Ratio"]
    b1 = [2, 1, 3, 1, 0, 0, 0, 6, 0]
    b2 = [1, 3, 4, 0, 1, 0, 0, 9, 0]
    b3 = [2, 5, 1, 0, 0, 1, 0, 3, 0]
    hx = [-3, -1, -2, 0, 0, 0, 1, 0, 0]
    evenMoreData = [b1, b2, b3, hx]
    print("\n\n 3 Variable and 3 Constraint Equations: \n Added some stuff to the other example")
    printTable(w, evenMoreData)
    simplexMethod(w, evenMoreData)


if __name__ == '__main__':
    main()
