def greedy_knapsack(values, weights, capacity):
    n = len(values)
    value_per_weight = [(v / w, v, w) for v, w in zip(values, weights)]
    value_per_weight.sort(reverse=True)

    knapsack = [0] * n  # Initialize the knapsack as empty

    kw = 0
    kv = 0

    for i in range(n):
        _, v, w = value_per_weight[i]
        if kw + w <= capacity:
            knapsack[i] = 1  # Include the item in the knapsack
            kw += w
            kv += v
    return kv, knapsack  # Return the total value and selected items

# Example usage:
values = [120, 60, 100]
weights = [30, 10, 20]
capacity = 50
optimal_value, selected_items = greedy_knapsack(values, weights, capacity)
print("Optimal Value:", optimal_value)
print("Selected Items (1 indicates inclusion, 0 indicates exclusion):", selected_items)
