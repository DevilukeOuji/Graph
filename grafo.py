# o grafo supõe valores de vértices de 0 a N   
class Graph():

    def __init__(self, v, typ, represent):
        self.v = v
        self.typ = typ
        self.represent = represent
        self.matrix = []
        self.listAdj = []
        self.weight = []

    def initMatrix(self):     
        for i in range(0, self.v):
            line = []
            self.matrix += [line]
            for j in range(0, self.v):
                line += [0]

    def initList(self):
        for i in range(0, self.v):
            line = []
            self.listAdj += [line]

    def addEdge(self, v, w, weight): #considerando que não há vértice 0
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.represent == 'matrix':
            if self.typ == 'nao_dir': self.matrix[w][v] = 1
            self.matrix[v][w] = 1
        else:
            if self.typ == 'nao_dir': self.listAdj[w] += [v]
            self.listAdj[v] += [w]
        self.weight += [weight]

    def remEdge(self, v, w): 
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.matrix[v][w] == 0:
            print('\nAresta inexistente.')
            return
        if self.represent == 'matrix':
            if self.typ == 'nao_dir': self.matrix[w][v] = 0
            self.matrix[v][w] = 0
        else:
            if self.typ == 'nao_dir': self.listAdj[w].remove(v)
            self.listAdj[v].remove(w)

    def edgeDegree(self, v):
        if v > self.v:
            print('\nO vértice não existe no grafo.')
            return
        grau = 0
        if self.represent == 'matrix':
            for i in self.matrix[v]:
                if i == 1: grau += 1
        else: 
            for i in self.listAdj[v]: grau += 1
        if self.tipo == 'dir':
            if self.represent == 'matrix':    
                for i in self.matrix:
                    if i[v] == 1: grau += 1
            else:
                for i in self.listAdj:
                    if v in i: grau += 1
        print(f'\nO grau do vértice {v} é: {grau}')
        return grau
    
    def existsEdge(self, v, w):
        if v > self.v or w > self.v: 
            print('\nUm dos vértices não existe no grafo.')
            return
        if self.represent == 'matrix':
            if self.matrix[v][w] == 1: return True
        else: 
            if w in self.listAdj[v]: return True
        return False

    def adjList(self,v):
        if v > self.v: return
        if self.represent == 'matrix':
            lista_adj = []
            for i in range(0,len(self.matrix[v])):
                if self.matrix[v][i] == 1: lista_adj += [i]
            return lista_adj
        else: return sorted(self.listAdj[v])

    def printGraph(self):
        if self.represent == 'matrix':
            print('\nMatriz de Adjacências')
            for i in range(0, len(self.matrix)):
                if i < 10: print('0'+f'{i}', end = ' ')
                else: print(i, end = ' ')
                print(self.matrix[i])
        else:
            print('\nLista de Adjacências')
            for i in range(0, len(self.listAdj)):
                print(i, end = ' ')
                print(self.listAdj[i])

    def ordWeight(self):
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

graph = Graph(12,'nao_dir','matrix')
if graph.represent == 'matrix':
    graph.initMatrix()
else:
    graph.initList()

graph.addEdge(11,1,20)
graph.addEdge(7,4,1)
graph.addEdge(6,3,3)
graph.addEdge(7,2,5)
graph.addEdge(11,7,3)
print(graph.weight)
graph.printGraph()