class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def knapsack(items, capacity):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)

        return node_value
    

    def branch_bound(i, weight, value):
        nonlocal max_value
        if weight <= capacity and value > max_value:
            max_value = value
        if i == len(items):
            return 0
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i+1, weight, value)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            branch_bound(i+1, weight + items[i].weight, value + items[i].value)


    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    branch_bound(0, 0, 0)
    return max_value


if __name__ == '__main__':
    items = [Item(3, 700), Item(1, 300), Item(2, 500),
             Item(2, 550), Item(3, 800)]
    capacity = 4
    max_value = knapsack(items, capacity)
    print(max_value)