from collections import deque

def componentes_conectadas (grafo):
    
    componentes = 0
    visitados = {nodes: False for nodes in grafo}
    
    for nodo in grafo:
        if visitados[nodo]:
            continue
        
        componentes += 1
        
        queue = deque()
        queue.append(nodo)
        
        visitados[nodo] = True
    
        while queue:
            current = queue.popleft()
            
            for vecino in grafo[current]:
                if not visitados[vecino]:
                    visitados[vecino] = True
                    queue.append(vecino)
                
                
    return componentes
                
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

resultado = componentes_conectadas(grafo)

print(resultado)
