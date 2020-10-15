

def main(adjList):
    visited = [False]*(len(adjList))
    for i in range(len(adjList)):
        if visited[i] == False:
            BFS(adjList,i,visited)



def BFS(adjList,node,visited):
    queue = []
    visited[node] = True
    queue.append(node)
    while len(queue) != 0:
        curr = queue.pop(0)
        print(curr)
        for ne in adjList[curr]:
            if visited[ne] == False:
                visited[ne] = True
                queue.append(ne)



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
