import math


class Item(object):

    # each item is represented by a item_id and weight

    n_items = 400
    n_instances = 0

    def __init__(self, weight):
        Item.n_instances += 1
        self.id = Item.n_instances - 1
        self.weight = weight
        self.orders = []
        self.order_items = []

    def add_order_items(self, order_item):
        self.orders.append(order_item.order_id)
        self.order_items.append(order_item.id)


class Position(object):

    # represents a set of x, y coordinates on a grid
    # a position will be assigned to each warehouse, order and drone
    # contains a method to calculate distance to another position

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pos2):
        return int(math.ceil(math.sqrt((self.x - pos2.x) ** 2 + (self.y - pos2.y) ** 2)))

    def __str__(self):
        return str((self.x, self.y))


class Grid(object):

    # represents a rectangular grid of a discrete number of locations
    # each moving object is assigned a position on this grid
    ## on each point there can be a warehouse, one or more order or one or more drones
    ## it is guaranteed that no order is located on the same location that a warehouse
    ## more than one drone are allowed to share a location

    def __init__(self, x, y):
        self.area = x * y


class Instructions(object):

    # represents the instruction set to submit for scoring
    # stored as a list of lists [[instr1], ...]
    # when a command is given to a drone, the related instruction is stored here
    def __init__(self):
        self.list = []

    def add_instruction(self, list):
        self.list.append(list)







