import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío para conflictos
G = nx.Graph()

# Definir jugadores con nombres (cada número es un identificador único)
jugadores = {
    0: "Jugador A",
    1: "Jugador B",
    2: "Jugador C",
    3: "Jugador D",
    4: "Jugador E",  # Jugadores sin conflictos
    5: "Jugador F"   # Jugadores sin conflictos
}

# Agregar los nodos (jugadores) al grafo
for id_jugador, nombre in jugadores.items():
    G.add_node(id_jugador, nombre=nombre)

# Definir conflictos entre jugadores (aristas de conflicto)
conflictos = [
    (0, 1, {"conflicto": "Desacuerdo"}),
    (0, 3, {"conflicto": "Desacuerdo"}),
    (2, 1, {"conflicto": "Desacuerdo"}),
    (2, 3, {"conflicto": "Desacuerdo"})
]
G.add_edges_from(conflictos)

# Generar posiciones para los nodos con mayor separación
pos = nx.spring_layout(G, seed=42, k=1.0)  # Aumentar k para separar nodos en conflicto

# Dibujar los nodos con etiquetas
nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=800)  # Aumentar tamaño de nodos
nx.draw_networkx_labels(G, pos, labels=jugadores, font_weight='bold', font_size=10)  # Aumentar tamaño de etiquetas

# Dibujar aristas de conflicto (en rojo y sólidas)
conflict_edges = list(G.edges(data=True))
nx.draw_networkx_edges(
    G, pos, edgelist=[(u, v) for u, v, d in conflict_edges],
    edge_color='red', width=2
)

# Agregar manualmente una arista que indique compatibilidad entre jugadores que no tienen conflictos
compatibilidad = [(4, 5)]
nx.draw_networkx_edges(
    G, pos, edgelist=compatibilidad,
    edge_color='green', style='dashed', width=2
)

# Preparar las etiquetas de las aristas para mostrar el tipo de relación
edge_labels = {}
for u, v, data in conflict_edges:
    edge_labels[(u, v)] = data["conflicto"]
edge_labels[(4, 5)] = "Sin desacuerdo"

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Ejemplo de Grafo: Jugadores, Conflictos y Compatibilidad")
plt.axis('off')
plt.show()