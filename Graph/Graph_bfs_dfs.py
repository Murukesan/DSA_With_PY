class Graph:
    def __init__(self,size):
        self.size=size
        self.vertex=['']*self.size
        self.adj_matrix=[[0]*size for i in range(self.size)]

    def add_vertex(self,index,data):
        if 0<=index<self.size:
            self.vertex[index]=data
        else:
            print("index out of range")
    def add_edge(self,u,v):
        if 0<=u<self.size and 0<=v<self.size:
            self.adj_matrix[u][v]=1
            self.adj_matrix[v][u] = 1
    def print_graph(self):
        print("Adjacency Matrix")
        for i in self.adj_matrix:
            print(i)
        print("Adjacency list")
        for i in range(self.size):
            print(f'{self.vertex[i]}: ',end=" ")
            for j in range(self.size):
                if self.adj_matrix[i][j]:
                    print(f'{self.vertex[j]}',end=" ")
            print()
    def dfs_util(self,start,visited):
        visited[start]=True
        print(self.vertex[start],end="->")
        for i in range(self.size):
            if self.adj_matrix[start][i]==1 and not visited[i]:
                self.dfs_util(i,visited)

    def dfs(self,start_vertex):
        visited=[False]*self.size
        start=self.vertex.index(start_vertex)
        self.dfs_util(start,visited)
    def bfs(self,start_vertex):
        print()
        visited=[False]*self.size
        queue=[self.vertex.index(start_vertex)]
        visited[queue[0]]=True
        while queue:
            print(queue)
            current=queue.pop(0)
            print(self.vertex[current],end="->")
            for i in range(self.size):
                if self.adj_matrix[current][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i]=True

graph=Graph(6)
graph.add_vertex(0,'A')
graph.add_vertex(1,'B')
graph.add_vertex(2,'C')
graph.add_vertex(3,'D')
graph.add_vertex(4,'E')
graph.add_vertex(5,'F')
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.print_graph()
graph.dfs('B')
graph.bfs('B')