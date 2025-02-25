
def submatriz(matrix):
    
    filas = len(matrix)
    columnas = len(matrix[0])
    
    max_side = 0
    
    dp = [[0] * columnas for _ in range(filas)]
    
    if not matrix:
        return 0
    
    for i in range(filas):
        for j in range(columnas):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    
                max_side = max(max_side,dp[i][j])
                
    return max_side

matrix = [[1,1,1,0],
          [0,1,1,0]
          ]
    
print(submatriz(matrix))