import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[0] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1) : 
  root,node = map(int,input().split())
  graph[root].append(node)
  graph[node].append(root)

def dfs(graph,v,visited) :
  for i in graph[v] :
    if visited[i] == 0:
      visited[i] = v
      dfs(graph,i,visited)

dfs(graph,1,visited)

for i in range(2,n+1) :
  print(visited[i])