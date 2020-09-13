from class_other import Position


class Warehouse(object):

    # represents the warehouses
    # each warehouse has a fixed position on the grid
    # inventory is given in input data, therefore loaded at instance creation
    # we see no need for a Warehouse_Item object at this point, provided we update inventory with each transaction
    ## inventory is stored as a dictionary {product_id: qty in stock}

    # WORK IN PROGRESS:
    ### the wh stores information about which orders are closer to it than to any other wh
    ### these are sorted by weight * distance
    ### the wh can respond to an inquiry from a drone to determine product availability

    n_warehouses = 10
    n_instances = 0

    def __init__(self, x, y, inventory):
        Warehouse.n_instances += 1
        self.id = Warehouse.n_instances - 1
        self.position = Position(x, y)
        self.inventory = inventory
        # self.closest_orders = []
        self.distances_to_orders = {}
        self.distances_to_order_items = {}

    def set_distances(self, id, distance, item=False):
        # to calculate distance to every order and order_item
        if item:
            self.distances_to_order_items[id] = distance
        else:
            self.distances_to_orders[id] = distance



    # def sort_closest_orders(self):
    #     # print("Original List: ", self.closest_orders)
    #     for i in range(len(self.closest_orders)):
    #         for j in range(len(self.closest_orders)):
    #             if self.closest_orders[j][3] > self.closest_orders[i][3]:
    #                 self.closest_orders[j], self.closest_orders[i] = self.closest_orders[i], self.closest_orders[j]
    #     # print("Final List: ", self.closest_orders)
    #
    # def is_available(self, product_id):
    #     return self.inventory[product_id]
