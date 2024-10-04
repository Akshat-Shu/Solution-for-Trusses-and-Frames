from Classes.forces import known_force, unknown_force
from Classes.joint import joint
from Classes.member import member

memberAB = member(
    1, [
        joint('B', [], [
            known_force(0, -10, 4, 2)
        ], 4, 2)
    ], [
        unknown_force(1, 1, 0, 0, 'A')
    ], []
)
#TODO: implement the second example (solving a truss)
memberBC = member(
    2, joint('C', [], [
        known_force
    ])
)