import sys

class DSU:
    def __init__(self):
        # Usamos diccionarios para manejar compuestos de cualquier valor (0 ≤ a,b ≤ 10^3)
        self.parent = {}
        self.rank = {}

    def add(self, a):
        # Si el compuesto a no existe en la estructura, lo inicializamos.
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 0

    def find(self, a):
        # Path compression para optimización
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        # Une los conjuntos que contienen a 'a' y 'b'. Devuelve False si ya están unidos (lo que genera ciclo)
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA == rootB:
            return False  # Ya están en el mismo conjunto
        
        # Unión por rango
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

def procesar_caso(pares):
    """
    Dado un listado de pares (tuplas con dos enteros), procesa el caso aplicando el DSU y devuelve el número
    de pares rechazados.
    """
    dsu = DSU()
    rechazos = 0

    for a, b in pares:
        # Asegurarse de agregar ambos compuestos al DSU, si aún no han sido registrados.
        dsu.add(a)
        dsu.add(b)
        
        # Si a y b ya están conectados, rechazar el par pues generaría un ciclo.
        if dsu.find(a) == dsu.find(b):
            rechazos += 1
        else:
            dsu.union(a, b)
    return rechazos

def main():
    # Leemos la entrada completa
    input_data = sys.stdin.read().strip()
    
    # Separamos las líneas y eliminamos líneas en blanco extra
    lines = [line.strip() for line in input_data.splitlines() if line.strip() != '']
    
    casos = []
    caso_actual = []
    
    for line in lines:
        if line == "-1":
            # Fin del caso de prueba actual.
            if caso_actual:
                casos.append(caso_actual)
                caso_actual = []
        else:
            # Cada línea con un par: dos enteros separados por un espacio.
            # Se convierten a enteros y se almacenan como tupla.
            try:
                a, b = map(int, line.split())
                caso_actual.append((a, b))
            except ValueError:
                # En caso de línea mal formateada, se ignora.
                continue

    # Procesamos cada caso de prueba y mostramos el resultado.
    resultados = []
    for caso in casos:
        rechazos = procesar_caso(caso)
        resultados.append(rechazos)
    
    # Imprimir cada resultado en una línea
    for r in resultados:
        print(r)

if __name__ == '__main__':
    main()
