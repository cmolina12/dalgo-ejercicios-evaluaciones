
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

visitado = {nodo: False for nodo in grafo}

for nodo in grafo:
    if not visitado[nodo]:
        dfs(nodo, grafo, visitado)
        
