import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dist = [0 for _ in range(n+1)]

for i in range(1,n) :
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


def dfs(graph,v,visited) : 
    visited[v] = 1
    for i in range(len(graph[v])) :
        w = graph[v][i][0]
        if not visited[w] :
            dist[w] = graph[v][i][1] + dist[v]
            dfs(graph,w,visited)
            

dfs(graph,1,visited)
print(max(dist))
