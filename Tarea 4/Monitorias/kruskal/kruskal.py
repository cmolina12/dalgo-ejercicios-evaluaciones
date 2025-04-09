

def kruskal(n, aristas):
    # n: número de nodos
    # aristas: lista de tuplas (peso, u, v)
    uf = UnionFind(n)
    aristas.sort()  # Ordenamos por peso
    mst = []
    total = 0

    for peso, u, v in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            total += peso
        if len(mst) == n - 1:
            break

    return total, mst
