from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0,-1,0, 1]
dy = [-1,0,1,0]


def dfs(x,y) :
  visited[x][y] = True
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n :
        if not visited[nx][ny] and arr[nx][ny] == 1 :
          dfs(nx,ny)

queue = deque()

def bfs(x,y) :
  visited = [[False] * n for _ in range(n)]
  queue.append((x,y))
  visited[x][y] = True
  cnt = 1
  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n :
        if not visited[nx][ny] :
          if arr[nx][ny] == 0 :
            cnt += 1
            visited[nx][ny] = True
            queue.append((nx,ny))
          else :
            return cnt

result = []

for i in range(n) :
  for j in range(n) :
    if not visited[i][j] and arr[i][j] == 1 :
      dfs(i,j)


    if not visited[i][j] and arr[i][j] == 0 :
      x = bfs(i,j)
      result.append(x)



print(result)


