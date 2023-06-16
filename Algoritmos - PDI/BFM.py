def BFM(Grafo, salida):
    dist, prev = {}, {}
    result = []

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
    return result, dist, prev #ver que onda con result

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



s, distancia, previos = BFM(grafo, '1')
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")