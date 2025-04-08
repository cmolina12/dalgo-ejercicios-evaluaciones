
# Implementar BFS recursivo e iterativo


def bfs_recursivo(grafo, fila, visitados):
    if len(fila) == 0:
        return
    else:
        vertice = fila.pop(0)
        visitados.append(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fila.append(vizinho)
        bfs_recursivo(grafo, fila, visitados)
    return visitados

