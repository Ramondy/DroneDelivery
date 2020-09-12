import math
from class_other import Grid


class Order(Grid):

    n_orders = 1250
    instance_created = 0

    def __init__(self, x, y, list_prod, list_wh, catalog):
        Order.instance_created += 1
        self.id = Order.instance_created - 1
        self.x = int(x)
        self.y = int(y)
        self.items_pending = {i: 0 for i in range(400)}
        self.weight = 0
        for each in list_prod:
            self.items_pending[int(each)] += 1
            self.weight += catalog.weight[int(each)]
        self.distances = {i: self.distance(list_wh[i], self) for i in range(len(list_wh))}
        self.available = {i: self.is_available(list_wh) for i in range(len(list_wh))}

        self.closest_wh = self.find_closest_wh(list_wh)
        self.delivered = False

    def is_available(self, list_wh):
        available = True
        for wh in list_wh:
            for prod in self.items_pending:
                ##tester au niveau wh, somme de qte par reference
                if self.items_pending[prod] > 0:
                    available *= (list_wh[wh].is_available(prod) >= self.items_pending[prod])
        return available

    def find_closest_wh(self, wh):
        result = None
        mini = math.inf
        for i in self.distances.keys():
            if self.distances[i] < mini:
                result = i
                mini = self.distances[i]

        wh[result].closest_orders.extend([(self.id, mini, self.weight, self.weight * mini, self.available[result])])
        return result

    def is_delivered(self):
        if sum(self.items_pending.values()) == 0:
            self.delivered = True
