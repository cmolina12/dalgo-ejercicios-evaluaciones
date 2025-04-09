from collections import deque

def patron_matriz(matriz, inicial):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    visitados = [[False] * columnas for _ in range(filas)]
    
    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    
    visitados[inicial[0]][inicial[1]] = True
    queue = deque()
    queue.append(inicial)
    
    while queue:
        i, j = queue.popleft()
        
    