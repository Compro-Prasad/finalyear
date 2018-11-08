#!/usr/bin/env python3

# Two person zero sum game
#               A
#        I   II   III   IV
#   I   20   15   12   35
# B II  25   14   8    10
#   III 40   2    10   5
#   IV  -5   4    11   0

rows = int(input("Enter number of strategies: "))
cost = [list(map(int, input().split())) for i in range(rows)]

row_min = map(min, cost)
col_max = map(max, zip(*cost))

min_max = max(row_min)
max_min = min(col_max)

print(min_max if min_max == max_min else "Error")
