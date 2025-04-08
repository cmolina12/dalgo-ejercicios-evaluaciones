from collections import deque # Importamos la libreria con la que usaremos la cola de prioridad

def bfs_bipartito(grafo):

    color = {node: 0 for node in grafo} # 0 indica que no tiene equipo aun, 1 indica equipo azul, 2 indica equipo rojo
    
    for i in grafo: # Para cado nodo del grafo, eso es necesario porque el punto de dividr esto en grupos es que hay componentes conexas que no van a estar coenctadas entre si, entonces esta es la unica manera de recorrer todo el grafo completo
        if color[i] == 0: # Si no tiene equipo, y esto es equivalente a la condicion de si no lo he visitado aun
            color[i] = 1 # Se le asigna equipo azul por predeterminado, esto da igual
            queue = deque() # Iniciamos el FIFO
            queue.append(i) # Metemos este nodo al fifo
            while queue: # Mientras hayan elementos en la cola de prioridad (FIFO)
                current = queue.popleft() # Sacamos el nodo a seguir
                for neighbor in grafo[current]: # Para cada vecino de ese nodo
                    if color[neighbor] == color[current]: # Si su color es el del nodo actual
                        return False # Hay que retornar falso, no se puede
                    if color[neighbor] == 0: # Si no al vecino no se le asignado un color (equipo)
                        color[neighbor] = -color[current] # EL color del vecino si o si tiene que ser opuesto al del nodo actual
                        queue.append(neighbor) # Metemos al vecino a la cola de prioridad para que sea analizado
    return True # Si nada falla dentro del algoritmo, entonces si se pueden dividir en los dos grupos

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
} # Grafo de ejemplo, esto es un diccionario donde las llaves son los nodos, y los valores son una lista que definen los adyacentes (para este problema, definidios como los enemigos de cada jugador (cada jugador representado por un nodo))

resultado = bfs_bipartito(grafo) # Ejecutamos el algoritmo y el resultado lo guardamos en una variable

print(resultado) # Imprimimos la variable