import math


class Catalog(object):

    # represents the set of products available in the simulation
    # the only attribute in this case is their weight
    # the data is stored in a dictionary: {product_id: product_weight}
    def __init__(self, weight_dict):
        self.weight = weight_dict


class Grid(object):

    # represents a rectangular grid of a discrete number of locations
    # each location has a x and y coordinate
    # on each point there can be a warehouse, one or more order or one or more drones
    # it is guaranteed that no order is located on the same location that a warehouse
    # more than one drone are allowed to share a location

    deadline = 112993
    x_dim = 400
    y_dim = 600

    def __init__(self):
        self.area = self.x_dim * self.y_dim

    def distance(self, A, B):
        # returns euclidian distance between two objects on the grip
        return int(math.ceil(math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)))


class Instructions(object):

    # represents the instruction set to submit for scoring
    # stored as a list of lists [[instr1], ...]
    # when a command is given to a drone, the related instruction is stored here
    def __init__(self):
        self.list = []

    def add_instruction(self, list):
        self.list.append(list)







