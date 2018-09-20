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

def get_uv(costs, allocs):
    u = [0]
    v = []
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            try:
                if (allocs[i][j] != 0):
                    v.append(u[i])
                else if not isnan(v[j]):
                    pass
            except IndexError:
                v.append(v[j])
