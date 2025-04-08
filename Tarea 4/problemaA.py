from collections import deque

def can_divide_into_teams(n, conflicts):
    if n == 0: # Si no hay jugadores, se pueden dividir en equipos.
        return True 
    
    # Construir la lista de adyacencia
    adj = [[] for _ in range(n)] 
    for a, b in conflicts: # Añadir conflictos como aristas en el grafo.
        adj[a].append(b) # Añadir conflicto entre a y b. Es decir, b es enemigo de a.
        adj[b].append(a) # Añadir conflicto entre b y a. Es decir, a es enemigo de b.
    
    color = [0] * n  # 0: sin color, 1: equipo A, -1: equipo B
    
    for i in range(n): # Recorrer cada jugador.
        if color[i] == 0:  # Si el jugador no tiene equipo asignado.
            queue = deque([i])  # Cola BFS iniciada en el jugador 'i'.
            color[i] = 1  # Asignar Equipo A.
            
            while queue: # Mientras haya jugadores en la cola.
                node = queue.popleft()  # Sacar el primer jugador de la cola.
                for neighbor in adj[node]:  # Recorrer sus enemigos.
                    if color[neighbor] == color[node]:  # Si están en el mismo equipo → Conflicto.
                        return False
                    if color[neighbor] == 0:  # Si no tiene equipo, asignar el opuesto.
                        color[neighbor] = -color[node]
                        queue.append(neighbor)  # Agregar a la cola para procesar sus enemigos.
    return True

#Ejemplo 1: Caso básico sin conflictos
n = 4
conflicts = []
print(can_divide_into_teams(n, conflicts))  # Salida esperada: True

#Ejemplo 2: Caso con un conflicto simple
n = 2
conflicts = [(0, 1)]
print(can_divide_into_teams(n, conflicts))  # Salida esperada: True

#Ejemplo 3: Caso con un conflicto que no permite dividir en equipos
n = 3
conflicts = [(0, 1), (1, 2), (2, 0)]
print(can_divide_into_teams(n, conflicts))  # Salida esperada: False

#Ejemplo 4: Caso con un conflicto que permite dividir en equipos
n = 4
conflicts = [(0, 1), (1, 2), (2, 3), (3, 0)]
print(can_divide_into_teams(n, conflicts))  # Salida esperada: True