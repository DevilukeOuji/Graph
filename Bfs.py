class BreadthFirstSearch:

    def BFS(self,graph,source):
        num_vert = numVertices_Arestas(grafo)
        color = [];predecessor = [];d = [];queue = []
        for u in range(0, num_vert):
            color += [white]
            predecessor += [-1]
            d += ['']
        color[source-1] = gray
        d[source-1] = 0
        queue.append(source)
        while queue:
            u = queue.pop(0)
            print(f'u:{u}')
            list_adj = listaAd(graph, u)
            if list_adj:
                for elem in list_adj:
                    if color[elem-1] == white:
                        color[elem-1] = gray
                        d[elem-1] = d[u] + 1
                        predecessor[elem-1] = u
                        queue.append(elem)
                    print(queue) #fila
            color[u-1] = preto
        print('d: ', d)