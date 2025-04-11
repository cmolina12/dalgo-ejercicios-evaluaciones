

def problema_C(grafo, n):
    
    distancia = [[float('inf')]*n for _ in range(n)]
    
    for nodo in range(n):
        distancia[nodo][nodo] = 0
        
    for u, v, peso in grafo:
        distancia[u][v] = peso
        distancia[v][u] = peso  # <- esta línea nueva
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancia[i][k] + distancia[k][j] < distancia[i][j]:
                    distancia[i][j] = distancia[i][k] + distancia[k][j]
                    
                    
                    
    mejor_ciudad = None
    mejor_promedio = float('inf')
    for i in range(n):
        total = 0
        alcanzables = 0
        for j in range(n):
            if i != j and distancia[i][j] != float('inf'):
                total += distancia[i][j]
                alcanzables += 1
                
        if alcanzables > 0:
            promedio = total/alcanzables
            if promedio < mejor_promedio:
                mejor_promedio = promedio
                mejor_ciudad = i
        
    return mejor_ciudad, mejor_promedio
    
n = 4
grafo = [
    (0, 1, 600000),  # Bogotá → Medellín
    (0, 2, 500000),  # Bogotá → Cali
    (1, 3, 900000),  # Medellín → Barranquilla
    (3, 2, 400000),  # Barranquilla → Cali
    (1, 2, 300000),  # Medellín → Cali
    (0, 3, 800000)   # Bogotá → Barranquilla
]



#ciudad, costo_prom = georgefloyd(grafo, n)

#nombres = ["Bogotá", "Medellín", "Cali", "Barranquilla"]
#print(f"La mejor ciudad es {nombres[ciudad]} con un promedio de {costo_prom:.0f}")

# Bogota - 0
# Medellin - 1
# Cali 








def floydwarshall2(grafo, n):
    
    distancia = [[float('inf')]*n for _ in range(n)]
    
    # 1
    
    for nodo in range(n):
        distancia[nodo][nodo] =0
        
    # 2
    for u, v, peso in grafo:
        distancia[u][v] = peso
        distancia[v][u] = peso
        
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancia[i][k] + distancia[k][j] < distancia[i][j]:
                    distancia[i][j] = distancia[i][k] + distancia[k][j]
                    
    mejor_ciudad = None
    mejor_promedio = float('inf')

    
    for i in range(n):
        total = 0
        alcanzables = 0
        for j in range(n):
            if i != j and distancia[i][j] != float('inf'):
                alcanzables += 1
                total += distancia[i][j]
                
        if alcanzables >= 1:
            promedio = total/alcanzables
            if promedio < mejor_promedio:
                mejor_promedio = promedio
                mejor_ciudad = i
                
    return mejor_ciudad, mejor_promedio
        
        
        
    
n = 4
grafo = [
    (0, 1, 600000),  # Bogotá → Medellín
    (0, 2, 500000),  # Bogotá → Cali
    (1, 3, 900000),  # Medellín → Barranquilla
    (3, 2, 400000),  # Barranquilla → Cali
    (1, 2, 300000),  # Medellín → Cali
    (0, 3, 800000)   # Bogotá → Barranquilla
]

ciudades = {
    0: "Bogotá",
    1: "Medellín",
    2: "Cali",
    3: "Barranquilla"
}

print("Prueba 2")
indice, promedio = floydwarshall2(grafo, n)

nombre = ciudades[indice]

print(nombre, promedio)