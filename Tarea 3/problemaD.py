

def max_coins(grid):
    
    filas = len(grid)
    columnas = len(grid[0])
    
    # Inicializar dp
    
    dp = [[float('-inf')]*columnas for _ in range(filas)]
    
    # Inicializar primera columna
    
    for fila in range(filas):
        if grid[fila][0] != "-1":
            dp[fila][0] = grid[fila][0]
            
    # Iterar
    
    for j in range(1,columnas):
        for i in range(filas):
            
            if grid[i][j] == "-1":
                dp[i][j] = float('-inf')
                continue
            
            # Tres opciones
            
            best_prev = dp[i][j-1] #Venir desde la izquierda primero
            
            if i > 0: # Si estamos en la fila 0 no podemos venir de arriba
                best_prev = max(best_prev, dp[i-1][j-1]) #Mejor opcion entre venir de la izquierda y venir de arriba
            if i < filas-1: # Si estamos en la ultima fila no podemos venir de abajo
                best_prev = max(best_prev, dp[i+1][j-1]) # Mejor opcion entre venir de la izquierda y venir de arriba
                
            # Actualizamos segun la mejor opcion
            
            dp[i][j] = grid[i][j] + best_prev


    # Retornar el mejor resultado encontrado, que estara en la ultima columna
    
    maximos = []
    for i in range(filas):
        maximos.append(dp[i][columnas-1])
    maximo = max(maximos)
    
    return maximo

# Ejemplo de uso

grid = [[0, 1, 2, 3, 4],
        
        [5, 6, 7, 8, 9],
        
        [10, 11, 12, 13, 14]]

max_monedas = max_coins(grid)
print(max_monedas)
