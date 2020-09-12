## imports
from class_other import Catalog, Grid, Instructions
from class_Drone import Drone
from class_Order import Order
from class_Warehouse import Warehouse

from func_other import *
from input_data import weight, warehouse_raw, orders_raw


if __name__ == '__main__':

    ### load data, create objects
    grid = Grid()
    instructions = Instructions()
    catalog = Catalog(weight)

    wh = {}
    for i in range(Warehouse.n_warehouses):
        wh[i] = Warehouse(warehouse_raw[i][0], warehouse_raw[i][1], warehouse_raw[i][2])

    drones = {}
    for i in range(Drone.n_drones):
        drones[i] = Drone()

    orders = {}
    for i in range(Order.n_orders):
        orders[i] = Order(to_list(orders_raw[i][0])[0], to_list(orders_raw[i][0])[1], to_list(orders_raw[i][2]), wh, catalog)

    for i in range(10):
        wh[i].sort_closest_orders()


    ### data exploration
    # for each in wh:
    #     print(len(wh[each].closest_orders))

    # plot_wh_and_orders(wh, orders)
    # total_slack(wh, orders)
    # total_slack2(wh, orders)

    ### warehouse sequence
    determine_wh_seq(wh)

    #for drone in drones:
    sum = 0
    for i in wh:
        for j in wh[i].closest_orders:
            sum += j[4]
    print(sum)

    sum = 0
    for i in orders:
        for j in orders[i].available:
            sum += orders[i].available[j]
    print(sum)










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



























