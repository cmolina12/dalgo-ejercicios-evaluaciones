import sys
import math

class DSU:
    """Implementación de la estructura Disjoint Set Union (Union-Find)."""
    def __init__(self, n):
        # Inicializa cada nodo como su propio padre.
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        # Encuentra el representante del conjunto que contiene a 'a'.
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        # Une los conjuntos que contienen a 'a' y 'b'.
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False  # 'a' y 'b' ya están en el mismo conjunto, unirlos formaría un ciclo.
        # Unión por rango
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

def distancia(p1, p2):
    """Calcula la distancia euclídea entre dos puntos."""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def main():
    input_data = sys.stdin.read().strip().splitlines()
    if not input_data:
        return

    # La primera línea indica el número de casos de prueba.
    t = int(input_data[0].strip())
    index = 1  # índice para recorrer las líneas de entrada

    resultados = []
    
    for _ in range(t):
        # Para cada caso se lee S y P.
        # Se ignoran posibles líneas en blanco.
        while index < len(input_data) and input_data[index].strip() == "":
            index += 1
        if index >= len(input_data):
            break
        s, p = map(int, input_data[index].split())
        index += 1
        
        # Se leen las coordenadas de los P puestos.
        puntos = []
        for _ in range(p):
            # Omitir líneas en blanco si las hubiera.
            while index < len(input_data) and input_data[index].strip() == "":
                index += 1
            x, y = map(int, input_data[index].split())
            puntos.append((x, y))
            index += 1
        
        # Se generan todas las aristas posibles (pares de puestos) junto con su distancia.
        aristas = []
        for i in range(p):
            for j in range(i + 1, p):
                d = distancia(puntos[i], puntos[j])
                aristas.append((d, i, j))
        
        # Se ordenan las aristas en orden creciente de distancia.
        aristas.sort(key=lambda x: x[0])
        
        # Se construye el MST utilizando Kruskal.
        dsu = DSU(p)
        mst_edges = []  # Almacena los pesos de las aristas seleccionadas en el MST.
        for d, u, v in aristas:
            if dsu.union(u, v):
                mst_edges.append(d)
                # Si ya se han unido los P puestos (se tienen P-1 aristas), se puede detener.
                if len(mst_edges) == p - 1:
                    break
        
        # Una vez construido el MST, se ordenan los pesos de sus aristas de manera descendente.
        mst_edges.sort(reverse=True)
        # Al tener S canales satelitales se pueden "omitir" los S-1 arcos más largos.
        # El valor de D que se requiere es el siguiente peso.
        # Por ejemplo, si S = 1, D es el mayor arco del MST.
        # Si S > 1, se elimina el mayor, el resultado es el arco que conecta los clusters restantes.
        respuesta = mst_edges[s - 1] if s - 1 < len(mst_edges) else 0
        
        resultados.append(f"{respuesta:.2f}")
    
    # Imprimir la respuesta para cada caso de prueba.
    for res in resultados:
        print(res)

if __name__ == '__main__':
    main()
