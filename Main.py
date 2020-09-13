## imports
from class_other import Item, Grid, Instructions
from class_Drone import Drone
from class_Order import Order
from class_Warehouse import Warehouse

from func_other import *
from input_data import weight, warehouse_raw, orders_raw

from pulp import *


if __name__ == '__main__':

    ### load data, create objects
    grid = Grid(400, 600)
    instructions = Instructions()

    items = {i: Item(weight=int(weight[i])) for i in range(Item.n_items)}

    warehouses = {i: Warehouse(x=warehouse_raw[i][0], y=warehouse_raw[i][1], inventory=warehouse_raw[i][2])
                  for i in range(Warehouse.n_warehouses)}

    drones = {i: Drone() for i in range(Drone.n_drones)}

    orders = {i: Order(x=string_to_list(orders_raw[i][0])[0], y=string_to_list(orders_raw[i][0])[1],
                       n_items=orders_raw[i][1], list_order_items_raw=string_to_list(orders_raw[i][2]),
                       items=items, warehouses=warehouses) for i in range(Order.n_orders)}

    # orders_smpl = sample_orders(orders, 10) # Order.n_orders
    orders_smpl = orders

############## LP:

    supply_nodes = [warehouses[i].id for i in range(warehouses[0].n_warehouses)]
    demand_nodes = [orders_smpl[i].order_items[j].id for i in range(len(orders_smpl)) for j in
                    range(orders_smpl[i].n_items)]
    products = [orders_smpl[i].order_items[j].item_id for i in range(len(orders_smpl)) for j in
                    range(orders_smpl[i].n_items)]

    routes_wip = list(zip(demand_nodes, products))
    routes = [(w, oi_p[0], oi_p[1]) for w in supply_nodes for oi_p in routes_wip]

    costs = [[warehouses[i].distances_to_order_items[j] for j in range(orders[0].order_items[0].n_instances)]
             for i in range(warehouses[0].n_warehouses)]
    costs = makeDict([supply_nodes, demand_nodes], costs, 0)

    model = LpProblem(name='transpo', sense=LpMinimize)
    vars = LpVariable.dicts("route", routes, lowBound=0, upBound=1, cat='Integer') # define variables

    # enter supply, demand, cost
    model += lpSum([vars[(w, oi, p)] * costs[w][oi] for (w, oi, p) in routes]) # define objective function | cost is 1 per distance_unit






    # for i in range(10):
    #     warehouses[i].sort_closest_orders()



    ### data exploration
    # for each in wh:
    #     print(len(wh[each].closest_orders))

    # plot_wh_and_orders(wh, orders)
    # total_slack(wh, orders)
    # total_slack2(wh, orders)

    ### warehouse sequence
    # determine_wh_seq(warehouses)

    #for drone in drones:
    # sum = 0
    # for i in wh:
    #     for j in wh[i].closest_orders:
    #         sum += j[4]
    # print(sum)
    #
    # sum = 0
    # for i in orders:
    #     for j in orders[i].available:
    #         sum += orders[i].available[j]
    # print(sum)











    ### tests
    # drones[0].move_n_load(wh[0], orders[0], {226: 1}, catalog, instructions)
    # print("loading")
    # drones[0].move_n_load(wh[0], orders[0], {183: 1}, catalog, instructions)
    # print("loading")
    # print(catalog.weight[226], catalog.weight[183])
    # print("load:", drones[0].load, "spare:", drones[0].spare_cap)
    # print("inventory:", drones[0].inventory[1])
    #
    # drones[0].move_n_deliver(orders[0], drones[0].inventory[0], instructions)
    # print("unloading")
    # print("load:", drones[0].load, "spare:", drones[0].spare_cap)
    # print("inventory:", drones[0].inventory[0])
    #
    # print(instructions.list)

    # print(wh[0].closest_orders)



























