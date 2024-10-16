class graph:
    def __init__(self,size):
        self.size = size
        self.add_adj = [[0] * size for i in range(size)]
        self.vertix = [''] * size
        
    def addadj(self,u,v,weight):
        if 0 <= v < self.size and 0 <= v < self.size:
            self.add_adj[u][v] = weight
            self.add_adj[v][u] = weight
            
    def add_vertix(self,v,data):
        if 0<= v <self.size:
            self.vertix[v] = data
            
    def print_graph(self):
        print('/n vertix')    
        for row in self.add_adj:
            print(' '.join(map(lambda x : str(x) if x is not None else '0',row)))
            
        for i,j in enumerate(self.vertix):
            print(f"vertic:{i} value:{j}") 
            
            
g  = graph(5)
g.addadj(0,1,3)
g.addadj(4,1,4)
g.addadj(2,4,3)
g.addadj(0,2,0)
g.addadj(2,1,4)
g.add_vertix(0,'B')
g.add_vertix(1,'C')
g.add_vertix(2,'D')
g.add_vertix(3,'E')
g.add_vertix(4,'F')

g.print_graph()

