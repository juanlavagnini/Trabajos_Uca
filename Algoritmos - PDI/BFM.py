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
            if dist[vecino] > dist[Q[0]] + Grafo[Q[0]][vecino]:
                dist[vecino] = dist[Q[0]] + Grafo[Q[0]][vecino]
                prev[vecino] = Q[0]
            if vecino not in Q:
                Q.append(vecino)
        Q.remove(Q[0])
    print(Q)
    return result

grafo = {
    '1': {'3': 1, '6': 2},
    '2': {'9': 1},
    '3': {'4': 2, '2': 2},
    '4': {'5': 3},
    '5': {'10': 4},
    '6': {'7': 2, '2': 1},
    '7': {'9': 3, '11': 2},
    '9': {'10': 2, '11': 2},
    '10': {},
    '11': {}
}

def main():
    s = BFM(grafo, "1")
    print("{:<14s} {:<10s} {:<10s} {:<10s}".format("Ruteador: "+ s[0],"Destino", "Next Hop", "Costo"))
    for destino in s[1]:
        if destino != s[0]:
            if  s[1][destino] == s[0]:
                nexthop = "directo"
            else:
                nexthop = s[1][destino]
            print("{:<14s} {:<10s} {:<10s} {:<10s}".format("", destino, nexthop, str(s[1][destino])))


main()