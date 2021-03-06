#!/usr/bin/env python3
#  LeastCost
#-------------
# Input:
# 3
# 4
# 10 15 15 20
# 20 25 15
# 10 0 20 11
# 12 7 9 20
# 0 14 16 18


import random

dem_sup_count = 3

demand = []
supply = []
costs = []

nr = int(input("Rows? "))
nc = int(input("Cols? "))

demand = input("Enter " + str(nc) + " demands: ")
demand = list(map(int, demand.split()))

supply = input("Enter " + str(nr) + " supplies: ")
supply = list(map(int, supply.split()))

demand_count = len(demand)
supply_count = len(supply)

print("Enter costs:")
for i in range(nr):
    costs.append(list(map(int, input().split())))

total_cost = 0

while demand_count > 0 and supply_count > 0:
    min_cost = 100000000000000
    min_x = 0
    min_y = 0
    for i in range(len(costs)):
        for j in range(len(costs[i])):
            if (costs[i][j] >= 0 and min_cost > costs[i][j]):
                min_cost = costs[i][j]
                min_x = j
                min_y = i
    min_ = min(demand[min_x], supply[min_y])
    demand[min_x] -= min_
    supply[min_y] -= min_
    total_cost += min_cost * min_
    #print(min_cost, min_)
    #print(demand)
    #print(supply)
    #print(min_y, min_x)
    #for i in costs:
    #    print(i)
    if (demand[min_x] == 0):
        for i in range(len(costs)):
            costs[i][min_x] = -1
        demand_count -= 1
    if (supply[min_y] == 0):
        for i in range(len(costs[min_y])):
            costs[min_y][i] = -1
        supply_count -= 1
    #costs = t1
    #demand = t2
    #supply = t3
    #print(total_cost)

print("Total cost:", total_cost)
