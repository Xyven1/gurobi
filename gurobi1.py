import gurobipy as grb
import numpy as np

N = 100

# create gurobi model
m = grb.Model()

m.params.NonConvex = 2

x = m.addVar(vtype=grb.GRB.INTEGER, name="x")
y = m.addVar(vtype=grb.GRB.INTEGER, name="y")
z = m.addVar(vtype=grb.GRB.INTEGER, name="z")

m.update()

m.addConstr(15*(x*x + y*y + z*z) == 34*(x*y+y*z+z*x), "c0")

m.addConstr(x >= 1, "c1")
m.addConstr(y >= x, "c2")
m.addConstr(z >= y, "c3")
m.addConstr(N >= z, "uBound")
m.addConstr(np.gcd(x, np.gcd(y, z))== 1, "coprime")

m.setObjective(z, grb.GRB.MAXIMIZE)

m.optimize()

# print x, y, z
print(x)
print(y)
print(z)
