from collections import deque

def bfs (adj, inicial):
    
    visited = {node: False for node in adj}
    distancia = {node: float('inf') for node in adj}
    
    queue = deque()
    
    visited[inicial] = True
    distancia[inicial] = 0
    queue.append(inicial)
    
    while queue:
        current = queue.popleft()
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distancia[neighbor] = distancia[current] + 1
                queue.append(neighbor)
            
    return distancia

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

inicial = 'A'

resultado = bfs(grafo,inicial)

print(resultado)





def bfs_2(adj, inicial):
    
    visitados = {nodes: False for nodes in adj}
    distancias = {nodes: float("inf") for nodes in adj}
    
    visitados[inicial] = True
    distancias[inicial] = 0
    queue = deque()
    queue.append(inicial)
    
    while queue:
        current = queue.popleft()
        for neighbor in adj[current]:
            if visitados[neighbor] == False:
                visitados[neighbor] = True
                distancias[neighbor] = 1 + distancias[current]
                queue.append(neighbor)
                
    return distancias

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

inicial = 'A'

resultado = bfs_2(grafo,inicial)

print(f"Resultado:{resultado}")