from sympy import Symbol, Eq, solve

from Classes.forces import unknown_force
from Classes.joint import joint
from Classes.member import member


class Truss:
    def __init__(self, members: list[member]):
        self.joints: dict[str, joint] = {}
        self.equations = []
        self.members = members

    def generate_and_solve(self):
        self.generate_equations()
        solved = solve(self.equations)
        print("Solved them!")
        print(solved)


    def generate_equations(self):
        if len(self.equations) != 0: return False
        # generate equations for members
        for memb in self.members:
            self.equations.extend(memb.generate_equations())

        # also generate equations for joints
            for jnt in memb.joints:
                if not jnt.name in self.joints:
                    self.joints[jnt.name] = joint(jnt.name, jnt.unknown_forces, jnt.known_forces, 0, 0)
                self.joints[jnt.name].unknown_forces.append(unknown_force(-1, -1, 0, 0, f"F{jnt.name}{memb.id}"))

        for jnt, val in self.joints.items():
            self.equations.extend(val.generate_equations())
        print(self.equations)
        return True