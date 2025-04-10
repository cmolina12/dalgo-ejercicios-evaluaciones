

import heapq

def dijkstra(adj, origen):
    
    distancias = {node: float('inf') for node in adj}
    visitados = {node: False for node in adj}
    
    distancias[origen] = 0
    pq = [[0,origen]]
    
    while pq:
        d_actual, nodo = heapq.heappop(pq)
        
        if visitados[nodo]:
            continue
        
        visitados[nodo] = True
        
        for vecino, peso in adj[nodo]:
            
            if distancias[vecino] > d_actual + peso:
                distancias[vecino] = d_actual + peso
                heapq.heappush(pq, (distancias[vecino], vecino))
                
    return distancias, visitados



adj = {
    'A': [('B', 4), ('C', 2)],  # A → B, A → C
    'B': [('A', 4), ('D', 5)],  # B → A, B → D
    'C': [('A', 2), ('D', 1)],  # C → A, C → D
    'D': [('B', 5), ('C', 1)]   # D → B, D → C
}

origen = 'A'

resultado = dijkstra(adj, origen)

print(resultado)


for node in adj:
    print(node)








import heapq

def dijsktra2(adj, origen):
    
    distancias = {node: float('inf') for node in adj}
    visitados = {node: False for node in adj}
    
    visitados[origen] = True
    distancias[origen] = 0
    
    heap = [[0,origen]]
    
    while heap:
        dist_actual, nodo = heapq.heappop(heap)
        
        for vecino, peso in adj[nodo]:
            visitados[vecino] = True
            if dist_actual + peso < distancias[vecino]:
                distancias[vecino] = dist_actual + peso
                heapq.heappush(heap, (distancias[vecino], vecino))
                
    return distancias

adj = {
    'A': [('B', 4), ('C', 2)],  # A → B, A → C
    'B': [('A', 4), ('D', 5)],  # B → A, B → D
    'C': [('A', 2), ('D', 1)],  # C → A, C → D
    'D': [('B', 5), ('C', 1)]   # D → B, D → C
}

origen = 'A'

resultado = dijsktra2(adj, origen)

print("Dijkstra 2")
print(resultado)


for node in adj:
    print(node)