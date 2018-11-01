#!/usr/bin/env python3

# Two person zero sum game
#               A
#        I   II   III   IV
#   I   20   15   12   35
# B II  25   14   8    10
#   III 40   2    10   5
#   IV  -5   4    11   0

cost = []
rows = int(input("Enter number of strategies: "))
for i in range(rows):
    cost.append(list(map(int, input().split())))

row_min = []
for i in range(rows):
    min = cost[i][0]
    for j in range(1, rows):
        if min > cost[i][j]:
            min = cost[i][j]
    row_min.append(min)

col_max = []
for i in range(rows):
    max = cost[0][i]
    for j in range(1, rows):
        if max < cost[j][i]:
            max = cost[j][i]
    col_max.append(max)

min_max = row_min[0]
max_min = col_max[0]
for i in range(1, rows):
    if row_min[i] > min_max:
        min_max = row_min[i]
    if col_max[i] < max_min:
        max_min = col_max[i]

if min_max == max_min:
    print(min_max)
else:
    print("You failed")
