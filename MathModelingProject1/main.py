"""
# Traae Bloxham
# Daniel Korytowski
# MATH 3310
# 3/6/22

# Midterm
"""

from tabulate import tabulate


def printTable(names, data):
    print(tabulate(data, headers=names))

def choosePivot(data):
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

def checkRatios(data, pivot):
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




def reduceOtherRowsTo0(data, row, column):
    rowCount = len(data)
    count = 0
    while count < rowCount:
        if count != row:
            columnCount = len(data[count])
            i = 0
            x = data[count][column] / data[row][column]
            while i < columnCount:
                data[count][i] = data[count][i] - (x * data[row][i])


def reduceRowTo1(data, row, column):
    divideby = data[row][column]
    for i in data[row]:
        i = i / divideby


def simplexMethod(varibles, data):
    pivotColumn = []
    pivotRows = []
    # step 1 choose the first pivot

    pcount = 0
    needToReduceagain = True

    while needToReduceagain:

        pivotColumn.append(choosePivot(data))
        print("\nPivoting on column: " + str(pivotColumn[pcount]))
        pivotRows.append(checkRatios(data, pivotColumn[pcount]))
        reduceRowTo1(data, pivotRows[pcount], pivotColumn[pcount])
        reduceOtherRowsTo0(data, pivotRows[pcount], pivotColumn[pcount])
        print("\n Pivot chosen, other rows reduced")
        printTable(varibles, data)

        pcount += 1
        needToReduceagain = False
        for i in data[len(data)-1]:
            if i < 0:
                needToReduceagain = True





def main():
    # data for the Carpenter problem
    # row x1  x2 y1 y2  z RHS  RATIO
    variables = ["x1", "x2", "y1", "y2", "z", "RHS"]
    r1 = [20, 30, 1, 0, 0, 690, 0]
    r2 = [ 5,  4, 0, 1, 0, 120, 0]
    fx = [-25, -30, 0, 0, 1, 0, 0]
    CarpenterData = [r1, r2, fx]
    print(len(CarpenterData))
    print("Data from the carpenter example:")
    printTable(variables, CarpenterData)
    simplexMethod(variables, CarpenterData)




if __name__ == '__main__':
    main()
