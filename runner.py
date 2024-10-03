from Classes.forces import unknown_force, known_force
from Classes.joint import joint
from Classes.member import member
from Classes.truss_problem import Truss



truss = Truss(members)
truss.generate_and_solve()
