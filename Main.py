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

    ### comment out the next line to run on full dataset
    # orders = sample_orders(orders, 10) - FIX GEOMETRY


    ### prepare data for LP:
    # https://coin-or.github.io/pulp/CaseStudies/a_transportation_problem.html

    supply_nodes = [warehouses[i].id for i in range(warehouses[0].n_warehouses)]  # list of warehouse.id

    demand_nodes = [orders[i].order_items[j].id for i in range(len(orders)) for j in  # list of order_item.id
                    range(orders[i].n_items)]

    products = [items[i].id for i in items]  # list of item.id
    product_by_order_item = [orders[i].order_items[j].item_id   # list of item.id by order_item
                             for i in range(len(orders))
                             for j in range(orders[i].n_items)]

    # product_by_order_item_dict = {demand_nodes[i] : {product_by_order_item_list[i] : 1} for i in range(len(demand_nodes))}

    supply = {i: warehouses[i].inventory for i in range(warehouses[0].n_warehouses)}

    demand = {i: {product_by_order_item[i]: 1} for i in demand_nodes}

    routes = list(zip(demand_nodes, product_by_order_item))
    routes = [(w, oi_p[0], oi_p[1]) for w in supply_nodes for oi_p in routes]  # list of (warehouse.id, order_item.id, item.id

    costs = [
            [warehouses[i].distances_to_order_items[j] for j in range(orders[0].order_items[0].n_instances)]
             for i in range(warehouses[0].n_warehouses)
            ]
    costs = makeDict([supply_nodes, demand_nodes], costs, 0)

    ### LP:
    model = LpProblem(name='transportation', sense=LpMinimize)
    vars = LpVariable.dicts("route", routes, lowBound=0, upBound=1, cat='Integer') # define variables

    # objective function
    model += lpSum([vars[(w, oi, p)] * costs[w][oi] for (w, oi, p) in routes]), "Sum_of_Transporting_Costs"
    # model.to_json("lpmodel.txt")

    # constraints
    # supply
    for w in supply_nodes:
        for p in products:
            model += lpSum([vars[w, oi, p] for oi in items[p].order_items]) <= supply[w][p],\
                     "Sum_of_Products_%s_out_of_Warehouse_%d" %(p, w)

    # demand
    count = 0
    for i in range(len(demand_nodes)):
        model += lpSum([vars[w, demand_nodes[i], product_by_order_item[i]] for w in warehouses]) >= demand[demand_nodes[i]][product_by_order_item[i]], \
                 "Sum_of_Products_%s_into_Order_item_%d" %(product_by_order_item[i], demand_nodes[i])

    model.to_json("lpmodel.txt")

    # print(vars)
    # print(vars[6, 9356, 351])

    # print(len(supply_nodes), supply_nodes[0])
    # print(len(products), products[0])
    # print(len(demand_nodes), demand_nodes[0])
    # print(len(product_by_order_item), product_by_order_item[0])
    # print(demand)

    # print(items[0].orders)
    # print([each.item_id for each in orders[187].order_items])




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



























