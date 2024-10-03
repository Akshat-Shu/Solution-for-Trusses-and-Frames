from Classes.forces import unknown_force, known_force
from sympy import Eq, Symbol

class joint:
    def __init__(self,name, unknown_forces: list[unknown_force], known_forces: list[known_force], pos_x, pos_y):
        self.known_forces = known_forces
        self.unknown_forces = unknown_forces
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name


    def generate_equations(self):
        known_x = 0
        known_y = 0
        known_torque = 0
        unknown_x = None
        unknown_y = None
        unknown_torque = None

        for knew_force in self.known_forces:
            known_x += knew_force.x
            known_y += knew_force.y
            known_torque += knew_force.pos_x * knew_force.y - knew_force.pos_y * knew_force.x
        for unknew_force in self.unknown_forces:
            symb_x = Symbol(unknew_force.name + 'x')
            symb_y = Symbol(unknew_force.name + 'y')

            if unknown_x:
                unknown_x += unknew_force.x_direction*symb_x
            else:
                unknown_x = unknew_force.x_direction*symb_x
            if unknown_y:
                unknown_y += unknew_force.y_direction*symb_y
            else:
                unknown_y = unknew_force.y_direction*symb_y


        res = []
        if unknown_x is not None:
            res.append(Eq(unknown_x, -known_x))
            print(f"got equation {unknown_x} = {-known_x}")
        if unknown_y is not None:
            res.append(Eq(unknown_y, -known_y))
            print(f"got equation {unknown_y} = {-known_y}")
        return res




