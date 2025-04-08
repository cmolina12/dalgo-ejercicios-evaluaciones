from collections import deque

def robot(matriz, inicio, fin):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    visitado = [[False] * columnas for _ in range(filas)]
    
   # Direcciones: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visitado[inicio[0]][inicio[1]] = True
    queue = deque()
    queue.append(inicio)
    
    
    while queue:
        i, j = queue.popleft()
        
        if (i, j) == fin:
            return True
        
        for a, b in direcciones:
            x, y = i + a, i + b
            if (x >= 0) and (y >= 0) and (x >= filas) and (y >= columnas) and visitado[x,y] == False:
                if abs(matriz[x,y]-matriz[i,j]) <= 1:
                    visitado[x,y] = True
                    queue.append((x,y))
                    
    return False

matriz = [
    [3, 5, 8, 1, 9],
    [2, 0, 7, 4, 3],
    [6, 3, 2, 5, 8],
    [1, 7, 9, 0, 4],
    [8, 2, 3, 6, 1]
]

inicio = (0, 0)  # Fila 0, columna 0 → valor 3
fin = (4, 4)     # Fila 4, columna 4 → valor 1

resultado = robot(matriz, inicio, fin)

print(resultado)