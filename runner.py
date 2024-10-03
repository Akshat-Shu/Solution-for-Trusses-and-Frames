from Classes.truss_problem import Truss

from Examples.Example1.truss_members1 import members as members1

truss = Truss(members1)
truss.generate_and_solve()
