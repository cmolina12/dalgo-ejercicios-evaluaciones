
# Problema Programacion Dinamica - Suma Maxima en una Matriz

# Dada una matriz a de tamaño m x n de numeros enteros (puede contener negativos), calcular la fila i y la columna j en la cual la suma de los elementos de la submatriz que va desde la fila 0 y columna 0 hasta la fila i y la columna j sea máxima

def suma_maxima_matriz(matrix):
    m = len(matrix) # Tamaño columnas
    n = len(matrix[0]) # Tamaño filas
    dp = [[0 for _ in range(n)] for _ in range(m)] # Inicializamos la matriz dp
    max_sum = float('-inf') # Inicializamos la suma maxima a infinito negativo
    max_i, max_j = 0, 0 # Inicializamos las coordenadas de la suma maxima


    for i in range(m): # Recorremos las columnas
        for j in range(n): # Recorremos las filas
        
            dp[i][j] = matrix[i][j] # Asignamos el valor de la matriz a la matriz dp
            
            if i > 0: # Si estamos en la fila 1 en adelante
                dp[i][j] += dp[i-1][j] # Sumamos el valor de la fila anterior
                
            if j > 0: # Si estamos en la columna 1 en adelante
                dp[i][j] += dp[i][j-1]
                
            if i > 0 and j > 0: # Si estamos en la fila 1 y columna 1 en adelante
                dp[i][j] -= dp[i-1][j-1] # Restamos el valor de la fila y columna anterior
                
            if dp[i][j] > max_sum: # Si el valor de la matriz dp es mayor que la suma maxima
                max_sum = dp[i][j] # Actualizamos la suma maxima
                max_i, max_j = i, j # Actualizamos las coordenadas de la suma maxima
            
    return max_sum, max_i, max_j, dp # Retornamos la suma maxima y las coordenadas

matrix = [
            [1, 2, -1, -4, -20],
            [-8, -3, 4, 2, 1],
            [3, 8, 10, 1, 3],
            [-4, -1, 1, 7, -6]
        ]

print(suma_maxima_matriz(matrix)) # (29, 2, 2)