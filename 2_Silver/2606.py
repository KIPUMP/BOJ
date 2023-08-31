import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

computer = int(input())
graph = [[] for _ in range(computer + 1)] 
visited = [False] * (computer + 1) 

for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
dfs(graph, 1, visited)
print(sum(visited)-1)
