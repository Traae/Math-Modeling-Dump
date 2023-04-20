# Traae Bloxham
# Daniel Korytowski
# Math Modeling
# 2/15/2022
# HOMEWORK REDO
import matplotlib.pyplot as plot


def sampleCode():
    S = [995]
    I = [5]
    R = [0]
    a = 7 / 4975
    time = [0]
    positive = 0
    j = 0
    while j < 100 and positive == 0:
        if S[j] - a * S[j] * I[j] < 0 or I[j] - 0.6 * I[j] + a * I[j] * S[j] < 0:
            positive = 1;
        else:
            S.append(S[j] - a * S[j] * I[j])
            I.append(I[j] - 0.6 * I[j] + a * I[j] * S[j])
            R.append(R[j] + 0.6 * I[j])
            time.append(j + 1)
            j = j + 1
    plot.plot(time, S, 'b-', label='S')
    plot.plot(time, I, 'r-', label='I')
    plot.plot(time, R, 'g-', label='R')
    plot.legend(loc='best')
    plot.show()


def prob4PowerPlantPopulation():
    currentPop = 4000
    population = [currentPop]
    # yearly change = -100 +400 -200 -200 = -100 Total
    yearlyChange = -100
    timeInYears = [0]
    year = 0
    yearsToProject = 5

    while year <= yearsToProject:
        # the next years is equal to the last year plus the change
        currentPop += yearlyChange
        population.append(currentPop)
        year += 1
        timeInYears.append(year)

    plot.axis([0, yearsToProject, currentPop, 4000])
    plot.plot(timeInYears, population, 'r-', label='Population')
    plot.show()


def prob5SIRmodel(suseptible, infected, recovered, infectionRate, recoveryRate):
    S = [suseptible]
    I = [infected]
    R = [recovered]
    a = infectionRate
    time = [0]
    positive = 0
    j = 0
    while j < 100 and positive == 0:
        if S[j] - a * S[j] * I[j] < 0 or I[j] - recoveryRate * I[j] + a * I[j] * S[j] < 0:
            positive = 1;
        else:
            S.append(S[j] - a * S[j] * I[j])
            I.append(I[j] - recoveryRate * I[j] + a * I[j] * S[j])
            R.append(R[j] + recoveryRate * I[j])
            time.append(j + 1)
            j = j + 1
    plot.plot(time, S, 'b-', label='S')
    plot.plot(time, I, 'r-', label='I')
    plot.plot(time, R, 'g-', label='R')
    plot.legend(loc='best')
    plot.show()


def main():
    # sampleCode()
    prob4PowerPlantPopulation()
    prob5SIRmodel(995, 5, 0, (7 / 4975), 0.6)
    prob5SIRmodel(5090, 10, 0, (5/6300), (.99 / 21))


# end main

if __name__ == '__main__':
    main()
