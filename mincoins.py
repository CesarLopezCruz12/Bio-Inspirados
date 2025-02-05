import matplotlib.pyplot as plt
import numpy as np

def min_coins():
    # Solicitar al usuario que ingrese las denominaciones de monedas separadas por comas
    #coins_str = input("Ingresa las denominaciones de monedas separadas por comas: ")
    #coins = [int(x) for x in coins_str.split(',')]
    coins = [1,2,5,10]
    # Solicitar al usuario que ingrese el valor máximo al que desea llegar
    #target_amount = int(input("Ingresa el valor máximo al que deseas llegar: "))
    target_amount = 30
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0
    coin_used = [-1] * (target_amount + 1)  # Para rastrear las monedas utilizadas

    for coin in coins:
        for i in range(coin, target_amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Recuperar las monedas utilizadas
    used_coins = []
    amount = target_amount
    while amount > 0:
        used_coins.append(coin_used[amount])
        amount -= coin_used[amount]

    # Crear una gráfica de líneas de la matriz dp
    plt.figure(figsize=(10, 6))
    plt.plot(range(target_amount + 1), dp, marker='o', linestyle='-')
    plt.xlabel('Valor')
    plt.ylabel('Número mínimo de monedas')
    plt.title('Matriz de Programación Dinámica (dp)')
    plt.grid(True)
    plt.show()

    return dp[target_amount], used_coins

# Ejecutar la función y obtener el número mínimo de monedas y las monedas utilizadas
min_num_coins, used_coins = min_coins()
print("Número mínimo de monedas:", min_num_coins)
print("Monedas utilizadas:", used_coins)
