import math
from class_Warehouse import Warehouse
from class_other import Position


class Order(object):

    # orders are defined by a position and a set of items represented as a dict: {product_id : order_qty}
    #

    n_orders = 1250
    n_instances = 0

    def __init__(self, x, y, n_items, list_order_items_raw, items):
        Order.n_instances += 1
        self.id = Order.n_instances - 1
        self.destination = Position(int(x), int(y))
        self.n_items = n_items
        self.n_delivered = 0

        # create order_items, stored in a list inside the order:
        self.order_items = [Order_item(order=self, item_id=int(each), items=items) for each in list_order_items_raw]


        # self.items_pending = {i: 0 for i in range(400)}
        # self.weight = 0
        # for each in list_items:
        #     self.items_pending[int(each)] += 1
        #     self.weight += list_items.weight[int(each)]
        # self.distances = {i: self.position.distance(list_wh[i].position) for i in range(Warehouse.n_warehouses)}
        # self.available = {i: self.is_available(list_wh) for i in range(Warehouse.n_warehouses)}
        #
        # self.closest_wh = self.find_closest_wh(list_wh)
        # self.delivered = False

    # def is_available(self, list_wh):
    #     available = True
    #     for wh in list_wh:
    #         for prod in self.items_pending:
    #             ##tester au niveau wh, somme de qte par reference
    #             if self.items_pending[prod] > 0:
    #                 available *= (list_wh[wh].is_available(prod) >= self.items_pending[prod])
    #     return available
    #
    # def find_closest_wh(self, wh):
    #     result = None
    #     mini = math.inf
    #     for i in self.distances.keys():
    #         if self.distances[i] < mini:
    #             result = i
    #             mini = self.distances[i]
    #
    #     wh[result].closest_orders.extend([(self.id, mini, self.weight, self.weight * mini, self.available[result])])
    #     return result
    #
    # def is_delivered(self):
    #     if sum(self.items_pending.values()) == 0:
    #         self.delivered = True


class Order_item(Order):

    n_instances = 0

    def __init__(self, order, item_id, items):
        Order_item.n_instances += 1
        self.id = Order_item.n_instances - 1
        self.order_id = order.id
        self.destination = order.destination
        self.item_id = item_id
        self.weight = items[item_id].weight

        self.warehouse = None # will be assigned when optimization problem is solved
        self.delivered = False

    def __str__(self):
        return str((self.order_id, str(self.destination), self.item_id, self.weight))

