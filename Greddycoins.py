def greedy_coin_machine(coins, target_amount):
    coins.sort(reverse=True)
    change = []
    remaining_amount = target_amount

    for coin in coins:
        while remaining_amount >= coin:
            change.append(coin)
            remaining_amount -= coin

    if remaining_amount == 0:
        return change
    else:
        return None

# Example usage:
coins = [25, 10, 5, 1]
target_amount = 63
change = greedy_coin_machine(coins, target_amount)
if change:
    print("Modenas:", change)
else:
    print("Solución no encontrada.")
