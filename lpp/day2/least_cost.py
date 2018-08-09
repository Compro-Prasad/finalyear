#!/usr/bin/env python3

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

print("Enter costs:")
for i in range(nr):
    costs.append(list(map(int, input().split())))

total_cost = 0

while len(costs) != 0:
    min_cost = 100000000000000
    min_x = 0
    min_y = 0
    for i in range(len(costs)):
        for j in range(len(costs[i])):
            if (min_cost > costs[i][j]):
                min_cost = costs[i][j]
                min_x = j
                min_y = i
    t1 = []  # costs
    t2 = []  # demand
    t3 = []  # supply
    min_ = min(demand[min_x], supply[min_y])
    demand[min_x] -= min_
    supply[min_y] -= min_
    #print(min_x, ", ", min_y)
    print(demand)
    #print(supply)
    if (demand[min_x] == supply[min_y]):
        for i in range(len(costs)):
            if (i != min_y):
                temp = []
                for j in range(len(costs[i])):
                    if (j != min_x):
                        temp.append(costs[i][j])
                        if (i != min_y and len(t2) == 0):
                            t2.append(demand[j])
                t1.append(temp)
                t3.append(supply[i])
    elif (demand[min_x] < supply[min_y]):
        for i in range(len(costs)):
            temp = []
            for j in range(len(costs[i])):
                if (j != min_x):
                    temp.append(costs[i][j])
                    if (len(t2) == 0):
                        t2.append(demand[j])
            if (len(temp) != 0):
                t1.append(temp)
                t3.append(supply[i])
    else:
        for i in range(len(costs)):
            if (i != min_y):
                temp = []
                for j in range(len(costs[i])):
                    temp.append(costs[i][j])
                    if (len(t2) == 0 and i != min_y):
                        t2.append(demand[j])
                t1.append(temp)
                t3.append(supply[i])
    total_cost += min_cost * costs[min_y][min_x]
    costs = t1
    demand = t2
    supply = t3
    #print(costs)

print("Total cost:", total_cost)
