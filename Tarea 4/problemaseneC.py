import sys
import math

class DSU: # el union find

    def __init__(self, n):
        # Cada nodo se inicializa como su propio padre.
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        # Búsqueda con compresión de caminos para optimización.
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        # Une los conjuntos que contienen a los elementos a y b.
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False  # Ya están en el mismo conjunto.
        # Unión por rango para mantener conjuntos equilibrados.
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

def calcular_mst(puntos):

    n = len(puntos) # Número de puntos
    aristas = [] # Lista para almacenar las aristas y sus distancias.
    # Se generan todas las aristas posibles con sus distancias euclidianas.
    for i in range(n): 
        for j in range(i + 1, n):
            d = math.hypot(puntos[i][0] - puntos[j][0], puntos[i][1] - puntos[j][1])
            aristas.append((d, i, j))
    aristas.sort(key=lambda x: x[0])  # Ordenar por distancia (costo)

    dsu = DSU(n)
    total = 0.0  # Acumula la longitud total utilizada en el MST.
    for d, u, v in aristas:
        if dsu.union(u, v):
            total += d
    return total

def procesar_caso(caso_lines):

    n = int(caso_lines[0].strip())
    puntos = []
    for i in range(1, n + 1):
        x, y = map(float, caso_lines[i].strip().split())
        puntos.append((x, y))
    resultado = calcular_mst(puntos)
    return "{:.2f}".format(resultado)

def leer_entrada():

    input_data = sys.stdin.read().strip().splitlines()
    if not input_data:
        return []
    
    casos = []
    # La primera línea indica el número de casos de prueba.
    t = int(input_data[0].strip())
    index = 1  # Posición actual en la entrada.
    for _ in range(t):
        # Se omiten líneas en blanco, si existen.
        while index < len(input_data) and input_data[index].strip() == "":
            index += 1
        if index >= len(input_data):
            break
        # La línea actual indica la cantidad de puntos para el caso.
        n = int(input_data[index].strip())
        caso_lines = [input_data[index].strip()]
        index += 1
        # Se leen las n líneas de coordenadas.
        for _ in range(n):
            while index < len(input_data) and input_data[index].strip() == "":
                index += 1
            if index < len(input_data):
                caso_lines.append(input_data[index].strip())
                index += 1
        casos.append(caso_lines)
    return casos

def main():

    casos = leer_entrada()
    resultados = []
    for caso_lines in casos:
        res = procesar_caso(caso_lines)
        resultados.append(res)
    for r in resultados:
        print(r)

if __name__ == '__main__':
    main()
