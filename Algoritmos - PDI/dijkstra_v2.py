def re_analizar(u,Grafo, dist, prev):
    for vecino in Grafo[u]:
        if dist[vecino] > dist[u] + Grafo[u][vecino]:
            dist[vecino] = dist[u] + Grafo[u][vecino]
            prev[vecino] = u
            re_analizar(vecino,Grafo,dist,prev)
    return dist, prev
def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u
            elif vecino not in Q: #quiere decir que el nodo estaba
                vecino = min(Grafo[u], key=dist.get)
                dist[u]= dist[vecino] + Grafo[u][vecino]
                prev[u] = vecino # si encontro una conexion al resto del grafo, me fijo si tiene mas conexiones y analizo si pasando por el mejora alguna
                re_analizar(u, Grafo, dist, prev)
    return result, dist, prev


grafo = {
    '1': {'3': 1, '6': 2},
    '2': {'9': 1, '3': 2, '6': 1},
    '3': {'4': 2},
    '4': {'5': 3},
    '5': {'10': 4},
    '6': {'7': 2},
    '7': {'9': 3, '11': 2},
    '9': {'10': 2, '11': 2},
    '10': {},
    '11': {}
}

s, distancia, previos = dijkstra(grafo, '1')
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")