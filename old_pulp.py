#%% PREPARE DATA FOR LP - Transportation Problem:

# https://coin-or.github.io/pulp/CaseStudies/a_transportation_problem.html

from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable, makeDict

supply_nodes = [warehouses[i].id for i in range(warehouses[0].n_warehouses)]  # list of warehouse.id

demand_nodes = [orders[i].order_items[j].id for i in range(len(orders)) for j in  # list of order_item.id
                range(orders[i].n_items)]

products = [items[i].id for i in items]  # list of item.id
product_by_order_item = [orders[i].order_items[j].item_id   # list of item.id by order_item
                         for i in range(len(orders))
                         for j in range(orders[i].n_items)]

supply = {i: warehouses[i].inventory for i in range(warehouses[0].n_warehouses)}

demand = {i: {product_by_order_item[i]: 1} for i in demand_nodes}

routes = list(zip(demand_nodes, product_by_order_item))
routes = [(w, oi_p[0], oi_p[1]) for w in supply_nodes for oi_p in routes]  # list of (warehouse.id, order_item.id, item.id

costs = [
        [warehouses[i].dist_to_order_items[j] for j in range(orders[0].order_items[0].n_instances)]
         for i in range(warehouses[0].n_warehouses)
        ]
costs = makeDict([supply_nodes, demand_nodes], costs, 0)


#%% CREATE LP MODEL

model = LpProblem(name='transportation', sense=LpMinimize)
vars = LpVariable.dicts("route", routes, lowBound=0, upBound=1, cat='Integer') # define variables

# objective function
model += lpSum([vars[(w, oi, p)] * costs[w][oi] for (w, oi, p) in routes]), "Sum_of_Transporting_Costs"

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

# model.to_json("transpo.txt")
# model.writeLP("transpo.lp")

#%% SOLVE LP MODEL

start_time = time.perf_counter()
model.solve()
end_time = time.perf_counter()

print(f"Solved in {(end_time - start_time):0.4f} seconds")
print("Status:", LpStatus[model.status])
print("Total Cost of Transportation = ", value(model.objective))