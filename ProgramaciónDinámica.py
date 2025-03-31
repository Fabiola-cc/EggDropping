import timeit
import matplotlib.pyplot as plt

# Function to find minimum number of attempts 
# needed in order to find the critical floor
def eggDrop(n, k):
    '''
    Este código fue obtenido de la página:
    https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

    Implementa una solución al Problema 'Egg Dropping Puzzle'
    Usando la técnica de tabulación (bottom-up), 
    pero con una optimización para mejorar el tiempo de ejecución.
    '''
    # create a 2D table to store the results
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    
    # to count the number of moves
    cnt = 0
    
    # while the number of floors is less than k
    while dp[cnt][n] < k:
        cnt += 1
        
        # for each egg
        for i in range(1, n + 1):
            dp[cnt][i] = 1 + dp[cnt - 1][i - 1] + dp[cnt - 1][i]
    return cnt

# Lista de valores de n y k para probar
test_cases = [
    (2, 10), (3, 15), (4, 20), (5, 25), (6, 30), (7, 35), (8, 40), (9, 45), (10, 50),
    (2, 50), (3, 60), (4, 70), (5, 80), (6, 90), (7, 100), (8, 110), (9, 120), (10, 130),
    (2, 150), (3, 170), (4, 200), (5, 220), (6, 250), (7, 280), (8, 300), (9, 350), (10, 400),
    (2, 500), (3, 600), (4, 700)
]

# Medir tiempos de ejecución
execution_times = []
theoretical_times = []

for n, k in test_cases:
    time_taken = timeit.timeit(lambda: eggDrop(n, k), number=10) / 10
    execution_times.append(time_taken)
    theoretical_times.append(n * k * 1e-6)  # Aproximación teórica O(n*k)

# Graficar los resultados en un solo figure con dos subgráficos
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Primera gráfica: Tiempo experimental vs teórico
axs[0].plot(range(len(test_cases)), execution_times, label="Tiempo experimental", marker='o')
axs[0].plot(range(len(test_cases)), theoretical_times, label="Tiempo teórico O(n*k)", linestyle='dashed')
axs[0].set_xlabel("Casos de prueba")
axs[0].set_ylabel("Tiempo de ejecución (s)")
axs[0].set_title("Comparación de tiempos de ejecución (worst case vs real)")
axs[0].legend()

# Segunda gráfica: Etiquetas (n, k) en el eje x
nk_labels = [f"({n},{k})" for n, k in test_cases]
axs[1].plot(nk_labels, execution_times, marker='o', linestyle='-', color='b')
axs[1].set_xlabel("(n, k)")
axs[1].set_ylabel("Tiempo de ejecución (s)")
axs[1].set_title("Tiempo de ejecución de eggDrop - Programación Dinámica")
axs[1].tick_params(axis='x', rotation=90)
axs[1].grid()

plt.tight_layout()
plt.show()