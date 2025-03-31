import timeit
import matplotlib.pyplot as plt
import numpy as np
import sys

# Aumentar el límite de recursión para permitir cálculos más grandes
sys.setrecursionlimit(10000)

# Implementación pura de Divide and Conquer para el problema Egg Drop
def egg_drop_pure_divide_conquer(n, k):
    """
    Implementación pura de Divide and Conquer para el problema Egg Drop.
    n: número de huevos
    k: número de pisos
    """
    # Casos base
    if k == 0 or k == 1:
        return k
    if n == 1:
        return k
    
    min_intentos = float('inf')
    
    # DIVIDIR: Probamos lanzar el huevo desde cada piso
    for x in range(1, k + 1):
        # CONQUISTAR: Resolvemos los subproblemas recursivamente
        
        # Caso 1: El huevo se rompe en el piso x
        se_rompe = egg_drop_pure_divide_conquer(n - 1, x - 1)
        
        # Caso 2: El huevo no se rompe en el piso x
        no_se_rompe = egg_drop_pure_divide_conquer(n, k - x)
        
        # COMBINAR: Tomamos el peor caso (máximo) y añadimos 1 por el intento actual
        intentos = 1 + max(se_rompe, no_se_rompe)
        
        # Actualizamos el mínimo
        min_intentos = min(min_intentos, intentos)
    
    return min_intentos

# Lista de valores de n y k más pequeños para evitar tiempos de ejecución excesivos
test_cases = [
    (1, 5), (1, 10), (1, 15),(2, 5), (2, 8),
    (2, 10),(2, 12), (2, 15),(3, 4), (3, 6), 
    (3, 8), (3, 10), (4, 5), (4, 7), (4, 9), 
    (4, 11),(5, 4), (5, 6), (5, 8),(3, 12), 
    (3, 15), (3, 18),(4, 12), (4, 14),(4, 15),
    (4, 17),(5, 10), (5, 12),(5,17),(5,18)
]

# Medir tiempos de ejecución
execution_times = []
theoretical_values = []

print("Midiendo tiempos de ejecución para Divide and Conquer puro...")
for n, k in test_cases:
    try:
        # Usar un número menor de repeticiones para evitar tiempos excesivos
        number_of_runs = 1  # Solo una ejecución para los casos más pesados
        time_taken = timeit.timeit(lambda: egg_drop_pure_divide_conquer(n, k), number=number_of_runs) / number_of_runs
        execution_times.append(time_taken)
        
        # Complejidad teórica O(k^n) para Divide and Conquer puro
        theoretical_value = k ** n
        theoretical_values.append(theoretical_value *1e-6)
        
        print(f"Caso (n={n}, k={k}) completado en {time_taken:.6f} segundos - Valor teórico: {theoretical_value}")
    except RecursionError:
        print(f"RecursionError para (n={n}, k={k}). Saltando este caso.")
        # Agregar None para mantener consistencia en los índices
        execution_times.append(None)
        theoretical_values.append(None)

# Filtrar casos donde hubo RecursionError
valid_indices = [i for i, t in enumerate(execution_times) if t is not None]
valid_execution_times = [execution_times[i] for i in valid_indices]
valid_theoretical_values = [theoretical_values[i] for i in valid_indices]
valid_test_cases = [test_cases[i] for i in valid_indices]

# Encontrar el factor de escala óptimo para ajustar la curva teórica a los datos reales
if valid_execution_times and valid_theoretical_values:
    scale_factor = np.sum(valid_execution_times) / np.sum(valid_theoretical_values)
    theoretical_times = [val * scale_factor for val in valid_theoretical_values]
    
    print(f"\nFactor de escala para O(k^n): {scale_factor:.12f}")
    
    # Graficar los resultados
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))
    
    # Primera gráfica: Tiempo experimental vs teórico
    axs[0].plot(range(len(valid_execution_times)), valid_execution_times, label="Tiempo experimental", marker='o')
    axs[0].plot(range(len(theoretical_times)), theoretical_times, label="Tiempo teórico O(k^n)", linestyle='dashed')
    axs[0].set_xlabel("Casos de prueba")
    axs[0].set_ylabel("Tiempo de ejecución (s)")
    axs[0].set_title("Comparación de tiempos de ejecución (teórico vs real)")
    axs[0].legend()
    axs[0].grid(True, linestyle='--', alpha=0.7)
    
    # Segunda gráfica: Etiquetas (n, k) en el eje x
    nk_labels = [f"({n},{k})" for n, k in valid_test_cases]
    axs[1].plot(nk_labels, valid_execution_times, marker='o', linestyle='-', color='r')
    axs[1].set_xlabel("(n, k)")
    axs[1].set_ylabel("Tiempo de ejecución (s)")
    axs[1].set_title("Tiempo de ejecución de eggDrop - Divide and Conquer")
    axs[1].tick_params(axis='x', rotation=90)
    axs[1].grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('egg_drop_dac_analysis.png', dpi=300, bbox_inches='tight')
