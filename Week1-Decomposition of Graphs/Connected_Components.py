'''
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components
in it.
Input Format. A graph is given in the standard format.
Constraints. 1 ≤ 𝑛 ≤ 103
, 0 ≤ 𝑚 ≤ 103
.
Output Format. Output the number of connected components
'''


def explore(adjList,a,visited,CCnum,cc):
    visited[a] = True
    CCnum[a] = cc
    for ele in adjList[a]:
        if not visited[ele]:
            explore(adjList,ele,visited,CCnum,cc)

def DFS(adjList):
    visited = [False]*(len(adjList))
    CCnum = [0]*(len(adjList))
    cc = 1
    for i in range(len(adjList)):
        if not visited[i]:
            explore(adjList,i,visited,CCnum,cc)
            cc += 1
    return max(CCnum)


if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    edgeList = []
    for i in range(m):
        a,b = map(int,input().split())
        edgeList.append([a,b])
    adjList = [[] for _ in range(n)]
    for l in edgeList:
        adjList[l[0]-1].append(l[1]-1)
        adjList[l[1]-1].append(l[0]-1)
    print(DFS(adjList))
