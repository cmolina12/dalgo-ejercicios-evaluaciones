import heapq

def vuelos_mas_baratos(flights, src, dst, k):
    
    adj = {}
    
    for fromi, toi, pricei in flights:
        if fromi not in adj:
            adj[fromi] = []
        adj[fromi].append((toi, pricei))
        
    heap = [(0, src, 0)]
    
    while heap:
        costo, ciudad, escalas = heapq.heappop(heap)

        if ciudad == dst:
            return costo
        
        if escalas <= k:
            for vecino, precio in adj[ciudad]:
                costo_nuevo = costo + precio
                escalas = escalas + 1
                heapq.heappush(heap,(costo_nuevo, vecino, escalas))
                
    return -1

flights = [
    ('A', 'B', 100),
    ('B', 'C', 100),
    ('A', 'C', 500),
    ('C', 'D', 100)
]

src ='A'
dst = 'D'
k = 2  # máximo 2 escalas → máximo 3 vuelos

print(vuelos_mas_baratos(flights, src, dst, k))  # → salida esperada: 300

