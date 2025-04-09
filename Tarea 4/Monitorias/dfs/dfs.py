from collections import deque

def dfs (inicial, adj, visitado):
    print(f"Visitando nodo: {inicial}")
    visitado[inicial] = True
    
    for neighbor in adj[inicial]:
        if not visitado[neighbor]:
            dfs(neighbor, adj, visitado)





# Inicialización
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'E'],
    'C': ['A'],
    'D': [],
    'E': ['B']
}


        
        
def dfs (inicial, adj):
    
    visitado = {node: False for node in adj}
    pila = deque()
    pila.append(inicial)
    
    while pila:
        
        nodo = pila.pop()
        
        for neighbor in nodo:
            if not visitado[neighbor]:
                visitado[neighbor] = True
                pila.append(neighbor)