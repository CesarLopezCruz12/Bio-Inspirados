import matplotlib.pyplot as plt

def knapsack():
    # Solicitar al usuario que ingrese los valores, pesos y la capacidad
    #values_str = input("Ingresa los valores de los objetos separados por comas: ")
    #weights_str = input("Ingresa los pesos de los objetos separados por comas: ")
    #capacity = int(input("Ingresa la capacidad de la mochila: "))

    # Convertir las cadenas en listas de valores y pesos
    #values = [int(x) for x in values_str.split(',')]
    #weights = [int(x) for x in weights_str.split(',')]

    values = [120, 60, 100]
    weights = [30, 10, 20]
    capacity = 90

    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    
        

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    plt.figure(figsize=(8, 6))
    plt.imshow(dp, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Valor')
    plt.xlabel('Capacidad de la mochila')
    plt.ylabel('Objetos')
    plt.title('Matriz de Programación Dinámica (dp)')
    plt.show()

    print("Matriz dp:")
    for row in dp:
        print(row)

    return dp[n][capacity], selected_items
    

    
# Ejecutar la función y obtener resultados
max_value, selected_items = knapsack()
print("Valor máximo:", max_value)
print("Elementos seleccionados:", selected_items)
