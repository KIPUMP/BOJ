import sys
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M) :
  u,v = map(int,input().split())
  arr[u].append(v)
  arr[v].append(u)

def dfs(graph,v,visited) :
  visited[v] = True
  for i in graph[v] :
    if visited[i] == False :
      dfs(graph,i,visited)
  
visited = [False] *(N+1)

cnt = 0
dfs(arr,1,visited)
for i in range(N+1) :
  if visited[i] == False :
    dfs(arr,i,visited) 
    cnt += 1

print(cnt)
