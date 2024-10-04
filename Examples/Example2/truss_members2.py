from Classes.forces import known_force, unknown_force
from Classes.joint import joint
from Classes.member import member

memberAB = member(
    1, [
        joint('B', [], [
            known_force(0, -10, 4, 2)
        ], 4, 2),
        joint('A', [
            unknown_force(0, 1, 0, 0, 'A')
        ], [], 0, 0)
    ],[], []
)
#TODO: implement the second example (solving a truss)
memberBC = member(
    2, [
        joint('C', [], [
            known_force(0,-10,4,2)
        ], 4, 2),
        joint('B', [], [
            known_force(0, -10, 0, 0)
        ], 0, 0)
    ], [], []
)

memberCD = member(
    3, [
        joint('C', [], [
            known_force(0,-10,0,0)
        ], 0, 0),
        joint('D', [], [], 4, 2)
    ], [], []
)

memberAL = member(
    4, [
        joint('A', [
            unknown_force(0, 1, 0, 0, 'A')
        ], [], 0, 0),
        joint('L', [], [], 4, 0)
    ], [], []
)

memberBL = member(
    5, [
        joint('B', [], [
            known_force(0, -10, 0, 0)
        ], 0, 0),
        joint('L', [], [], 0, -2)
    ], [], []
)

memberKL = member(
    6, [
        joint('K', [], [], 0, 0),
        joint('L', [], [], -4, 0)
    ], [], []
)

memberBK = member(
    7, [
        joint('B', [], [
            known_force(0, -10, 0, 0)
        ], 0, 0),
        joint('K', [], [], 4, -2)
    ], [], []
)

memberCK = member(
    8, [
        joint('C', [], [
            known_force(0, -10, 0, 0)
        ], 0, 0),
        joint('K', [], [], 0, -4)
    ], [], []
)

memberCJ = member(
    9,
)

members = [
    memberAB, memberBC,
]