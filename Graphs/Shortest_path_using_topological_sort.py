# code by yashwanthguguloth24
# Using topological sort to find shortest path of weighted directed DAG Graph 

from collections import defaultdict
import sys

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # consider as directed graph
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))

    def dfs(self,i,stack):
        self.visited[i] = True
        for k in self.graph[i]:
            if self.visited[k[0]] == False:
                self.dfs(k[0],stack)

        stack.append(i)


    def Topological_sort(self):
        self.visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs(i,stack)
        return stack[::-1]

    def Shortest_path(self,start):
        dist = [sys.maxsize]*self.V
        top = self.Topological_sort()
        dist[start] = 0
        for i in range(self.V):
            node_index = top[i]
            if dist[node_index] != sys.maxsize:
                for edge in self.graph[node_index]:
                    new_dist = dist[node_index]+edge[1]
                    if dist[edge[0]] == sys.maxsize:
                        dist[edge[0]] = new_dist
                    else:
                        dist[edge[0]] = min(dist[edge[0]],new_dist)
        print(dist[top[-1]])
        print(dist)

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 3, 6)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 4, -1)
    g.addEdge(4, 5, -2)
    g.Shortest_path(0)
