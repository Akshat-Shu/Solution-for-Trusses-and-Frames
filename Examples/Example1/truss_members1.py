from Classes.member import member
from Classes.forces import unknown_force, known_force
from Classes.joint import joint

# modelled on the basis of example_1.jpg
# program returns the correct answer for all values of forces
member1 = member(
    1, [
        joint('C', [], [], 0, -220),
        joint('D', [], [], 100, -300)
    ],
    [
        unknown_force(1,1,0, 0,'A')
    ],
    [] # this is the known forces acting on the object
)

member2 = member(
    2, [
        joint('C', [], [], 0, 0),
        joint('E', [], [], 250, 0)
    ],
    [
        unknown_force(1,0, 60,60, 'B')
    ],
    [known_force(0, -480, 100, 0)],
    )

member3 = member(
    3, [
        joint('D', [], [], 0, 0),
        joint('E', [], [], 150, 80)
    ],
    [], [],
    )

members = [
    member1, member2, member3
]