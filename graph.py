# o grafo supõe valores de vértices de 0 a N   

class Matriz():
    def __init__(self, v, tipo):
        self.v = v
        self.tipo = tipo
        self.rep = 'matriz'
        self.matriz = []
        self.linha_matriz = []
        self.weight = []
        for i in range(0, self.v):
            linha_matriz = []
            self.matriz += [linha_matriz]
            for j in range(0, self.v):
                linha_matriz += [0]
    
    def addAresta(self, v, w, weight): #considerando que não há vértice 0
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.tipo == 'nao_dir':
            self.matriz[w][v] = 1
        self.matriz[v][w] = 1
        self.weight += [weight]

    def remAresta(self, v, w): 
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.matriz[v][w] == 0:
            print('\nAresta inexistente.')
            return
        self.matriz[v][w] = 0
        if self.tipo == 'nao_dir':
            self.matriz[w][v] = 0

    def grauVertice(self, v):
        if v > self.v:
            print('\nO vértice não existe no grafo.')
            return
        grau = 0
        for i in self.matriz[v]:
            if i == 1: grau += 1
        if self.tipo == 'dir':
            for i in self.matriz:
                if i[v] == 1: grau += 1
        print(f'\nO grau do vértice {v} é: {grau}')
        return grau
    
    def existeAresta(self, v, w):
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.matriz[v][w] == 1: 
            #print(f'\nA aresta {v},{w} existe!')
            return True
        #print(f'\nA aresta {v},{w} não existe!')
        return False
    def listAd(self,v):
        if v > self.v: return
        lista_adj = []
        for i in range(0,len(self.matriz[v])):
            if self.matriz[v][i] == 1: lista_adj += [i]
        #print(f'\nLista de adjacências de {v}:{lista_adj}')
        return lista_adj
    
    '''def ordenaPeso(self):
        ordenadas = []
        pesos = self.weight.copy() ; lista = self.listAdj.copy()
        arestas = []
        for i in lista:
            for j in i:
                tupla = (lista.index(i),j)
                if (j,lista.index(i)) in arestas: continue
                arestas += [tupla]
        for _ in range(len(arestas)):
            menor = min(pesos)
            menor_aresta = arestas[pesos.index(menor)]
            ordenadas += [menor_aresta]
            pesos.remove(menor); arestas.remove(menor_aresta)
        return ordenadas'''

    def imprimirGrafo(self):
        print('\nMatriz de Adjacências')
        for i in range(0, len(self.matriz)):
            if i < 10: print('0'+f'{i}', end = ' ')
            else: print(i, end = ' ')
            print(self.matriz[i])

class Lista():
    def __init__(self, v, tipo):
        self.v = v
        self.tipo = tipo
        self.rep = 'lista'
        self.listAdj = []
        self.weight = []
        self.linha_lista = []
        for i in range(0, self.v):
            linha_lista = []
            self.listAdj += [linha_lista]
    
    def addAresta(self, v, w, weight): #considerando que não há vértice 0
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.tipo == 'nao_dir':
            self.listAdj[w] += [v]
        self.listAdj[v] += [w]
        self.weight += [weight]

    def remAresta(self, v, w): 
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if w not in self.listAdj:
            print('\nAresta inexistente.')
            return
        self.listAdj[v].remove(w)
        if self.tipo == 'nao_dir': self.listAdj[w].remove(v)

    def grauVertice(self, v):
        if v > self.v:
            print('\nO vértice não existe no grafo.')
            return
        grau = 0
        for i in self.listAdj[v]: grau += 1
        if self.tipo == 'dir':
            for i in self.listAdj:
                if v in i: grau += 1
        print(f'\nO grau do vértice {v} é: {grau}')
        return grau
    
    def existeAresta(self, v, w):
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if w in self.listAdj[v]: 
            #print(f'\nA aresta {v},{w} existe!')
            return True
        #print(f'\nA aresta {v},{w} não existe!')
        return False
    
    def listAd(self,v):
        if v > self.v: return
        #print(f'\nLista de adjacências de {v}:{sorted(self.listAdj[v])}')
        return sorted(self.listAdj[v])
    
    def ordenaPeso(self):
        ordenadas = []
        pesos = self.weight.copy() ; lista = self.listAdj.copy()
        arestas = []
        for i in lista:
            for j in i:
                tupla = (lista.index(i),j)
                if (j,lista.index(i)) in arestas: continue
                arestas += [tupla]
        for _ in range(len(arestas)):
            menor = min(pesos)
            menor_aresta = arestas[pesos.index(menor)]
            ordenadas += [menor_aresta]
            pesos.remove(menor); arestas.remove(menor_aresta)
        return ordenadas

    def imprimirGrafo(self):
        print('\nLista de Adjacências')
        for i in range(0, len(self.listAdj)):
            print(i, end = ' ')
            print(self.listAdj[i])

class DepthFirstSearch():

    def depthFirstSearch(self,graph, source):
        num_vert = graph.v
        color = [];predecessor = [];d = []; t = [];time = 0
        for u in range(0, num_vert):
            color += ['white'];predecessor += [-1]
            d += ['']
            t += ['']
        time = DepthFirstSearch.dfs(self,graph, source, time, color,predecessor, d, t)
        for u in range(0, num_vert):
            if color[u] == 'white': 
                time = DepthFirstSearch.dfs(self,graph, u, time, color,predecessor, d, t)
        #print(f'predecessor:{predecessor}')
        return t

    def dfs(self,graph, u, time, color,predecessor, d, t):
        color[u] = 'gray'
        time += 1
        d[u] = time
        adj_list = graph.listAd(u)
        if adj_list:
            for elem in adj_list:
                if color[elem] == 'white':
                    predecessor[elem] = u
                    time = DepthFirstSearch.dfs(self,graph, elem,time, color,predecessor, d, t)
        color[u] = 'black'
        time += 1
        t[u] = time
        '''print('color: ', color)
        print('d: ', d)
        print('t: ', t)'''
        return time

class BreadthFirstSearch:

    def BFS(self,graph,source):
        num_vert = graph.v
        color = [];predecessor = [];d = [];queue = []
        for u in range(0, num_vert):
            color += ['white']
            predecessor += [-1]
            d += [100000]
        color[source] = 'gray'
        d[source] = 0
        queue.append(source)
        while queue:
            u = queue.pop(0)
            list_adj = graph.listAd(u)
            if list_adj:
                for elem in list_adj:
                    if color[elem] == 'white':
                        color[elem] = 'gray'
                        d[elem] = d[u] + 1
                        predecessor[elem] = u
                        queue.append(elem)
                    #print(queue)
            color[u] = 'black'
        print(f'predecessor:{predecessor}')

class ConnectedComponents():

    def __init__(self):
        self.cont = 0
        self.identifier = []

    def conec(self,graph):
        num_vert = graph.v
        color = [];predecessor = []
        for u in range(0, num_vert):
            color += ['white'];predecessor += [-1];self.identifier += [-1]
        for u in range(0, num_vert):
            if color[u] == 'white': 
                time = ConnectedComponents.dfs(self,graph, u, color,predecessor)
                self.cont += 1
        return self.identifier

    def dfs(self,graph, u, color,predecessor):
        color[u] = 'gray'
        self.identifier[u] = self.cont
        adj_list = graph.listAd(u)
        if adj_list:
            for elem in adj_list:
                if color[elem] == 'white':
                    predecessor[elem] = u
                    time = ConnectedComponents.dfs(self,graph, elem,color,predecessor)
        color[u] = 'black'
        return self.identifier
    
    def nConnected(self):
        return self.cont
    
    def connected(self, v, w):
        return self.identifier[v] == self.identifier[w]

class TopoOrder():

    def top_ord(self, graph, source):
        dfs = DepthFirstSearch()
        time = dfs.depthFirstSearch(graph, source)
        ordered = []; edges = []
        time_cp = time.copy()
        for _ in range(0, len(time)):
            higher = max(time)
            ordered += [time_cp.index(higher)]
            time.remove(higher)
          
        for i in ordered:
            for j in ordered:
                if graph.existeAresta(i,j) and ordered.index(i) < ordered.index(j): edges += [(i+1,j+1)]
        print('Arestas: ', edges)
        return ordered
    
    #somente adiciona 1 a todos os elementos da lista dos ordenados
    #já que os exemplos do slide começam com o vértice 1
    def add(self,orde):
        ordered = list(map(lambda x: x+1, orde))
        print(f'Ordenados (+1): {ordered}')

class Kruskal():

    def Kruskal(self, graph, v):
        sets = {i:{i} for i in range(v)}
        ordered = g.ordenaPeso()
        for edge in ordered:
            c0 = -1; c1 = -1
            for s in sets:
                if edge[0] in sets[s]: c0 = s
                if edge[1] in sets[s]: c1 = s
            if c0 != c1 and c0 != -1 and c1 != -1:
                sets[c0] = sets[c0].union(sets[c1])
                sets.pop(edge[1],None)
        return sets


g = Lista(9, 'nao_dir')
g.addAresta(0,1,4)
g.addAresta(0,8,8)
g.addAresta(1,8,11)
g.addAresta(1,2,8)
g.addAresta(2,3,7)
g.addAresta(2,5,4)
g.addAresta(2,6,2)
g.addAresta(3,4,9)
g.addAresta(3,5,14)
g.addAresta(4,5,10)
g.addAresta(5,7,2)
g.addAresta(6,7,6)
g.addAresta(6,8,7)
g.addAresta(7,8,1)

'''g = Lista(8,'nao_dir')
g.addAresta(0,1,3)
g.addAresta(0,2,14)
g.addAresta(1,2,8)
g.addAresta(1,5,5)
g.addAresta(2,3,6)
g.addAresta(2,4,5)
g.addAresta(3,4,12)
g.addAresta(4,7,9)
g.addAresta(4,5,7)
g.addAresta(5,6,15)'''
Kruskal = Kruskal()
set = Kruskal.Kruskal(g,g.v)
print(set)
'''# exemplos do slide
gr = Lista(9,'dir')
gr.addAresta(0,2,0)
gr.addAresta(0,3,0)
gr.addAresta(1,3,0)
gr.addAresta(2,5,0)
gr.addAresta(2,3,0)
gr.addAresta(5,8,0)
gr.addAresta(6,5,0)
gr.addAresta(6,7,0)
gr.addAresta(7,8,0)

g = Lista(6,'dir')
g.addAresta(0,1,0)
g.addAresta(1,2,0)
g.addAresta(3,2,0)
g.addAresta(3,4,0)
g.addAresta(3,5,0)
g.addAresta(4,0,0)
g.addAresta(4,1,0)
g.addAresta(4,5,0)
g.addAresta(5,2,0)

#chamada ordenação topológica
print('Os vértices foram adicionados de 0 a N, mas printados de 1 a N+1\n')
ord_top = TopoOrder()
ordenados = ord_top.top_ord(g, 4)
ord_top.add(ordenados)
print('\n')
ordenados = ord_top.top_ord(gr, 6)
ord_top.add(ordenados)'''

'''g = Lista(13,'nao_dir')
g.addAresta(0,1)
g.addAresta(0,2)
g.addAresta(0,6)
g.addAresta(0,5)
g.addAresta(4,5)
g.addAresta(5,3)
g.addAresta(4,3)
g.addAresta(6,4)
g.addAresta(7,8)
g.addAresta(9,10)
g.addAresta(9,11)
g.addAresta(9,12)
g.addAresta(11,12)'''


#chamada de componentes conectados
'''con = ConnectedComponents()
ide = con.conec(g)
print(ide)
print(con.nConnected())
print(con.connected(0,1))'''

#chamada da busca em profundidade
#dfs = DepthFirstSearch()
#dfs.depthFirstSearch(g)

#chamada da busca em largura
#bfs = BreadthFirstSearch()
#bfs.BFS(g,9)


'''g = Lista(18,'nao_dir')
g.addAresta(0,1)
g.addAresta(0,2)
g.addAresta(0,4)
g.addAresta(0,14)
g.addAresta(1,4)
g.addAresta(1,5)
g.addAresta(2,3)
g.addAresta(3,6)
g.addAresta(3,10)
g.addAresta(3,17)
g.addAresta(4,5)
g.addAresta(4,7)
g.addAresta(4,8)
g.addAresta(5,6)
g.addAresta(5,8)
g.addAresta(6,9)
g.addAresta(6,10)
g.addAresta(7,14)
g.addAresta(8,9)
g.addAresta(8,12)
g.addAresta(9,12)
g.addAresta(10,13)
g.addAresta(10,17)
g.addAresta(11,12)
g.addAresta(12,13)
g.addAresta(13,17)
g.addAresta(14,15)
g.addAresta(15,16)
g.addAresta(15,17)
g.addAresta(16,17)'''

    
# Exemplo de grafo representado por lista de adjacências
'''grafo = Lista(20,'dir')
grafo.addAresta(10,1)
grafo.addAresta(0,6)
grafo.addAresta(3,1)
grafo.addAresta(0,11)
grafo.addAresta(12,4)
grafo.addAresta(4,5)
grafo.addAresta(2,0)
grafo.addAresta(8,3)
grafo.addAresta(6,7)
grafo.addAresta(15,17)
grafo.addAresta(18,16)
grafo.addAresta(15,4)
grafo.addAresta(15,3)
grafo.addAresta(18,1)
grafo.addAresta(5,12)
grafo.addAresta(6,8)
grafo.addAresta(15,18)
grafo.addAresta(6,10)
grafo.addAresta(0,19)
grafo.addAresta(19,4)
grafo.addAresta(17,10)
grafo.addAresta(9,3)
grafo.addAresta(2,9)
grafo.addAresta(14,5)
grafo.addAresta(7,14)
grafo.addAresta(13,2)
grafo.addAresta(8,13)
grafo.grauVertice(3)
grafo.existeAresta(13,2)
grafo.existeAresta(3,4)
grafo.existeAresta(2,2)
grafo.listAd(3)
grafo.listAd(8)
grafo.listAd(13)
grafo.imprimirGrafo()'''



#Exemplo de grafo representado por matriz de adjcências
'''graph = Matriz(12, 'nao_dir')
graph.addAresta(11,1)
graph.addAresta(9,10)
graph.addAresta(7,4)
graph.addAresta(7,4)
graph.addAresta(3,3)
graph.addAresta(6,5)
graph.addAresta(5,6)
graph.addAresta(0,11)
graph.addAresta(4,8)
graph.addAresta(9,3)
graph.addAresta(2,4)
graph.addAresta(2,6)
graph.addAresta(6,3)
graph.addAresta(4,11)
graph.addAresta(11,7)
graph.remAresta(11,7)
graph.remAresta(1,4)
graph.grauVertice(3)
graph.grauVertice(11)
graph.existeAresta(6,3)
graph.existeAresta(2,3)
graph.existeAresta(1,1)
print(graph.listAd(11))
graph.listAd(2)
graph.listAd(7)
print(graph.listAd(4))
graph.imprimirGrafo()'''
