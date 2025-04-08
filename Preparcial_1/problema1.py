
def pascal_triangle(N):
    dp = [[1] * (i + 1) for i in range(N)]  # Inicializamos la estructura de la tabla
    
    for i in range(2,N):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp

# Ejemplo de uso
N = 5
resultado = pascal_triangle(N)

for fila in resultado:
    print(fila)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

