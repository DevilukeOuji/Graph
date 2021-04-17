class ComponentesConec():
    def __init__(self):
        self.cont = 0

    def conec(self,graph):
        num_vert = graph.v
        color = [];predecessor = [];identifier = []
        for u in range(0, num_vert):
            color += ['white'];predecessor += [-1];identifier += [-1]
        for u in range(0, num_vert):
            if color[u] == 'white': 
                time = ComponentesConec.dfs(self,graph, u, color,predecessor)
                self.cont += 1
        print(f'predecessor:{predecessor}')
        return identifier

    def dfs(self,graph, u, color,predecessor):
        color[u] = 'gray'
        identifier[u] = self.cont
        adj_list = graph.listAd(u)
        if adj_list:
            for elem in adj_list:
                if color[elem] == 'white':
                    predecessor[elem] = u
                    time = ComponentesConec.dfs(self,graph, elem,color,predecessor)
        color[u] = 'black'
        return identifier
    
    def cont(self):
        return self.cont
    
    def connected(self, v, w):
        return identifier[v] == identifier[w]
