from collections import deque

R,C = map(int,input().split())
ground = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y) :
  queue = deque(ground)
  visited[x][y] = True
  if ground[x][y] == "#" :
      while queue :
        queue.popleft()
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and ground[nx][ny] == "#":
            ground[nx][ny] = "."
            visited[nx][ny] = True


cnt = 0
for i in range(R) :
  for j in range(C) :
    if not visited[i][j] and ground[i][j] == "#":
      cnt += 1
      bfs(i,j)

print(cnt)
    
