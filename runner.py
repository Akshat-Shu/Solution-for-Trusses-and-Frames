from Classes.truss_problem import Truss

from Examples.Example1.truss_members1 import members as members1
from Examples.Example3.truss_members3 import members as members3

truss3 = Truss(members3)
truss1 = Truss(members1)


truss1.generate_and_solve()
truss3.generate_and_solve()