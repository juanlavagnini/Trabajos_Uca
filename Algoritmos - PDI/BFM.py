import time
def next_hop(previos, nodo, salida):
    while previos[nodo] != salida:
        nodo = previos[nodo]
    return nodo
def BFM(Grafo, salida):
    dist, prev = {}, {}
    result = [salida, prev, dist]

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0
    Q = [salida]

    while Q:
        for vecino in Grafo[Q[0]]:
            if dist[vecino] > dist[Q[0]] + Grafo[Q[0]][vecino] and (Q[0]!=prev[vecino] and prev[Q[0]]!=vecino):
                dist[vecino] = dist[Q[0]] + Grafo[Q[0]][vecino]
                prev[vecino] = Q[0]
                if vecino not in Q:
                    Q.append(vecino)
        Q.remove(Q[0])
    return result


grafo = {
    '1': {'3': 1, '6': 2},
    '2': {'9': 1, '3': 2, '6': 1},
    '3': {'4': 2, '2': 2, '1': 1},
    '4': {'5': 3, '3': 2},
    '5': {'10': 4, '4': 3},
    '6': {'7': 2, '2': 1, '1': 2},
    '7': {'9': 3, '11': 2, '6': 2},
    '9': {'10': 2, '11': 2, '7': 3, '2': 1},
    '10': {'5': int(-1), '9': 2},
    '11': {'7': 2, '9': 2}
}

def main():
    inicio_de_tiempo = time.time()
    for router in grafo:
        s = BFM(grafo, router)
        print("{:<14s} {:<10s} {:<10s} {:<10s}".format("Ruteador: "+ s[0],"Destino", "Next Hop", "Costo"))
        for destino in s[1]:
            if destino != s[0]:
                if  s[1][destino] == s[0]:
                    nexthop = "directo"
                else:
                    nexthop = next_hop(s[1],destino,s[0])
                print("{:<14s} {:<10s} {:<10s} {:<10d}".format("", destino, nexthop, s[2][destino]))
        print("_______________________________________________")
    tiempo_final = time.time()
    tiempo = tiempo_final - inicio_de_tiempo
    print(tiempo)
main()



