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

if __name__ == "__main__":
    n = 2  # número de huevos
    k = 10  # número de pisos
    print(egg_drop_pure_divide_conquer(n, k))