from collections import deque

def bfs_oompaloompa(grafo, inicial):
    color = {node: 0 for node in grafo}  # 0: no asignado, 1: verdad, -1: mentira
    color[inicial] = 1  # El inicial dice la verdad

    queue = deque([inicial]) # Inicializamos la cola con el nodo inicial

    while queue: # Mientras haya nodos por visitar
        current = queue.popleft() # Saco el nodo pendiente en la cola FIFO
        
        for neighbor in grafo[current]: # Para cada vecino del nodo actual
            if color[neighbor] == 0: # Esta es nuestra manera de decir si no ha sido visitado
                # Asignamos el color opuesto al del nodo actual (Uno dice verdad/mentira el otro si o si tiene que decir lo contrario)
                color[neighbor] = -color[current]
                queue.append(neighbor)
            elif color[neighbor] == color[current]: # Si ya se visito y tiene el mismo color
                # Si el vecino ya tiene color y es igual al actual, conflicto
                return False
            
    if 0 in color.values(): # Si aun hay un nodo que no visitamos, significa que no es conexo el grafo
        return False # En ese caso, no podemos determinar la respuesta, asi que retornamos falso


    return True


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
} 

inicial = 'A'
print(bfs_oompaloompa(grafo, inicial))  # Debería retornar True
