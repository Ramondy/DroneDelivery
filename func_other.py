import matplotlib.pyplot as plt
import random
random.seed = 0


def string_to_list(astring):
    return astring.split(" ")


def string_to_dict(astring):
    alist = string_to_list(astring)
    adict = {}
    for i in range(len(alist)):
        adict[i] = int(alist[i])
    return adict

# def


def plot_wh_and_orders(wh, orders):
    wh_x_list = [wh[i].x for i in range(len(wh))]
    wh_y_list = [wh[i].y for i in range(len(wh))]
    order_x_list = [orders[i].x for i in range(len(orders))]
    order_y_list = [orders[i].y for i in range(len(orders))]

    plt.plot(order_x_list, order_y_list, 'o', color='r')
    plt.plot(wh_x_list, wh_y_list, '^', color='b')

    plt.axis([0, 400, 0, 600])
    plt.show()

    return


def sample_orders(orders, k):
    # returns a sample of k orders from the initial dataset
    idx_sel = random.choices(population=range(orders[0].n_orders), k=k)

    result = {}
    for i in range(k):
        result[i] = orders[idx_sel[i]]

    return result




# def determine_wh_seq(wh):
#     wh_index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#     return result
#
#
# # def total_supply(wh):
#    ts = {i: 0 for i in range(400)}
#    for i in wh:
#        for j in ts:
#         ts[j] += wh[i].inventory[j]
#    return ts
#
#
# def total_demand(orders):
#     td = {i: 0 for i in range(400)}
#     for i in orders:
#         for j in td:
#             td[j] += orders[i].items_pending[j]
#     return td
#
#
# def total_slack(wh, orders):
#     tsu = {i: 0 for i in range(400)}
#     for i in wh:
#         for j in tsu:
#             tsu[j] += wh[i].inventory[j]
#
#     td = {i: 0 for i in range(400)}
#     for i in orders:
#         for j in td:
#             td[j] += orders[i].items_pending[j]
#
#     tsl = {i: 0 for i in range(400)}
#     for i in tsl:
#         tsl[i] += tsu[i] - td[i]
#
#     # print("total_supply:", tsu)
#     # print("total_demand:", td)
#     # print("total_slack:", tsl)
#     return
#
#
# def total_slack_pwh(wh, orders):
#     # tsu = {i: 0 for i in range(400)}
#     # for i in wh:
#     #     for j in tsu:
#     #         tsu[j] += wh[i].inventory[j]
#
#     for i in wh:
#         tdw = {k: 0 for k in range(400)}
#         for j in wh[i].closest_orders:
#             for k in tdw:
#                 tdw[k] += orders[j].items_pending[k]
#         # print("total_demand_wh:", i, tdw)
#
#         tslw = {i: 0 for i in range(400)}
#         for k in tslw:
#             tslw[k] += wh[i].inventory[k] - tdw[k]
#         print("total_slack_wh:", i, tslw)
#
#     return
