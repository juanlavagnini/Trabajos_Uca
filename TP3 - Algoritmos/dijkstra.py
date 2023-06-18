grafo = {
    '1': {'3': 1, '6': 2},
    '2': {'9': 1, '3': 2, '6': 1},
    '3': {'4': 2, '2': 2, '1': 1},
    '4': {'5': 3, '3': 2},
    '5': {'10': 4, '4': 3},
    '6': {'7': 2, '2': 1, '1': 2},
    '7': {'9': 3, '11': 2, '6': 2},
    '9': {'10': 2, '11': 2, '2': 1, '7': 3},
    '10': {'5': 4, '9': 2},
    '11': {'7': 2, '9': 2}
}
def dijkstra(grafo, salida):
    dist, prev = {}, {}
    for vertice in grafo:
        dist[vertice] = float('inf')
        prev[vertice] = None
    dist[salida] = 0

    visitado = []

    while len(visitado) < len(grafo):
        dist_min = float('inf')
        nodo_min = None
        for nodo in grafo:
            if nodo not in visitado and dist[nodo] < dist_min:
                dist_min = dist[nodo]
                nodo_min = nodo

        visitado.append(nodo_min)

        for vecino, costo in grafo[nodo_min].items():
            distancia = dist[nodo_min] + costo
            if distancia < dist[vecino]:
                dist[vecino] = distancia
                prev[vecino] = nodo_min

    return visitado, dist, prev

def next_hop(previos, nodo, salida):
    while previos[nodo] != salida:
        nodo = previos[nodo]
    return nodo

def armarTabla():
    for i in grafo:
        print("{:<14} {:<10} {:<10} {:<10}".format("Ruteador: "+i,"Destino", "Distancia", "NextHop"))
        usados, distancia, previos = dijkstra(grafo, i)
        for nodo in distancia:
            dis = distancia[nodo]
            pre = previos[nodo]
            if pre != None:
                if pre!=i:
                    nextHop = next_hop(previos, nodo, i)
                    print("{:<14} {:<10} {:<10} {:<10}".format("",nodo, dis, nextHop))
                else:
                    print("{:<14} {:<10} {:<10} {:<10}".format("",nodo, dis, "Directo"))
        print("_______________________________________________")
def main():
    armarTabla()
main()