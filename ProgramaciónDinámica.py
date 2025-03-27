'''
Este código fue obtenido de la página:
https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

Implementa una solución al Problema 'Egg Dropping Puzzle'
Usando la técnica de tabulación (bottom-up), 
pero con una optimización para mejorar el tiempo de ejecución.
'''

# Function to find minimum number of attempts 
# needed in order to find the critical floor
def eggDrop(n, k):
    
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

if __name__ == "__main__":
    n = 2
    k = 10
    print(eggDrop(n, k))
