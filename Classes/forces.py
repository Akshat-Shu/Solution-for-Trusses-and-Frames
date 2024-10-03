class known_force:
    def __init__(self,x,y, pos_x, pos_y):
        self.x = x
        self.y = y
        self.pos_x = pos_x
        self.pos_y = pos_y

class unknown_force:
    def __init__(self,x_direction,y_direction, pos_x, pos_y, name):
        self.x_direction = x_direction
        self.y_direction = y_direction
        # if either of x_direction or y_direction is 0, then we interpret that there is no force in such a direction on the member
        self.pos_x = pos_x
        self.name = name
        self.pos_y = pos_y

    def __neg__(self):
        return unknown_force(-self.x_direction,-self.y_direction, self.pos_x, self.pos_y, self.name)
