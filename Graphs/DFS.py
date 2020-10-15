
def main(adjList):
    visited = [False]*(len(adjList))
    DFS(adjList,0,visited)


def DFS(adjList,node,visited):
    if visited[node] == False:
        print(node)
        visited[node] = True
        for ne in adjList[node]:
            DFS(adjList,ne,visited)



if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    edgeList = []
    for i in range(m):
        a,b = map(int,input().split())
        edgeList.append([a,b])
    adjList = [[] for _ in range(n)]
    for l in edgeList:
        adjList[l[0]].append(l[1])
        adjList[l[1]].append(l[0])
    main(adjList)
