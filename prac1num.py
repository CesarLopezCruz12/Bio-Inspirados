import numpy as np

# Genera una lista de 100 números aleatorios de punto flotante entre -1000 y 1000
num_mtz = np.random.randint(-1000, 1001, 100)

# Imprime la lista de números aleatorios
print(num_mtz)
# Encuentra los dos números más pequeños y los dos números más grandes
sml_nums = np.partition(num_mtz, 2)[:2]
lag_nums = np.partition(num_mtz, -2)[-2:]

# Imprime los resultados
print("Los dos números más pequeños son:", sml_nums)
print("Los dos números más grandes son:", lag_nums)