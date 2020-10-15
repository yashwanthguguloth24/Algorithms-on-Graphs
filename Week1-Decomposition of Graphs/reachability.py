'''
Task. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
and 𝑣 of the graph.
Constraints. 2 ≤ 𝑛 ≤ 103
; 1 ≤ 𝑚 ≤ 103
; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.
Output Format. Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.
'''

def explore(adjList,a,visited):
    visited[a] = True
    for ele in adjList[a]:
        if not visited[ele]:
            explore(adjList,ele,visited)

def reach(adjList, x, y):
    visited = [False]*(len(adjList))
    explore(adjList,x,visited)
    if visited[y] == True:
        return 1
    else:
        return 0


if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    edgeList = []
    for i in range(m):
        a,b = map(int,input().split())
        edgeList.append([a,b])
    x,y = map(int,input().split())
    adjList = [[] for _ in range(n)]
    for l in edgeList:
        adjList[l[0]-1].append(l[1]-1)
        adjList[l[1]-1].append(l[0]-1)
    print(reach(adjList,x-1,y-1))
