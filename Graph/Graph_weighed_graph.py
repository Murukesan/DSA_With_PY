class Graph:
    def __init__(self,size):
        self.size=size
        self.adj_matrix=[[0]*size for i in range(size)]
        self.vertex=['']*size
    def add_vertex(self,vertex,data):
        if 0<=vertex<self.size:
            self.vertex[vertex]=data
    def add_edge(self,u,v,weight):
        if 0<=u<self.size and 0<=v<self.size:
            self.adj_matrix[u][v]=weight
    def print_graph(self):
        print("Adjacency Matrix")
        for i in self.adj_matrix:
            print(i, end="\n")

        print("Adjacency List")
        for i in range(len(self.vertex)):
            print(f'{self.vertex[i]}: ',end="")
            for j in range(len(self.vertex)):
                if self.adj_matrix[i][j]:
                    print(f'{self.vertex[j]}',end=" ")
            print()


g=Graph(4)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')
g.add_vertex(3,'D')
g.add_edge(0,1,1)
g.add_edge(0,2,2)
g.add_edge(0,3,3)
g.add_edge(1,3,4)
g.print_graph()

