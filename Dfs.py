class DepthFirstSearch():

    def depthFirstSearch(self,graph):
        num_vert = graph.v
        color = [];predecessor = [];d = []; t = [];time = 0
        for u in range(0, num_vert):
            color += ['white'];predecessor += [-1]
            d += ['']
            t += ['']
        for u in range(0, num_vert):
            if color[u] == 'white': 
                time = DepthFirstSearch.dfs(self,graph, u+1, time, color,predecessor, d, t)
        print(f'predecessor:{predecessor}')
        return t

    def dfs(self,graph, u, time, color,predecessor, d, t):
        color[u-1] = 'gray'
        time += 1
        d[u-1] = time
        adj_list = graph.listAd(u)
        if adj_list:
            for elem in adj_list:
                if color[elem-1] == 'white':
                    predecessor[elem-1] = u
                    time = DepthFirstSearch.dfs(self,graph, elem,time, color,predecessor, d, t)
        color[u-1] = 'black'
        time += 1
        t[u-1] = time
        '''print('color: ', color)
        print('d: ', d)
        print('t: ', t)'''
        return time
