import math


class Catalog(object):

    # represents the set of products available in the simulation
    # the only attribute in this case is their weight
    # the data is stored in a dictionary: {product_id: product_weight}
    def __init__(self, weight_dict):
        self.weight = weight_dict


class Position(object):

    # represents a set of x, y coordinates on a grid
    # a position will be assigned to each warehouse, order and drone
    # contains a method to calculate distance to another position

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pos2):
        return int(math.ceil(math.sqrt((self.x - pos2.x) ** 2 + (self.y - pos2.y) ** 2)))


class Grid(object):

    # represents a rectangular grid of a discrete number of locations
    # each moving object is assigned a position on this grid
    ## on each point there can be a warehouse, one or more order or one or more drones
    ## it is guaranteed that no order is located on the same location that a warehouse
    ## more than one drone are allowed to share a location

    deadline = 112993
    x_dim = 400
    y_dim = 600

    def __init__(self):
        self.area = self.x_dim * self.y_dim


class Instructions(object):

    # represents the instruction set to submit for scoring
    # stored as a list of lists [[instr1], ...]
    # when a command is given to a drone, the related instruction is stored here
    def __init__(self):
        self.list = []

    def add_instruction(self, list):
        self.list.append(list)







