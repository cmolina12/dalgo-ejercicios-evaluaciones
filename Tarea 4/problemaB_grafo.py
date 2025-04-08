import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Definir los barrios con nombres (cada número es un identificador único)
barrios = {
    0: "Centro",
    1: "Norte",
    2: "Sur",
    3: "Este",
    4: "Oeste"
}

# Agregar los nodos (barrios) con el atributo 'nombre'
for id_barrio, nombre in barrios.items():
    G.add_node(id_barrio, nombre=nombre)

# Definir las calles entre barrios con nombres (cada tupla es una arista)
calles = [
    (0, 1, {"calle": "Avenida Libertad"}),
    (1, 2, {"calle": "Calle 5 de Mayo"}),
    (2, 0, {"calle": "Bulevar Central"}),
    (1, 3, {"calle": "Avenida del Sol"}),
    (3, 4, {"calle": "Calle del Horizonte"})
]

# Agregar las aristas (calles) al grafo
G.add_edges_from(calles)

# Definir la posición de los nodos para una mejor visualización
pos = nx.spring_layout(G, seed=42)

# Dibujar el grafo, utilizando los nombres de los barrios para las etiquetas
nx.draw(G, pos, with_labels=True, labels=barrios, node_color='lightblue', edge_color='gray', node_size=600, font_weight='bold')

# Dibujar las etiquetas de las aristas con los nombres de las calles
edge_labels = {(u, v): data["calle"] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Ejemplo de Grafo: Barrios y Calles")
plt.show()
