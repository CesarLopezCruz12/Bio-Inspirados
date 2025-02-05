import math
import matplotlib.pyplot as plt
import numpy as np

# Definir la función f(t)


def f(t):
    return math.sin((2 * math.pi * t) / 5 + 0.2)

# Definir la función t(f(t))


def t_f(t):
    return t * f(t)

# Definir la derivada de f(t)


def df(t):
    return (2 * math.pi / 5) * math.cos((2 * math.pi * t) / 5 + 0.2)


# Definir el intervalo de tiempo y el número de puntos
tiempo_inicial = 0
tiempo_final = 20  # Dos periodos completos (10 segundos por periodo)
puntos = 1000  # Puedes ajustar este número para controlar la resolución

# Calcular los valores de f(t) en intervalos de tiempo
intervalo_tiempo = (tiempo_final - tiempo_inicial) / puntos
valores_f = [f(tiempo_inicial + i * intervalo_tiempo) for i in range(puntos)]

# Calcular los valores de t(f(t)) a partir de los valores de f(t)
valores_t_f = [t_f(tiempo_inicial + i * intervalo_tiempo)
               for i in range(puntos)]

# Calcular los valores de la derivada df(t) en intervalos de tiempo
valores_df = [df(tiempo_inicial + i * intervalo_tiempo) for i in range(puntos)]

# Encontrar los puntos donde la pendiente es más cercana a cero
tolerancia = 0.1  # Establece una tolerancia para considerar pendiente cercana a cero
puntos_cercanos_a_cero = [i for i, df in enumerate(
    valores_df) if abs(df) < tolerancia]

# Crear una lista de valores de tiempo
valores_tiempo = [tiempo_inicial + i * intervalo_tiempo for i in range(puntos)]

# Crear la gráfica de t(f(t)) y marcar los puntos cercanos a cero
plt.figure(figsize=(10, 6))
plt.plot(valores_tiempo, valores_t_f, label='t(f(t))')
plt.scatter([valores_tiempo[i] for i in puntos_cercanos_a_cero], [valores_t_f[i]
            for i in puntos_cercanos_a_cero], c='red', marker='o', label='Pendiente cercana a cero')
plt.xlabel('Tiempo')
plt.ylabel('t(f(t))')
plt.title('Gráfica de t(f(t)) con Puntos de Pendiente Cercana a Cero')
plt.grid(True)
plt.legend()
plt.show()
