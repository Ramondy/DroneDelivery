from class_other import Position


class Parcel(object):

    # represents a lot of one or more identical products loaded on a drone
    # loading / unloading a parcel represents an instruction to be recorded for scoring

    def __init__(self, x, y):
        self.destination = Position(x, y)
        self.inventory = {i: 0 for i in range(400)}
        self.weight = 0

    def __str__(self):
        return str(("dest:", (self.x, self.y), "weight:", self.weight, self.inventory))


class Drone(object):

    #

    n_drones = 30
    max_cap = 200
    start_x = 113
    start_y = 179

    instance_created = 0

    def __init__(self, x=start_x, y=start_y):
        Drone.instance_created += 1
        self.id = Drone.instance_created - 1
        # self.x = x
        # self.y = y
        self.position = Position(x, y)
        self.max_cap = self.max_cap
        self.load = 0
        self.spare_cap = self.max_cap
        self.inventory = []
        self.time_steps = 0

    def move_n_load(self, warehouse, order, kvp, catalog, instructions):
        self.time_steps += self.position.distance(warehouse.position) + 1
        self.position.x = warehouse.position.x
        self.position.y = warehouse.position.y
        parcel = Parcel(order.position.x, order.position.y)

        for each in kvp:
            parcel.inventory[each] += kvp[each]
            parcel.weight += catalog.weight[each] * kvp[each]
            warehouse.inventory[each] -= kvp[each]

        self.inventory.append(parcel)
        self.load += parcel.weight
        self.spare_cap -= parcel.weight

        assert self.spare_cap >= 0

        instructions.add_instruction([self.id, "L", order.id, list(kvp.keys())[0], list(kvp.values())[0]])

    def move_n_deliver(self, order, parcel, instructions):
        self.time_steps += self.position.distance(parcel) + 1
        self.position.x = parcel.destination.x
        self.position.y = parcel.destination.y
        for each in parcel.inventory:
            if parcel.inventory[each] > 0:
                order.items_pending[each] -= parcel.inventory[each]
                instructions.add_instruction([self.id, "D", order.id, each, parcel.inventory[each]])

        self.load -= parcel.weight
        self.spare_cap += parcel.weight

        order.is_delivered()
        self.inventory.remove(parcel)


    # def move_n_unload(self, warehouse, order, parcel):
    #     self.time_steps += self.distance(self, warehouse) + 1
    #     self.x = warehouse.x
    #     self.y = warehouse.y
    #     for each in list_prod:
    #         self.inventory[each] -= 1
    #         warehouse.inventory[each] += 1
