from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
num = 1
res = int(1e9)

def bfs(i,j) :
  que = deque()
  que.append([i,j])
  while que :
    x,y = que.popleft()
    for (h,w) in [[1,0],[0,1],[-1,0],[0,-1]] :
      dx = x + h
      dy = y + w
      if 0 <= dx < n and 0 <= dy < n :
        if not visited[dx][dy] and graph[dx][dy] :
          visited[dx][dy] = 1
          graph[dx][dy] = num 
          que.append([dx,dy])

def bfs2(v) :
  queue = deque()
  dist = [[-1] * n for _ in range(n)] 
  
  for i in range(n) :
    for j in range(n) :
      if graph[i][j] == v :
        dist[i][j] = 0
        queue.append([i,j])

  while queue :
    x,y = queue.popleft()
    for (w,h) in [[1,0],[0,1],[-1,0],[0,-1]] :
      dx, dy = x + w , y + h
      if 0 <= dx < n and 0 <= dy < n :
        if graph[dx][dy] and graph[dx][dy] != v :
          return dist[x][y]
        elif (not graph[dx][dy]) and dist[dx][dy] == -1 :
          dist[dx][dy] = dist[x][y] + 1
          queue.append([dx,dy])


  return int(1e9)

for i in range(n) :
  for j in range(n) :
    if graph[i][j] and not visited[i][j] :
      visited[i][j] = 1
      graph[i][j] = num 
      bfs(i,j)
      num += 1

for v in range(1,num) :
  res = min(res,bfs2(v))
print(res)