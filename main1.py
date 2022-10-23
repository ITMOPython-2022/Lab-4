backpack_items = {
    'в': [3, 25, 0, 0],
    'п': [2, 15, 0, 0],
    'б': [2, 15, 0, 0],
    'а': [2, 10, 0, 0],
    'и': [1, 5, 1, 0],
    'н': [1, 15, 0, 0],
    'т': [3, 20, 0, 0],
    'о': [1, 25, 0, 0],
    'ф': [1, 15, 0, 0],
    'д': [1, 10, 1, 0],
    'к': [2, 20, 0, 0],
    'р': [2, 20, 0, 0]
}


def get_memtable(items, max_area):
    area = [items[item][0] for item in items]
    value = [items[item][1] for item in items]
    n = len(value)

    table = [[0 for a in range(max_area + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(max_area + 1):
            if i == 0 or a == 0:
                table[i][a] = 0

            elif area[i - 1] <= a:
                table[i][a] = max(value[i - 1] + table[i - 1][a - area[i - 1]], table[i - 1][a])

            else:
                table[i][a] = table[i - 1][a]

    return table, area, value


def get_selected_items_list(_items, max_area=9, sick='no'):
    items = {}
    if sick == 'no':
        for key, item in _items.items():
            if item[2] == 0:
                items[key] = item

    table, area, value = get_memtable(items, max_area)
    names = [key for key, value in items.items()]

    # for i, row in enumerate(table):
    #     if i >= 1:
    #         print(names[i - 1], row)
    #     else:
    #         print(" ", row)

    n = len(value)
    res = table[n][max_area]
    print("Итоговые очки выживания: ", res + 10)
    a = max_area
    items_list = []

    if res < 0:
        print("Том умер")
        return

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][a]:
            continue
        else:
            items_list.append(names[i - 1])
            res -= value[i - 1]
            a -= area[i - 1]

    k = 0
    # print(items_list)
    while len(items_list) or k < 1:
        free = 3
        k += 1
        i = 0
        row = ''
        while i < len(items_list) or free > 0:
            item = items_list[i]
            if item:
                size = backpack_items[item][0]
                if size <= free:
                    row += f'[{item}] ' * size
                    free -= size
                    items_list.remove(item)
                    i = 0
                else:
                    i += 1

        print(row)

    return


get_selected_items_list(backpack_items)
