#!/usr/bin/env python3

from math import isnan

def get_an_occupied_cell(allocs, i, j):
    try:
        if (allocs[i][j + 1] != 0):
            return i, j+1
    except IndexError:
        pass
    try:
        if (allocs[i+1][j] != 0):
            return i+1, j
    except IndexError:
        pass
    try:
        if (allocs[i-1][j] != 0):
            return i-1, j
    except IndexError:
        pass
    try:
        if (allocs[i][j-1] == ):
            return i, j-1
    except IndexError:
        pass
    return -1, -1

def create_cycle(allocs, neg_i, neg_j):
    cycle_coordinates = []
    i, j = get_an_occupied_cell(allocs, neg_i, neg_j)
    while i != neg_i and j != neg_j:
        if i == -1 or j == -1:
            raise Exception("Couldn't find another cell")
        cycle_coordinates.append((i, j))
        i, j = get_an_occupied_cell(allocs, i, j)
    return cycle_coordinates

def get_min_in_cycle(allocs, cycle_coordinates):
    min = 0
    for i in cycle_coordinates:
        if min > allocs[i[0]][i[1]]:
            min = allocs[i[0]][i[1]]
    return min

def modify_cycle(allocs, cycle_coordinates):
    t = 1
    min = get_min_in_cycle(allocs, cycle_coordinates)
    for i in cycle_coordinates:
        x, y = i[0]
        allocs[x][y] = min + int(t * allocs[x][y])
        if t == 1:
            t = -1
        else:
            t = 1

def get_all_allocated_coordinates(allocs):
    coordinates = []
    for i in range(len(allocs)):
        for j in range(len(allocs[0])):
            if allocs[i][j] > 0:
                coordinates.append((i, j))
    return coordinates

def isAnyNan(l):
    for i in l:
        if isnan(i):
            return True
    return False

def get_uv(costs, allocs):
    u = []
    v = []
    for i in costs:
        u.append(float('nan'))
        if len(v) == 0:
            for j in costs[0]:
                v.append(float('nan'))
    u[0] = 0
    coordinates = get_all_allocated_coordinates(allocs)
    stopLoopCount = 0
    while isAnyNan(u) or isAnyNan(v):
        stopLoopCount += 1
        for x, y in coordinates:
            if not isnan(u[x]) and isnan(v[y]):
                v[y] = costs[x][y] - u[x]
            else if isnan(u[x]) and not isnan(v[y]):
                u[x] = costs[x][y] - v[y]
        if stopLoopCount % 100 == 0:
            ans = input("Loop ran for {0} times. Do you want to continue? [y] ".format(stopLoopCount))
            if ans != 'y':
                break
    return u, v

def isValid(costs, allocs, u, v):
    min_val = 1000000000000000
    min_x = -1
    min_y = -1
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if allocs[i][j] == 0:
                x = costs[i][j] - u[i] - v[j]
                if x < min_val:
                    min_val = x
                    min_x, min_y = i, j
    return min_x, min_y
