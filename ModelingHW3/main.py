"""
# Traae Bloxham
# Daniel Korytowski
# MATH 3310
# 4/12/22

# Homework 3

I placed my answers in the printout this time, so they're next to the code's output.
"""
import random

from tabulate import tabulate


def main():

    events = [' ', 'E', 'F', 'G', 'H']
    choices = [['A', 7, 10, -30, 25],
              ['B', 3, 3, 3, 3],
              ['C', 2, 2, 10, -2],
              ['D', 6, 9, 10, -13]]

    print(tabulate(choices, headers=events))

    #1
    print("\n#1: I'd choose c\n" +
          "It's the only choice with gains that beat the potential loss. \n" +
          "while still having a large-ish prize.")

    myChoice = 2
    events.append('E[x]')
    events.append('E[x] * 12')
    events.append('Output')
    for c in choices:
        c.append(((c[1] + c[2] + c[3] + c[4]) / 4))
        c.append(c[5] * 12)
        c.append(0)


    print("\n#2 I used my birthday as a seed value: 52394\n")
    random.seed(52394)

    count = 12
    while count > 0:
        count -= 1
        for c in choices:
            c[7] += c[random.randint(1, 4)]

    print("#2-a: After 12 runs the Results are:\n")
    print(tabulate(choices, headers=events))

    print("\n My net profit is: " + str(choices[myChoice][-1]))
    print("\n#2-B Well, no. I still made profit, and mathematically I'm really close to the expectation." +
          "\n\n#2-C For the seed I chose however, choice A did really well. But choice A has a higher variance." +
          "\n With a different seed, choice A could have also done really poorly." +
          "\n As shown the statistical expectation of each choice is the same, so choosing a Var(x) that has"+
          "\n the potential to score bigger that E[x], while not risking a negative profit is still my strategy.")





if __name__ == '__main__':
    main()
