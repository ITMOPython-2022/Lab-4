def knapsack(C, weight, cost, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i - 1] <= j:
                K[i][j] = max(cost[i - 1] + K[i - 1][j - weight[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K


items = ['rifle', 'pistol', 'ammo', 'medkit', 'inhaler', 'knife',
        'axe', 'talisman', 'flask', 'food', 'crossbow']
values = [25, 15, 15, 20, 5, 15, 20, 25, 15, 20, 20]
weights = [3, 2, 2, 2, 1, 1, 3, 1, 1, 2, 2]
capacity = 8
all_points = sum(values)
init_points = 25
count = len(values)

K = knapsack(capacity, weights, values, count)

i, j, total = count, capacity, 0
res = K[count][capacity]
while i > 0 and res > 0:
    if res != K[i - 1][j]:
        print(items[i - 1], "value", values[i - 1], "points,", weights[i - 1], "cells")
        total += weights[i - 1]
        res -= values[i - 1]
        j -= weights[i - 1]
    i -= 1
print("\nTotal weight:", total, "\b, knapsack value:", K[count][capacity])
points = K[count][capacity] + init_points - (all_points - K[count][capacity])
print("Overall value", all_points)
print("Total value", points)

