from Classes.forces import unknown_force, known_force
from Classes.joint import joint
from sympy import Eq, Symbol


class member:
    def __init__(self, member_id, joints: list[joint], unknown_forces: list[unknown_force], known_forces: list[known_force]):
        self.unknown_forces = unknown_forces
        self.known_forces = known_forces
        self.id = member_id
        self.joints = joints
        for joint in joints:
            self.unknown_forces.append(unknown_force(1, 1, joint.pos_x, joint.pos_y, f"F{joint.name}{self.id}"))

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
            new_torque = unknew_force.y_direction * unknew_force.pos_x * symb_y - unknew_force.x_direction * unknew_force.pos_y * symb_x
            if unknown_torque:
                unknown_torque += new_torque
            else:
                unknown_torque = new_torque

        res = []
        if unknown_torque is not None:
            res.append(Eq(unknown_torque, -known_torque))
            print(f"got equation {unknown_torque} = {-known_torque}")
        if unknown_x is not None:
            res.append(Eq(unknown_x, -known_x))
            print(f"got equation {unknown_x} = {-known_x}")
        if unknown_y is not None:
            res.append(Eq(unknown_y, -known_y))
            print(f"got equation {unknown_y} = {-known_y}")
        return res
