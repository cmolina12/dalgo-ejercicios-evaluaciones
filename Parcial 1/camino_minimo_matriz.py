
#Dada una matriz a[m][n] de números enteros positivos, encuentra el camino desde (0,0) hasta (m-1,n-1) con la menor suma posible.
#Solo puedes moverte hacia la derecha (→) o hacia abajo (↓).

def min_path_sum(matrix):
    columnas = len(matrix)
    filas = len(matrix[0])
    
    dp = [[0]*filas for _ in range(columnas)]
    
    # Inicializamos la primera celda 
    dp[0][0] = matrix[0][0]
    
    # Para primera fila porque solo desde izquierda
    for j in range(1,filas):
        dp[0][j] = matrix[0][j] + dp[0][j-1]

    # Para la primera columna donde solo podemos venir de arriba
    for i in range(1, columnas):
        dp[i][0] = matrix[i][0] + dp[i-1][0]
        
    # Recursion
    
    for i in range(1,filas):
        for j in range(1,columnas):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i][j-1])
            
    # Respuesta en la ultima celda de la matriz dp  
    return dp[filas-1][columnas-1]

