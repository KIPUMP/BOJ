from collections import deque
import copy
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs() :
  queue = deque()
  tmp_graph = copy.deepcopy(graph)

  for i in range(n) :
    for j in range(m) :
      if tmp_graph[i][j] == 2 :
        queue.append((i,j))

  while queue :
    x , y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m :
        if tmp_graph[nx][ny] == 0 :
          tmp_graph[nx][ny] = 2
          queue.append((nx,ny))

  global result
  count = 0
  for i in range(n) :
    for j in range(m) :
      if tmp_graph[i][j] == 0 :
        count += 1
  result = max(result,count)      

def make_wall(count) :
  if count == 3 :
    bfs()
    return

  for i in range(n) :
    for j in range(m) :
      if graph[i][j] == 0 :
        graph[i][j] = 1
        make_wall(count+1)
        graph[i][j] = 0       

for i in range(n) :
  graph.append(list(map(int,input().split())))

result = 0
make_wall(0)
print(result)
