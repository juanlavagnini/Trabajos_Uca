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
        nodo_actual = Q[0]
        tiempo_parcial_inicio = time.time()
        for vecino in Grafo[nodo_actual]:
            if dist[vecino] > dist[nodo_actual] + Grafo[nodo_actual][vecino]: #and (nodo_actual!=prev[vecino] and prev[nodo_actual]!=vecino):
                dist[vecino] = dist[nodo_actual] + Grafo[nodo_actual][vecino]
                previo = prev[vecino]
                prev[vecino] = nodo_actual
                print("Estado intermedio -> (P:",prev[vecino], ",D:", dist[vecino],")")
                if vecino not in Q: #Se implementa la variante ESOPO-PAPE
                    if previo==None: #si el nodo fue no fue revisado se lo revisa con prioridad
                        Q.insert(0, vecino) 
                    else: #si ya fue revisado, se lo deja al final de la cola
                        Q.append(vecino)
        Q.remove(nodo_actual)
        #time.sleep(1) el tiempo es tan chico que se necesitaria un delay para poder observarlo
        tiempo_parcial_fin = time.time()
        tiempo_parcial = tiempo_parcial_fin - tiempo_parcial_inicio
        print("La revision de el nodo {:2}".format(nodo_actual), end=" ")
        print("tardo {:>10.10f}".format(tiempo_parcial), " segundos")
    return result

"""
grafo = {
    '1': {'3': 1, '6': 2},
    '2': {'9': 1, '3': 2, '6': 1},
    '3': {'4': 2, '2': 2, '1': 1},
    '4': {'5': 3, '3': 2},
    '5': {'10': 4, '4': 3},
    '6': {'7': 2, '2': 1, '1': 2},
    '7': {'9': 3, '11': 2, '6': 2},
    '9': {'10': 2, '11': 2, '7': 3, '2': 1},
    '10': {'5': 4, '9': 2},
    '11': {'7': 2, '9': 2}
}"""

def cargar_grafo():
    f = open("grafo.txt", "r")
    grafo = {}
    for line in f.readlines():
        datos = line.split(",")
        if datos[0] in grafo.keys():
            grafo[datos[0]][datos[1]] = int(datos[2])
        else:
            grafo[datos[0]] = {datos[1]: int(datos[2])}
    return grafo

def main():
    grafo = cargar_grafo()
    for router in grafo:
        inicio_de_tiempo = time.time()
        s = BFM(grafo, router)
        print()
        print("{:<24s} {:<20s} {:<20s} {:<20s}".format("Ruteador: "+ s[0],"Destino", "Next Hop", "Costo"))
        for destino in s[1]:
            if destino != s[0]:
                if  s[1][destino] == s[0]:
                    nexthop = "directo"
                else:
                    nexthop = next_hop(s[1],destino,s[0])
                print("{:<24s} {:<20s} {:<20s} {:<20d}".format("", destino, nexthop, s[2][destino]))
        print("_____________________________________________________________________")
        #time.sleep(1)
        tiempo_final = time.time()
        tiempo = tiempo_final - inicio_de_tiempo
        print("El tiempo total acumulado del router", s[0], "fue", tiempo)
        print()
main()
