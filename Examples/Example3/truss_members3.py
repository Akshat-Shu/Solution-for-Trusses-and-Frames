from Classes.forces import unknown_force, known_force
from Classes.joint import joint
from Classes.member import member

memberAC = member(
    1, [
        joint('B', [], [], 0.5, 0)
    ], [unknown_force(1, 1, 0, 0, 'A')],
    [known_force(0, -250, 0.8, 0)]
)

memberBD = member(
    2, [
        joint('B', [], [], 0, 0),
        joint('D', [], [], 0.15, 0.15*(3**0.5))
    ], [], []
)

memberDE = member(
    3, [
        joint('D', [], [], 0, 0)
    ], [
        unknown_force(0, 1, 0.2, 0, 'F'),
        unknown_force(1, 1, 0.4, 0, 'E')
    ], []

)

members = [memberAC, memberBD, memberDE]