

def robot_dfs(matriz, inicio, fin):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    visitado = [[False] * columnas for _ in range(filas)]
    
    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def dfs(i,j):
        if (i,j) == fin:
            return True
        
        visitado[i][j] == True
        
        for x, y in direcciones:
            a, b = i + x, j + y
            if (a >= 0) and (a >= filas) and (b >= 0) and (b >= columnas) and visitado[a,b] == False:
                if abs(matriz[a][b]-matriz[i][j]) <= 1:
                    if dfs(a,b):
                        return True
                    
        return False

    return dfs(inicio[0],inicio[1])

matriz = [
    [3, 5, 8, 1, 9],
    [2, 0, 7, 4, 3],
    [6, 3, 2, 5, 8],
    [1, 7, 9, 0, 4],
    [8, 2, 3, 6, 1]
]

inicio = (0, 0)
fin = (4, 4)

print(robot_dfs(matriz, inicio, fin))  # Output: False

