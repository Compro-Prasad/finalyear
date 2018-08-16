#!/usr/bin/env python3
#  VAM
#-------
# Input:
# 100 300 300
# 300 200 200
# 5 4 3
# 8 4 3
# 9 7 5

costs = []
supply = list(map(int, input("Enter supply: ").split()))
demand = list(map(int, input("Enter demand: ").split()))

supply_sum = sum(supply)
demand_sum = sum(demand)

supply_count, demand_count = len(supply), len(demand)

def check_small(x):
    if x == -1:
        return 100000000000000
    return x

print("Enter costs: ")
for i in range(supply_count):
    costs.append(list(map(int, input().split())))

total_cost = 0

while (supply_count > 0 and demand_count > 0):
    supply_diff_max = 0
    demand_diff_max = 0
    supply_diff_pos = 0
    demand_diff_pos = 0
    min_ = 100000000000000
    min_pos = 0
    one = True
    one_min = 100000000000000
    one_min_posx = 0
    one_min_posy = 0
    for i in range(len(supply)):
        x = sorted(costs[i], key=check_small)
        if (x[1] != -1 and x[1] - x[0] > supply_diff_max):
            one = False
            supply_diff_max = x[1] - x[0]
            supply_diff_pos = i
    for i in range(len(demand)):
        x = []
        f = False
        for j in range(len(supply)):
            if costs[j][i] != -1:
                f = True
                if (one_min > costs[j][i]):
                    one_min_posx = i
                    one_min_posy = j
            x.append(costs[j][i])
        if f:
            x = sorted(x, key=check_small)
            if (x[1] != -1 and x[1] - x[0] > demand_diff_max):
                one = False
                demand_diff_max = x[1] - x[0]
                demand_diff_pos = i
    #print(demand_diff_max, supply_diff_max)
    #print(demand_diff_pos, supply_diff_pos)
    if (demand_diff_max > supply_diff_max):
        for i in range(len(supply)):
            x = check_small(costs[i][demand_diff_pos])
            if (x < min_):
                min_ = x
                min_pos = i
        supply_diff_pos = min_pos
    else:
        for i in range(len(demand)):
            x = check_small(costs[supply_diff_pos][i])
            if (x < min_):
                min_ = x
                min_pos = i
        demand_diff_pos = min_pos
    if (one):
        demand_diff_pos = one_min_posx
        supply_diff_pos = one_min_posy
    min_sd = min(supply[supply_diff_pos], demand[demand_diff_pos])
    supply[supply_diff_pos] -= min_sd
    demand[demand_diff_pos] -= min_sd
    #print(supply_diff_pos, demand_diff_pos)
    #print("Cost:", costs[supply_diff_pos][demand_diff_pos], ", Value:", min_sd)
    total_cost += min_sd * costs[supply_diff_pos][demand_diff_pos]
    if (supply[supply_diff_pos] == 0):
        supply_count -= 1
        for i in range(len(demand)):
            costs[supply_diff_pos][i] = -1
    if (demand[demand_diff_pos] == 0):
        demand_count -= 1
        for i in range(len(supply)):
            costs[i][demand_diff_pos] = -1

print("Total cost:", total_cost)
#print(costs)
