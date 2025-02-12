def read_file(filename):
    values = []
    weights = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # First line is the capacity
        capacity = int(lines[0].strip())
        
        # Each next line is value and weight
        for line in lines[1:]:
            value, weight = map(int, line.strip().split())
            values.append(value)
            weights.append(weight)
    
    return capacity, values, weights


def knapsack(capacity, weights, values):
    if len(weights) == 0 or len(weights) != len(values) or capacity < 0:
        raise ValueError("Invalid input")

    N = len(weights)
    DP = [[0] * (capacity + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        w, v = weights[i - 1], values[i - 1]

        for sz in range(1, capacity + 1):
            DP[i][sz] = DP[i - 1][sz]
            if sz >= w and DP[i - 1][sz - w] + v > DP[i][sz]:
                DP[i][sz] = DP[i - 1][sz - w] + v

    items_selected = []
    sz = capacity
    for i in range(N, 0, -1):
        if DP[i][sz] != DP[i - 1][sz]:
            item_index = i - 1
            items_selected.append(item_index)
            sz -= weights[item_index]

    return DP[N][capacity], items_selected


filename = '1'
capacity, values, weights = read_file(filename)
max_profit, items_selected = knapsack(capacity, weights, values)

print("Maximum Profit:", max_profit)
print("Items Selected (0-based indices):", items_selected)
