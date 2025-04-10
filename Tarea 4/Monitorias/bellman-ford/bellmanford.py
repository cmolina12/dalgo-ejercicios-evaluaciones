
def bellmanford(lista):
    
    nodos = set()
    
    for u, v, peso in lista:
        nodos.add(u)
        nodos.add(v)
        
    n = len(nodos)
    
    distancia = {n: float('inf') for n in nodos}
    
    distancia['A'] = 0
    
    for _ in range(n-1):
        for u, v, peso in lista:
            if distancia[u] + peso < distancia[v]:
                distancia[v] = distancia[u] + peso
                
    # Ciclo negativo
    
    for u, v, peso in lista:
        if distancia[u] + peso < distancia[v]:
            return True
    
    return False, distancia
    

    
    


lista = [('A','B',4), 
         
         ('B','C',2)]

resultado = bellmanford(lista)

print(resultado)





#lista de aristas

def bellmanford2(lista):
    
    nodos = set()
    
    for u, v, _ in lista:
        nodos.add(u)
        nodos.add(v)
        
    n = len(nodos)
    
    distancias = {node: float('inf') for node in nodos}
    
    distancias['A'] = 0
    
    for _ in range(n-1):
        for u, v , peso in lista:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                
    # Revisar ciclo negativo
    
    for u, v, peso in lista:
        if distancias[u] + peso < distancias[v]:
            return True
        
    return False, distancias

lista = [('A','B',4), 
         
         ('B','C',2)]

print("prueba 2")

resultado = bellmanford2(lista)

print(resultado)