def encontar_puentes(grafo):
    # Lista de adyacencia

    puentes = [] # Donde guardaremos los puentes "calles criticas"
    visitado = {node: False for node in grafo} # Estructura para saber si ya visitamos el nodo
    descubrimiento = {node: 0 for node in grafo}  # Estructura para guardar el tiempo de descubrimiento
    bajo = {node: 0 for node in grafo} # Estructura para guardar el tiempo bajo
    tiempo = [0] # Usamos una lista para poder modificarla dentro de la funcion dfs, es simplemente el contador de tiempo

    def dfs(nodo, padre): # En cada itereacion del DFS tiene que entrar a la funcion dfs, y el padre es el nodo que lo llamo. Esto se debe a que es necesario saber de donde viene un nodo para poder determinar si es un puente o no
        visitado[nodo] = True # Marcamos el nodo como visitado
        descubrimiento[nodo] = bajo[nodo] = tiempo[0] # Guardamos el tiempo de descubrimiento y el tiempo bajo, estos son iguales al inicio inicialmente
        tiempo[0] += 1 # Aumentamos el tiempo de descubrimiento, esto es simplemente un contador que se va incrementando cada vez que se visita un nodo

        for neighbor in grafo[nodo]: # Para cada vecino del nodo
            if not visitado[neighbor]: # Si ese vecino no se ha visitado
                dfs(neighbor, nodo) # Llamamos a la funcion dfs para ese vecino, y le pasamos el nodo actual como padre. Hacemos dfs lo más profundo posible

                # Una vez salgamos de la funcion dfs, tenemos que actualizar el tiempo bajo del nodo actual con lo que se encontro en la funcion dfs
                bajo[nodo] = min(bajo[nodo], bajo[neighbor]) # Esto es simplemente el tiempo bajo del nodo actual, y lo actualizamos con el tiempo bajo del vecino, si es menor

            if bajo[neighbor] > descubrimiento[nodo]: # Si el tiempo bajo del vecino es mayor al tiempo de descubrimiento del nodo actual, significa que no hay un camino alternativo para llegar al nodo actual, por lo que es un puente
                puentes.append((nodo, neighbor)) # Agregamos el puente a la lista de puentes

            # Si el vecino ya fue visitado y no es el padre, significa que hay un ciclo (O mas bien, un camino alternativo para retornar a algun punto del grafo), por lo que tenemos que actualizar el tiempo bajo del nodo actual
            elif neighbor != padre:
                bajo[nodo] = min(bajo[nodo], descubrimiento[neighbor]) # El nuevo tiempo bajo sera el minimo entre el bajo actual y el tiempo de descubrimiento del vecino. Esto es simplemente para actualizar el tiempo bajo del nodo actual, si es menor al tiempo bajo actual

    for nodo in grafo: # Recorremos todos los nodos del grafo, esto es necesario porque el grafo puede estar desconectado, por lo que tenemos que asegurarnos de visitar todos los nodos
        if not visitado[nodo]: # Si el nodo no ha sido visitado, llamamos a la funcion dfs para ese nodo
            dfs(nodo, None) # Llamamos a la funcion dfs para ese nodo, y le pasamos None como padre, ya que no hay padre en este caso

    return puentes # Devuelve una lista de tuplas con los puentes encontrados en el grafo. Un puente es una arista que, si se elimina, aumenta el número de componentes conexos del grafo.


# Ejemplo de uso:
grafo = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}


print("Calles críticas (puentes):", encontar_puentes(grafo))
