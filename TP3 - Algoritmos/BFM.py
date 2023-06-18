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
        tiempo_parcial_inicio = time.time()
        for vecino in Grafo[Q[0]]:
            if dist[vecino] > dist[Q[0]] + Grafo[Q[0]][vecino]: #and (Q[0]!=prev[vecino] and prev[Q[0]]!=vecino):
                dist[vecino] = dist[Q[0]] + Grafo[Q[0]][vecino]
                prev[vecino] = Q[0]
                print("Estado intermedio -> (P:", prev[vecino], ",D:", dist[vecino], ")")
                if vecino not in Q:
                    Q.append(vecino)
        # time.sleep(1) el tiempo es tan chico que se necesitaria un delay para poder observarlo
        tiempo_parcial_fin = time.time()
        tiempo_parcial = tiempo_parcial_fin - tiempo_parcial_inicio
        print("La revision de el nodo {:2}".format(Q[0]), end=" ")
        print("tardo {:>10.10f}".format(tiempo_parcial), " segundos")
        Q.remove(Q[0])
    return result


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


