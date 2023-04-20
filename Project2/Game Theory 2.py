import numpy as np
from sympy import symbols, Eq, solve, init_printing

init_printing()

def y1(x):
    return 500*x+100*(1-x)

def y2(x):
    return 300*x+900*(1-x)

x, y = symbols('x y')
eq1=Eq((500*x+100*(1-x))-(300*x+900*(1-x)),0)
# This is two different ways of solving what you have, depending if you want
# your output to be a float or not.
x1=solve(eq1,x)
x2=np.array(x1).astype(np.float64)
q1=y1(x1[0])
q2=y1(x2[0])
temp=0
y1AT0=y1(temp)
y2AT0=y2(temp)
temp=1
y1AT1=y1(temp)
y2AT1=y2(temp)
Firm=max([q1,y1AT0,y2AT1])
Economy=min([q1,y2AT0,y1AT1])