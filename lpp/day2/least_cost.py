f#!/usr/bin/env python3

import random

dem_sup_count = 3

demand = []
supply = []
costs = []
lc = []

nr = int(input("Rows? "))
nc = int(input("Cols? "))

demand = input("Enter " + str(nc) + " demands: ")
demand = list(map(int, demand.split()))

supply = input("Enter " + str(nc) + " supplies: ")
supply = list(map(int, supply.split()))

print("Enter costs:")
for i in range(dem_sup_count):
    costs.append(list(map(int, input().split())))
    lc.append(t)

total_cost = 0

while len(a) != 0:
    min_cost = 0
    min_x = 0
    min_y = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (min_cost < a[i][j]):
                min_cost = a[i][j]
                min_x = j
                min_y = i
    t1 = []  # costs
    if (demand[min_x] == supply[min_y]):
        for i in range(len(a)):
            if (i != min_y):
                temp = []
                for j in range(len(a[i])):
                    if (j != min_x):
                        temp.append(a[i][j])
                t1.append(temp)
    elif (demand[min_x] < supply[min_y]):
        for i in range(len(a)):
            temp = []
            for j in range(len(a[i])):
                if (j != min_x):
                    temp.append(a[i][j])
            if (len(temp) != 0):
                t1.append(temp)
    else:
        for i in range(len(a)):
            if (i != min_y):
                temp = []
                for j in range(len(a[i])):
                    temp.append(a[i][j])
                t1.append(temp)
    total_cost = min_cost * costs[i][j]
    costs = t1
