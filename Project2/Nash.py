import nashpy as nash
import numpy as np
from scipy.optimize import linprog
A = np.array([[0.337, 0.283, 0.188, 0.200], [0.246, 0.571, 0.347, 0.227],
[0.220, 0.339, 0.714, 0.154], [0.200, 0.303, 0.227, 0.500]])
B = 1-A
prisoners_dilemma = nash.Game(B, A)
equilibria1=prisoners_dilemma.support_enumeration()
equilibria2=prisoners_dilemma.vertex_enumeration()
equilibria3=prisoners_dilemma.lemke_howson_enumeration()
for eq1 in equilibria1:
    print(eq1)
    outcome=prisoners_dilemma[eq1]
    print(outcome,'outcome1')
for eq2 in equilibria2:
    print(eq2)
    outcome=prisoners_dilemma[eq2]
    print(outcome,'outcome2')
for eq3 in equilibria3:
    print(eq3)
    outcome=prisoners_dilemma[eq3]
    print(outcome,'outcome3')
G=1-A
(n,m) = np.shape(G)
A_ub = -np.transpose(G)
# we add an artificial variable to maximize, present in all inequalities
A_ub = np.append(A_ub, np.ones((m,1)), axis = 1)
# all inequalities should be inferior to 0
b_ub = np.zeros(m)
# the sum of all variables except the artificial one should be equal to one
A_eq = np.ones((1,n+1))
A_eq[0][n] = 0
b_eq = 1
c = np.zeros(n + 1)
# -1 to maximize the artificial variable we’re going to add
c[n] = -1
res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
bounds=(0,None),method='revised simplex')
print((res.x[:-1], -res.fun))