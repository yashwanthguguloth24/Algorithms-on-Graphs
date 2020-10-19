## code by yashwanthguguloth24
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # consider as an directed graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,i,stack):
        self.visited[i] = True
        for k in self.graph[i]:
            if self.visited[k] == False:
                self.dfs(k,stack)

        stack.append(i)


    def Topological_sort(self):
        self.visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs(i,stack)
        print(stack[::-1])

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.Topological_sort()
